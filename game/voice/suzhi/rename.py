import os

def rename_files_by_time(folder_path, extension=".wav", prefix="", start_index=1):
    # 1. 获取文件夹内所有指定后缀的文件
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(extension)]
    
    # 2. 按文件的【修改时间】进行排序 (从早到晚)
    # 如果你想按【创建时间】，在Windows下通常是一样的，但在某些系统可以用 os.path.getctime
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    
    print(f"找到 {len(files)} 个文件，准备重命名...")

    # 3. 循环重命名
    for i, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename)
        
        # 构建新名字，例如: 1.wav 或 suzhi_01.wav
        # str(i + start_index) 就是 1, 2, 3...
        new_name = f"{prefix}{i + start_index}{extension}"
        new_path = os.path.join(folder_path, new_name)
        
        # 防止重名冲突（如果文件夹里已经有 1.wav，可能会报错，所以加个判断）
        if old_path == new_path:
            continue
            
        try:
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_name}")
        except FileExistsError:
            print(f"跳过: {new_name} 已存在，请确保文件夹内没有冲突的文件名。")

    print("✅ 全部完成！")

# ================= 配置区 =================
# 把这里改成你存放音频的文件夹路径
target_folder = r"E:\galmaker\SnowLove\game\voice\suzhi" 

# 运行函数
# 如果你想要纯数字文件名 (1.wav)，prefix留空
rename_files_by_time(target_folder, extension=".wav", prefix="suzhi_")

# 如果你想要带角色名 (suzhi_1.wav)，可以这样写：
# rename_files_by_time(target_folder, extension=".wav", prefix="suzhi_")