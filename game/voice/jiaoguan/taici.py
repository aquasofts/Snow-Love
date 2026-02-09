import os
import re

# ================= 配置区域 =================
# 请在这里输入存放 wav 文件的文件夹路径
# Windows路径示例: r"C:\Users\Mosior\Desktop\VoiceLines"
# 注意：路径前加 r 可以防止转义字符报错
TARGET_FOLDER = r"C:\Users\mosior\Desktop\雪之恋\jiaoguan"
# ===========================================

# 你提供的119个名字（台词列表）
raw_names = """
全体都有！立正——！向右看齐！

入列！下次早点！

那边那两个！干什么呢！眉来眼去的！出列！

第三排那个戴眼镜的，眼神乱飘什么？

是不是觉得这身军装不够帅，想去跑两圈展示一下身材？

全体都有！稍息！

讲一下。
上午的训练，整体表现尚可，但个别同学意志力薄弱。

记住，你们是未来的工程师，连这点苦都吃不了，以后怎么去工地？

鉴于刚才有人乱动，延长十五分钟站姿体验。

谁在叹气？很有个性嘛。再加五分钟。

解散！休息二十分钟！

吵什么？很有精神嘛。

行了。多大点事？没水了再去买。

对着长辈大声喧哗，这就是你的教养？你的军人风度呢？

全体都有！因为不懂得尊重他人，罚站十分钟！好好反省一下什么是素质！

全体都有！立正！

经过一周的适应性训练，你们已经初步具备了军人的模样。但是，这还不够！

下周五，将举行全校新生军训汇报表演。这是检验你们成果的时刻，也是展现土木系风采的时刻！

安静！

为了保证汇演效果，从今天开始，我们将重新编队。所有人将被打散，重新划分为三个部分：

第一，分列式方队。这是最精锐的部队，将代表系里走过主席台，接受检阅。要求动作标准，身材匀称，意志力强！

第二，合唱团。负责在看台上唱军歌，展现气势。

第三，观训营。身体素质无法适应高强度训练的，进入观训营。

分列式方队，是荣誉，也是地狱。训练强度将是现在的两倍。怕苦的，现在就可以后退一步去合唱团。

第一排，出列！正步走！

停！第三个，顺拐了，去合唱团。第五个，罗圈腿太严重，去合唱团。第一个，留下。

下一组！

正步——走！

停！

第二个，不错。踢腿高度标准，落地有声。入列，第一排面。

下一组！正步——走！

停！

眼镜扶好。眼神再犀利点，别像没睡醒一样。

不过，节奏感不错，身板也直。入列。

下一组！

停！

那个白净的男生，你在跳机械舞吗？

很有想法。但是正步需要的是爆发力，不是优雅。

你的协调性还得练练。去合唱团吧，那边可能更适合你的……气质。

服从命令！

恭喜你们，留到了最后。

但不要高兴得太早。从现在起，你们不再是个体，而是一个整体。

方队的要求只有一个：整齐划一。

一人出错，全队受罚！

右腿踢出！定住！谁敢动！

脚尖下压！把腿抬高！

女生方队第一排排头！晃什么！腿软了？

没有就给我站稳！排头兵要是倒了，整个方队就垮了！再加两分钟定型！

停——！都给我停下！

土木系的！你们是在梦游吗？那个排面，歪得像贪吃蛇一样！
尤其是第三列！脚抬高！砸地要有声音！

中午还想不想吃饭了？我看你们是精神太好了，不饿是吧？

全体都有——向后转！跑步回原点！再来一遍！

全停！

现在是11点40分，距离正式汇演还有40分钟。

为了保持这种紧绷的状态，为了防止你们吃饱了犯困——

所有人原地休息！不许解散！不许去食堂！

克服饥饿感，这是军人的必修课！听明白了吗？！

正步——走！！！

哼，算你们这群小兔崽子没给我丢人。排头兵！出列领奖！
"""

def clean_filename(name):
    """
    将文件名中的非法字符（Windows下）转换为全角字符，
    并去除首尾空格。
    """
    # 替换半角符号为全角，避免Windows文件名报错
    name = name.replace('?', '？').replace('!', '！').replace(':', '：')
    name = name.replace('<', '＜').replace('>', '＞').replace('*', '＊')
    name = name.replace('/', '／').replace('\\', '＼').replace('|', '｜')
    name = name.replace('"', '”')
    
    # 去除首尾空格和换行符
    name = name.strip()
    return name

def rename_files():
    # 1. 处理名字列表
    # 按行分割，并去除空行
    name_list = [line.strip() for line in raw_names.split('\n') if line.strip()]
    
    print(f"检测到台词数量: {len(name_list)} 条")

    # 2. 获取文件夹中的 wav 文件
    if not os.path.exists(TARGET_FOLDER):
        print(f"错误: 找不到文件夹 {TARGET_FOLDER}")
        return

    files = [f for f in os.listdir(TARGET_FOLDER) if f.lower().endswith('.wav')]
    
    # 3. 按创建时间排序 (从旧到新)
    # Windows上 getctime 获取的是创建时间
    files.sort(key=lambda x: os.path.getctime(os.path.join(TARGET_FOLDER, x)))
    
    print(f"检测到 .wav 文件数量: {len(files)} 个")

    if len(files) == 0:
        print("文件夹中没有 wav 文件。")
        return

    # 4. 开始重命名
    count = 0
    for i, old_filename in enumerate(files):
        # 如果文件数量多于名字数量，停止重命名并提示
        if i >= len(name_list):
            print(f"警告: 文件数量 ({len(files)}) 多于名字数量 ({len(name_list)})，剩余文件未重命名。")
            break
        
        # 获取新名字并清理非法字符
        new_base_name = clean_filename(name_list[i])
        new_filename = f"{new_base_name}.wav"
        
        old_path = os.path.join(TARGET_FOLDER, old_filename)
        new_path = os.path.join(TARGET_FOLDER, new_filename)
        
        # 处理重名情况 (如果生成的这个名字已经存在)
        if os.path.exists(new_path) and old_path != new_path:
            duplicate_count = 1
            while os.path.exists(new_path):
                new_filename = f"{new_base_name}({duplicate_count}).wav"
                new_path = os.path.join(TARGET_FOLDER, new_filename)
                duplicate_count += 1
        
        try:
            os.rename(old_path, new_path)
            # 打印日志（可选）
            # print(f"已重命名: {old_filename} -> {new_filename}")
            count += 1
        except Exception as e:
            print(f"重命名 {old_filename} 失败: {e}")

    print("-" * 30)
    print(f"完成！共成功修改 {count} 个文件。")

if __name__ == "__main__":
    rename_files()