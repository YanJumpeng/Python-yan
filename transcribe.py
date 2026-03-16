import whisper
import sys
import os

# ─────────────────────────────────────────
# 繁体 → 简体转换（用opencc，没装则跳过）
# ─────────────────────────────────────────
def to_simplified(text):
    try:
        import opencc
        converter = opencc.OpenCC('t2s')
        return converter.convert(text)
    except ImportError:
        return text  # 没装opencc就原样返回

# ─────────────────────────────────────────
# 主程序
# ─────────────────────────────────────────
if len(sys.argv) < 2:
    print("用法：python transcribe.py 视频文件1.mp4 [视频文件2.mp4 ...]")
    sys.exit(1)

# 加载模型（只加载一次）
print("加载模型中...")
model = whisper.load_model("medium")

for file_path in sys.argv[1:]:
    if not os.path.exists(file_path):
        print(f"\n⚠️  文件不存在，跳过：{file_path}")
        continue

    print(f"\n正在识别：{file_path}")
    result = model.transcribe(file_path, language="zh")
    text = result["text"]

    # 转简体
    text = to_simplified(text)

    print("\n===== 识别结果 =====")
    print(text)

    # 保存txt
    output_path = os.path.splitext(file_path)[0] + "_transcript.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\n✓ 已保存到：{output_path}")

print("\n全部完成。")
