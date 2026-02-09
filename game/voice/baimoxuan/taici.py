import os
import re

# ================= 配置区域 =================
# 请在这里输入存放 wav 文件的文件夹路径
# Windows路径示例: r"C:\Users\Mosior\Desktop\VoiceLines"
# 注意：路径前加 r 可以防止转义字符报错
TARGET_FOLDER = r"C:\Users\mosior\Desktop\雪之恋\baimoxuan"
# ===========================================

# 你提供的119个名字（台词列表）
raw_names = """
コンクリートのスランプ……骨材の粒度分布……だめ……この公式は間違っている……

魔女の法則によれば……ここにトカゲの尻尾を少し……あ、違う、減水剤だ……

観測者……？

見たのか？　私の「禁忌の錬成陣」を見たのか？

うぅ……先輩？　それとも同級生？

その……上の本を取ってくれないかな？　私……魔力が足りなくて。

私は……バベルの塔を建設するためだ！
神域へと至る塔を！　感謝する、巨人族の善人よ。我が名は白墨萱。こう呼ぶといい――「構造力学の魔女」と。

ん？　この匂い……イチゴミルクか？

しかも……乾燥した糖分結晶の匂い？　お前……甘ったるい罪を背負っているな。

ほう？　本妻のオーラ？　防御力は高いが、攻撃性が高すぎる。クラックが生じやすいぞ。
補強が必要だ。

達者でな。報酬として、祈りを捧げよう……
お前の骨格強度が、その剪断力に耐えられることを。

観測した。二つの独立した生命体が、高カロリーの物質交換を行っている。
かつ、「ホルモン」という名の化学反応を伴っている。興味深い実験サンプルだ。ちょっと失礼。

訂正する。避難ではない。「トラス構造の耐震シミュレーション」を徹夜で完了させた後の、戦略的撤退だ。

機体エネルギーが枯渇した、至急高タンパクの補給が必要だ。食堂の人口密度が設定値を超えていたため、空席の検索に貴重な三分二十秒を消費した。

知っている。お前は「ディフェンダー」だ。昨日図書館で会った。縄張り意識が過剰だな、学術交流の妨げになる。それに……

空間利用率最大化の原則に基づけば、この椅子のアイドル状態は公共資源の浪費だ。ここの人員密度は一平方メートルあたり四人、対してこの椅子の占有面積は〇・二五平方メートル。ゆえに私がここに座ることは、構造力学的な最適解であり、資源配分のパレート最適にも合致する。

んん……油脂。喜ばしい炭素鎖構造だ。この高熱量は迅速にATPへと変換される。

巨人よ。お前の卵。タンパク質の凝固具合が完璧で、表面張力も良好に保たれている。お前が孵化させたのか？

ほう？　この反応……生物学上、「配偶者防衛行動」と呼ばれるものだな。
通常、繁殖期の……哺乳類に見られる。配偶者と子孫を守るため、メスは極めて強い攻撃性を示す。興味深いサンプルだ。

それはセロリジュースだ。飲むか？　巨人。神経シナプスの伝達速度を上げ、少しは賢くなれるぞ。
味は生物化学兵器を咀嚼しているよう、あるいは液状の芝生を飲んでいるようだがな。

承諾しかねる。データ収集が未完了だ。「巨人」が食事をする際の下顎の咬合力を観察する必要がある。これは新型破砕機の設計において参考価値があるんだ。それに、お前たちのその「非合理的」な食事交流モードに興味がある。
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