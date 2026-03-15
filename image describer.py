import cv2
import gradio as gr
import requests
import base64
import time

# 阿里云 API Key
DASHSCOPE_API_KEY = ""  # 替换为真实Key


# 加载 YuNet 模型（阈值可调）
detector = cv2.FaceDetectorYN.create(
    model="face_detection_yunet_2023mar.onnx",
    config="",
    input_size=(640, 640),
    score_threshold=0.56,  # 可根据需要调整：0.1-0.5
    nms_threshold=0.3,
    top_k=5000
)


def call_api_with_retry(img_base64, retries=3, delay=2):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "qwen-vl-plus",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"image": f"data:image/jpeg;base64,{img_base64}"},
                        {
                            "text": "请用中文详细描述这张图片，包括场景、人物（如果有）、他们的表情、动作、穿着，以及背景中的物体和整体氛围。"}
                    ]
                }
            ]
        }
    }
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            result = response.json()
            description = result['output']['choices'][0]['message']['content'][0]['text']
            return description
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                return f"识别失败（重试{retries}次后仍出错）: {str(e)}"


def describe_image(image):
    img_with_faces = image.copy()
    h, w = image.shape[:2]
    detector.setInputSize((w, h))
    _, faces = detector.detect(image)

    faces_list = []
    if faces is not None:
        for face in faces:
            x, y, w_face, h_face = face[:4].astype(int)
            faces_list.append((x, y, w_face, h_face))
            cv2.rectangle(img_with_faces, (x, y), (x + w_face, y + h_face), (0, 255, 0), 2)

    _, buffer = cv2.imencode('.jpg', image)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    description = call_api_with_retry(img_base64)

    face_count = len(faces_list)
    if face_count > 0:
        description += f"\n\n👤 检测到 {face_count} 张人脸，已在图片中用绿色框标出。"
    else:
        description += "\n\n👤 未检测到人脸。"

    return img_with_faces, description


iface = gr.Interface(
    fn=describe_image,
    inputs=gr.Image(),
    outputs=[gr.Image(), "text"],
    title="AI图片描述助手",
    description="上传真人合影，AI描述 + 人脸检测"
)

iface.launch()