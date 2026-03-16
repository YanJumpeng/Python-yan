import whisper
import sys
import os

# 加载模型，第一次会自动下载
# 模型大小选项：tiny / base / small / medium / large
# 中文内容推荐用 medium 或 large，准确率更高
model = whisper.load_model("medium")

# 视频/音频文件路径
file_path = sys.argv[1] if len(sys.argv) > 1 else "video.mp4"

print(f"正在识别：{file_path}")
result = model.transcribe(file_path, language="zh")

# 输出文字
text = result["text"]
print("\n===== 识别结果 =====")
print(text)

# 保存到同目录下的txt文件
output_path = os.path.splitext(file_path)[0] + "_transcript.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"\n已保存到：{output_path}")