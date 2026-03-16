项目名称：AI图片描述（人脸识别）Demo

角色：独立开发-全流程实现

技术栈：pycharm、OpenCV、Gradio、YuNet、千问VL

核心功能：
1.人脸检测：自动检测图片中的人脸，并绘制绿色的边界框，同时统计人脸数量
2.AI图片描述：调用大模型，生成详细、准确的中文描述。
3.可视化验证：让用户直观判断AI的准确性（例如描述6人就框出6张脸）

-完成多模态模型调研与选型
-完成模型本地加载、推理代码编写
-构建前后端可视化界面（Gradio/Streamlit）
-对描述结果做优化与 prompt 工程
-测试不同场景效果，调整输出格式

## 演示视频
[点击观看]([你的B站视频链接])
https://www.bilibili.com/video/BV1ErwMz5E6i/?vd_source=4ced34d0d4d89e9976c8f4ce40386868
## 使用方法
1. 安装依赖：`pip install opencv-python gradio requests`
2. 下载YuNet模型（已包含）
3. 在代码中填入自己的阿里云API Key
4. 运行 `python image_describer.py`

难点：
1.问题：漏检、误检
   解决：调低阈值提高召回率，增大面积过滤，最终召回率达到80%，误检率降低40%

2.问题：检测与描述结果不同（误检、漏检）
   解决：设计一致性检查，检测结果与描述提到的人数比对。
