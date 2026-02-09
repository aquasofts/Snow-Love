import os
import subprocess

# --- 配置区域 ---
# 目标格式
TARGET_EXT = ".ogg"
# 源格式
SOURCE_EXT = ".wav"
# FFmpeg 音质 (4 约为 128kbps, 适合 RenPy)
QUALITY = "4"

def batch_convert_replace():
    # 获取当前脚本所在的目录
    root_dir = os.getcwd()
    
    print(f"正在扫描目录: {root_dir}")
    print("注意：转换成功后将直接删除源文件！")
    print("-" * 30)

    success_count = 0
    fail_count = 0

    # os.walk 会递归遍历所有子文件夹
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # 检查是否为 wav 文件 (忽略大小写)
            if filename.lower().endswith(SOURCE_EXT):
                
                # 构建完整路径
                source_file = os.path.join(dirpath, filename)
                # 构建新文件名 (保持同路径，同名，改后缀)
                file_no_ext = os.path.splitext(source_file)[0]
                target_file = file_no_ext + TARGET_EXT
                
                print(f"[处理中] {filename} ...")

                # 构建 FFmpeg 命令
                # -y: 覆盖已存在的 ogg 文件
                # -v error: 只显示错误信息，保持清爽
                cmd = [
                    'ffmpeg', '-y',
                    '-i', source_file,
                    '-q:a', QUALITY,
                    '-v', 'error', 
                    target_file
                ]

                try:
                    # 执行转换
                    result = subprocess.run(cmd, check=True)
                    
                    # 再次确认新文件真的生成了
                    if os.path.exists(target_file):
                        # --- 关键步骤：删除源文件 ---
                        os.remove(source_file)
                        print(f"   └-> [成功] 已转换为 ogg 并删除原 wav")
                        success_count += 1
                    else:
                        print(f"   └-> [错误] 转换命令虽运行，但未找到输出文件。保留原文件。")
                        fail_count += 1

                except subprocess.CalledProcessError:
                    print(f"   └-> [失败] FFmpeg 转换出错。保留原文件。")
                    fail_count += 1
                except Exception as e:
                    print(f"   └-> [异常] {e}")
                    fail_count += 1

    print("-" * 30)
    print(f"处理完成。成功: {success_count}, 失败: {fail_count}")
    if success_count > 0:
        print("请检查文件夹，原 wav 文件已被替换为 ogg。")

if __name__ == "__main__":
    # 检查 FFmpeg 是否存在
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        batch_convert_replace()
    except FileNotFoundError:
        print("错误：未找到 ffmpeg。请确保已安装 ffmpeg 并添加到系统环境变量 Path 中。")