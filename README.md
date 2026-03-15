# AI-image-descriptor
AI图片描述助手，人脸检测+多模态描述
# AI图片描述助手

一个基于多模态大模型的图片描述工具，支持人脸检测和AI描述生成。

## 功能
- 上传图片，自动检测人脸并画绿框
- 调用阿里云通义千问VL生成详细描述
- 支持多人合影，阈值可调

## 技术栈
- Python、OpenCV、YuNet
- 阿里云百炼API
- Gradio

## 演示视频
[点击观看](你的B站视频链接)

## 使用方法
1. 安装依赖：`pip install opencv-python gradio requests`
2. 下载YuNet模型（已包含）
3. 在代码中填入自己的阿里云API Key
4. 运行 `python image_describer.py`
