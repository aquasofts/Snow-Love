# ==========================================
# 全局设置：角色与特效定义
# ==========================================

# --- 角色定义 ---
define m = Character("木子米", color="#4db6ac")
define s = Character("素织", color="#ef5350")
define x = Character("路人学长", color="#ffb74d")
define f = Character("木子米父母", color="#8d6e63")
define j = Character("教官", color="#546e7a")
define l = Character("凌宁", color="#81d4fa")
define a = Character("保洁大妈", color="#bdbdbd")
define e = Character("空军少尉", color="#1a237e")
define stu_a = Character("路人同学A", color="#aaaaaa")
define stu_b = Character("路人同学B", color="#aaaaaa")
define stu_c = Character("路人同学C", color="#aaaaaa")
define b = Character("白墨萱", color="#a3a3a3")
define tea_math = Character("高数老师", color="#555555")
define tea_draft = Character("制图老师", color="#5d4037")
define tea_cad = Character("实训老师", color="#3e7d4e")  # 第八新增：电脑实训周老师
define aunt = Character("阿姨", color="#ff8a65")
define unknown = Character("？？？", color="#aaaaaa")

# --- 手机聊天角色 ---
define s_phone = Character("素织", kind=nvl, image="suzhi_icon", what_prefix="【微信】")
define m_phone = Character("木子米", kind=nvl, image="muzimi_icon", what_prefix="【微信】")

# --- 特效定义 ---
define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define soft_shake = Move((5, 0), (-5, 0), .1, bounce=True, repeat=True, delay=0.5)

transform slight_shake:
    linear 2.0 xoffset 10
    linear 2.0 xoffset -10
    repeat

# 慢动作平移（用于草莓牛奶演出）
transform slow_motion_pan:
    xalign 0.0 yalign 0.5
    linear 3.0 xalign 1.0

# 跑步颠簸效果
transform running_shake:
    subpixel True
    block:
        yoffset 0
        linear 0.1 yoffset -10
        linear 0.1 yoffset 0
        repeat

# [第五章新增特效] Q版动画：疯狂乱窜 (木子米逃跑)
transform panic_run_left:
    xalign 0.8 yalign 0.5
    parallel:
        linear 0.5 xalign 0.2
        linear 0.5 xalign 0.8
        repeat
    parallel:
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        repeat

# [第五章新增特效] Q版动画：紧追不舍 (素织追打)
transform chase_run_left:
    xalign 0.9 yalign 0.5 # 紧跟在后面
    parallel:
        linear 0.5 xalign 0.3
        linear 0.5 xalign 0.9
        repeat
    parallel:
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        repeat

# [第五章新增特效] Q版动画：原地蹦跶 (白墨萱够书)
transform jump_attempt:
    xalign 0.5 yalign 0.5
    block:
        linear 0.2 yoffset -60 # 跳起
        linear 0.2 yoffset 0   # 落下
        pause 0.1
        repeat

# ==========================================
# 音频素材定义
# ==========================================
# 前四章音频
define audio.bgm_daily = "audio/bgm_daily.mp3" # 假设补全
define audio.bgm_campus = "audio/bgm_campus.mp3" # 假设补全
define audio.bgm_warm = "audio/bgm_warm.mp3" # 假设补全
define audio.bgm_march = "audio/bgm_march.mp3" # 假设补全
define audio.bgm_military_drum = "audio/bgm_military_drum.mp3" # 假设补全
define audio.bgm_break_time = "audio/bgm_break_time.mp3" # 假设补全
define audio.bgm_depressing_piano = "audio/bgm_depressing_piano.mp3" # 假设补全
define audio.bgm_warm_guitar = "audio/bgm_warm_guitar.mp3" # 假设补全
define audio.bgm_humorous = "audio/bgm_humorous.mp3" # 假设补全
define audio.bgm_bright_violin = "audio/bgm_bright_violin.mp3" # 假设补全
define audio.bgm_stealth_happy = "audio/bgm_stealth_happy.mp3" # 假设补全
define audio.bgm_victory = "audio/bgm_victory.mp3" # 假设补全
define audio.bgm_love = "audio/bgm_love.mp3" # 假设补全

define audio.se_birds = "audio/se_birds.mp3"        # 鸟叫声
define audio.se_foot_stomp = "audio/se_foot_stomp.mp3" # 正步踏步声
define audio.se_crickets = "audio/se_crickets.mp3"     # 蟋蟀/夜晚虫鸣
define audio.se_whistle = "audio/se_whistle.mp3"
define audio.se_stomach = "audio/se_stomach.mp3"
define audio.se_market = "audio/se_market.mp3"
define audio.se_bump = "audio/se_bump.mp3"
define audio.se_window = "audio/se_window.mp3"
define audio.se_cicada = "audio/se_cicada.mp3" # 假设补全
define audio.se_footsteps_crowd = "audio/se_footsteps_crowd.mp3" # 假设补全
define audio.se_pour_water = "audio/se_pour_water.mp3" # 假设补全
define audio.se_drag = "audio/se_drag.mp3" # 假设补全
define audio.se_cough = "audio/se_cough.mp3" # 假设补全
define audio.se_door_kick = "audio/se_door_kick.mp3" # 假设补全

# [第五章新增音频 - 统一命名格式]
define audio.bgm_daily = "audio/bgm_daily.mp3"
define audio.bgm_daily_funny = "audio/bgm_daily_funny.mp3"
define audio.bgm_chase = "audio/bgm_chase.mp3"
define audio.bgm_classroom = "audio/bgm_classroom.mp3"
define audio.bgm_awkward = "audio/bgm_awkward.mp3"
define audio.bgm_daily_warm = "audio/bgm_daily_warm.mp3"
define audio.bgm_school = "audio/bgm_school.mp3"
define audio.bgm_night = "audio/bgm_night.mp3"

define audio.se_bell = "audio/sfx_bell.mp3"
define audio.se_bump_sfx = "audio/sfx_bump.mp3" # 第五章的撞击声
define audio.se_splat = "audio/sfx_splat.mp3"
define audio.se_hit = "audio/sfx_hit.mp3"
define audio.se_book_drop = "audio/sfx_book_drop.mp3"
define audio.se_phone = "audio/sfx_phone.mp3"


# ==========================================
# 图片素材定义
# ==========================================

# --- 素织 (suzhi) ---
image suzhi casual angry = Transform("images/char/suzhi/suzhi casual angry.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual normal = Transform("images/char/suzhi/suzhi casual normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo default = Transform("images/char/suzhi/suzhi camo default.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo surprised = Transform("images/char/suzhi/suzhi camo surprised.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo embarrassed = Transform("images/char/suzhi/suzhi camo embarrassed.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo angry = Transform("images/char/suzhi/suzhi camo angry.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo normal = Transform("images/char/suzhi/suzhi camo normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi camo smile = Transform("images/char/suzhi/suzhi camo smile.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual reading = Transform("images/char/suzhi/suzhi casual reading.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual shy = Transform("images/char/suzhi/suzhi casual shy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
# 脏脸。脸上和衣服上有草莓牛奶污渍。 此注释不允许删除
image suzhi casual wet = Transform("images/char/suzhi/suzhi casual wet.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
# 脱掉外套穿着内衬抱胸  此注释不允许删除
image suzhi shirt shy = Transform("images/char/suzhi/suzhi shirt shy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual gloomy = Transform("images/char/suzhi/suzhi casual gloomy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual surprise = Transform("images/char/suzhi/suzhi casual surprise.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image suzhi casual smile = Transform("images/char/suzhi/suzhi casual smile.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)


# --- 路人学长 (senior) ---
image senior happy = Transform("images/char/senior/senior happy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 教官/少尉 (instructor) ---
image instructor cold = Transform("images/char/instructor/instructor cold.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 凌宁 (lingning) ---
image lingning camo weak = Transform("images/char/lingning/lingning camo weak.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning camo tired = Transform("images/char/lingning/lingning camo tired.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual depressed = Transform("images/char/lingning/lingning casual depressed.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual surprised = Transform("images/char/lingning/lingning casual surprised.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual happy = Transform("images/char/lingning/lingning casual happy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual ashamed = Transform("images/char/lingning/lingning casual ashamed.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning camo default = Transform("images/char/lingning/lingning camo default.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
#pose是jojo形象 尽量少用
image lingning casual pose = Transform("images/char/lingning/lingning casual pose.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual run = Transform("images/char/lingning/lingning casual run.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning casual tired = Transform("images/char/lingning/lingning casual tired.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image lingning camo surprised = Transform("images/char/lingning/lingning camo surprised.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 白墨萱 (baimoxuan) ---
image baimoxuan coat crazy = Transform("images/char/baimoxuan/baimoxuan coat crazy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 高数老师 (mathteacher) ---
# --- 高数老师 (mathteacher) ---
# 30多岁 女性 长相甜美 温柔 此注释不允许删除 
image mathteacher normal = Transform("images/char/mathteacher/mathteacher normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 保洁大妈 (auntie) ---
image auntie working = Transform("images/char/auntie/auntie working.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image auntie confused = Transform("images/char/auntie/auntie confused.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image auntie surprised = Transform("images/char/auntie/auntie surprised.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 制图老师 (tea_draft) ---
image tea_draft strict = Transform("images/char/tea_draft/tea_draft strict.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image tea_draft normal = Transform("images/char/tea_draft/tea_draft normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image tea_draft angry = Transform("images/char/tea_draft/tea_draft angry.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 实训老师 (tea_cad) --- [第八章新增]
image tea_cad normal = Transform("images/char/tea_cad/tea_cad normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image tea_cad smile = Transform("images/char/tea_cad/tea_cad smile.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image tea_cad strict = Transform("images/char/tea_cad/tea_cad strict.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)

# --- 食堂阿姨 (aunt) ---
image aunt happy = Transform("images/char/aunt/aunt happy.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image aunt normal = Transform("images/char/aunt/aunt normal.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)
image aunt confused = Transform("images/char/aunt/aunt confused.png", xsize=3000, ysize=1030, fit="contain", xalign=0.5, yalign=1.0)


# --- 背景定义 ---
image bg park_path = Transform("images/bg/park_path.jpg", fit="cover")
image bg school_gate = Transform("images/bg/school_gate.jpg", fit="cover")
image bg dorm_room_clean   = Transform("images/bg/dorm_room_clean.jpg", fit="cover")
image bg dorm_room_morning  = Transform("images/bg/dorm_room_morning.png", fit="cover")
image bg playground  = Transform("images/bg/playground.jpg", fit="cover")
image bg playground_morning = Transform("images/bg/playground_morning.png", fit="cover")
image bg playground_sunset  = Transform("images/bg/playground_sunset.png", fit="cover")
image bg rest_area_sunset   = Transform("images/bg/rest_area_sunset.png", fit="cover")
image bg playground_night   = Transform("images/bg/playground_night.png", fit="cover")
image bg dorm_boys_night    = Transform("images/bg/dorm_boys_night.jpg", fit="cover")
image bg classroom_clean    = Transform("images/bg/classroom_clean.png", fit="cover")
image bg classroom_full    = Transform("images/bg/classroom_full.png", fit="cover")
image bg rest_area = Transform("images/bg/rest_area.png", fit="cover")
image bg dorm_room_sunset = Transform("images/bg/dorm_room_sunset.jpg", fit="cover")
image bg stairwell = Transform("images/bg/stairwell.jpg", fit="cover")
image bg stadium_grandstand = Transform("images/bg/stadium_grandstand.png", fit="cover")
image bg dining_door = Transform("images/bg/dining_door.png", fit="cover")
image bg dining_inside = Transform("images/bg/dining_inside.png", fit="cover")
image bg stadium_grandstand_sunset = Transform("images/bg/stadium_grandstand_sunset.png", fit="cover")
image bg cafeteria_table = Transform("images/bg/cafeteria_table.png", fit="cover")
image bg classroom_desk = Transform("images/bg/classroom_desk.png", fit="cover")
image bg cafeteria_closeup = Transform("images/bg/cafeteria_closeup.jpg", fit="cover")
image bg library = Transform("images/bg/library.jpg", fit="cover")
image bg black = Transform("images/bg/black.png", fit="cover")
image bg playground_morning_and_morning = Transform("images/bg/playground_morning_and_morning.png", fit="cover")

# --- 第八章新增背景 (复用现有素材) ---
image bg computer_lab = Transform("images/bg/classroom_full.png", fit="cover")  # 电子阅览室
image bg library_shelves = Transform("images/bg/library.jpg", fit="cover")  # 五楼专业书库
image bg library_counter = Transform("images/bg/library.jpg", fit="cover")  # 自助借书机
image bg shop = Transform("images/bg/dining_door.png", fit="cover")  # 小卖部


# --- CG插画定义 ---
image cg eye_contact = Transform("images/cg/eye_contact.jpg", fit="cover")
image cg cleaning_stairs = Transform("images/cg/cleaning_stairs.jpg", fit="cover")
image cg suzhi_camo_smile = Transform("images/cg/suzhi_camo_smile.jpg", fit="cover")
image cg lingning_mechanical = Transform("images/cg/lingning_mechanical.png", fit="cover")
image cg eating_pancakes = Transform("images/cg/eating_pancakes.png", fit="cover")
image cg marching_legs = Transform("images/cg/marching_legs.png", fit="cover")
image cg suzhi_banner = Transform("images/cg/suzhi_banner.png", fit="cover")
image cg campus_road_blur = Transform("images/cg/campus_road_blur.png", fit="cover")
image cg suzhi_reading = Transform("images/cg/suzhi_reading.png", fit="cover")
image cg cafeteria_protect = Transform("images/cg/cafeteria_protect.jpg", fit="cover")
image cg suzhi_night_smile = Transform("images/cg/suzhi_night_smile.jpg", fit="cover")
image cg suzhi_cold_morning = Transform("images/cg/suzhi_cold_morning.png", fit="cover")

# --- 杂项素材 & Q版SD素材 (新增) ---
# 牛奶飞溅
image image_milk_splash = Transform("images/misc/image_milk_splash.png", fit="contain", xalign=0.5, yalign=0.5)
# 生气符号
image icon_angry_mark = Transform("images/misc/icon_angry_mark.png", zoom=0.8)
# 微信头像
image suzhi_icon = Transform("images/misc/suzhi_icon.png", xysize=(150, 150), fit="contain")
image muzimi_icon = Transform("images/misc/muzimi_icon.png", xysize=(150, 150), fit="contain")
# [第五章新增 Q版小人] - 请确保 images/misc/ 目录下有这些文件
image sd_notebook_pig = Transform("images/misc/sd_notebook_pig.png", fit="contain", xalign=0.5, yalign=0.5)
image sd_muzimi_run = Transform("images/misc/sd_muzimi_run.png", fit="contain", xalign=0.5, yalign=0.5)
image sd_suzhi_run = Transform("images/misc/sd_suzhi_run.png", fit="contain", xalign=0.5, yalign=0.5)
image sd_baimoxuan_getbook = Transform("images/misc/sd_baimoxuan_getbook.png", fit="contain", xalign=0.5, yalign=0.5)

# ==========================================
# 第一章：入学
# ==========================================
label start:

    # --- 场景一：动植物公园 ---
    scene bg park_path with fade
    
    play music bgm_daily fadein 1.0

    "（长春的风，似乎总比家乡来得更直爽一些。）"
    "（虽然还是九月初，但在这个位于东北腹地的城市，空气里已经隐约能嗅到一丝秋天的凉意。）"

    m "趁着明天才去长春工程学院报道，今天陪老爸老妈来逛逛这有名的动植物公园。"

    play sound se_bump
    show layer master at vpunch
    "{b}砰！{/b}"

    m "哎哟！"

    show suzhi casual angry at center with dissolve

    voice "voice/suzhi/suzhi_061.ogg"
    s "你走路不看路的吗？"

    m "（揉着肩膀）抱歉抱歉，刚才光顾着看那边的猴山了……"

    "我低下头，发现地上掉了一个精致的挂件。"
    m "啊，你的东西掉了。"

    "我捡起挂件，递了过去。"

    voice "voice/suzhi/suzhi_008.ogg"
    s "（一把夺过，仔细检查了一下）……啧，还好没摔坏。这可是限量版的。"

    m "那个，真的不好意思。我不是故意的。"

    show suzhi casual normal

    voice "voice/suzhi/suzhi_007.ogg"
    s "（叹气）算了，看在你态度诚恳的份上。"
    voice "voice/suzhi/suzhi_095.ogg"
    s "这里人多，下次小心点。长这么大个子，别像个没头苍蝇似的。"

    m "（苦笑）是是是，受教了。"

    hide suzhi with easeoutright

    m "（看着她离开的方向）真是个脾气有点冲的女生啊……不过，长得倒是挺好看的。"
    m "算了，一个小插曲而已。还是赶紧跟上老爸老妈吧。"

    stop music fadeout 1.0

    # --- 场景二：校门口 ---
    scene bg school_gate with fade
    
    play music bgm_campus fadein 1.0

    "（长春工程学院。）"
    "（这就是我未来四年要生活的地方吗？）"
    m "（土木工程系……听说是这个学校的王牌专业，看来以后的日子不会太轻松啊。）"

    f "儿子！别发呆了，行李箱提好！"
    m "来了来了！"

    show senior happy at center with dissolve

    x "哎！那边的学弟！是土木系的吧？来来来，家长把行李给我，我带你们去办手续！"
    m "谢谢学长！麻烦您了。"
    x "客气啥！到了长工程就是一家人！咱们土木那是杠杠的！走，先带你们去宿舍！"

    # --- 场景三：宿舍 ---
    scene bg dorm_room_clean with fade
    
    play music bgm_warm fadein 1.0

    x "到了，这就是传说中的 {b}六公寓{/b} 。这可是咱们学校条件数一数二的楼了。"

    m "（环顾四周，放下行李）哇……"

    play sound se_window
    "我走到阳台边，推开窗户。"

    m "（感叹）真不错啊！"
    m "我原本以为北方的宿舍会比较粗犷，没想到这六公寓这么宽敞，采光也好，而且看起来很新。"
    m "看来我运气不错，分到了个好窝。"

    show senior happy at right with moveinright

    x "哈哈，那是！六公寓可是风水宝地。行了学弟，你先收拾着，明天早上操场集合，别迟到啊！"

    m "好的，谢学长！"

    hide senior with dissolve

    scene black with dissolve
    "在父母帮忙铺好床铺后……"

    scene bg dorm_room_clean with dissolve
    "（躺在陌生的床上，看着天花板。）"
    m "（新的生活，就要开始了吗？希望一切顺利吧。）"

    stop music fadeout 1.0

    # --- 场景四：操场 ---
    scene bg playground with fade
    
    play music bgm_march fadein 1.0

    voice "voice/jiaoguan/jiaoguan_023.ogg"
    j "全体都有！立正——！向右看齐！"

    m "（嘶……这九月的太阳怎么比昨天还毒。）"
    m "（土木工程系的方队……应该是这里吧。）"

    "我急匆匆地跑入队伍末尾。"

    m "报告！"
    voice "voice/jiaoguan/jiaoguan_019.ogg"
    j "入列！下次早点！"
    m "是！"

    "我站定，擦了擦汗，下意识地往旁边的女生队列看了一眼。"
    m "（咱们土木系的女生可是稀有动物，不知道有没有长得好看的……）"

    # 镜头推近
    show bg playground:
        ease 1.0 zoom 1.5 align (0.5, 0.5)

    show suzhi camo default at center with dissolve

    m "（瞳孔地震）嗯？！"

    "此时，她似乎感觉到了视线，转过头来。"

    # --- CG 播放 ---
    stop music
    scene cg eye_contact with flash

    voice "voice/suzhi/suzhi_004.ogg"
    s "……是你？！"
    m "……是你？！"

    # 恢复场景
    scene bg playground 
    
    show suzhi camo surprised at center
    with fade

    voice "voice/suzhi/suzhi_023.ogg"
    s "（惊讶地指着我）那个动物园的冒失鬼？"
    m "（惊讶地指着她）那个脾气很冲的……"

    voice "voice/jiaoguan/jiaoguan_060.ogg"
    j "那边那两个！干什么呢！眉来眼去的！出列！"

    show suzhi camo embarrassed with vpunch

    m "（尴尬地小声说）完蛋……"
    voice "voice/suzhi/suzhi_103.ogg"
    s "（咬牙切齿地小声说）都怪你……"

    m "（我做梦也没想到。）"
    m "（那个在动物园跟我有过节的女生，不仅是我的校友。）"
    m "（居然还是同一个专业、站在同一个方队的同学！）"
    m "（我的大学生活，看来注定没法平静了……）"

    centered "第一章 完"
    jump chapter_2


label chapter_2:

    # 【场景一：长春工程学院 - 西操场 - 上午】
    scene bg playground_morning
    with fade

    # BGM：节奏单调、略带压抑的军训鼓点
    play music audio.bgm_military_drum loop
    # 音效：知了的叫声，嘈杂且烦人
    play sound audio.se_cicada loop

    # (画面微微晃动，模拟站军姿时的眩晕感)
    show bg playground_morning at slight_shake

    m "(腿……已经没有知觉了。)"
    m "(汗水顺着鬓角流进眼睛里，咸涩得让人想流泪，但我连眨眼都不敢太用力。)"
    m "(这就是长春工程学院的军训吗？传说中的“土木铁军”第一课，果然名不虚传。)"

    show instructor cold at center with dissolve
    voice "voice/jiaoguan/jiaoguan_048.ogg"
    e "（声音不大，但透着一股冷冽的穿透力）第三排那个戴眼镜的，眼神乱飘什么？"
    voice "voice/jiaoguan/jiaoguan_039.ogg"
    e "是不是觉得这身军装不够帅，想去跑两圈展示一下身材？"
    # (全场寂静，只有风吹过衣角的猎猎声，几个女生忍不住偷瞄教官挺拔的侧脸)
    stop sound fadeout 1.0

    m "(余光瞥向右前方）"
    m "(素织就在那里。)"
    m "(她站得笔直，帽檐压得很低，看不清表情，但那倔强的下巴线条清晰可见。)"
    m "(明明是个看起来挺娇气的女生，没想到毅力比凌宁还要强。)"

    # (镜头切换至凌宁)
    hide instructor
    show lingning camo weak at center with dissolve
    
    voice "voice/lingning/lingning_105.ogg"
    l "木子米……我恐怕已到极限了……今日的阳光真是无情啊。"
    
    voice "voice/lingning/lingning_061.ogg"
    l "若此刻能有一杯加冰的柠檬水，当是人间至福……"

    m "别说话了，凌宁。再坚持五分钟，少尉看表了。"

    voice "voice/lingning/lingning_158.ogg"
    l "五分钟？这简直度日如年。看着那位教官冷峻的面容，我只觉得比烈日还要难熬。"
    
    voice "voice/lingning/lingning_073.ogg"
    l "我现在……哪怕是一口普通的自来水，也会感激涕零的"
    show instructor cold at center with dissolve
    hide lingning

    voice "voice/jiaoguan/jiaoguan_022.ogg"
    e "全体都有！稍息！"
    voice "voice/jiaoguan/jiaoguan_057.ogg"
    e "（摘下墨镜，露出一双锐利的眼睛，环视一周）讲一下。"
    voice "voice/jiaoguan/jiaoguan_002.ogg"
    e "上午的训练，整体表现尚可，但个别同学意志力薄弱。"
    voice "voice/jiaoguan/jiaoguan_056.ogg"
    e "记住，你们是未来的工程师，连这点苦都吃不了，以后怎么去工地？"
    voice "voice/jiaoguan/jiaoguan_061.ogg"
    e "鉴于刚才有人乱动，延长十五分钟站姿体验。"

    show lingning camo weak at right with dissolve
    
    voice "voice/lingning/lingning_003.ogg"
    l "哎……天亡我也。"

    voice "voice/jiaoguan/jiaoguan_058.ogg"
    e "谁在叹气？很有个性嘛。再加五分钟。"

    # (一片死寂，所有人的心里都在滴血，但碍于少尉的气场，没人敢出声)
    hide lingning
    hide instructor

    m "( 绝望。)"
    m "(此刻，操场边那一排摆放整齐的水瓶，简直散发着圣洁的光辉。)"
    m "(那是我们最后的希望。)"

    # 【场景二：操场边缘 - 休息区 - 二十分钟后】
    stop music fadeout 1.0
    scene bg rest_area
    with fade

    # BGM：欢快的休息音乐，夹杂着嘈杂的人声
    play music audio.bgm_break_time loop
    # 音效：人群轰然散开的脚步声
    play sound audio.se_footsteps_crowd

    show instructor cold at center
    voice "voice/jiaoguan/jiaoguan_055.ogg"
    e "解散！休息二十分钟！"
    hide instructor with dissolve

    show lingning camo tired at center
    
    voice "voice/lingning/lingning_115.ogg"
    l "水……我的生命之源，我来了。"

    # (凌宁虽然极度口渴，但依然保持着快步走的姿态，而不是像其他人那样狂奔，木子米紧随其后)
    # (画面切换：放水区)
    # (此时，一个穿着蓝色保洁服的大妈正背对着学生们，手里拿着一个巨大的黑色塑料袋。她动作麻利地拿起地上的水瓶，拧开盖子，哗啦一声倒掉里面的水，然后将瓶子踩扁扔进袋子)
    
    hide lingning
    show auntie working at center
    # 音效：倒水声
    play sound audio.se_pour_water

    show lingning camo surprised at left with vpunch
    
    voice "voice/lingning/lingning_053.ogg"
    l "天哪……？"

    # (木子米也停下了脚步，愣住了)
    # (只见大妈并没有停手，她拿起半瓶还剩很多的矿泉水，那是凌宁特意用手帕擦拭过瓶身的，毫不犹豫地倒进了旁边的排水沟)
    play sound audio.se_pour_water

    voice "voice/lingning/lingning_099.ogg"
    l "且慢！阿姨！请手下留情！"

    a "啥？"

    voice "voice/lingning/lingning_043.ogg"
    l "那是我的水……我才刚刚买来，才喝了一小口。你为何要将它倒掉？"

    a "这地儿不让乱扔垃圾。我看这瓶子都在地上晒半天了，寻思是没人要的。"

    voice "voice/lingning/lingning_012.ogg"
    l "怎会是没人要的？我们在那训练呢，瓶子当然在地上晒着了"

    # (周围的同学也围了过来，因为极度的干渴和疲惫，大家的情绪都像火药桶一样)
    stu_a "就是啊，我那瓶也是满的！"
    stu_b "怎么这样啊，我们累死累活的，连口水都不让喝？"
    stu_c "这大妈是不是为了卖瓶子赚钱疯了啊？"

    # (素织也走了过来，手里拿着空瓶子，显然她原本也想来喝水，却发现自己的水也没了)
    show suzhi camo normal at right
    voice "voice/suzhi/suzhi_035.ogg"
    s "阿姨，我们在训练，水瓶放在这是为了休息时喝。"
    voice "voice/suzhi/suzhi_056.ogg"
    s "您不问一声就倒掉，是不是太过分了？"
    a "我看这水都被太阳晒热了，塑料瓶晒久了有毒！"
    a "再说，这一地乱七八糟的，领导检查看见了要扣俺工资的！"
    
    voice "voice/lingning/lingning_045.ogg"
    l "即便有毒，那也是我们自己的选择！您……您怎么能这样不近人情？"
    
    voice "voice/lingning/lingning_078.ogg"
    l "我们真的快要渴晕过去了"
    
    voice "voice/lingning/lingning_001.ogg"
    l "……扣工资并非小事, 但这也不是您随意处置他人财物的理由啊！"
    a "你这学生咋说话呢！俺这是为了你们好！"
    a "这一地的瓶子，哪瓶是谁的你们分得清吗？万一喝错了传染病咋整？"

    m "（眼看局势要失控）凌宁，冷静点。"

    voice "voice/lingning/lingning_106.ogg"
    l "木子米，这让我如何冷静？这简直是……简直是不可理喻！"

    # (就在这时，一道挺拔的身影挡住了阳光)
    show instructor cold at center with dissolve
    hide auntie
    hide suzhi
    hide lingning

    voice "voice/jiaoguan/jiaoguan_028.ogg"
    e "吵什么？很有精神嘛。"
    
    show lingning camo weak at left
    
    voice "voice/lingning/lingning_102.ogg"
    l "教官，这位阿姨将我们的饮用水全部处理掉了，我们在试图……讲道理。"

    voice "voice/jiaoguan/jiaoguan_054.ogg"
    e "（冷冷地扫了一眼满地的空瓶和大妈手里的袋子，眉头微皱）行了。多大点事？没水了再去买。"
    voice "voice/jiaoguan/jiaoguan_033.ogg"
    e "（目光如炬地盯着凌宁）对着长辈大声喧哗，这就是你的教养？你的军人风度呢？"

    voice "voice/lingning/lingning_086.ogg"
    l "我……并非有意喧哗，只是……"

    voice "voice/jiaoguan/jiaoguan_021.ogg"
    e "全体都有！因为不懂得尊重他人，罚站十分钟！好好反省一下什么是素质！"

    m "（一把拉住凌宁）别解释了，教官不会听的。"

    # (凌宁委屈地闭上了嘴，眼神中满是不解和受伤，看了一眼大妈，最终叹了口气。大妈提着黑袋子，嘴里嘟囔着听不清的话，转身走了)
    hide lingning
    hide instructor
    
    # (素织看着大妈的背影，又看了一眼虽然委屈但依然站得笔直的凌宁，若有所思)
    show suzhi camo default at center with dissolve
    pause 1.0

    # 【场景三：六公寓 - 走廊 - 傍晚】
    stop music fadeout 1.5
    scene bg stairwell
    with fade

    # BGM：低沉、压抑的钢琴曲
    play music audio.bgm_depressing_piano

    m "(下午的训练简直是地狱。)"
    m "(空军少尉虽然长得帅，但罚起人来简直是魔鬼。)"
    m "(大家心里都憋着一股火，那股火全冲着那个保洁大妈去了。)"
    m "(“那个贪财的大妈”、“那个不可理喻的老太婆”……各种难听的绰号在新生群里传开了。)"
    m "(虽然大妈的做法确实不对，但大家的话是不是太重了点？)"

    # (木子米拿着脸盆准备去水房洗漱，路过楼梯间时，听到了奇怪的声音)
    # 【音效：沉重的拖拽声，偶尔伴随着咳嗽声】
    play sound audio.se_drag
    queue sound audio.se_cough

    m "嗯？"
    
    # (木子米停下脚步，透过楼梯间的缝隙看去)
    # (CG图：昏暗的楼梯拐角，保洁大妈正跪在地上。她并没有在整理卖钱的瓶子，而是在用抹布一点一点擦拭台阶上的泥印。那是男生们白天军训回来时，鞋底带着的泥土)
    
    scene cg cleaning_stairs with dissolve

    m "（心中一震）那是……"

    a "哎哟……这帮娃娃，咋就把地踩得这么脏。明天领导来检查卫生，要是这块儿不干净，又要挨批了。"

    # (大妈费力地站起来，旁边放着那个巨大的黑色塑料袋。袋子口敞开着，木子米惊讶地发现，里面并没有多少瓶子，反而塞满了各种被踩扁的易拉罐、废纸团，还有……几双看起来像是被扔掉的破鞋垫)
    
    a "这瓶里剩那么多水，晒了一天，塑料味儿那么大，喝了坏肚子咋整。现在的孩子，咋就不懂呢。"

    m "……"

    # (木子米此时才注意到，大妈的身旁放着一个巨大的不锈钢保温桶，上面贴着一张歪歪扭扭的纸条，写着“绿豆汤”三个字)

    a "这绿豆汤也凉了，本来寻思给他们解解暑，结果一个个凶得像小老虎……"
    a "尤其是那个长得挺白净的小伙子，看着挺斯文，急起来脸都红了。"
    a "算了，倒了吧，明天再熬新的。"
    m "(我的胸口像是被什么东西撞了一下。)"
    m "(原来……是这样吗？)"
    m "(我们以为她是贪图瓶子的小便宜，以为她是无理取闹。)"
    m "(却没人想过，在她的认知里，暴晒后的陈水确实是“脏水”。)"
    m "(她甚至……还准备了绿豆汤。)"

    # (木子米深吸一口气，推开了楼梯间的门)
    # 【场景四：楼梯间 - 傍晚】
    scene bg stairwell
    with dissolve
    
    # BGM：温暖、舒缓的吉他曲
    play music audio.bgm_warm_guitar

    show auntie surprised at center
    m "阿姨。"

    a "哎呀妈呀！吓死俺了……是你啊小伙子，你是那个……那个不咋说话的。你也来骂俺？"

    m "不是。阿姨，我来帮您倒垃圾吧。"

    a "啊？不用不用！脏！你们是大学生，是拿笔杆子的手，哪能干这个。"

    m "没事，我们在家也干活。而且这泥印也是我们踩的，该我们不好意思才对。"

    a "这孩子……怪懂事的。"

    m "阿姨，白天的事儿，大家是太渴了，火气大。您别往心里去。其实大家都知道您辛苦。"

    a "我不怪你们。俺就是……嘴笨"
    a "我寻思那水晒热了不能喝，我家那孙子要是喝了这种水，肯定要打手板的。"
    a "本来想告诉你们这有绿豆汤，结果那白净小伙一急，我就懵了。"
    m "原来这绿豆汤是给我们的？"

    a "是啊！天这么热，俺看你们站得脸都白了。这是俺自己掏钱买的绿豆，放了冰糖呢！"

    m "阿姨，这汤别倒。正好大家都渴着呢。"

    # 【场景五：男生宿舍 - 晚上】
    stop music fadeout 1.0
    scene bg dorm_boys_night
    with fade

    # BGM：轻松、幽默的日常曲
    play music audio.bgm_humorous loop

    # 背景：乱糟糟的男生宿舍，凌宁正坐在床上，手里拿着一本书，但显然看不进去
    show lingning casual depressed at center
    
    voice "voice/lingning/lingning_114.ogg"
    l "真是令人郁闷。我实在无法理解，那位阿姨为何要这般固执。还有那位少尉，虽说军令如山，但也太不通人情了……"

    # (砰的一声，宿舍门被踢开)
    play sound audio.se_door_kick
    with vpunch

    m "（抱着那个巨大的不锈钢保温桶）凌宁，拿碗来！"

    show lingning casual surprised at center
    
    voice "voice/lingning/lingning_112.ogg"
    l "木子米？你抱着这庞然大物是何意？莫非是食堂的存货？"

    m "抢什么抢。这是“赔偿”。"

    voice "voice/lingning/lingning_131.ogg"
    l "赔偿？"

    m "那个大妈给的。绿豆汤，冰糖的。"

    voice "voice/lingning/lingning_098.ogg"
    l "真的吗？她会有这般好意？……不会有什么问题吧？"

    m "喝不喝？不喝我给隔壁寝室了。"

    voice "voice/lingning/lingning_065.ogg"
    l "嗯？！……啊，真是舒畅！天哪，竟是冰镇的！"
    
    voice "voice/lingning/lingning_025.ogg"
    l "这绿豆熬得恰到好处，口感绵密，甜度适中……"

    # (木子米把事情的原委，包括大妈擦地、担心暴晒水质变质的事情，原原本本地讲了一遍)
    
    show lingning casual ashamed at center
    
    # (宿舍里渐渐安静下来，凌宁捧着空碗，白皙的脸庞泛起了一丝红晕，表情变得非常惭愧)

    voice "voice/lingning/lingning_015.ogg"
    l "呃……你是说，她是担心水质变坏才倒掉的？"

    m "嗯。而且她怕我们中暑，特意熬的汤，结果被你急切的样子吓得不敢拿出来。"

    voice "voice/lingning/lingning_031.ogg"
    l "这……这让我显得像是无理取闹的纨绔子弟一般。"
    
    voice "voice/lingning/lingning_004.ogg"
    l "哎，我今日的举止实在是有失风度，竟误解了一位长辈的好意。"
    
    voice "voice/lingning/lingning_052.ogg"
    l "真是……太失礼了"

    m "行了，明天见到人家，知道该咋办了吧？"

    show lingning casual happy at center
    
    voice "voice/lingning/lingning_062.ogg"
    l "自然！我定当诚恳致歉，绝不推脱！"

    # 【场景六：操场 - 休息区 - 次日中午】
    stop music fadeout 1.5
    scene bg playground
    with fade

    # BGM：明亮、温馨的钢琴与小提琴合奏
    play music audio.bgm_bright_violin loop

    # (休息哨声响起)
    play sound audio.se_whistle

    # (这一次，没人再抱怨水的事。凌宁整理了一下军装，深吸一口气，走到正在收拾垃圾的保洁大妈面前)
    show auntie surprised at right
    show lingning camo default at left
    
    voice "voice/lingning/lingning_018.ogg"
    l "阿姨……请留步。"

    a "干啥？"

    voice "voice/lingning/lingning_149.ogg"
    l "（突然非常标准地鞠了一躬）真的非常抱歉！"
    
    voice "voice/lingning/lingning_103.ogg"
    l "昨日是我鲁莽了，言语多有冒犯，请您原谅！"
    
    voice "voice/lingning/lingning_039.ogg"
    l "还有……您的绿豆汤美味至极，万分感谢您的关照！"

    a "哎呀，你这孩子，咋行这么大礼。"
    a "好喝就行，好喝就行！今天还有呢！"
    a "看你这白白净净的，多喝点解暑！"

    # (周围的同学都善意地笑了起来，气氛瞬间变得融洽)
    # (木子米站在人群外，微笑着看着这一幕)
    # (突然，一阵清风吹过，淡淡的香气传来)

    hide auntie
    hide lingning
    with dissolve

    voice "voice/suzhi/suzhi_068.ogg"
    s "看来，误会解除了？"

    # (木子米转头，发现素织不知何时站在了他身边，手里拿着一瓶水)
    show suzhi camo normal at center with dissolve

    m "是啊。有时候，眼睛看到的并不一定是真相。大家只是立场不同罢了。"

    voice "voice/suzhi/suzhi_116.ogg"
    s "听说是你昨天晚上去跟阿姨沟通的？"

    m "碰巧遇到了而已。"

    show suzhi camo smile at center
    voice "voice/suzhi/suzhi_132.ogg"
    s "（看不出来，你这人虽然看着呆呆的，办事还挺靠谱的。"
    voice "voice/suzhi/suzhi_022.ogg"
    s "连那个冷冰冰的少尉刚才都夸了我们班风气不错。"

    # (CG图：素织的特写。阳光透过树叶洒在她脸上，那原本清冷的眸子里，此刻倒映着木子米的影子，带着一丝认可和温柔)
    scene cg suzhi_camo_smile with dissolve

    voice "voice/suzhi/suzhi_080.ogg"
    s "喏，这个给你。"

    m "这是？"

    voice "voice/suzhi/suzhi_115.ogg"
    s "昨天看你水也没了，今天多买了一瓶。"
    voice "voice/suzhi/suzhi_001.ogg"
    s "算是……替那个有些少爷脾气但还算懂事的室友，谢谢你的绿豆汤情报。"

    # (素织转身离开，马尾辫在脑后轻轻晃动)
    
    m "（握着还有些冰凉的水瓶，心跳似乎漏了一拍）"
    m "谢我……吗？"

    m "(手中的矿泉水瓶上还凝结着水珠。)"
    m "(那个“大妈倒水风波”，就这样以一种意想不到的温馨方式画上了句号。)"
    m "(而我和素织之间，似乎也因为这场小小的风波，有了一些不一样的默契。)"
    m "(长春的秋天，好像也没那么冷了。)"

    # 【第二章 完】

    jump chapter_3

# ==========================================
# 剧本正文 - 第三章：正步与心跳的共鸣
# ==========================================

label chapter_3:

    # 【场景一：操场 - 清晨 - 军训第二周】
    # 模拟睡眼惺忪，从模糊逐渐变清晰
    scene bg dorm_room_morning with fade
    play music audio.bgm_daily fadein 1.0
    play sound audio.se_birds loop

    # 内心独白
    m "（早晨五点半。）"
    m "（生物钟已经完全被军号声驯化了。）"
    m "（长春的九月中旬，早晚温差开始显现。从温暖的被窝里爬出来钻进冰凉的迷彩服，需要莫大的勇气。）"

    # 凌宁画外音
    voice "voice/lingning/lingning_002.ogg"
    l "啊……这清晨的寒气，简直是在侵蚀我的灵魂。"

    # 立绘出现：凌宁。虽然穿着迷彩服，但他的扣子扣得一丝不苟
    show lingning camo weak at center with dissolve

    voice "voice/lingning/lingning_109.ogg"
    l "木子米，你看我的脸色是否有些苍白？这几日的紫外线虽然强烈，但这早晨的寒风更是肌肤的大敌。"

    m "（整理着腰带）看起来挺红润的，凌宁。赶紧吧，迟到一分钟，少尉的眼神能把你冻成冰雕。"

    show lingning camo tired
    
    voice "voice/lingning/lingning_154.ogg"
    l "（打了个寒颤）哦，那位冷面骑士。不得不说，他的威严确实令人折服，但能否稍微……温柔那么一点点？"

    m "走吧，听说今天有重要宣布。"

    stop sound fadeout 1.0
    stop music fadeout 1.0

    # 【场景二：操场 - 集合点 - 上午】
    scene bg playground_morning with fade
    play music audio.bgm_military_drum fadein 2.0

    # 背景：整齐排列的新生方阵，阳光开始变得刺眼
    # 空军少尉登场
    show instructor cold at center

    voice "voice/jiaoguan/jiaoguan_024.ogg"
    e "（拿着扩音器，声音穿透力极强）全体都有！立正！"
    voice "voice/jiaoguan/jiaoguan_052.ogg"
    e "经过一周的适应性训练，你们已经初步具备了军人的模样。但是，这还不够！"
    voice "voice/jiaoguan/jiaoguan_006.ogg"
    e "下周五，将举行全校新生军训汇报表演。这是检验你们成果的时刻，也是展现土木系风采的时刻！"

    # 台下一阵骚动
    play sound audio.se_footsteps_crowd # 模拟骚动声

    voice "voice/jiaoguan/jiaoguan_032.ogg"
    e "安静！"
    voice "voice/jiaoguan/jiaoguan_010.ogg"
    e "为了保证汇演效果，从今天开始，我们将重新编队。所有人将被打散，重新划分为三个部分："
    voice "voice/jiaoguan/jiaoguan_047.ogg"
    e "第一，分列式方队。这是最精锐的部队，将代表系里走过主席台，接受检阅。要求动作标准，身材匀称，意志力强！"
    voice "voice/jiaoguan/jiaoguan_051.ogg"
    e "第二，合唱团。负责在看台上唱军歌，展现气势。"
    voice "voice/jiaoguan/jiaoguan_049.ogg"
    e "第三，观训营。身体素质无法适应高强度训练的，进入观训营。"

    # 少尉顿了顿
    voice "voice/jiaoguan/jiaoguan_026.ogg"
    e "分列式方队，是荣誉，也是地狱。训练强度将是现在的两倍。怕苦的，现在就可以后退一步去合唱团。"

    # 人群中出现了短暂的沉默
    hide instructor

    m "（两倍强度……）"
    m "（理智告诉我，去合唱团摸鱼是个不错的选择。)"
    m "(凌宁肯定会选合唱团吧，毕竟那里不用晒太阳，还能发挥他那“贵族般”的嗓音。）"
    m "（但是……）"

    # 木子米下意识地看向不远处的女生队列
    # CG片段：人群中的素织。
    # 这里使用立绘模拟CG的聚焦感
    show suzhi camo normal at center with dissolve

    m "（她肯定会留下的。）"
    m "（如果我现在退缩了，好像……就输了什么东西。）"
    hide suzhi with dissolve

    show lingning camo default at center with moveinright

    voice "voice/lingning/lingning_108.ogg"
    l "木子米，虽然我的双腿在抗议，但身为七尺男儿，若连挑战都不敢面对，岂不是有辱斯文？"

    m "凌宁？你想进方队？"

    voice "voice/lingning/lingning_097.ogg"
    l "自然。荣誉即吾命。哪怕是倒下，我也要倒在冲锋的路上……或者正步的路上。"

    m "好，那我们一起。"

    # 【场景三：操场中央 - 选拔现场 - 上午】
    scene bg playground with fade
    play music audio.bgm_march fadein 1.0
    
    # 音效：整齐的踏步声
    play sound audio.se_foot_stomp

    show instructor cold at center
    voice "voice/jiaoguan/jiaoguan_046.ogg"
    e "第一排，出列！正步走！"
    
    # 几名男生踢着正步走过
    voice "voice/jiaoguan/jiaoguan_017.ogg"
    e "停！第三个，顺拐了，去合唱团。第五个，罗圈腿太严重，去合唱团。第一个，留下。"

    # 残酷的筛选在继续
    voice "voice/jiaoguan/jiaoguan_004.ogg"
    e "下一组！"
    hide instructor

    # 轮到女生组了
    show suzhi camo normal at center with dissolve

    m "（即使在一群穿着同样迷彩服的女生中，素织依然很显眼。）"
    m "（她的动作很利落，没有多余的晃动。）"

    voice "voice/jiaoguan/jiaoguan_041.ogg"
    e "正步——走！"
    play sound audio.se_foot_stomp

    # 素织踢腿带风，摆臂定格准确
    show suzhi camo angry # 表现凛冽的英气

    voice "voice/jiaoguan/jiaoguan_016.ogg"
    e "（眼中闪过一丝赞赏，但很快掩饰住）停！"
    voice "voice/jiaoguan/jiaoguan_050.ogg"
    e "第二个（指素织），不错。踢腿高度标准，落地有声。入列，第一排面。"

    voice "voice/suzhi/suzhi_074.ogg"
    s "（大声）是！"

    # 素织出列，站在了象征“精锐”的指定区域
    hide suzhi
    show suzhi camo normal at right
    # 眼神交互
    # 素织微微侧头，似乎在人群中寻找着什么
    
    m "（该我了。）"
    hide suzhi

    show instructor cold at center
    voice "voice/jiaoguan/jiaoguan_005.ogg"
    e "下一组！正步——走！"

    m "（绷直脚尖。）"
    m "（压住重心。）"
    m "（不要晃动。）"
    m "（我感觉全身的肌肉都在紧绷，每一次砸地都震得脚底发麻。）"

    voice "voice/jiaoguan/jiaoguan_014.ogg"
    e "停！"
    # 教官走到面前
    voice "voice/jiaoguan/jiaoguan_045.ogg"
    e "（上下打量）眼镜扶好。眼神再犀利点，别像没睡醒一样。"
    voice "voice/jiaoguan/jiaoguan_007.ogg"
    e "不过，节奏感不错，身板也直。入列。"

    m "是！"
    hide instructor

    # 木子米跑向指定区域。路过素织所在的队列时，两人的目光短暂交汇
    scene cg suzhi_camo_smile with dissolve
    pause 1.0
    
    m "（素织微微挑眉，似乎在说：“你也来了？”）"
    m "（我回以一个淡淡的微笑：“当然。”）"

    # 然而，并不是所有人都有好运
    scene bg playground with fade
    voice "voice/jiaoguan/jiaoguan_003.ogg"
    e "下一组！"

    # 凌宁上场了
    # 切换到凌宁机械舞CG
    stop music fadeout 0.5
    play music audio.bgm_humorous fadein 0.5
    show cg lingning_mechanical with vpunch

    voice "voice/jiaoguan/jiaoguan_015.ogg"
    e "停！"
    voice "voice/jiaoguan/jiaoguan_059.ogg"
    e "（皱眉）那个白净的男生，你在跳机械舞吗？"

    voice "voice/lingning/lingning_094.ogg"
    l "报告教官！我正在努力控制肌肉的平衡，试图达到力与美的统一！"

    voice "voice/jiaoguan/jiaoguan_035.ogg"
    e "（忍住笑）很有想法。但是正步需要的是爆发力，不是优雅。"
    voice "voice/jiaoguan/jiaoguan_012.ogg"
    e "你的协调性还得练练。去合唱团吧，那边可能更适合你的……气质。"
    
    voice "voice/lingning/lingning_156.ogg"
    l "（如遭雷击，摇摇欲坠）教官……能不能再给我一次机会？我可以……"

    voice "voice/jiaoguan/jiaoguan_040.ogg"
    e "服从命令！"
    
    voice "voice/lingning/lingning_148.ogg"
    l "（行了一个有些悲壮的军礼）是……"

    hide cg lingning_mechanical
    scene bg playground
    show lingning camo tired at center

    # 凌宁垂头丧气地走向合唱团区域
    
    voice "voice/lingning/lingning_143.ogg"
    l "（投来了一个“你要连我的份一起努力”的哀怨眼神）"

    # 【场景四：分列式方队训练区 - 下午】
    scene bg playground_sunset with fade
    stop music fadeout 1.0
    play music audio.bgm_depressing_piano fadein 1.0

    # 字幕：分列式方队正式成立
    centered "分列式方队正式成立"

    show instructor cold at center
    voice "voice/jiaoguan/jiaoguan_036.ogg"
    e "恭喜你们，留到了最后。"
    voice "voice/jiaoguan/jiaoguan_011.ogg"
    e "但不要高兴得太早。从现在起，你们不再是个体，而是一个整体。"
    voice "voice/jiaoguan/jiaoguan_038.ogg"
    e "方队的要求只有一个：整齐划一。"
    voice "voice/jiaoguan/jiaoguan_001.ogg"
    e "一人出错，全队受罚！"

    # 接下来的几个小时，是枯燥到令人发指的单兵动作定型
    voice "voice/jiaoguan/jiaoguan_027.ogg"
    e "右腿踢出！定住！谁敢动！"
    voice "voice/jiaoguan/jiaoguan_053.ogg"
    e "脚尖下压！把腿抬高！"

    m "（一分钟……两分钟……）"
    m "（这种单腿站立的姿势简直是反人类的。）"
    m "（汗水流进眼睛里，好痛。）"
    m "（我偷瞄了一眼侧前方。那是女生方队的方阵。）"

    # 展示腿部特写CG
    show cg marching_legs with dissolve

    m "（素织就在那里，第一排的最左侧，也就是所谓的“排头兵”。）"
    m "（那个位置是全队的基准，压力最大。）"

    # 突然，素织身体晃了一下
    with soft_shake

    voice "voice/jiaoguan/jiaoguan_031.ogg"
    e "（立刻捕捉到）女生方队第一排排头！晃什么！腿软了？"

    voice "voice/suzhi/suzhi_073.ogg"
    s "（咬牙，大声）报告！没有！"

    voice "voice/jiaoguan/jiaoguan_043.ogg"
    e "没有就给我站稳！排头兵要是倒了，整个方队就垮了！再加两分钟定型！"

    # 周围传来轻微的抱怨声
    unknown "（小声）哎呀，累死了……都怪排头……"

    m "（素织的背影明显僵硬了一下，但她没有说话，只是把腿抬得更高了，甚至超过了标准线。）"
    m "（她是个要强的人。）"
    m "（这种时候，她肯定比谁都难受。）"
    m "（那些抱怨声，像针一样扎在她身上吧。）"

    hide cg marching_legs with dissolve

    # 【场景五：训练间隙 - 休息区】
    scene bg rest_area_sunset with fade
    play music audio.bgm_break_time fadein 1.0

    # 背景：夕阳西下，大家瘫坐在草地上
    # 素织一个人坐在稍微远一点的树荫下
    show suzhi camo normal at center with dissolve

    m "（犹豫了一下，走过去）还好吗？"

    # 素织迅速穿上鞋，警惕地抬头
    show suzhi camo surprised
    voice "voice/suzhi/suzhi_006.ogg"
    s "是你啊。没事。"

    m "（指了指她的脚）刚才定型的时候，我看你有点抖。是不是鞋磨脚？"

    show suzhi camo embarrassed
    voice "voice/suzhi/suzhi_113.ogg"
    s "（沉默了一会儿，偏过头）新鞋都这样。而且……作为排头，我不能让人觉得我娇气。"

    m "没人觉得你娇气。能坚持下来已经很厉害了。"

    show suzhi camo normal
    voice "voice/suzhi/suzhi_017.ogg"
    s "（自嘲地笑了一下）刚才害大家多站了两分钟，肯定有人在心里骂我。"

    m "（坐到她旁边，保持着礼貌的距离）那是教官严厉，不怪你。而且……"
    m "你刚才把腿抬高纠正姿势的时候，真的很帅。"

    # 素织愣了一下，转过头看着木子米
    show suzhi camo smile
    voice "voice/suzhi/suzhi_077.ogg"
    s "帅？你是第一个用这个词形容女生的。"

    m "在这里，这可是最高评价。"

    # 素织轻轻笑了一声，原本紧绷的肩膀放松了下来
    s "你也不赖。男生方队在后面，我也听到了，你们那个踢腿的声音，挺响的。"

    m "哈哈，那是为了掩盖我们整齐度不够的事实，用音量凑数。"

    # 凌宁突然出现
    show lingning casual pose at left with moveinleft
    
    voice "voice/lingning/lingning_019.ogg"
    l "噢，多么和谐的画面。而我，一个被流放到合唱团的孤独灵魂，只能在远处吟唱悲伤的旋律。"

    m "凌宁！你来慰问我们了？"

    voice "voice/lingning/lingning_142.ogg"
    l "（递过饮料，姿态依然优雅）拿去吧，这是合唱团的福利。"
    
    voice "voice/lingning/lingning_077.ogg"
    l "我们在树荫下练声，看着你们在烈日下挥洒汗水，"
    
    voice "voice/lingning/lingning_085.ogg"
    l "我的良心深受谴责……大约有一秒钟那么久。"
    show suzhi camo smile
    s "（接过饮料，对凌宁点头）谢谢。你的室友挺有趣的。"

    voice "voice/lingning/lingning_150.ogg"
    l "（对素织行了个绅士礼）美丽的小姐，这是我的荣幸。愿这瓶饮料能抚平你脚上的伤痛——虽然它并不能外敷。"

    m "（无奈）你快回去吧，别在这拉仇恨了。"

    hide lingning with moveoutleft

    # 【场景六：夜间加练 - 操场】
    scene bg playground_night with fade
    stop music fadeout 1.5
    play sound audio.se_crickets loop

    # 背景：夜晚的操场，灯光昏暗
    # 木子米正在练习摆臂，突然发现素织也在不远处练习
    show suzhi camo angry at center with dissolve

    m "（已经九点了。）"
    m "（她还在练。白天那个小失误，她真的很在意。）"

    # 木子米走过去
    m "这么晚还不回去？再练下去肌肉会拉伤的。"

    show suzhi camo normal
    s "（喘着气，停下动作）我想找找感觉。那个节奏点，我总觉得慢了半拍。"

    m "我帮你喊口令？旁观者清。"

    s "（擦了擦汗）好。麻烦了。"

    m "预备——踢！"

    # 素织踢腿
    play sound audio.se_foot_stomp
    
    m "稍微慢了。落地的时候要干脆，利用重力砸下去，不要犹豫。想象地上有那个……"

    voice "voice/suzhi/suzhi_006.ogg"
    s "有什么？"

    m "有那个把你水倒掉的阿姨的扫帚？"

    show suzhi camo smile
    voice "voice/suzhi/suzhi_013.ogg"
    s "（噗嗤一声笑了出来）什么烂比喻。"

    m "有用就行。再来！预备——踢！"
    
    play sound audio.se_foot_stomp

    s "这次呢？"

    m "完美。声音很实。"

    show suzhi camo smile
    voice "voice/suzhi/suzhi_026.ogg"
    s "（深吸一口气，脸上露出了满意的神色）谢谢。感觉找到了。"

    m "（看着月光下的素织，她额前的碎发被汗水打湿，眼神却比星星还亮）"
    m "那个……汇演的时候，我们方队就在你们后面。"
    
    s "嗯？"

    m "我会看着你的背影走的。所以……你只要大胆往前走就好。如果排头稳了，我们后面也就稳了。"

    voice "voice/suzhi/suzhi_033.ogg"
    s "（沉默了片刻，眼神变得柔和）嗯。不会让你失望的。"

    # 两人并肩坐在草地上休息
    stop sound fadeout 1.0
    play music audio.bgm_warm fadein 1.0
    
    # 切换CG：素织夜间微笑
    scene cg suzhi_night_smile with dissolve

    m "（所谓战友。）"
    m "（所谓同伴。）"
    m "（在这一刻，我好像理解了这两个词的含义。）"
    m "（这不仅仅是枯燥的训练，更是两颗心在同一个频率上跳动的过程。）"

    # 【场景七：宿舍 - 深夜】
    scene bg dorm_boys_night with fade
    play music audio.bgm_daily fadein 1.0

    # 凌宁敷着面膜
    show lingning casual pose at center
    
    voice "voice/lingning/lingning_140.ogg"
    l "（敷着面膜，躺在床上发出含糊的声音）木子米，你回来得甚晚。莫非是与那位佳人有了什么月下之约？"

    m "（疲惫地爬上床）只是加练而已。别乱想。"

    voice "voice/lingning/lingning_055.ogg"
    l "呵，加练。年轻人的借口总是如此拙劣又可爱。不过……"
    
    voice "voice/lingning/lingning_146.ogg"
    l "（翻了个身）我看那位素织小姐，对你也并非无意。她的眼神，比这面膜里的精华还要浓郁。"

    m "睡你的觉吧，合唱团的大歌星。"

    voice "voice/lingning/lingning_057.ogg"
    l "哼，明日我要去竞选领唱。即便不能在跑道上挥洒汗水，我也要在看台上用歌声征服全场。"

    voice "voice/lingning/lingning_020.ogg"
    l "晚安，我的步兵朋友。"

    m "晚安。"

    hide lingning with dissolve

    # 木子米闭上眼睛
    scene black with fade
    
    m "（还有一周。）"
    m "（期待那一天的到来。）"

    # 【第三章 完】
    jump chapter_4



label chapter_4:

    # ==========================================
    # 【场景一：体育场 - 上午 - 彩排现场】
    # ==========================================
    
    # 映射背景：体育场
    scene bg stadium_grandstand with fade

    # 映射BGM：Tension_Drill -> audio.bgm_military_drum
    play music audio.bgm_military_drum fadein 1.0

    # 画面特效：白色闪光，模拟强烈的眩晕感
    with flash
    with vpunch # 震动一下表现身体不适

    m "（视线模糊，呼吸沉重）又是这该死的哨声……这是第几次了？第九次？还是第十次？"
    m "汗水顺着帽檐滑进眼睛里，蛰得生疼。"
    m "但我不敢动，连眨眼都不敢。"
    m "哪怕只是动一根手指，那个魔鬼都会瞬移到我面前。"

    # 立绘：教官
    show instructor cold at center with dissolve

    voice "voice/jiaoguan/jiaoguan_013.ogg"
    e "停——！都给我停下！"

    # 音效：刺耳电流声 -> 模拟哨声
    play sound audio.se_whistle
    with soft_shake

    voice "voice/jiaoguan/jiaoguan_030.ogg"
    e "土木系的！你们是在梦游吗？那个排面，歪得像贪吃蛇一样！"
    voice "voice/jiaoguan/jiaoguan_034.ogg"
    e "尤其是第三列！脚抬高！砸地要有声音！ "
    voice "voice/jiaoguan/jiaoguan_008.ogg"
    e "中午还想不想吃饭了？我看你们是精神太好了，不饿是吧？ "
    voice "voice/jiaoguan/jiaoguan_020.ogg"
    e "全体都有——向后转！跑步回原点！再来一遍！ "
    # 音效：一片压抑的哀嚎声，杂乱的跑步声 -> 使用人群脚步声
    play sound audio.se_footsteps_crowd

    m "腿已经不是自己的了，像是灌了铅，每迈出一步都要调动全身的肌肉。"
    m " 这就是军训的最后一天吗？传说中的决胜日"
    m "……空气里全是焦躁、汗臭和绝望的味道。"
    hide instructor with dissolve

    # 视角拉近描写
    m "我不自觉地看向左前方。 那里有一个身影，即使在所有人都弯腰喘气的时候，她依然挺得笔直。"

    # 【CG特写】由于素材库中暂无"素织背影"CG，此处使用近距离立绘配合文字演出代替，或者使用黑屏独白
    # 这里使用立绘放大模拟聚焦
    show suzhi camo normal at center:
        zoom 1.1
    with dissolve

    m "素织…… 明明大家受的苦是一样的，明明这里的温度已经接近四十度。"
    m "但只要看着她那个倔强又好看的背影，看着那一丝不苟的马尾辫随着步伐轻轻甩动……"

    m "奇怪。 "
    m " 那种要把骨架拆散的疲惫感，好像消退了一点点。"
    m "这就是所谓的“精神氮泵”吗？"
    m "如果不跟上她的脚步，大概我会觉得自己是个逃兵吧。"

    m "（咬牙，小声）拼了……再来十圈也无所谓！"

    stop music fadeout 2.0
    window hide
    pause 1.0


    # ==========================================
    # 【场景二：体育场角落 - 中午】
    # ==========================================

    # 映射背景：休息区/角落
    scene bg rest_area with fade

    # 映射BGM：Sneaky_Step -> audio.bgm_stealth_happy
    play music audio.bgm_stealth_happy fadein 1.0

    show instructor cold at center with dissolve

    voice "voice/jiaoguan/全jiaoguan_016.ogg"
    e "全停！ 现在是11点40分，距离正式汇演还有40分钟。 为了保持这种紧绷的状态，为了防止你们吃饱了犯困——"
    voice "voice/jiaoguan/jiaoguan_037.ogg"
    e "所有人原地休息！不许解散！不许去食堂！ 克服饥饿感，这是军人的必修课！听明白了吗？！"

    # 众学生（使用旁白代替）
    "众学生" "（有气无力）听——明——白——了……"

    # 音效：肚子叫
    play sound audio.se_stomach

    hide instructor with dissolve

    # 木子米状态
    m "完了……彻底完了。"
    m "早上因为太紧张只喝了一杯豆浆"
    m "现在我的胃正在消化它自己。"
    m "这种状态上场，我不变成正步踢腿的僵尸才怪。"
    # 音效：衣料摩擦
    play sound audio.se_bump_sfx

    m "突然，一只手轻轻戳了戳我的后背。"
    m " 那触感很轻。"
    m "但在这种绝望时刻。"
    m "简直像是天使的召唤。"
    # 立绘：素织 左右张望
    show suzhi camo default at center with easeinright
    
    voice "voice/suzhi/suzhi_072.ogg"
    s "（压低声音，气声）喂，木子米。活着吗？"

    m "（虚弱）快……不行了……这是谋杀……"

    voice "voice/suzhi/suzhi_098.ogg"
    s "想不想吃东西？"

    m "（瞬间睁大眼）想！做梦都想！"
    m "但是教官那个阎王就在那边盯着……"
    # 表情变化：狡黠/微笑
    show suzhi camo smile

    voice "voice/suzhi/suzhi_064.ogg"
    s "跟我来。 我昨天观察过了，那边的凉亭就能直接跑掉，"
    voice "voice/suzhi/suzhi_121.ogg"
    s "从凉亭穿过去就是食堂。 来回只需要五分钟。"

    m "越狱？！在这时候？"
    m "素织，你可是标兵啊！要是被抓到……"

    # 表情变化：愤怒/锐利 -> angry
    show suzhi camo angry

    voice "voice/suzhi/suzhi_092.ogg"
    s "怕了？ 那我一个人去了。到时候我吃着你看着，别流口水。"

    m "谁怕了！走！ "
    m "为了五脏庙，共犯就共犯！"
    m "大不了回来一起罚站！"
    stop music fadeout 1.0
    scene black with dissolve


    # ==========================================
    # 【场景三：校外小吃街后巷 - 中午】
    # ==========================================

    # 映射背景：小吃街后巷 (使用 dining_door 作为最接近的户外餐饮入口背景)
    scene bg dining_door with fade

    # 映射BGM：Street_Market -> 使用环境音效 se_market
    play sound audio.se_market loop volume 0.6

    # 显示CG：两人吃手抓饼
    show cg eating_pancakes with dissolve

    s "唔……！"
    voice "voice/suzhi/suzhi_039.ogg"
    s "（用力吞咽）太好吃了……木子米。这绝对是我这辈子吃过最好吃的手抓饼。"
    voice "voice/suzhi/suzhi_094.ogg"
    s "里面加的这根烤肠简直是世界珍宝。"
    m "（猛点头）那是因为这是“违禁品”。"

    m "这就是“自由”的味道啊！"

    m "还有这孜然味，简直是救命的仙丹。"

    m "真没想到。 那个“优等生”素织，居然会带头违反纪律，还在这啃大饼。"

    voice "voice/suzhi/suzhi_133.ogg"
    s "规则是死的，人是活的。"
    voice "voice/suzhi/suzhi_130.ogg"
    s "如果不吃饱，哪有力气把那面锦旗扛回来？"
    voice "voice/suzhi/suzhi_017.ogg"
    s "我又不是铁做的机器人。"
    voice "voice/suzhi/suzhi_050.ogg"
    s "而且……"

    m "而且？"

    voice "voice/suzhi/suzhi_047.ogg"
    s "（移开视线）刚才解散的时候，我看你脸色发白，嘴唇都在抖。 "

    voice "voice/suzhi/suzhi_014.ogg"
    s "我怕你待会儿晕倒在主席台前……那样不仅丢我们土木系的人"
    voice "voice/suzhi/suzhi_051.ogg"
    s "还……挺让人担心的。"
    m "心脏……好像漏跳了一拍。 胃里暖暖的，心里也暖暖的。"
    m "（挠头，傻笑）原来是专门为了照顾我这个“病号”啊？"

    voice "voice/suzhi/suzhi_108.ogg"
    s "（声音提高八度）少自作多情！我是为了集体的荣誉！ "
    voice "voice/suzhi/suzhi_081.ogg"
    s "快把垃圾收好！还有三分钟集合，要是迟到了教官会扒了我们的皮！"
    m "是！遵命，长官！"

    # 音效：急促脚步声
    stop sound fadeout 1.0
    play sound audio.se_foot_stomp # 假设有跑步声，或者用 generic run
    
    scene black with dissolve


    # ==========================================
    # 【场景四：体育场 - 下午 - 汇演进行中】
    # ==========================================

    # 映射背景：体育场
    scene bg stadium_grandstand with fade

    # 映射BGM：March_Anthem -> audio.bgm_march
    play music audio.bgm_march volume 0.8 fadein 2.0

    # 主持人广播音
    "主持" "下面向我们要走来的是——土木工程学院代表队！\n他们步伐矫健，他们意志如钢！"

    m "来了。 这一刻终于来了。 "
    m "下午两点，一天中最毒辣的太阳。"
    m "我们在烈日下整整站了三个小时军姿，等待的只有这一分钟的检阅。"
    m "汗水已经流干了，只能感觉到皮肤上细微盐粒摩擦的刺痛感。"
    m "但是，现在不一样了"
    m " 吃饱了肚子的我们，现在体内燃烧着的是碳水化合物转化成的纯粹斗志！"

    show instructor cold at left with vpunch
    voice "voice/jiaoguan/jiaoguan_042.ogg"
    e "正步——走！！！"

    hide instructor

    # 音效：正步声
    play sound audio.se_foot_stomp loop

    # 显示CG：腿部特写
    show cg marching_legs with flash

    m "脚掌砸向地面的痛感已经麻木了。"
    m "视线里只有前面同学的后脑勺，耳边只有风声和大家整齐的呼吸声。"
    m "我看得到前排素织的背影。"
    m "她的肩膀纹丝不动。"
    m "她是我们的箭头，是我们的锋刃。"
    m "我们是一个整体。"
    m "为了这半个月流掉的几斤汗水，为了那个偷偷吃掉的手抓饼……"

    stop sound # 停止脚步声，准备呐喊

    # 震动屏幕模拟呐喊
    with vpunch
    "全体方队" "向右——看！ "
    "一！！二！！三！！四！！"

    m "那一声呐喊，仿佛把头顶那一层厚厚的积云都给震碎了！ "
    m "这就是……我们的力量！"
    stop music fadeout 2.0
    scene black with dissolve


    # ==========================================
    # 【场景五：操场中央 - 颁奖仪式 - 黄昏】
    # ==========================================

    # 映射背景：夕阳下的体育场
    scene bg stadium_grandstand_sunset with fade

    # 映射BGM：Victory_Sunset -> audio.bgm_victory
    play music audio.bgm_victory fadein 2.0

    "校领导" "经过评委组的一致决定，获得本次军训汇报表演，第一名的是——（停顿） 土木工程学院！"


    # 立绘：凌宁 跳起来
    show lingning camo default at right with vpunch
    
    voice "voice/lingning/lingning_064.ogg"
    l "好！！！太棒了！！！" 
    
    voice "voice/lingning/lingning_128.ogg"
    l "木子米！素织小姐！看到了吗！"
    
    voice "voice/lingning/lingning_157.ogg"
    l "那是第一名！"
    
    voice "voice/lingning/lingning_054.ogg"
    l "太优雅了！"
    
    voice "voice/lingning/lingning_028.ogg"
    l "这才是土木人的魂！"
    
    voice "voice/lingning/lingning_027.ogg"
    l "这才是优雅的极致！"

    # 立绘：教官 微笑（虽然素材是cold，但文字描述了）
    show instructor cold at left
    
    voice "voice/jiaoguan/jiaoguan_029.ogg"
    e "哼，算你们这群小兔崽子没给我丢人。排头兵！出列领奖！"

    voice "voice/suzhi/suzhi_074.ogg"
    s "是！"

    hide lingning
    hide instructor
    with dissolve

    m "我看着素织跑向主席台。她每一步都跑得轻盈而有力，仿佛卸下了千斤重担。"

    # 【CG时刻：锦旗与少女】
    scene black with dissolve
    show cg suzhi_banner with dissolve

    # 配合描述
    m "那个瞬间，周围的喧嚣仿佛都被按下了静音键。 时间好像静止了。"
    m "我想，哪怕过了十年，二十年，我也永远不会忘记这个画面。"
    m " 那个举着锦旗的女孩，那个笑容…… 比这漫天的晚霞还要耀眼，比所有的奖章都要珍贵。"
    m " 比这漫天的晚霞还要耀眼，比所有的奖章都要珍贵"
    pause 2.0
    scene black with dissolve


    # ==========================================
    # 【场景六：解散后 - 操场边缘】
    # ==========================================

    # 映射背景：夕阳下的操场
    scene bg playground_sunset with fade

    play music audio.bgm_warm fadein 2.0

    # 画面：两人并肩
    # 立绘：素织 迷彩服
    show suzhi camo normal at center with dissolve

    voice "voice/suzhi/suzhi_076.ogg"
    s "呼…… 累死我了……感觉腿已经离家出走了，现在连站起来的力气都没有。"
    s "（把锦旗小心翼翼地交给路过的班长，然后毫无形象地瘫坐在地上）" # 文字演出

    # 木子米没有立绘，只有对话
    m "恭喜啊，排头兵。 刚才那个特写，如果拍下来绝对能当明年学校的招生简章封面。标题就叫“热血青春”。"


    # 表情变化：微笑
    show suzhi camo smile

    voice "voice/suzhi/suzhi_046.ogg"
    s "（接过水，仰头喝了一大口，转头看着木子米）你也一样。"
    s "刚才踢正步的时候，我能感觉到后面的节奏很稳。"
    voice "voice/suzhi/suzhi_082.ogg"
    s "就像有一堵墙在后面推着我一样。"
    voice "voice/suzhi/suzhi_029.ogg"
    s "如果没有你们在后面撑着，我这第一排也不敢走得那么大步。"

    m "（耸耸肩，笑）那是，毕竟吃了你的手抓饼。"
    m "这就是“拿人手短，吃人嘴软”，总得卖力气还债吧。"
    # 表情变化：娇羞/笑
    show suzhi camo embarrassed with soft_shake

    voice "voice/suzhi/suzhi_084.ogg"
    s "（扑哧一笑，轻轻锤了一下木子米的肩膀）就知道吃。满脑子都是手抓饼。"

    # 短暂沉默
    stop sound fadeout 2.0
    
    # 表情变化：正常/温柔
    show suzhi camo normal

    voice "voice/suzhi/suzhi_005.ogg"
    s "（抬头看着天空，长舒一口气）不过……终于结束了。 这半个月，简直像过了一年那么长。"

    m "是啊，结束了。 但这只是军训结束了。明天开始，就是真正的大学生活了。"

    show suzhi camo smile

    voice "voice/suzhi/suzhi_034.ogg"
    s "（轻声，眼神温柔）嗯。 希望以后的日子，也能像今天这样。"
    voice "voice/suzhi/suzhi_011.ogg"
    s "……虽然过程累得要死，还要冒着风险翻墙…… 但只要结果是好的，就都值得"

    # 结尾演出：拉远镜头，影子重叠
    scene bg playground_sunset with dissolve:
        zoom 1.0
        linear 5.0 zoom 1.1 # 缓慢推近模拟情感升华

    m "军训结束了。 但我预感，我和她的故事，才刚刚翻开了第一页。"
    m "（微笑）下一次，换我请你吃手抓饼吧，素织。"

    # 第四章结束
    scene black with fade
    stop music fadeout 3.0
    jump chapter_5



# ==========================================
# 剧本正文 - 第五章：大学生活的“真实”面貌
label chapter_5:
# ==========================================
# 第五章：大学生活的“真实”面貌
# ==========================================

    # 【场景一：男生宿舍 - 清晨】
    scene bg dorm_room_morning with fade

    # 使用变量播放，fadein 设置淡入时间
    play music bgm_daily_funny fadein 1.0

    # 镜头缓慢平移效果 (ATL)
    # 从左边缘 (0.0) 平移到右边缘 (1.0)，耗时4秒
    camera:
        xalign 0.0
        linear 4.0 xalign 1.0

    "镜头缓慢平移，扫过满地的军训迷彩服尸体，最后定格在木子米流着口水的睡脸上。"

    # 这里的 extend 可以用于连接上一句，或者直接分行写
    m "（意识模糊）嗯……没有哨声……世界……是如此的安详。"
    m "（意识模糊）嗯……"
    m "没有哨声。"
    m "没有那个魔鬼少尉的咆哮。"
    m "没有“土木系，起床”的咆哮。"
    m "世界……是如此的安详。"
    m "这就是……天堂吗？"

    # 凌宁突然的大声打断
    voice "voice/lingning/lingning_145.ogg"
    l "（超大声）啊！这是何等残酷的宿命！我的刘海……竟向左偏离了0.5度！"

    # 镜头切回中心 (或者切到说话人位置)
    # 如果需要瞬间切回，不需要 linear；如果需要滑回，加上 linear 0.5
    camera:
        xalign 0.5

    m "（惊醒）怎、怎么了？！"

    # 凌宁：日常 Pose 从右侧移入
    show lingning casual pose at right with moveinright
    
    voice "voice/lingning/lingning_017.ogg"
    l "早安，我的战友。"
    
    voice "voice/lingning/lingning_011.ogg"
    l "不，今日起，请称呼我为——“寻觅真理的贵族学者”。"
    
    voice "voice/lingning/lingning_130.ogg"
    l "你看，这瓶“皇家定型喷雾”，能否挽救我这不听话的发梢？"

    # 描述性动作
    m "（死鱼眼，重新倒回枕头上）"
    
    m "现在才七点半……"
    m "第一节课是八点。"
    m "你能不能让我再享受三分钟？"

    voice "voice/lingning/lingning_071.ogg"
    l "No, no, no，木子米，你太松懈了。"
    
    voice "voice/lingning/lingning_132.ogg"
    l "军训是肉体的磨炼，而大学课堂，是灵魂的战场！"
    
    voice "voice/lingning/lingning_117.ogg"
    l "尤其是第一节课！"
    
    voice "voice/lingning/lingning_042.ogg"
    l "那是决定你在班级女生心中地位的“首秀”！"
    
    voice "voice/lingning/lingning_093.ogg"
    l "你是想做一个默默无闻的路人A，还是像我一样，成为照亮教室的恒星？"

    m "（内心）这家伙……绝对是那种会在开学典礼上扔玫瑰花的类型。"
    m "（内心）而且……白色西装？你是去上高数课还是去参加婚礼？"

    # 旁白或动作描述
    "（叹气，爬下床）"

    m "如果你所谓的“恒星”是指像个反光板一样闪瞎别人的眼睛，那你赢了。"
    m "话说，我们要去哪个教室？"

    voice "voice/lingning/lingning_153.ogg"
    l "（自信满满）作为情报通，我早已调查清楚。"
    
    voice "voice/lingning/lingning_095.ogg"
    l "就在——那个很高的楼。"

    m "……哈？"

    voice "voice/lingning/lingning_133.ogg"
    l "长春工程学院有哪个楼高？"
    
    voice "voice/lingning/lingning_014.ogg"
    l "呃……就是那个……看起来充满了智慧气息的楼。"

    "（吐掉牙膏泡沫，抓起手机一看）"

    m "第三教学楼，402室。"
    m "距离这里步行需要五分钟。"
    m "而现在时间是——7点55分。"

    # 这里可以加个淡出或者震动效果表示完蛋了
    with vpunch
    "两人对视一眼。"
    "...."

    # 凌宁：震惊
    show lingning casual surprised with vpunch
    
    voice "voice/lingning/lingning_051.ogg"
    l "什……什么？！!!"
    m "跑起来！小贵族！"

        # ==========================================
    # 场景二：校园大道 - 奔跑中 【7:55】
    # ==========================================

    # --- 场景初始化 ---
    stop music fadeout 1.0
    
    # 播放快节奏、欢乐的追逐曲
    play music audio.bgm_chase fadein 0.5 volume 0.8

    # 背景：快速后退的校园景色 (使用模糊的校园路CG)
    # 使用 running_shake 模拟第一人称视角的剧烈晃动
    scene cg campus_road_blur at truecenter, running_shake

    # 模拟沉重的喘息声（可以通过文字或音效辅助）
    # 这里使用 vpunch 模拟心脏剧烈跳动或脚步沉重的一下震击
    with vpunch
    
    # --- 内心独白 ---
    # 此时主要展示背景晃动，木子米内心疯狂吐槽

    m "（剧烈喘息）呼……呼……"
    
    m "失策了！"
    m "完全失策了！"
    m "我以为脱下迷彩服就能摆脱这种极限奔跑的命运。"
    m "结果……这比五公里负重跑还刺激啊！"

    m "因为——"

    # --- 凌宁登场 ---
    # 凌宁从左侧追上来，保持跑步姿势，并且同样应用颠簸效果
    show lingning casual run at center, running_shake with moveinleft

    voice "voice/lingning/lingning_147.ogg"
    l "（气喘吁吁，双手向后像忍者一样摆动）"
    
    voice "voice/lingning/lingning_059.ogg"
    l "木子米！慢……慢一点！"
    
    voice "voice/lingning/lingning_135.ogg"
    l "风！"
    
    voice "voice/lingning/lingning_136.ogg"
    l "风会把我的发型吹乱的！"
    
    # 特写凌宁的滑稽感，稍微放大一点
    show lingning casual run at center, running_shake:
        zoom 1.1
    
    voice "voice/lingning/lingning_033.ogg"
    l "这是对美学的亵渎！"

    # --- 互动吐槽 ---
    m "亵渎你个大头鬼啊！"
    m "还有五分钟！"
    
    # 镜头轻微推拉，增加紧迫感
    camera:
        linear 0.5 zoom 1.05
        linear 0.5 zoom 1.0
    
    m "而且这该死的教学楼为什么建在坡上？！"
    m "长春是平原吧？但这学校里为什么会有好汉坡？！"

    # --- 场景切换：到达大门 ---
    # 两人冲上长坡，背景切换到教学楼大门
    # 使用带有闪白的转场，模拟冲出林荫道见到阳光/建筑的感觉
    
    scene bg school_gate at truecenter
    with flash

    # 停止相机的持续晃动，改为定格的喘息
    camera:
        zoom 1.0
    
    # 凌宁状态切换为累瘫/绝望
    show lingning casual tired at center with dissolve

    m "到了！快走楼梯！"

    # 凌宁绝望的特写
    show lingning casual tired:
        linear 0.2 zoom 1.2 yoffset 20
        linear 0.2 zoom 1.2 yoffset 0
        repeat 2
    
    voice "voice/lingning/lingning_151.ogg"
    l "（绝望的哀嚎）四楼？！"
    
    # 音乐淡出，预示着接下来是爬楼梯的痛苦或转场
    stop music fadeout 2.0
    
    voice "voice/lingning/lingning_100.ogg"
    l "吾命休矣……"

    # 屏幕变黑，结束本小节
    scene black with dissolve


    # ... (前文保持不变)

    # CG 结束，切回教室背景
    scene bg classroom_desk with dissolve
    # 【BGM：突然停止】
    stop music fadeout 0.5

    # 【画面：教室门口】
    # 暂时使用走廊或教室门口背景，如果没有专门的门口背景，可以用教室背景代替，或者黑屏过渡
    scene bg classroom_full with fade

    # 【BGM：转为教室里的嘈杂人声】
    # 这里使用定义的 bgm_classroom 作为环境音
    play music audio.bgm_classroom fadein 1.0 volume 0.8

    # 凌宁和木子米气喘吁吁
    show lingning casual tired at center with dissolve
    
    # 模拟气喘吁吁的震动效果
    with vpunch

    # (内心独白)
    m "赶……赶上了。"
    m "铃声还没响。"
    m "但是……"

    # 木子米扫视教室内
    # 稍微平移背景模拟扫视效果
    show bg classroom_full:
        xalign 0.5
        linear 2.0 xalign 0.6
        linear 2.0 xalign 0.4
        linear 1.0 xalign 0.5

    m "（环顾四周，倒吸一口凉气）"

    # (内心独白)
    m "满员？！"
    m "这就是大学第一节课的热情吗？"
    m "前排全是学霸，后排全是想摸鱼的大神。"
    m "中间……中间也没有空位了啊！"

    # 凌宁整理领带，试图恢复优雅
    # 切换凌宁立绘
    show lingning casual pose with dissolve

    voice "voice/lingning/lingning_048.ogg"
    l "看来，只有那个位置了。"
    
    voice "voice/lingning/lingning_008.ogg"
    l "那是神留给我们的“VIP席位”。"

    # 木子米顺着视线看去
    m "（顺着凌宁的视线看去……）"
    m "第一排。"
    m "正对着讲台。"
    m "也就是传说中的“吃粉笔灰特等席”。"
    m "而且……只有两个空位。"

    # 木子米绝望
    show lingning at left with move
    m "（绝望）饶了我吧……坐在老师眼皮子底下，我想补觉都不行。"

    # ？？？的声音传来
    unknown "……这里。"

    # 木子米愣住
    stop music fadeout 2.0 # 声音出现时，环境音稍微减弱或停止以突出
    m "（诶？）"
    
    # 镜头推进，聚焦后排
    # 这里我们将凌宁隐藏，展示素织
    hide lingning with dissolve

    # (立绘出现：素织 - 看书状态)
    show suzhi casual reading at center with dissolve

    # (特别描述)
    # 这里用较长的旁白来描写外貌变化
    window show
    "循声望去，教室中后排靠窗的一个角落。"
    "她脱去了臃肿的迷彩服，换上了一件米白色的宽松针织衫，领口系着一个小小的蓝色蝴蝶结。"
    "下身是一条淡格子的百褶裙，露出修长且线条优美的小腿。"
    "头发没有像军训时那样扎成利落的马尾，而是随意地披散在肩头，显得格外温柔慵懒。"
    "她戴着一副细框眼镜，正一只手托着腮，一只手转着笔，看似在看书，其实眼神正往这边瞟。"
    window hide

    # (内心独白)
    # 播放一段稍微轻快或惊讶的BGM
    play music audio.bgm_daily_warm fadein 1.0

    m "！！！"
    m "那个是……素织？"
    m "这……这反差也太大了吧！"
    m "军训时的那个“女武神”去哪了？"
    m "这完全就是个文学少女啊！"
    m "这就是所谓的“皮肤切换”吗？氪金了吗？"

    # 素织发现木子米在发呆
    # 切换立绘：害羞/微怒
    show suzhi casual shy with dissolve
    
    # 只有素织说话时才带名字
    voice "voice/suzhi/suzhi_091.ogg"
    s "（眉头微微一皱，脸颊泛起一丝红晕，小声喊道）"
    s "呆子！看什么看！"
    voice "voice/suzhi/suzhi_036.ogg"
    s "这边……有个空位。"

    # 木子米发现占座的水杯
    "我这才发现，素织旁边的桌子上放着一个粉色的水杯，显然是帮人占座的。"

    # 凌宁复活，凑过来
    show lingning casual happy at left with moveinleft

    voice "voice/lingning/lingning_152.ogg"
    l "（凑到耳边）哦~ 多么感人的战友情。"
    
    voice "voice/lingning/lingning_127.ogg"
    l "去吧，木子米。"
    
    voice "voice/lingning/lingning_007.ogg"
    l "那个位置属于你。"
    
    voice "voice/lingning/lingning_088.ogg"
    l "我就牺牲一下，去第一排沐浴知识（粉笔灰）的洗礼了。"

    m "（感动）凌宁……你真是个好人。"
    m "下辈子我一定做牛做马报答你。"

    # 凌宁潇洒离开
    # 切换凌宁立绘为普通的或得意的，然后消失
    
    voice "voice/lingning/lingning_119.ogg"
    l "不必，请我喝一个月的冰红茶即可。"
    
    hide lingning with moveoutleft

    # 木子米走向座位
    m "（深吸一口气，顶着全班男生“羡慕嫉妒恨”的目光，穿过过道，走到素织身边……）"


    # --- 场景初始化 ---
    # 播放轻快俏皮的BGM
    play music audio.bgm_daily_funny fadein 1.0 volume 0.8

    # 背景：近景特写，两人的课桌
    scene bg classroom_desk with fade

    # 旁白/环境音：窗外树叶摇晃 (假定有环境音，如果没有则跳过)
    # play sound audio.se_birds volume 0.3 loop

    # --- 第一幕：占座 ---

    # 动作：木子米坐下
    # 屏幕轻微晃动模拟坐下的动作
    with vpunch
    "我小心翼翼地坐下，把书包塞进桌洞。"

    m "呼……谢了。"
    m "没想到你会帮我占座。"

    # 素织登场：穿着便装，拿着书（假装在看）
    # 使用 casual reading 立绘
    show suzhi casual reading at center with dissolve

    # 细节：书拿倒了（通过对话体现，立绘保持reading状态）
    # 素织并没有看他
    voice "voice/suzhi/suzhi_107.ogg"
    s "别误会。"
    voice "voice/suzhi/suzhi_101.ogg"
    s "本来是给……给室友占的。"

    # 切换表情：傲娇/生气
    show suzhi casual angry at center
    voice "voice/suzhi/suzhi_066.ogg"
    s "但是她突然说要陪男朋友坐后面。"
    voice "voice/suzhi/suzhi_037.ogg"
    s "这位置空着也是空着，要是坐个不认识的男生，我会不自在。"
    voice "voice/suzhi/suzhi_049.ogg"
    s "与其那样，不如……不如让你这个“熟人”坐这。"
    voice "voice/suzhi/suzhi_109.ogg"
    s "至少……你不打呼噜。"

    # 内心独白
    window hide
    pause 0.5
    m "(书拿倒了哦，素织同学。)"
    m "(而且你的耳朵红得像熟透的番茄一样。这借口找得也太蹩脚了吧！)"
    window show

    m "（故意调侃）哦？"

    # 木子米打量素织
    m "不过，这身衣服……很适合你。"
    m "差点没认出来。"

    # --- 第二幕：羞涩的素织 ---

    # 身体猛地一僵，转过头
    # 切换表情：惊讶 -> 害羞
    show suzhi casual surprise at center
    with soft_shake
    voice "voice/suzhi/suzhi_078.ogg"
    s "很……很奇怪吗？"

    show suzhi casual shy at center
    voice "voice/suzhi/suzhi_060.ogg"
    s "是不是太……太花里胡哨了？"
    voice "voice/suzhi/suzhi_104.ogg"
    s "凌宁那家伙之前说我是“穿裙子的花木兰”……"

    m "（真诚地微笑）不。"
    m "很好看。"
    m "真的。"
    m "比军装更适合你。"

    # CG插图时刻
    # 原文描述：素织特写，羞涩低头，卷发梢，暖阳背景
    window hide
    scene cg suzhi_reading with fade
    window show

    voice "voice/suzhi/suzhi_009.ogg"
    s "（蚊子叫般的声音）……笨蛋。"
    voice "voice/suzhi/suzhi_136.ogg"
    s "就会说好听的。"

    # 恢复场景
    scene bg classroom_desk 
    show suzhi casual shy at center
    with dissolve

    # --- 第三幕：杀手王登场 ---

    # 音效：上课铃
    stop music fadeout 2.0
    play sound audio.se_bell
    pause 1.5

    # 老师进场
    # 修正：高数老师是甜美风格，但外号“杀手王”
    hide suzhi with dissolve
    show mathteacher normal at center with dissolve

    "（这时，一个长相甜美的女老师走上讲台，带着温柔的笑容）"

    tea_math "好了！上课！"
    tea_math "这就是土木系的新生吗？看来精神头都不错啊。"
    tea_math "我是你们的高数老师，大家都叫我“杀手王”。"
    
    # 播放压抑的BGM
    play music audio.bgm_classroom fadein 1.0

    tea_math "希望期末的时候，你们还能笑得出来。"
    
    # 全班寒意
    show layer master:
        matrixcolor TintMatrix("#aaddff") * SaturationMatrix(0.8)
    with dissolve
    "（全班顿时感到一股寒意）"
    show layer master:
        matrixcolor IdentityMatrix()
    with dissolve

    tea_math "翻开书第一页。"
    tea_math "我们要讲的是——函数的极限。"
    tea_math "注意听！这一章如果听不懂，后面的微积分你们就只能看天书了！"

    # --- 第四幕：催眠高数 ---

    # 时间流逝效果
    scene black with dissolve
    "（五分钟后）"
    scene bg classroom_desk with dissolve

    m "(不行了。)"
    m "(这是什么催眠魔法？)"
    m "(明明每个字都听得懂，连在一起就变成了外星语。)"

    # 数学公式
    # 注意：Ren'Py 默认不支持 LaTeX 渲染，这里按要求作为文本显示
    m "lim(x→0) (sin x / x) = 1 ……"

    m "这到底为什么等于1？"
    m "难道不是把 $x$ 约掉剩下 $\sin$ 吗？（大误）"

    # 木子米瞌睡效果
    # 模拟眼皮打架：画面忽明忽暗，或者模糊
    show layer master:
        ease 2.0 blur 10.0
    
    "(眼皮越来越重，脑袋开始像小鸡啄米一样点……)"

    # --- 第五幕：猪头画像 ---

    # 突然的触感
    stop music
    play sound audio.se_hit # 比如轻轻拍打或者冰凉触感的声音
    show layer master:
        blur 0.0
    with vpunch

    m "（激灵一下醒来）嗯？！"

    # 侧头看素织
    # 素织一脸嫌弃，把水杯贴在他胳膊上
    # 使用 gloomy 或者 angry 表情
    show suzhi casual gloomy at center with dissolve

    voice "voice/suzhi/suzhi_006.ogg"
    s "（压低声音）喂。"
    voice "voice/suzhi/suzhi_093.ogg"
    s "第一节课就睡？你是不想活了吗？"
    voice "voice/suzhi/suzhi_020.ogg"
    s "那个“杀手王”已经盯你两次了。"
    play music audio.bgm_daily_funny fadein 1.0
    m "（擦了擦嘴角的口水）抱歉……"
    m "但这真的比安眠药还管用。你怎么能听得这么津津有味的？"

    show suzhi casual normal
    voice "voice/suzhi/suzhi_041.ogg"
    s "（指了指笔记本）这哪里津津有味了？"
    voice "voice/suzhi/suzhi_018.ogg"
    s "我是在……画画。"

    # 木子米凑过去看
    m "（凑过去一看）"

    # 显示SD小人动画：猪
    show sd_notebook_pig at truecenter with zoomin

    m "（满头黑线）这就是你的听课成果？"
    m "而且为什么要给猪起我的名字？这算是职场霸凌吗？"

    # 素织理直气壮
    # 这里不需要隐藏SD图，可以作为前景保留，或者隐藏后切回素织
    hide sd_notebook_pig with dissolve

    show suzhi casual smile
    voice "voice/suzhi/suzhi_038.ogg"
    s "因为这只猪睡相很难看。"
    voice "voice/suzhi/suzhi_045.ogg"
    s "和你刚才一模一样。这叫……艺术写生。"

    m "你这就是单纯的报复吧！"
    m "把笔给我，我要行使肖像权，给这只猪画上眼镜！"

    # --- 第六幕：触电 ---

    # 切换回傲娇/护食状态
    show suzhi casual angry
    voice "voice/suzhi/suzhi_125.ogg"
    s "不给！这是我的创作！"
    voice "voice/suzhi/suzhi_112.ogg"
    s "你要画自己在书上画！"

    # 动作描写：桌底下的推拉
    show suzhi casual surprise at center
    with hpunch

    # 触碰瞬间
    stop music fadeout 0.5
    play music audio.bgm_love fadein 2.0
    "(素织的手指不经意间碰到了木子米的手背，微凉，柔软。)"

    # 画面定格/静止
    pause 1.0

    # 播放暖色调/浪漫BGM


    "(两人动作同时停住。)"
    "(一种异样的电流顺着接触点蔓延开来。)"

    # 素织反应：迅速缩手，埋头
    # 切换到害羞状态
    show suzhi casual shy with dissolve
    
    # 可以加一个大幅度的脸红特写

    "(素织像是被烫到一样迅速缩回手，把头埋进书里，整个人缩成一团。)"
    # 木子米反应
    m "（摸了摸鼻子，心跳有点快）"

    voice "voice/suzhi/suzhi_002.ogg"
    s "（声音颤抖）……好好听课。"
    voice "voice/suzhi/suzhi_083.ogg"
    s "别……别闹了。"

    # 木子米反应
    m "（摸了摸鼻子，心跳有点快）"

    m "……哦。"
    
    # 【关键修复】：在这里重置镜头！！！
    # 如果不加这几行，之后的场景会一直保持放大1.2倍且向下偏移的状态，导致立绘只露半截
    scene black with fade
    stop music fadeout 3.0
    "高数课终于结束了"
   
    # 【场景五：课间休息 - 教室走廊】
    # 【10:00】
    # 【背景：拥挤的走廊，学生们都在聊天打闹】
    scene bg classroom_full with fade
    
    # 字幕：时间地点
    show text "【10:00 教室走廊】" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    # 【BGM：轻松、搞怪的曲调（类似《Whatcha doing?》风格）】
    play music audio.bgm_daily_funny fadein 1.0

    # (木子米靠在栏杆上，手里拿着一盒草莓牛奶)
    "（木子米靠在栏杆上，手里拿着一盒草莓牛奶）"

    # (内心独白)
    # 木子米：
    # 高数课终于结束了。
    m "（高数课终于结束了。）"

    # 脑细胞死了一半。
    m "（脑细胞死了一半。）"

    # 急需糖分补充。
    m "（急需糖分补充。）"

    # 这盒草莓牛奶简直是救命稻草。
    m "（这盒草莓牛奶简直是救命稻草。）"

    # (这时，素织从洗手间回来，手里湿漉漉的，显然刚洗完脸)
    # 此时立绘应该已经恢复正常全身显示了
    show suzhi casual normal at center with dissolve
    "（这时，素织从洗手间回来，手里湿漉漉的，显然刚洗完脸）"

    # 素织：
    # （看到木子米）
    # 哎，你居然买到了？
    voice "voice/suzhi/suzhi_025.ogg"
    s "（看到木子米）哎，你居然买到了？"

    # 我去小卖部的时候，草莓味的已经卖光了。
    voice "voice/suzhi/suzhi_016.ogg"
    s "我去小卖部的时候，草莓味的已经卖光了。"

    # 只剩下……香菜味的酸奶。
    # 简直是黑暗料理。
    show suzhi casual angry
    voice "voice/suzhi/suzhi_122.ogg"
    s "只剩下……香菜味的酸奶。简直是黑暗料理。"

    # 木子米：
    # （得意地晃了晃手里的盒子）
    # 这就是手速的差距。
    m "（得意地晃了晃手里的盒子）这就是手速的差距。"

    # 怎么样？想喝吗？
    m "怎么样？想喝吗？"

    # 叫一声“好哥哥”我就……
    m "叫一声“好哥哥”我就……"

    # 素织：
    # （白眼翻到天上去）
    # 想得美。
    show suzhi casual angry # 保持嫌弃表情
    voice "voice/suzhi/suzhi_127.ogg"
    s "（白眼翻到天上去）想得美。"

    # 我自己有水。
    voice "voice/suzhi/suzhi_131.ogg"
    s "我自己有水。"

    # (素织刚想从兜里掏纸巾擦手，结果因为手太滑，没拿住，一张纸巾都没带出来)
    "（素织刚想从兜里掏纸巾擦手，结果因为手太滑，没拿住，一张纸巾都没带出来）"

    # 素织：
    # 啧。
    show suzhi casual gloomy
    voice "voice/suzhi/suzhi_088.ogg"
    s "啧。"

    # 忘带纸了。
    voice "voice/suzhi/suzhi_089.ogg"
    s "忘带纸了。"

    # 喂，木子米，借张纸。
    voice "voice/suzhi/suzhi_071.ogg"
    s "喂，木子米，借张纸。"

    # 木子米：
    # （正准备把吸管插进牛奶盒里）
    # 等下，我找找。
    m "（正准备把吸管插进牛奶盒里）等下，我找找。"

    # 我记得包里有……
    m "我记得包里有……"

    # (就在这时，走廊上两个打闹的男生猛地撞了木子米一下)
    # 【SE：沉闷的撞击声】
    play audio audio.se_bump_sfx
    with vpunch
    
    # 【SE：液体喷溅声】
    # (声音会在下面动作发生时配合播放，这里先显示旁白)
    "（就在这时，走廊上两个打闹的男生猛地撞了木子米一下）"

    # 木子米：
    # 哇！
    m "哇！"

    # (手中的草莓牛奶在挤压下，吸管虽然没插进去，但盒子口直接爆开，一道粉红色的液体划出一道优美的抛物线——)
    # (直直地飞向了素织)
    
    # 演出：喷溅
    play audio audio.se_splat
    show image_milk_splash at slow_motion_pan onlayer screens zorder 100
    
    "（手中的草莓牛奶在挤压下，吸管虽然没插进去，但盒子口直接爆开，一道粉红色的液体划出一道优美的抛物线——）"
    
    # (CG时间：慢动作)
    # (素织瞪大了眼睛，看着那团粉红色的液体飞来。她下意识地张开嘴想惊呼，结果……)
    show suzhi casual surprise
    window hide
    pause 1.0 # 模拟慢动作停顿
    "（直直地飞向了素织）"
    "（素织瞪大了眼睛，看着那团粉红色的液体飞来。她下意识地张开嘴想惊呼，结果……）"

    # 【SE：啪叽】
    hide image_milk_splash onlayer screens
    play audio audio.se_splat
    with flash # 视觉冲击

    # (画面恢复)
    # (素织的脸上、白色的针织衫上，全是粉红色的草莓牛奶。最要命的是，有一点点溅到了她的嘴角，看起来就像是……偷吃没擦嘴)
    # 切换立绘：湿身
    show suzhi casual wet
    
    "（素织的脸上、白色的针织衫上，全是粉红色的草莓牛奶。最要命的是，有一点点溅到了她的嘴角，看起来就像是……偷吃没擦嘴）"

    # (空气凝固了)
    stop music fadeout 0.5
    "（空气凝固了）"

    # 木子米：
    # （举着空盒子，石化）
    # ……
    m "（举着空盒子，石化）……"

    # ……完蛋了。
    m "……完蛋了。"

    # 我的人生，到此结束了。
    m "我的人生，到此结束了。"

    # 素织：
    # （低头看了看自己心爱的衣服，又摸了摸脸上的粘稠液体）
    # （缓缓抬头，眼神里失去了高光，变成了纯黑色的深渊）
    # 播放尴尬BGM
    play music audio.bgm_awkward fadein 0.5
    
    s "（低头看了看自己心爱的衣服，又摸了摸脸上的粘稠液体）"
    s "（缓缓抬头，眼神里失去了高光，变成了纯黑色的深渊）"

    # 素织：
    # （语气平静得可怕）
    # 木。子。米。
    voice "voice/suzhi/suzhi_118.ogg"
    s "（语气平静得可怕）木。子。米。"

    # 木子米：
    # （后退一步）
    # 那个……听我解释。
    m "（后退一步）那个……听我解释。"

    # 这是流体力学的奇迹。
    m "这是流体力学的奇迹。"

    # 是不可抗力。
    m "是不可抗力。"

    # 而且……粉色很衬你……
    m "而且……粉色很衬你……"

    # 素织：
    # （握紧了拳头，额头上蹦出一个红色的井字）
    show icon_angry_mark at truecenter:
        yoffset -350
    with vpunch
    
    # 这是我昨天刚买的新衣服！！！
    voice "voice/suzhi/suzhi_040.ogg"
    s "（握紧了拳头，额头上蹦出一个红色的井字）这是我昨天刚买的新衣服！！！"

    # 而且黏糊糊的难受死了！！！
    voice "voice/suzhi/suzhi_053.ogg"
    s "而且黏糊糊的难受死了！！！"

    # 你给我……去死吧！！！
    voice "voice/suzhi/suzhi_030.ogg"
    s "你给我……去死吧！！！"
    hide icon_angry_mark

    # (SD小人动画：素织变成狂暴模式，追着木子米在走廊里暴打)
    
    # 切换BGM
    play music audio.bgm_chase
    
    # 隐藏正常立绘，显示背景模糊
    hide suzhi
    scene bg classroom_full:
        blur 10
    
    # 显示Q版追逐


    show sd_suzhi_run at chase_run_left
    
    "给我停下！！！"
    hide sd_suzhi_run

    # 木子米：
    # （抱头鼠窜）
    # 女侠饶命！我赔！我赔还不成吗！
    show sd_muzimi_run at panic_run_left
    m "（抱头鼠窜）女侠饶命！我赔！我赔还不成吗！"

    # 我去帮你洗！
    m "我去帮你洗！"
    

    hide sd_muzimi_run

    scene bg classroom_full

    # 凌宁：
    # （此时正拿着一杯咖啡路过，看到这一幕，优雅地抿了一口）
    show lingning casual happy at center with dissolve
    
    voice "voice/lingning/lingning_139.ogg"
    l "（此时正拿着一杯咖啡路过，看到这一幕，优雅地抿了一口）"

    # 哦~
    
    voice "voice/lingning/lingning_021.ogg"
    l "哦~"

    # 这就是所谓的“打情骂俏”吗？
    
    voice "voice/lingning/lingning_026.ogg"
    l "这就是所谓的“打情骂俏”吗？"

    # 青春啊，真是充满了甜腻的草莓味。
    
    voice "voice/lingning/lingning_134.ogg"
    l "青春啊，真是充满了甜腻的草莓味。"

    # 只不过……
    # （看着木子米被逼到墙角）
    show lingning casual pose
    
    voice "voice/lingning/lingning_063.ogg"
    l "只不过……（看着木子米被逼到墙角）"

    # 愿主保佑你，我的朋友。
    
    voice "voice/lingning/lingning_072.ogg"
    l "愿主保佑你，我的朋友。"

    stop music fadeout 2.0
    scene black with fade

    # ==========================================
    # 【场景六：教学楼某空教室 - 10:15】
    # ==========================================

    # 【背景：空无一人的小教室，窗帘半拉着，光线昏暗】
    # 使用 classroom_clean 作为基础，如果支持，后续可加 matrixcolor TintMatrix 调暗
    scene bg classroom_clean
    with fade

    # 【BGM：略带暧昧、尴尬的曲调】
    play music audio.bgm_awkward fadein 1.0

    # (素织坐在椅子上，脱下了针织衫，只穿着里面的白色衬衫。她正拿着湿巾，一脸委屈地擦着裙子上的奶渍)
    # 根据全局设置，调用脱外套的立绘
    show suzhi shirt shy at center
    with dissolve

    # 旁白描述
    "（素织坐在椅子上，脱下了针织衫，只穿着里面的白色衬衫。她正拿着湿巾，一脸委屈地擦着裙子上的奶渍。）"

    # (木子米则拿着那件针织衫，在这个有水池的角落里拼命搓洗)
    "（木子米则拿着那件针织衫，在这个有水池的角落里拼命搓洗。）"

    m "（心虚）那个……这里有个污渍很难洗掉。可能要用肥皂。"

    # 素织：(脸红红的，抱着胸，似乎觉得只穿衬衫在男生面前有点不妥，虽然并不暴露)
    # 保持 shirt shy 立绘，配合晃动效果增强情绪
    voice "voice/suzhi/suzhi_012.ogg"
    s "（脸红红的，抱着胸）……别废话。洗不干净你就死定了。这可是限量版。"

    # 木子米：(回头看了一眼)
    "（木子米回头看了一眼。）"

    # (素织此时抱着双臂，衬衫的扣子因为动作显得有些紧绷，勾勒出原本被针织衫遮住的、意外有料的身材曲线。再加上裙子上那点点粉红色的印记，和她羞愤欲绝的表情……)
    # 镜头轻微推进，强调视线（如果不需要镜头缩放可删除 zoom 1.1）
    show suzhi shirt shy at center:
        ease 1.0 zoom 1.1

    # (内心独白)
    m "（非礼勿视。非礼勿视。我是个正直的土木男。）"
    m "（但……这画面杀伤力太大了。平时看着瘦瘦小小的，没想到……）"

    # 素织：(敏锐地察觉到了视线)
    # 触发震动特效
    show suzhi shirt shy at slight_shake
    voice "voice/suzhi/suzhi_069.ogg"
    s "你在看哪？！变态！"

    # 镜头复原
    show suzhi shirt shy at center:
        ease 0.2 zoom 1.0

    m "（立刻转头，疯狂搓衣服）我看衣服！我在看衣服的纹理！我在思考纤维的构造！"

    # 素织：(哼了一声，有些别扭地把腿并拢)
    voice "voice/suzhi/suzhi_006.ogg"
    s "（哼了一声，有些别扭地把腿并拢）……喂。"
    voice "voice/suzhi/suzhi_044.ogg"
    s "刚才……虽然是你弄脏的。但……你挡在前面的时候，没被烫到吧？"
    voice "voice/suzhi/suzhi_021.ogg"
    s "那两个人拿着好像是热豆浆。"

    # 木子米：(一愣，看了看自己的手背，确实有一块红了)
    m "（一愣，看了看自己的手背，确实有一块红了）啊，没事。皮糙肉厚的。"
    m "只要你的脸没事就行。要是毁容了，我可赔不起一辈子的饭票。"

    # 素织：(愣住) (脸瞬间爆红，头顶冒出蒸汽)
    # 使用 Flash 模拟脸瞬间爆红的冲击感
    show suzhi shirt shy at slight_shake
    with flash

    voice "voice/suzhi/suzhi_059.ogg"
    s "谁……谁要你赔一辈子！谁要吃你的饭票！"
    voice "voice/suzhi/suzhi_027.ogg"
    s "你……这个笨蛋！不可理喻！"

    # (素织抓起桌上的书，对着木子米的后背扔了过去)
    # 【SE：书本砸中的闷响】
    play sound audio.se_hit
    # 使用 vpunch 模拟砸中时的屏幕震动
    with vpunch

    m "痛！你这又是怎么了？关心你也不行吗？"
    m "女人的心思真是比高数还难懂啊！"

    # (素织把头埋进臂弯里，露出的耳朵红得滴血)
    # 这里可以用 dissolve 稍微淡化一下立绘，或者保持原样
    "（素织把头埋进臂弯里，露出的耳朵红得滴血。）"

    # (内心独白)
    voice "voice/suzhi/suzhi_144.ogg"
    s "（……笨蛋。）"
    voice "voice/suzhi/suzhi_145.ogg"
    s "（这种话……怎么能随随便便说出口啊。）"
    voice "voice/suzhi/suzhi_146.ogg"
    s "（犯规。太犯规了。明明只是个木头……）"

    # (黑屏)
    scene bg black
    with fade

    # 停止BGM，或者换成更轻快的，这里根据剧本衔接暂时停止
    stop music fadeout 1.0

    # 剧本继续在黑屏或转场中进行
    m "呼……这也太刺激了，只是上个学而已，感觉比拆弹还累。"

    # 凌宁声音出现，可以加上 mystery 或者是 funny 的BGM
    play music audio.bgm_daily_funny fadein 1.0

    voice "voice/lingning/lingning_029.ogg"
    l "这就是青春的试炼！"
    
    voice "voice/lingning/lingning_036.ogg"
    l "接下来，我们将前往那个神秘的——“图书馆”。"
    
    voice "voice/lingning/lingning_124.ogg"
    l "听说那里有一位“魔女”正在等待着命运的羔羊。"

    voice "voice/suzhi/suzhi_141.ogg"
    s "魔女？我看是中二病吧。话说，木子米，我的衣服还没干，我不出去了！"

    m "好好好，我给你扇干行了吧？"

    # 场景结束，跳转下一章

    # ==========================================
# 场景七：空教室门口 - 走廊
# 时间：10:30
# ==========================================

    # 【BGM：滑稽、充满疑虑的悬疑曲】
    # 使用提供的素材中最接近“滑稽疑虑”风格的音乐
    play music audio.bgm_stealth_happy fadein 1.0

    scene bg classroom_clean with dissolve

    # (木子米推开门)
    play sound audio.se_drag # 模拟推拉门的声音
    pause 0.5

    # (素织跟在后面，把那件还没完全干透的针织衫抱在怀里，遮挡着胸口)
    # 使用 suzhi shirt shy (脱掉外套穿着内衬抱胸) 最符合描述
    show suzhi shirt shy at left with moveinleft

    # (门口，凌宁正背对着门...看到门开了，他缓缓转身)
    # 凌宁登场，使用 casual pose (摆姿势)
    show lingning casual pose at right with dissolve

    # 凌宁：出来了吗？ 比我预想的时间要短了三分钟。
    
    voice "voice/lingning/lingning_091.ogg"
    l "出来了吗？"
    
    voice "voice/lingning/lingning_082.ogg"
    l "比我预想的时间要短了三分钟。"
    
    # 凌宁表情微调：带着一种看透红尘的微笑
    show lingning casual happy
    
    voice "voice/lingning/lingning_049.ogg"
    l "看来在那个封闭的空间里，你们并没有进行关于宇宙真理的深层探讨。"

    # 木子米：（满头黑线） 你在门口站岗干什么？
    # 木子米没有立绘，通常为第一人称视角或画外音
    m "（满头黑线） 你在门口站岗干什么？ 这反而更可疑好不好！ 路过的每个人都在看你！"

    # 凌宁：（优雅地摊手）
    show lingning casual pose
    
    voice "voice/lingning/lingning_092.ogg"
    l "我在守护你们的隐私。"
    
    voice "voice/lingning/lingning_010.ogg"
    l "要知道，青春的冲动就像暴风雨中的蝴蝶，脆弱而美丽。"
    
    voice "voice/lingning/lingning_076.ogg"
    l "若是被俗人打扰了这“清洗罪孽（指洗衣服）”的神圣仪式，岂不可惜？"

    # 素织：（脸还是红的，听到凌宁的话，额头又冒出了井字）
    # 在素织头上显示生气符号
    show icon_angry_mark at left:
        yoffset -350 # 调整符号位置到头顶
        xoffset 100
    with vpunch # 配合震动加强语气

    # 为了表现愤怒，虽然她是羞涩姿态，但语气是愤怒的
    voice "voice/suzhi/suzhi_106.ogg"
    s "凌宁！ 你再胡说八道，我就把你那天晚上敷面膜的照片发到新生群里！"

    hide icon_angry_mark # 隐藏生气符号

    # 凌宁：（脸色瞬间变得苍白，优雅崩塌）
    # 使用 casual surprised (惊讶/被吓到) 或 ashamed (羞愧)
    show lingning casual surprised with soft_shake
    
    voice "voice/lingning/lingning_037.ogg"
    l "唔！这……这是犯规的战术！"
    
    show lingning casual ashamed
    
    voice "voice/lingning/lingning_121.ogg"
    l "素织小姐，请务必手下留情！"
    
    voice "voice/lingning/lingning_044.ogg"
    l "那是我身为贵族的最后尊严！"

    # (内心独白) 木子米： 看来，就算是贵族，也有怕被社会性死亡的时候。
    m "（看来，就算是贵族，也有怕被社会性死亡的时候。 不过…… 看着这两个人像小学生一样斗嘴。）"
    m "（这种感觉，居然还不赖。）"

    # 木子米： 行了，别贫了。 下一节课是什么？
    m "行了，别贫了。 下一节课是什么？"

    # 凌宁：（恢复正经，推了推不存在的眼镜）
    show lingning casual pose with dissolve
    
    voice "voice/lingning/lingning_101.ogg"
    l "没有课了。"
    
    voice "voice/lingning/lingning_047.ogg"
    l "但是，身为土木系的精英，我们有一个必须攻略的副本。"
    
    voice "voice/lingning/lingning_041.ogg"
    l "那就是—— 第十一节流通过程与物质交换中心。"

    # 木子米： 说人话。
    m "说人话。"

    # 凌宁： 食堂。 抢饭。
    show lingning casual happy
    
    voice "voice/lingning/lingning_137.ogg"
    l "食堂。"
    
    voice "voice/lingning/lingning_138.ogg"
    l "抢饭。"

    # 场景结束，淡出
    scene black with fade
    stop music fadeout 1.0


# ==========================================
# 场景八：二食堂 - 午餐高峰期
# 时间：11:50
# ==========================================

    # 【BGM：激昂、混乱的战争进行曲】
    play music audio.bgm_march fadein 0.5 volume 1.0

    # 【音效：嘈杂的人声】
    # 循环播放市场/人群嘈杂声模拟食堂环境
    play sound audio.se_market loop volume 0.7

    # 【背景：人山人海的食堂】
    # 使用 dining_inside (食堂内部)
    scene bg dining_inside with fade

    # 【画面：SD小人动画】
    # 使用提供的 Q版素材和 transform 模拟混乱奔跑的场面
    # 这里通过 parallel 动画让 Q版小人在背景上快速穿梭，模拟"丧尸涌向窗口"的氛围
    show sd_muzimi_run at chase_run_left zorder 1

    "（无数的学生像丧尸一样涌向窗口，木子米、素织和凌宁显得弱小又无助）"
    hide sd_muzimi_run

    # 屏幕震动表现混乱
    show sd_suzhi_run at chase_run_left zorder 1
    voice "voice/suzhi/suzhi_114.ogg"
    s "快，这边这边。"
    hide sd_suzhi_run
    with vpunch
    


    # 隐藏Q版小人，切回正常立绘对话模式
    

    with dissolve

    # (内心独白) 木子米
    m "（地狱。 这里绝对是地狱。）" 
    m "（长春工程学院的学生难道平时都不吃饭的吗？ 为什么一到饭点就变成了饥饿游戏？！）"

    # 凌宁： （站在人群外围，面露难色）
    # 使用 lingning casual tired 或 weak 表现抗拒
    show lingning casual tired at right with dissolve
    
    voice "voice/lingning/lingning_022.ogg"
    l "这……这不符合美学。"
    
    voice "voice/lingning/lingning_035.ogg"
    l "在如此拥挤的环境中进食，还要为了一个鸡腿而此时此刻，这有辱斯文。"
    
    voice "voice/lingning/lingning_087.ogg"
    l "我决定去买面包。"

    # 素织： （眼神犀利）
    # 使用 suzhi casual angry 表现气场全开 (假设此时已穿好外套或无视服装bug，使用常规立绘表达情绪)
    show suzhi casual angry at left with moveinleft

    voice "voice/suzhi/suzhi_087.ogg"
    s "（眼神犀利，盯着远处的“特色盖浇饭”窗口） 不行！ 为了下午的英语分级考试，必须吃米饭补充碳水。"
    voice "voice/suzhi/suzhi_105.ogg"
    s "凌宁你去看包占座。 木子米，你跟我走！"

    # 木子米： 哈？我也要去挤？
    m "哈？我也要去挤？"

    # 素织： （一把拽住木子米的袖子，气场全开）
    # 播放撞击声或接触声
    play audio audio.se_bump_sfx
    
    # 素织逼近
    show suzhi casual angry at center with move

    voice "voice/suzhi/suzhi_065.ogg"
    s "少废话！ 你是肉盾！ 我们要执行“钳形攻势”！" 
    voice "voice/suzhi/suzhi_015.ogg"
    s "我去排队，你负责挡住后面插队的人！"

    # (还没等木子米反抗，他就被素织拖进了人群的洪流中)
    # 使用震动和快速移出效果模拟被拖走
    show suzhi casual angry at right with move
    hide suzhi with moveoutright
    hide lingning with dissolve
    
    stop sound fadeout 1.0 # 停止人群嘈杂声
    
    # 再次震动屏幕，模拟冲入人群的冲击感
    with vpunch
    "(还没等木子米反抗，就被素织拖进了人群的洪流中)"

    scene black with fade
    stop music fadeout 1.0
    

    # 【背景：极度拥挤的特写。四周全是人头】
    # 使用预设的特写背景，配合震动模拟拥挤感
    scene bg cafeteria_closeup with fade
    
    # 【BGM：延续上一场的激昂战争曲】
    play music audio.bgm_march if_changed
    
    # 【音效：嘈杂人声】
    play sound audio.se_market loop volume 0.8

    # 定义临时角色（仅本场景使用）
    $ man = Character("路人壮汉", color="#c62828")
    $ woman = Character("路人学姐", color="#ad1457")
    $ auntie = Character("食堂阿姨", color="#795548")

    # 模拟人群推搡的震动
    with soft_shake
    man "阿姨！我要两份红烧肉！多给点汤！"
    
    with soft_shake
    woman "别挤啊！谁踩我鞋了！"

    # 木子米：（被挤得变了形）
    # 使用猛烈震动 vpunch 表现被挤压
    with vpunch
    m "（被挤得变了形，像一张贴在墙上的海报） 素织……我还活着吗？"
    m "我的肋骨好像在抗议。"

    # 旁白描述
    "（在木子米身前，被他用双臂撑出的一小块空间保护着）"
    "（她抬头看了一眼满头大汗、正艰难地用背部抵挡后方冲击的木子米）"

    # ==========================================
    # 【CG插图：近距离特写 - 守护】
    # ==========================================
    scene cg cafeteria_protect with dissolve

    # 【演出效果：心跳漏一拍】
    # 瞬间降低背景噪音和音乐音量，制造“世界突然安静”的效果
    $ renpy.music.set_volume(0.2, delay=0.5, channel='music')
    stop sound fadeout 0.5

    # 稍微停顿，强调眼神接触
    pause 0.5

    # 素织：（心跳突然漏了一拍）
    voice "voice/suzhi/suzhi_009.ogg"
    s "……笨蛋。"
    voice "voice/suzhi/suzhi_042.ogg"
    s "这都要护住我……逞什么强"
    # 【演出效果：回到现实】
    # 恢复音量和噪音
    $ renpy.music.set_volume(1.0, delay=0.2, channel='music')
    play sound audio.se_market loop volume 0.8

    # 木子米：（听到声音，低头）
    m "（听到声音，低头） 你说啥？ 太吵了听不见！ "
    m "阿姨问你要什么菜！快喊！"

    # 素织：（回过神，脸一红）
    voice "voice/suzhi/suzhi_126.ogg"
    s "两份土豆牛肉！不要香菜！"

    # 食堂阿姨：（手抖如帕金森）
    auntie "好嘞！"

    # 【演出效果：阿姨手抖】
    # 屏幕向下轻微一沉，配合音效
    with vpunch
    "（勺子一抖，两块牛肉掉回了盆里）"

    # (内心独白) 木子米
    # 使用快速震动表现内心的崩溃
    m "（阿姨！ 那是我的肉啊！ 那是我的命啊！ 您的手是装了震动马达吗？！）"

    scene black with fade
    stop music fadeout 1.0
    stop sound fadeout 1.0
    # 【BGM：轻松、温馨的日常曲】
    # 使用 bgm_daily_warm 营造吃饭时的放松氛围
    play music audio.bgm_daily_warm fadein 1.0

    # 【背景：餐桌，三人终于坐定】
    # 使用 cafeteria_table (餐桌视角)
    scene bg cafeteria_table with fade

    # 【音效：周围依然嘈杂，但这一桌仿佛有了空气墙】
    # 降低背景嘈杂声音量，表现“空气墙”内的私密感
    play sound audio.se_market loop volume 0.3

    # 凌宁在右边，素织在左边，木子米第一人称
    show lingning casual pose at right with dissolve
    show suzhi casual normal at left with dissolve

    # 木子米：（看着盘子里可怜巴巴的三块牛肉）
    m "（看着盘子里可怜巴巴的三块牛肉）"
    m " ……这就是战争的代价吗？"
    m "我感觉我消耗的热量比摄入的还要多。"

    # 凌宁：（优雅地撕开一个小面包）
    show lingning casual happy
    
    voice "voice/lingning/lingning_046.ogg"
    l "所以说，智者不入爱河，贵族不抢饭桌。"
    
    voice "voice/lingning/lingning_118.ogg"
    l "虽然我依然很饿，但我保持了风度。"

    # 素织：（戳着盘子里的土豆）
    # 表情切换为犹豫/羞涩
    show suzhi casual shy
    "（素织戳着盘子里的土豆，看了看木子米那副惨兮兮的样子）"
    
    pause 0.5
    
    voice "voice/suzhi/suzhi_006.ogg"
    s "……喂。"

    m "嗯？"

    # 素织夹肉动作
    # 播放一个小音效模拟夹菜/放碗里的声音
    play audio audio.se_bump 
    with soft_shake # 屏幕轻微震动表现动作迅速

    # 素织：（动作飞快地丢进木子米的碗里）
    # 恢复正常表情掩饰害羞，或者保持羞涩但嘴硬
    show suzhi casual normal 
    voice "voice/suzhi/suzhi_148.ogg"
    s "（夹起自己盘子里最大的一块牛肉，动作飞快地丢进木子米的碗里）" 
    voice "voice/suzhi/脂身が多いのは嫌いなの。ゴミ処理手伝ってあげただけよ。suzhi_107.ogg"
    s "我不喜欢吃太肥的。 帮你解决垃圾。 别多想。"

    # 木子米内心吐槽
    m "（看着碗里那块明明是半肥半瘦、口感最好的牛肉）"
    m "（这哪里肥了？这明明是极品好吗！素织同学，你的傲娇属性已经暴露无遗了啊！）"

    # 木子米：（抬头，坏笑）
    m "（抬头，坏笑） 哦？是吗？ 那既然是垃圾，我就勉为其难地……"

    # 素织：（瞪眼）
    show suzhi casual angry
    voice "voice/suzhi/suzhi_139.ogg"
    s "不吃还我！"

    # 木子米：（一口塞进嘴里）
    m "（一口塞进嘴里） 唔！好吃！ 真香！ 这是充满爱意的牛肉！"

    # 素织：（脸红到了脖子根）
    # 切换到极度害羞/生气的表情
    show suzhi casual shy at left:
        linear 0.1 xoffset 10
        linear 0.1 xoffset -10
        repeat 2 # 快速抖动表现慌乱
        linear 0.1 xoffset 0

    voice "voice/suzhi/suzhi_086.ogg"
    s "咳！咳咳！ 谁……谁有爱意了！"
    voice "voice/suzhi/suzhi_138.ogg"
    s "吃饭都堵不住你的嘴！ 变态！"

    # 凌宁：（看着两人，默默地把手里的面包捏扁了）
    # 表情切换为郁闷/死鱼眼
    show lingning casual depressed with dissolve
    
    voice "voice/lingning/lingning_141.ogg"
    l "（看着两人，默默地把手里的面包捏扁了）"
    
    voice "voice/lingning/lingning_050.ogg"
    l "我觉得…… 我应该在车底，不应该在这里。"
    
    # 柠檬味时刻
    
    voice "voice/lingning/lingning_024.ogg"
    l "这面包怎么吃出了一股柠檬味？"

    # 场景温馨淡出
    scene black with fade
    stop music fadeout 1.5
    stop sound fadeout 1.5

# ==========================================
# 场景十一：图书馆 - 下午 14:00
# ==========================================


    # 【BGM：静谧、神秘的轻音乐】
    # 使用 bgm_school 营造图书馆的安静氛围，或者 bgm_depressing_piano 营造古籍区的神秘感
    # 这里选用 bgm_school 作为基础背景音
    play music audio.bgm_school fadein 1.0 volume 0.6

    # 【背景：巨大的图书馆内部】
    scene bg library with fade

    # (字幕：为了逃避下午的暴晒，三人决定去图书馆“预习”——其实是吹空调)
    centered "为了逃避下午的暴晒，三人决定去图书馆“预习”——其实是吹空调。"

    # 凌宁、素织、木子米入场
    show lingning casual pose at right with dissolve
    show suzhi casual normal at left with dissolve

    # 凌宁：（压低声音）
    
    voice "voice/lingning/lingning_144.ogg"
    l "（压低声音） 这就是知识的殿堂。"
    
    voice "voice/lingning/lingning_120.ogg"
    l "空气中都弥漫着墨水的芬芳。"
    
    voice "voice/lingning/lingning_089.ogg"
    l "我要去找几本关于西方建筑美学的书，陶冶一下情操。"

    # 木子米： 你是去找画册看图吧？
    m "你是去找画册看图吧？"

    # 素织： 我也去找几本专业书。
    voice "voice/suzhi/suzhi_019.ogg"
    s "我也去找几本专业书。 土木概论老师推荐的那几本，据说很难抢。"
    voice "voice/suzhi/suzhi_119.ogg"
    s "木子米，你……就在这占座吧。 别乱跑，也别睡着流口水。"

    # 木子米： 我是那种人吗？ 去吧去吧。
    m "我是那种人吗？ 去吧去吧。"

    # (两人离开后)
    hide lingning
    hide suzhi
    with dissolve

    # (木子米百无聊赖地趴在桌子上)
    m "（好无聊。 手机快没电了。 稍微……逛逛吧。）"
    m "（听说这图书馆顶层有一些很少人借的古籍……其实是积灰的老书。）"

    # (木子米起身，漫无目的地穿梭)
    # 切换背景或做平移效果暗示移动
    scene bg library:
        xalign 0.0
        linear 3.0 xalign 0.5
    with dissolve

    # 【音效：书本掉落的声音】
    play sound audio.se_book_drop
    with vpunch # 吓一跳的震动

    m "嗯？"

    # (木子米转过转角，看到了令人震惊的一幕)
    # (立绘出现：？？？ - 白墨萱)
    # 使用 "coat crazy" 立绘表现炸毛和疯狂科学家形象
    show baimoxuan coat crazy at center with dissolve

    # 神秘女生：（眼神空洞，语速极快）
    # 使用 b 代表白墨萱
    voice "voice/baimoxuan/baimoxuan_011.ogg"
    unknown "（眼神空洞，语速极快） 混凝土的坍落度……骨料的级配…… 不行……这个公式不对……"
    
    voice "voice/baimoxuan/baimoxuan_027.ogg"
    unknown "根据魔女的法则……这里应该加一点蜥蜴的尾巴…… 啊不对，是加减水剂……"

    # (内心独白) 木子米
    m "（……蜥蜴的尾巴？ 这家伙在说什么？ 这是土木系的学生？还是霍格沃茨的交换生？）"

    # 木子米：（小心翼翼地）
    m "（小心翼翼地） 那个……同学？ 你没事吧？书掉地上了。"

    # 神秘女生：（猛地抬头）
    # 播放惊悚或悬疑的小音效
    play music audio.bgm_stealth_happy fadein 0.5 # 切换BGM表现古怪氛围

    voice "voice/baimoxuan/baimoxuan_023.ogg"
    unknown "（猛地抬头，眼镜反过一道寒光） （声音阴森） 观测者……？"
    
    voice "voice/baimoxuan/baimoxuan_021.ogg"
    unknown "你看到了？ 你看到了我的“禁忌炼成阵”？"

    # 木子米：（看了一眼地上的书堆）
    m "（看了一眼地上的书堆，确实摆得像个魔法阵） 不……我只是看到你在乱扔公物。"

    # 神秘女生：（推了推眼镜，突然换了一副表情，变得像小动物一样可怜）
    # 因为没有特定表情差分，通过震动或位置移动表现情绪变化
    show baimoxuan coat crazy at center:
        yoffset 0
        linear 0.2 yoffset 10
    
    voice "voice/baimoxuan/baimoxuan_001.ogg"
    unknown "（推了推眼镜，突然换了一副表情，变得像小动物一样可怜） 呜……学长？还是同级？"
    
    voice "voice/baimoxuan/baimoxuan_005.ogg"
    unknown "能不能……帮我把上面那本书拿下来？ 我……我的魔力（身高）不够。"

    # ==========================================
    # 【SD小人动画：够书】
    # ==========================================
    # 隐藏正常立绘，显示Q版小人
    hide baimoxuan
    
    # 使用预设的跳跃 transform
    show sd_baimoxuan_getbook at jump_attempt 

    "（SD小人动画：女生垫着脚尖，在那蹦跶，但距离那本书还有十万八千里）"

    # 隐藏Q版，恢复正常
    hide sd_baimoxuan_getbook
    show baimoxuan coat crazy at center with dissolve

    # 木子米：（叹气） （伸手轻松拿下那本书）
    m "（叹气） （伸手轻松拿下那本书） 给。 《高层建筑结构设计》？ 这书……大一看不懂吧？"

    # 神秘女生：（接过书，眼神变得狂热）
    voice "voice/baimoxuan/baimoxuan_018.ogg"
    b "我是为了……建造巴比伦塔！"
    
    voice "voice/baimoxuan/baimoxuan_017.ogg"
    b "通往神域的塔！ 谢谢你，巨人族的好心人。 吾名 {color=#a3a3a3}白墨萱{/color} 。 你可以称呼我为——“结构力学的魔女”。"

    # 木子米：（满头黑线）
    m "（满头黑线） 我是木子米。 建议你少看点轻小说，多睡会觉。 你的黑眼圈都快掉到下巴了。"

    # 白墨萱：（突然凑近）
    show baimoxuan coat crazy:
        ease 0.3 zoom 1.2 yoffset 50 # 镜头拉近效果

    voice "voice/baimoxuan/baimoxuan_010.ogg"
    b "（突然凑近木子米，鼻子耸动了一下） 嗯？ 这股味道…… 是草莓牛奶？"
    
    voice "voice/baimoxuan/baimoxuan_004.ogg"
    b "而且是……干燥后的糖分结晶的味道？ 你……身上有甜腻的罪孽。"

    # (内心独白) 木子米
    # 恢复立绘大小
    show baimoxuan coat crazy:
        ease 0.3 zoom 1.0 yoffset 0

    m "（！！！ 这家伙是狗鼻子吗？！ 我明明洗过了！ 而且“甜腻的罪孽”是什么鬼形容词！）"

    # 素织：（突然出现在身后，声音冰冷）
    # 音乐戛然而止，或切换到尴尬BGM
    stop music fadeout 0.5
    
    # 素织从屏幕边缘阴暗地出现
    show suzhi casual angry at left with moveinleft

    voice "voice/suzhi/suzhi_117.ogg"
    s "木。子。米。"

    # 木子米：（僵硬地回头）
    # 屏幕剧烈震动一下
    with vpunch
    m "（僵硬地回头） 嗨……素织。 你听我解释，这是……"

    # 素织：（目光在白墨萱和木子米之间来回扫视）
    voice "voice/suzhi/suzhi_058.ogg"
    s "（目光在白墨萱和木子米之间来回扫视，看着白墨萱抓着木子米衣角的手）" 
    voice "voice/suzhi/suzhi_147.ogg"
    s "我就离开十分钟。 你就开始勾搭……奇怪的小学妹了？ 还真是“乐于助人”啊。"

    # 白墨萱：（看着素织，歪了歪头）
    # 白墨萱完全读不懂空气
    voice "voice/baimoxuan/baimoxuan_008.ogg"
    b "（看着素织，歪了歪头） 哦？ 正宫的气场？ 防御力很强，但攻击性过高。 容易产生裂缝（指感情破裂）。"
    
    voice "voice/baimoxuan/baimoxuan_020.ogg"
    b "需要加固。"

    # 素织：（额头青筋暴起）
    # 加上生气符号
    show icon_angry_mark at left:
        xoffset 100 yoffset -350
    with vpunch

    voice "voice/suzhi/suzhi_135.ogg"
    s "你说谁需要加固？！ 还有谁是正宫啊！ 木子米！回去了！"
    
    hide icon_angry_mark

    # (素织一把拽住木子米的后领)
    # 播放拖拽/打击音效
    play sound audio.se_hit 
    
    # 快速移出屏幕
    show suzhi casual angry at right with move
    hide suzhi with moveoutright
    
    # 模拟木子米被拖走的视角
    m "救命！ 白同学！魔女小姐！救我！"

    # 白墨萱：（挥着小手，面无表情）
    show baimoxuan coat crazy at center
    
    voice "voice/baimoxuan/baimoxuan_026.ogg"
    b "（挥着小手，面无表情） 走好。 作为报酬，我会为你祈祷……" 
    
    voice "voice/baimoxuan/baimoxuan_002.ogg"
    b "祈祷你的骨骼强度能承受住那股剪力。"

    scene black with fade
    stop music fadeout 1.0

    # 【BGM：温馨、静谧的夜曲】
    play music audio.bgm_night fadein 1.5 volume 0.8

    # 【背景：熄灯后的宿舍，只有手机屏幕的光亮】
    scene bg dorm_boys_night with fade

    # (木子米躺在床上，翻来覆去睡不着)
    # 使用ADV模式进行独白
    m "（今天真是……漫长的一天。）"
    m "（草莓牛奶事件、抢饭大战、还有那个奇怪的“魔女”白墨萱。）"
    m "（这就是大学生活吗？ 比我想象的要……热闹得多。）"

    # (手机震动) 【微信提示音】
    play sound audio.se_phone
    with soft_shake # 手机震动效果]

    # ==========================================
    # 进入手机短信模式 (NVL)
    # ==========================================
    # 清空之前的NVL文本
    nvl clear

    # 素织：睡了吗？
    s_phone "睡了吗？"

    # 木子米：没呢。在回味今天的牛肉。（滑稽表情）
    m_phone "没呢。在回味今天的牛肉。" # 假装那个生气符号是某种表情，或者这里只用文字

    # 素织：……闭嘴。
    s_phone "……闭嘴。"
    s_phone "那个……衣服洗过了。"
    s_phone "但是还有一点印子。"
    s_phone "以后要是穿不出去了，你得负责。"

    # 木子米： （打字） 行行行，我负责。 大不了我肉偿。
    # 这里模拟打错字，先显示出来
    m_phone "行行行，我负责。 大不了我肉偿。"

    # (手指一滑，发送键按下)
    # 稍微停顿让玩家看清
    window hide # 隐藏对话框
    pause 0.5
    
    # (内心独白) 木子米： 等等！ 撤回！
    # 切回ADV模式表现惊恐
    with vpunch
    m "（等等！ 撤回！ 我要打的是“赔偿”啊！ 为什么输入法会联想出“肉偿”啊！）"
    m "（这该死的智能纠错！）"

    # 【系统提示：对方已撤回一条消息】
    # 使用居中且灰色的文本模拟系统提示
    nvl clear
    "{color=#888888}【系统提示：对方已撤回一条消息】{/color}"

    # (但显然，素织已经看到了)
    # 稍微停顿
    pause 1.0

    # 素织： …… 流氓！ 去死吧！
    s_phone "……"
    s_phone "流氓！ 去死吧！ 💣🔪"

    # 木子米： （绝望地捂住脸）
    # 切回ADV模式
    m "（绝望地捂住脸） 听我解释啊！ 那是输入法的锅！"
    m "（完了……明天的英语分级考试，我可能会死在考场上。）"

    # (手机又震动了一下)
    play sound audio.se_phone
    pause 0.5

    # 素织： ……不过。
    s_phone "……不过。"
    s_phone "谢谢你今天帮我挡着。"
    s_phone "后面的人……其实挺挤的。"
    s_phone "晚安。"

    # (木子米愣住了)
    window hide
    pause 1.0

    # (看着最后那条消息，嘴角不自觉地上扬)
    m "（看着最后那条消息，嘴角不自觉地上扬）"

    # ==========================================
    # 【CG插图：素织在女生宿舍的床上】
    # ==========================================
    # 音乐淡出，或者切换到更轻柔的旋律
    scene cg suzhi_night_smile with fade

    # 木子米： （轻声） 晚安。 傲娇怪。
    m "（轻声） 晚安。 傲娇怪。"

    # 【第五章 完】
    scene black with fade
    stop music fadeout 2.0
    jump chapter_6

# ==========================================
# 剧本正文 - 第六章：极寒、升旗与修罗场餐桌
# ==========================================

# ==========================================
# 剧本正文 - 第六章：极寒、升旗与修罗场餐桌
# ==========================================

# --- 本章新增素材定义 (根据需求添加) ---
# 注意：请确保文件名与此处一致，或根据实际情况调整路径
# image suzhi winter down_jacket = "images/char/suzhi/suzhi_winter_down_jacket.png" # 已移除冬装定义

label chapter_6:

    # ==========================================
    # 【场景一：男生宿舍 - 周日傍晚 18:00】
    # ==========================================
    
    # 背景：dorm_room_sunset
    scene bg dorm_room_sunset with fade

    # BGM：合适的bgm (日常)
    play music audio.bgm_daily fadein 1.0

    # (画面：木子米正瘫在椅子上，手里拿着手柄，屏幕上显示着“GAME OVER”)
    # 使用文字描述代替画面
    "（木子米正瘫在椅子上，手里拿着手柄，屏幕上显示着“GAME OVER”）"

    # (内心独白) 木子米
    m "啊……这就是生活。"
    m "没有哨声，没有正步，没有那个魔鬼少尉的怒吼。"
    m "军训结束后的第一个周末，简直是上帝赐予土木狗的礼物。"
    m "在这两天里，我除了吃饭和上厕所，基本上就在床上和椅子之间进行两点一线的位移。"
    m "这就是物理学上的——“绝对静止”。"
    m "哪怕屏幕上是刺眼的“GAME OVER”，我的内心依然平静如水。"

    # 凌宁： （正对着镜子敷着一张黑色的面膜，手里端着一杯红茶，小拇指高高翘起）
    # 复用立绘：casual pose
    show lingning casual pose at center with dissolve

    voice "voice/lingning/lingning_107.ogg"
    l "木子米，你这种姿态，简直像是一只失去了梦想的咸鱼。"
    
    voice "voice/lingning/lingning_009.ogg"
    l "要知道，即便是周末，贵族也要保持优雅的姿态。"
    
    voice "voice/lingning/lingning_129.ogg"
    l "你看我，正在通过冥想来净化这周被高数课污染的灵魂。"
    
    voice "voice/lingning/lingning_023.ogg"
    l "这面膜可是我托人从海外代购的“深海泥”，能让我的肌肤重回十八岁的光泽……"
    
    voice "voice/lingning/lingning_060.ogg"
    l "……虽然我现在也才十八岁。"

    # 木子米： （翻了个白眼，放下手柄，伸了个懒腰）
    m "得了吧，凌宁。"
    m "你那个“冥想”就是贴着面膜刷朋友圈。"
    m "而且，你那杯红茶已经凉透了，表面都结了一层茶渍了，这符合你的“贵族美学”吗？"

    # 凌宁： （优雅地揭下面膜一角，露出洁白的皮肤，眼神深邃）
    # 切换表情：casual happy
    show lingning casual happy

    voice "voice/lingning/lingning_056.ogg"
    l "哼，你不懂。" 
    
    voice "voice/lingning/lingning_090.ogg"
    l "凉茶亦有凉茶的风味，正如人生总有低谷。"
    
    voice "voice/lingning/lingning_126.ogg"
    l "苦涩中带着回甘，这才是成熟男人的味道。"
    
    voice "voice/lingning/lingning_040.ogg"
    l "而且，明天又是崭新的一周，我们要以完美的精神面貌去迎接……"

    # (突然，两人的手机同时发出了尖锐且急促的提示音，打破了这份宁静) 
    # 【SE：Ding! Ding! Ding!】
    stop music fadeout 0.5
    play sound audio.se_phone
    queue sound audio.se_phone
    queue sound audio.se_phone
    with soft_shake

    # 木子米： （懒洋洋地拿起手机，眉头微皱）
    m "谁啊？这么大火气？ 难道是代班发红包了？还是哪位大神又在群里表白了？"

    # (特写：手机屏幕界面)
    # 使用NVL模式模拟手机通知
    window hide
    nvl clear
    
    "{color=#ff0000}【土木工程学院25级新生群】{/color}\n\n【代班】：@全体成员"
    "【紧急通知】：\n 接学院通知，为加强爱国主义教育，展现土木学子风采，提升新生凝聚力。"
    "明天（周一）早晨6:00，全院大一新生于操场举行升旗仪式。"
    "要求：\n全员着装整齐（建议穿厚点，早晨气温较低），5:45集合完毕。\n严禁迟到！严禁缺席！缺席者通报批评并扣除综测分！"
    
    nvl clear
    window show

    # (沉默。死一般的沉默。只有电脑机箱风扇的嗡嗡声。)
    stop sound
    "…………"
    
    # (画面回归：木子米的手柄彻底掉在了地上，发出沉闷的响声。凌宁刚刚揭了一半的面膜啪嗒一声掉在地上，像一块黑色的抹布。)
    play sound audio.se_book_drop # 模拟掉落声

    # 木子米： （瞳孔地震，声音颤抖）
    m "六……六点？"
    m "5:45集合？"
    m "也就是说，为了洗漱、穿衣、抢厕所，我们最晚5:15就要起床？"
    
    with vpunch
    m "这还是人过的日子吗？！"

    # 凌宁： （看着地上的面膜，发出一声凄厉的惨叫）
    # 切换表情：casual surprised
    show lingning casual surprised with vpunch

    voice "voice/lingning/lingning_070.ogg"
    l "不！！！"
    
    voice "voice/lingning/lingning_084.ogg"
    l "我的美容觉！"
    
    voice "voice/lingning/lingning_075.ogg"
    l "我的生物钟！"
    
    voice "voice/lingning/lingning_069.ogg"
    l "我的胶原蛋白！"
    
    voice "voice/lingning/lingning_032.ogg"
    l "这简直是对人权的践踏！"
    
    voice "voice/lingning/lingning_123.ogg"
    l "是对美学的亵渎！"
    
    # 切换表情：casual depressed
    show lingning casual depressed
    
    voice "voice/lingning/lingning_074.ogg"
    l "现在的长春早晨只有几度你知道吗？！"
    
    voice "voice/lingning/lingning_116.ogg"
    l "零度线徘徊啊！"
    
    voice "voice/lingning/lingning_079.ogg"
    l "这是要把我们冻成冰雕艺术品吗？！"
    
    voice "voice/lingning/lingning_080.ogg"
    l "我那件单薄的风衣根本扛不住这种魔法攻击啊！"

    # 木子米： （绝望地看向窗外）
    # 播放风声/压抑BGM
    play music audio.bgm_depressing_piano fadein 1.0

    m "（此时天色已暗，窗户缝隙里传来了呼啸的风声，树枝在风中狂乱舞动）"
    
    # (内心独白) 木子米
    m "听这风声……像是在嘲笑我们。"
    m "明天的操场，绝对是西伯利亚体验营。"
    m "再见了，我那短暂而美好的周末。 我的天堂，崩塌了。"
    m "我甚至能预见到明天早上那如同丧尸出笼般的场景……"


    # ==========================================
    # 【场景二：操场 - 周一清晨 05:50】
    # ==========================================

    # 背景：playground_morning
    scene bg playground_morning_and_morning with fade
    
    # BGM：合适的 (寒冷/压抑)
    play music audio.bgm_depressing_piano volume 0.8

    # (画面晃动，模拟木子米在寒风中颤抖的视角，视线有些模糊)
    show bg playground_morning_and_morning at slight_shake

    # (内心独白) 木子米
    m "冷。"
    m "好冷。 非常冷。"
    m "如果说军训时的烈日是物理攻击，那现在的寒风就是魔法穿透伤害。"
    m "它无视你的防御，顺着领口、袖口、裤脚，直接钻进你的骨髓里，冻结你的灵魂。"
    m "这就是长春的十月吗？这分明是北极的夏天！"
    m "我的脚趾已经失去了知觉，仿佛踩在两块冰砖上。"

    # 凌宁： （站在旁边，裹着一件看起来很贵但并不保暖的羊绒风衣，整个人在以高频率震动，牙齿打架的声音清晰可闻）
    # 复用立绘：casual tired (模拟发抖)
    show lingning casual tired at center with dissolve
    
    voice "voice/lingning/lingning_104.ogg"
    l "木……木子米……"
    
    voice "voice/lingning/lingning_058.ogg"
    l "我觉得……我的下巴……好像……冻掉了……"
    
    voice "voice/lingning/lingning_034.ogg"
    l "这种天气……居然……还要……升旗……"
    
    voice "voice/lingning/lingning_030.ogg"
    l "这不优雅……这一点都……不优雅……"
    
    voice "voice/lingning/lingning_006.ogg"
    l "我应该……穿那件……那件看起来像熊一样的羽绒服的……"
    
    voice "voice/lingning/lingning_096.ogg"
    l "失策……"

    # 木子米： （把羽绒服的拉链拉到最上面，只露出一双眼睛，双手插在袖筒里）
    m "省省力气吧……别说话了。"
    m "说话会带走热量。"
    m "而且你看，辅导员正盯着这边呢，你要是想上去发表个“冻感获奖感言”，我不拦着你。"
    m "你看前面。"

    # (镜头切换：女生方队)
    hide lingning with dissolve

    # (虽然大家都裹得很严实，但在清晨的寒风中，依然显得有些单薄。有些女生甚至在原地小幅度跺脚取暖)
    # (木子米在人群中搜寻着那个熟悉的身影)

    # ========================================================
    # 【更新】 使用 CG：寒风中的素织 代替原本的文字描述+立绘
    # ========================================================
    
    # 隐藏对话框，展示CG
    window hide
    scene cg suzhi_cold_morning with dissolve
    window show

    # (CG特写描述)
    "（她穿着一件米白色的长款羽绒服，领口拉得高高的，遮住了小半张脸，露出的几缕发丝被风吹得有些凌乱。）"
    "（并没有戴围巾，显得脖颈修长而干净。她的鼻尖被冻得通红，双手深深地插在口袋里，虽然缩着脖子，但站姿依然比周围的人挺拔。）"
    "（似乎感觉到了视线，她微微侧头，眼神迷离，显然还没睡醒，甚至还没来得及戴隐形眼镜，眯着眼睛的样子像只困倦的猫。）"

    # (内心独白) 木子米
    m "在那儿。"
    m "即便裹成了粽子，她还是那么显眼。"
    m "没有戴那条红围巾啊……也是，听说那条围巾拿去干洗了。"
    m "不过…… 看着她露在外面的那个冻红的鼻尖，居然觉得有点……可爱？"
    m "平时那个总是冷着脸、怼天怼地的素织，现在的样子倒是多了几分呆萌。"
    m "噗……要是让她知道我这么形容，估计又要踩我一脚。"

    # (就在这时，广播响起了刺耳的电流声)
    # 【SE：电流声/铃声】
    stop music fadeout 0.5
    play sound audio.se_bell

    # 恢复场景，回退立绘：使用 casual normal
    scene bg playground_morning_and_morning
    show suzhi casual normal at center
    with fade

    # 【广播音：升旗仪式，现在开始！全体肃立！出旗！】
    "{b}【广播音】{/b}：升旗仪式，现在开始！全体肃立！出旗！"

    # (激昂的国歌声响起)
    play music audio.bgm_march fadein 1.0

    # (所有人不得不把手从温暖的口袋里拿出来，行注目礼。寒风无情地掠过每一只暴露在空气中的手)
    # (内心独白) 木子米
    m "手…… 我的手…… 失去知觉了。"
    m "看着国旗缓缓升起，我的爱国之情很热烈，但我的手指真的很冰凉，僵硬得像枯树枝。"
    m "这一刻，脑海中那些关于高数、关于作业的烦恼统统消失了。"
    m "我唯一的念头就是—— 豆浆。 热腾腾的、冒着白气的、甜度适中的豆浆。"
    m "最好再来一根刚出锅的油条。 那是生命的救赎。"


    # ==========================================
    # 【场景三：二食堂 - 早晨 06:30】
    # ==========================================

    # 背景：cafeteria_closeup
    scene bg cafeteria_closeup with fade

    # BGM：嘈杂的人声 (se_market) + bgm (funny)
    play sound audio.se_market loop volume 0.8
    play music audio.bgm_daily_funny fadein 1.0

    # (画面：木子米端着餐盘，站在食堂中央，一脸茫然。餐盘里的粥随着人群的挤压在边缘晃荡)
    # (SD小人动画：木子米头顶着“寻找座位”的任务标记...)
    show sd_muzimi_run at panic_run_left
    "（木子米端着餐盘，站在食堂中央，一脸茫然。餐盘里的粥随着人群的挤压在边缘晃荡。）"
    hide sd_muzimi_run with dissolve

    # (内心独白) 木子米
    m "失策了。"
    m "大意了。"
    m "全土木学院的人都在同一时间解散。 全土木学院的人都在同一时间涌向食堂。"
    m "这哪里是吃饭，这分明是《丧尸围城》的片场！"
    m "放眼望去，别说空位了，连站着吃的地方都快没了。"
    m "空气中弥漫着一股焦躁和饥饿的味道。"

    # 凌宁： （不知何时已经被人群冲散了）
    # （远处传来凌宁微弱且绝望的呼喊）
    
    voice "voice/lingning/lingning_081.ogg"
    l "哎呀！别挤我的风衣！"
    
    voice "voice/lingning/lingning_066.ogg"
    l "这是羊毛的！"
    
    voice "voice/lingning/lingning_038.ogg"
    l "那位同学！"
    
    voice "voice/lingning/lingning_125.ogg"
    l "你的肉包子油蹭到我袖子上了！"
    
    voice "voice/lingning/lingning_068.ogg"
    l "Oh no！"
    
    voice "voice/lingning/lingning_083.ogg"
    l "我的绅士风度！"

    # 木子米： （叹气，摇了摇头）
    m "看来凌宁是没指望了，他正在进行一场保卫羊毛大衣的圣战。"
    m "我手里这碗好不容易抢到的皮蛋瘦肉粥，再不找地方放就要凉了。"
    m "我的手已经酸了。 难道这就是我今天的命运？ 站着喝粥？还是去外面吹着冷风吃？"

    # ？？？： （远处传来一个清脆的声音，穿透了嘈杂的人群）
    unknown "喂！ 那边那个呆子！ 往哪看呢！"

    # (木子米愣了一下，循声望去，试图在涌动的人头中定位声源)
    # (镜头推近：食堂靠窗的一个角落。素织正坐在那里，有些显眼。)
    # 切换背景至餐桌
    scene bg cafeteria_table with fade

    # 素织：挥舞油条
    # 回退立绘：使用 casual angry (嫌弃表情)
    show suzhi casual angry at center with dissolve

    "（素织正坐在那里，有些显眼。她一只手拿着勺子，另一只手高高举起，甚至还拿着一根刚咬了一口的油条在挥舞，像是在挥舞荧光棒。）"

    # 素织： （看到木子米终于看过来，立刻放下油条，有些不自然地指了指对面的空位，脸上带着一丝嫌弃）
    voice "voice/suzhi/suzhi_100.ogg"
    s "看什么看！ 这里！ 你是瞎了吗！"

    # (木子米如获大赦，端着餐盘艰难地穿过人群，嘴里说着“借过借过”，像是在穿越雷区，终于挤到了素织那一桌)
    "（木子米如获大赦，端着餐盘艰难地穿过人群，嘴里说着“借过借过”，像是在穿越雷区，终于挤到了素织那一桌。）"


    # ==========================================
    # 【场景四：食堂角落 - 双人餐桌】
    # ==========================================

    # BGM：轻快、温馨的钢琴曲，带着一点点暧昧
    stop sound fadeout 1.0
    play music audio.bgm_daily_warm fadein 1.0

    # 背景：cafeteria_table (已在)

    # 木子米： （把餐盘放下，一屁股坐在椅子上，长舒一口气）
    m "呼…… 素织，你是天使吗？"
    m "我刚才差点以为我要蹲在门口吃了，或者和凌宁一样在人海中沉沦。"

    # 素织： （傲娇地哼了一声，低头喝了一口豆浆，掩饰表情）
    # 切换表情：casual shy
    show suzhi casual shy
    voice "voice/suzhi/suzhi_123.ogg"
    s "少恶心了。 我只是……只是刚才占座的时候，多占了一个。"
    
    voice "voice/suzhi/suzhi_120.ogg"
    s "本来想把包放那儿的，不想让那个油腻腻的学长坐我对面。"
    
    voice "voice/suzhi/suzhi_137.ogg"
    s "看你像个无头苍蝇一样转来转去，怪可怜的。 就算是……日行一善吧。"

    # (木子米： （坐下，看着素织）)
    # (她已经把羽绒服的帽子摘了下来，拉链也拉开了一些，露出里面加绒卫衣的领口，白皙的脖颈和红润的脸颊形成鲜明对比。)
    # (脸上被风吹出的红晕还没消退，看起来格外可爱)

    # (内心独白) 木子米
    m "“日行一善”吗？"
    m "可是你看，这里明明是四人桌，旁边两个位置都堆满了书，显然是帮室友占的。 这剩下的唯一一个位置，分明是特意留给我的吧？"
    m "而且她刚才挥舞油条的动作……噗，真是毫无形象可言。"
    m "但我还是别拆穿她了，不然这顿早饭可能要变成“谋杀现场”。"

    # 木子米： （搅拌着粥，感受着热气扑面而来）
    m "不管怎么说，谢了。 刚才外面真冷啊，我看你一直在抖。 没戴围巾，脖子不冷吗？"

    # 素织： （动作顿了一下，眼神有些闪烁，不自然地摸了摸脖子）
    # 切换表情：casual surprise
    show suzhi casual surprise
    voice "voice/suzhi/suzhi_057.ogg"
    s "哪有。 我穿了加绒的卫衣，领子很高。"
    
    voice "voice/suzhi/suzhi_055.ogg"
    s "倒是你，穿那么少，在那一直吸鼻涕。"
    
    voice "voice/suzhi/suzhi_124.ogg"
    s "脏死了。 还有，你的粥都要洒出来了，能不能稳重点。"

    # 木子米： （尴尬地摸了摸鼻子）
    m "这是生理反应！我又控制不了鼻涕！ 而且……"
    m "（突然发现素织盘子里有两个剥好的鸡蛋，光溜溜的，摆得很整齐）"
    m "那个，素织同学。 你早餐吃这么丰盛吗？两个鸡蛋？ 这胆固醇是不是有点超标？"

    # 素织： （脸一红，眼神慌乱了一瞬，随即迅速把其中一个鸡蛋夹起来，动作粗暴地丢进木子米的碗里）
    # 切换表情：casual angry
    show suzhi casual angry with vpunch

    voice "voice/suzhi/suzhi_142.ogg"
    s "闭嘴！ 买多了！ 食堂阿姨手抖给多了不行吗？"
    
    voice "voice/suzhi/suzhi_052.ogg"
    s "而且这鸡蛋有点小，我吃不饱……不对，我是说我吃不下了！"
    
    voice "voice/suzhi/suzhi_097.ogg"
    s "帮我处理掉！ 要是剩下了，又要被那个保洁阿姨念叨浪费粮食。"

    # (内心独白) 木子米
    m "食堂阿姨手抖会多给一个剥好的鸡蛋？"
    m "而且还是剥得这么完美的鸡蛋？ 这概率比我高数考满分还低吧？ 这分明是……特意买给我的吧？"

    # 木子米： （看着碗里的鸡蛋，忍不住笑出了声，心里暖暖的）
    m "是是是，阿姨手抖。 那我就勉为其难，帮你分担这份“多余的营养”吧。 正好我也需要补充点蛋白质，不然脑子都被冻僵了。"

    # 素织： （瞪了他一眼，但嘴角却止不住地上扬，耳根微红）
    # 切换表情：casual smile
    show suzhi casual smile
    voice "voice/suzhi/suzhi_043.ogg"
    s "吃你的饭！ 再废话就把鸡蛋吐出来！ 真是的，给你吃还那么多废话。"

    # (两人之间的气氛变得微妙而温馨。周围的嘈杂声仿佛都变成了背景音。窗外的阳光洒在桌面上，升腾的热气模糊了彼此的脸庞，有一种岁月静好的错觉)
    "（两人之间的气氛变得微妙而温馨。周围的嘈杂声仿佛都变成了背景音。窗外的阳光洒在桌面上，升腾的热气模糊了彼此的脸庞，有一种岁月静好的错觉。）"

    # (内心独白) 木子米
    m "这算什么？"
    m "共进早餐？ 虽然环境是乱糟糟的食堂，但这感觉……居然还不赖。"
    m "如果每天早晨都能这样……"

    # ？？？： （突然,一个没有任何起伏、甚至带着一丝机械感的清冷声音在头顶响起，打破了这份旖旎）
    
    voice "voice/baimoxuan/baimoxuan_022.ogg"
    unknown "观测到了。 两个独立的生命体，正在进行高热量的物质交换。"
    
    voice "voice/baimoxuan/baimoxuan_003.ogg"
    unknown "且伴随着名为“荷尔蒙”的化学反应。 有趣的实验样本。 打断一下。"

    # (木子米和素织同时吓了一跳，抬头看去)
    play sound audio.se_bump_sfx
    with vpunch


    # ==========================================
    # 【场景五：食堂 - 餐桌】
    # ==========================================

    # BGM：适合的 (古怪/潜行)
    play music audio.bgm_stealth_happy fadein 1.0

    # 【立绘：白墨萱】【背景：cafeteria_table】
    # 回退素织立绘：使用 casual angry
    show suzhi casual angry at left with move
    show baimoxuan coat crazy at right with dissolve

    # 木子米： （嘴里的粥差点喷出来，剧烈咳嗽起来）
    m "咳咳咳！ 白……白墨萱？！"
    m "你怎么在这儿？ 还有，你这身打扮……你是刚从实验室逃难出来吗？ 还是在实验室里住了三天？"

    # 白墨萱： （毫不客气地拉开旁边的椅子——把素织用来占座的书推到一边，书本发出摩擦声，她直接坐下，发出一声满足的叹息）
    # 播放推书声
    play sound audio.se_drag
    
    voice "voice/baimoxuan/baimoxuan_024.ogg"
    b "纠正。 不是逃难。 是通宵完成了“桁架结构抗震模拟”后的战略性撤退。"
    
    voice "voice/baimoxuan/baimoxuan_015.ogg"
    b "我的机体能量已耗尽，急需高蛋白补充。 食堂的人流密度超过了我的预设值，寻找空位耗费了我宝贵的3分20秒。"

    # 素织： （看着白墨萱推开自己的书，眉头瞬间皱成了“川”字，眼神变得犀利）
    # （语气降温至零下，散发着杀气）
    voice "voice/suzhi/suzhi_063.ogg"
    s "喂。 那是我的书。 而且……这里有人了。"
    
    voice "voice/suzhi/suzhi_128.ogg"
    s "你没看到我们正在吃饭吗？"

    # 白墨萱： （转头看着素织，推了推眼镜，镜片反光，完全无视了素织的怒气）
    voice "voice/baimoxuan/baimoxuan_016.ogg"
    b "我知道。 你是“防御者”。 昨天在图书馆见过。 你的领地意识过剩，这不利于学术交流。 而且……"
    
    b "（指了指空位，一本正经地分析）"
    
    voice "voice/baimoxuan/baimoxuan_019.ogg"
    b "根据空间利用率最大化原则，这把椅子的闲置是对公共资源的浪费。 这里的人员密度为每平方米4人，而这把椅子占用面积0.25平方米。 所以我坐这里，符合结构力学的最优解，也符合资源分配的帕累托最优。"

    # 素织： （额头青筋暴起，手里的筷子都要捏断了，声音提高了一个八度）
    show suzhi casual angry with vpunch
    voice "voice/suzhi/suzhi_028.ogg"
    s "你……！"
    
    voice "voice/suzhi/suzhi_099.ogg"
    s "什么叫“防御者”！ 还有，谁跟你讨论结构力学了！ 这是礼貌问题！礼貌！"
    
    voice "voice/suzhi/suzhi_102.ogg"
    s "你不懂先来后到吗？！"

    # 木子米： （感到一阵恶寒，夹在两个女人中间瑟瑟发抖，连忙出来打圆场）
    m "那个……素织，冷静点，别生气。"
    m "白同学她……脑回路可能跟正常人不太一样。 你就当她是……是个正在加载程序的机器人？"
    m "或者是刚出土的文物？"

    # 白墨萱： （无视了剑拔弩张的气氛，直接抓起一个油腻腻的鸡腿咬了一口，发出清脆的咀嚼声）
    voice "voice/baimoxuan/baimoxuan_009.ogg"
    b "嗯……油脂。 令人愉悦的碳链结构。 这种高热量能迅速转化为ATP。"
    
    # （突然凑近木子米，鼻子几乎贴到了木子米的脸上，木子米甚至能闻到她身上淡淡的机油味）
    show baimoxuan coat crazy:
        ease 0.3 zoom 1.2 xoffset -100

    voice "voice/baimoxuan/baimoxuan_013.ogg"
    b "巨人。 你的鸡蛋。 蛋白的凝固程度很完美，表面张力保持得不错。 是你孵化的吗？"

    # 木子米： （战术后仰，差点连人带椅子翻过去）
    m "不！ 这是煮熟的！孵化不出来的！ 还有，别靠这么近！ 你的眼镜都要戳到我眼睛了！"
    
    # 恢复立绘位置
    show baimoxuan coat crazy:
        ease 0.3 zoom 1.0 xoffset 0

    # 素织： （啪的一声把筷子拍在桌子上，震得碗里的粥都洒了出来）
    play sound audio.se_bump
    # （伸出一只手，直接挡在白墨萱和木子米中间，像护食的母狮子，眼神凶狠）
    
    voice "voice/suzhi/suzhi_111.ogg"
    s "离他远点！ 这是我给…… 这是我的鸡蛋！ 你想吃自己买去！ 别打他的主意！"

    # 白墨萱： （歪了歪头，看着素织的手，又看了看素织愤怒的脸，仿佛在观察一种新物种）
    voice "voice/baimoxuan/baimoxuan_007.ogg"
    b "哦？ 这种反应…… 在生物学上，被称为“护偶行为”。"
    
    voice "voice/baimoxuan/baimoxuan_025.ogg"
    b "通常出现在繁殖季节的……哺乳动物身上。 为了保护配偶和后代，雌性会表现出极强的攻击性。 有趣的样本。"

    # 素织： （脸瞬间爆红，像个熟透的番茄，甚至蔓延到了脖子根）
    # （尖叫，声音颤抖）
    show suzhi casual surprise with vpunch
    voice "voice/suzhi/suzhi_143.ogg"
    s "闭嘴！！！ 什么繁殖季节！ 你这个疯女人在说什么胡话！"
    
    voice "voice/suzhi/suzhi_134.ogg"
    s "谁……谁是配偶啊！ 木子米！你管管她！ 你是死人吗！"

    # 木子米： （一脸生无可恋，双手举起投降状，欲哭无泪）
    m "我……我管不了啊！"
    m "这可是魔女啊！ 我说的话她能听懂一半就不错了！ 而且“繁殖季节”什么的……我也很无辜啊！"

    # 白墨萱： （淡定地喝了一口那杯绿色的饮料，完全不受干扰）
    voice "voice/baimoxuan/baimoxuan_006.ogg"
    b "那是芹菜汁。 你要喝吗？巨人。 可以提高神经突触的传导速度，让你更聪明一点。"
    
    voice "voice/baimoxuan/baimoxuan_012.ogg"
    b "虽然味道像是在咀嚼生化武器，或者像是在喝液态的草地。"

    # 木子米： （疯狂摇头，脸色发青）
    m "不用了！谢谢！ 我还想多活两年！ 这种黑暗料理你自己留着吧！"

    # (画面：三人同框。中间是无奈扶额、只想找个地缝钻进去的木子米，左边是气鼓鼓、脸红红的素织，右边是面无表情、正在狂啃鸡腿的白墨萱。周围是嘈杂的食堂背景，路过的同学纷纷投来八卦的目光)
    # (内心独白) 木子米
    m "救命。"
    m "这顿饭还能好好吃吗？ 左边是傲娇的青梅竹马（伪），右边是中二病的科学怪人。 我的餐桌变成了战场。"
    m "而且…… 我看周围的人都已经开始拿出手机拍照了，还有人在窃窃私语。"
    m "明天校内论坛的头条绝对是——《土木系修罗场：两女争一男，究竟是人性的扭曲还是道德的沦丧？》"
    m "或者是——《震惊！某土木男在食堂公然开后宫！》 我要社会性死亡了。"

    # 素织： （深吸几口气，努力平复心情，重新拿起筷子，手还在微微发抖）
    # （冷冷地瞥了白墨萱一眼，语气中充满了敌意）
    show suzhi casual gloomy
    voice "voice/suzhi/suzhi_110.ogg"
    s "既然坐下了，就安静吃饭。"
    
    voice "voice/suzhi/suzhi_140.ogg"
    s "吃完赶紧走。 别打扰我们。 你的白大褂味太重了，影响食欲。"

    # 白墨萱： （咀嚼着红烧肉，腮帮子鼓鼓的，像只仓鼠）
    voice "voice/baimoxuan/baimoxuan_014.ogg"
    b "无法承诺。 数据采集尚未完成。 我需要观察“巨人”在进食时的下颚咬合力。 这对我设计新型破碎机有参考价值。 而且，我对你们这种“非理性”的进食交流模式很感兴趣。"

    # 木子米： （哭笑不得，敲了敲桌子）
    m "我是破碎机吗？！ 白同学，能不能请你把我想象成人类？ 哪怕是只猴子也行啊！"

    # 素织： （突然冷笑一声，夹起一块咸菜里巨大的姜块，放到木子米碗里）
    show suzhi casual smile
    voice "voice/suzhi/suzhi_075.ogg"
    s "呵。 既然你是破碎机，那这个你也吃了吧。 我不爱吃姜。"
    
    voice "voice/suzhi/suzhi_067.ogg"
    s "反正你是机器，应该没有味觉吧？"

    # 木子米： （看着碗里那块伪装成土豆的巨大姜块，欲哭无泪）
    m "素织…… 这是迁怒吧？"
    m "这绝对是迁怒吧？！ 我是无辜的啊！"


    # ==========================================
    # 【场景六：食堂外 - 去教室的路上 07:15】
    # ==========================================

    # 背景：campus_road_blur
    scene cg campus_road_blur with fade
    
    # BGM：轻快的校园步行曲
    play music audio.bgm_campus fadein 1.0

    # (白墨萱因为要去实验室，在食堂门口就跟他们分道扬镳了——临走前还顺走了木子米口袋里的一颗薄荷糖，说是作为“实验报酬”，留下木子米在风中凌乱)
    "（白墨萱因为要去实验室，在食堂门口就跟他们分道扬镳了——临走前还顺走了木子米口袋里的一颗薄荷糖，说是作为“实验报酬”，留下木子米在风中凌乱。）"

    # (木子米和素织并肩走着。素织一直低着头，踢着脚下的小石子，似乎还在生气，脚步有些快)
    # 保持 casual 立绘
    show suzhi casual normal at center with dissolve

    # 木子米： （试探性地，小心翼翼地开口）
    m "那个……还在生气？ 气坏了身子可不划算。"

    # 素织： （没好气地，头也不回）
    # 切换表情：casual gloomy
    show suzhi casual gloomy
    voice "voice/suzhi/suzhi_079.ogg"
    s "没有。 我跟一个神经病生什么气。 那是浪费我的情绪。 倒是你。"

    # 木子米：
    m "我？ 我怎么了？"

    # 素织： （停下脚步，转过身，认真地盯着木子米，眼神里带着一丝警告）
    voice "voice/suzhi/suzhi_096.ogg"
    s "你以后……离那个白墨萱远点。"
    
    voice "voice/suzhi/suzhi_024.ogg"
    s "那个女人……很危险。 不仅脑子不正常，而且……很奇怪。"

    # 木子米： （有些好笑）
    m "危险？你是说她会用扳手敲我的头吗？ 还是把我抓去当小白鼠？ 她就是有点中二，沉迷学术，其实人不坏。"

    # 素织： （咬了咬嘴唇，眼神有些复杂，似乎有些话想说又没说出口）
    # 切换表情：casual shy
    show suzhi casual shy
    voice "voice/suzhi/suzhi_090.ogg"
    s "笨蛋。 我指的不是那个危险。 那个女人的眼神……像是要把你拆了一样。 总之……"

    # （她突然伸出手，帮木子米整理了一下被风吹乱的衣领，动作轻柔而自然）
    show suzhi casual normal:
        ease 0.5 zoom 1.1 yoffset 50
    "（她突然伸出手，帮木子米整理了一下被风吹乱的衣领，动作轻柔而自然。）"

    voice "voice/suzhi/suzhi_031.ogg"
    s "你是我的……室友的邻居的朋友。 要是被怪人拐跑了，我会很没面子的。 而且，那个鸡蛋是我给你的，要是被她抢走了，我就……我就再也不给你买了！ 懂了吗？"

    # 木子米： （看着近在咫尺的脸庞，闻到了她身上淡淡的洗发水香味，混合着清晨空气的清冽味道） （心跳突然漏了一拍，脸颊微微发热）
    # 恢复立绘
    show suzhi casual normal:
        ease 0.5 zoom 1.0 yoffset 0
    m "懂……懂了。 放心吧。 我又不是实验器材，拐不跑的。 而且，我也更喜欢吃正常的早餐。"

    # 素织： （满意地拍了拍他的肩膀，恢复了平时的傲气，嘴角勾起一抹不易察觉的微笑）
    # 切换表情：casual smile
    show suzhi casual smile
    voice "voice/suzhi/suzhi_070.ogg"
    s "这就好。 算你识相。 走吧，第一节课是制图，要是迟到了，老师会把你的头按在图纸上摩擦的。"

    # 木子米： （惨叫，看了看表）
    m "啊！差点忘了！ 只剩五分钟了！ 快跑！"

    # (两人在林荫道上奔跑起来，书包在背上跳跃，留下一串青春的脚步声和笑声)
    play sound audio.se_foot_stomp
    hide suzhi with moveoutright

    # (内心独白) 木子米
    m "虽然早起很痛苦。"
    m "虽然升旗很冷。 虽然早饭吃得像打仗。 但是…… 看着前面那个飞扬的马尾辫，还有她因为奔跑而泛红的脸颊。 我觉得，这个周一，好像也没那么糟糕。"
    m "大概吧。 只要不是每天都有修罗场就好……"
    
    # 第六章 完
    scene black with fade
    stop music fadeout 2.0
    centered "{size=60}第六章 完{/size}"

    jump chapter_7


label chapter_7:

    # ==========================================
    # 【场景一：制图教室 - 上课时间】
    # ==========================================

    scene bg classroom_desk with fade

    play music audio.bgm_classroom fadein 1.0

    "上课铃声还没响。"
    "工程制图课。"
    "听说老师是个狠人。"

    show lingning casual pose at left with moveinleft

    l "这就是制图教室吗。"
    l "一股子蓝图味。"
    l "我的艺术细胞在躁动。"

    show suzhi casual normal at right with moveinright

    s "你那不是艺术细胞。"
    s "是戏精细胞。"

    m "别吵了。"
    m "赶紧找位置坐。"

    show lingning casual happy

    l "我要坐窗边。"
    l "光线好。"
    l "画图需要氛围感。"

    s "随你。"
    s "我坐这里就行。"
    s "离黑板近。"

    m "那我坐你后面。"

    show suzhi casual gloomy

    s "为什么。"

    m "方便借橡皮。"

    show suzhi casual angry

    s "你没带？"

    m "忘了。"

    s "你脑子也忘了。"

    show lingning casual surprised

    l "我有备用的。"
    l "皇家橡皮。"
    l "要吗。"

    show suzhi casual normal

    m "你的太香了。"
    m "用了会头晕。"

    show lingning casual depressed

    l "不懂欣赏。"

    play sound audio.se_bell

    "老师来了。"

    hide lingning with dissolve
    hide suzhi with dissolve

    show tea_draft strict at center with dissolve

    tea_draft "安静。"
    tea_draft "我是你们的制图老师。"
    tea_draft "姓严。"
    tea_draft "严谨的严。"

    show tea_draft normal

    tea_draft "我的课有三个规矩。"
    tea_draft "第一。"
    tea_draft "不许迟到。"
    tea_draft "第二。"
    tea_draft "不许抄袭。"
    tea_draft "第三。"
    tea_draft "不许敷衍。"

    show tea_draft strict:
        ease 0.3 zoom 1.05

    tea_draft "听懂了吗。"

    show tea_draft strict:
        ease 0.3 zoom 1.0

    m "听懂了。"
    l "明白。"
    s "是。"

    show tea_draft normal

    tea_draft "很好。"
    tea_draft "翻开书。"
    tea_draft "今天学基本线条。"
    tea_draft "别小看线条。"

    show tea_draft strict

    tea_draft "线都画不直。"
    tea_draft "别当工程师。"

    show lingning casual happy at left with dissolve
    show suzhi casual normal at right with dissolve

    l "画直线。"
    l "这还不简单。"
    l "我有尺子。"

    show tea_draft strict at center with dissolve

    tea_draft "尺子？"

    with vpunch

    tea_draft "谁让你用尺子。"

    show lingning casual surprised

    l "不用尺子？"

    tea_draft "徒手画。"

    l "徒手？"

    show tea_draft normal

    tea_draft "对。"
    tea_draft "尺子是辅助。"
    tea_draft "手稳才叫本事。"

    show lingning casual depressed

    l "这不科学。"

    tea_draft "科学在后头。"
    tea_draft "现在练手感。"

    show tea_draft strict

    tea_draft "开始。"

    show suzhi casual normal

    s "别抱怨了。"
    s "画吧。"

    m "凌宁你手抖吗。"

    show lingning casual happy

    l "怎么可能。"
    l "我是经过军训洗礼的人。"

    show suzhi casual smile

    s "那你线条怎么像蚯蚓。"

    show lingning casual surprised

    l "这是艺术。"
    l "曲线美。"

    show suzhi casual normal

    s "老师要直线。"

    show lingning casual pose

    l "直线缺乏灵魂。"

    show tea_draft strict at center with dissolve

    tea_draft "那位同学。"
    tea_draft "你叫凌宁？"

    show lingning casual surprised

    l "是的老师。"

    tea_draft "你的线条很有个性。"

    show lingning casual happy

    l "谢谢老师。"

    show tea_draft angry

    with vpunch

    tea_draft "但这是工程制图。"
    tea_draft "不是抽象画。"

    show tea_draft strict

    tea_draft "重画。"

    show lingning casual depressed

    l "是。"

    show suzhi casual smile

    s "噗。"

    m "别笑。"
    m "你画得怎么样。"

    show suzhi casual normal

    s "自己看。"

    m "哇。"
    m "好直。"

    show suzhi casual smile

    s "练过。"

    m "什么时候。"

    s "暑假。"
    s "提前预习了。"

    m "厉害。"

    s "还行。"

    show suzhi casual smile

    s "比某人强。"

    show lingning casual ashamed

    l "我听见了。"
    l "这是人身攻击。"

    show suzhi casual normal

    s "我说的是事实。"

    show tea_draft strict at center with dissolve

    tea_draft "安静。"
    tea_draft "画完的举手。"

    show suzhi casual normal at right with dissolve

    s "我。"

    show tea_draft normal at center with dissolve

    tea_draft "拿过来。"
    tea_draft "嗯。"

    show tea_draft strict

    tea_draft "不错。"
    tea_draft "线条有力。"
    tea_draft "继续努力。"

    show suzhi casual smile

    s "谢谢老师。"

    show tea_draft normal

    tea_draft "下一个。"
    tea_draft "木子米。"

    m "在。"

    tea_draft "你的线呢。"

    m "画完了。"

    tea_draft "拿过来。"

    show tea_draft normal

    tea_draft "还行。"
    tea_draft "基本功不扎实。"
    tea_draft "多练。"

    m "是。"

    show lingning casual happy at left with dissolve

    l "到我了到我了。"

    show tea_draft strict at center with dissolve

    tea_draft "凌宁。"

    show lingning casual surprised

    l "在。"

    tea_draft "你这画的是线吗。"

    show lingning casual happy

    l "报告老师。"
    l "是线。"

    show tea_draft angry

    with vpunch

    tea_draft "我看像波浪。"

    show lingning casual surprised

    l "波浪也是线。"

    show tea_draft strict

    with vpunch

    tea_draft "闭嘴。"
    tea_draft "重画三遍。"

    show lingning casual depressed

    l "是。"

    show suzhi casual normal at right with dissolve

    m "同情你。"

    show lingning casual depressed

    l "友谊呢。"

    m "跟波浪一起飞走了。"

    show suzhi casual smile

    s "活该。"

    show lingning casual ashamed

    l "你们太冷酷了。"

    show tea_draft strict at center with dissolve

    tea_draft "现在教大家画平行线。"
    tea_draft "间距保持一致。"
    tea_draft "这是基本功中的基本功。"
    tea_draft "看黑板。"
    tea_draft "手腕放松。"
    tea_draft "手臂不动。"
    tea_draft "靠手腕发力。"
    tea_draft "这样画出来的线才匀称。"

    show tea_draft normal

    tea_draft "明白吗。"

    show suzhi casual normal at right with dissolve

    s "明白。"

    m "明白。"

    show lingning casual depressed at left with dissolve

    l "明白。"

    show tea_draft strict

    tea_draft "开始练。"
    tea_draft "二十分钟后检查。"

    show suzhi casual normal

    m "手腕好酸。"

    s "慢慢来。"
    s "你太用力了。"

    m "不用力画不直。"

    show suzhi casual normal:
        ease 0.5 zoom 1.1 yoffset 50

    s "方法不对。"
    s "你看我。"
    s "这样。"
    s "手腕带动笔。"
    s "不是手指。"

    show suzhi casual normal:
        ease 0.5 zoom 1.0 yoffset 0

    m "试试看。"
    m "好像好点。"

    show suzhi casual smile

    s "对吧。"

    show lingning casual depressed

    l "素织老师。"
    l "救救我。"

    show suzhi casual smile

    s "你放弃吧。"

    show lingning casual surprised

    l "不能区别对待。"

    show suzhi casual normal

    s "你基础太差。"

    show lingning casual depressed

    l "我心灵受伤了。"

    m "别演了。"
    m "赶紧练。"

    show lingning casual tired

    l "好吧。"
    l "为了不被老师骂。"

    show tea_draft strict at center with dissolve

    tea_draft "时间到。"
    tea_draft "检查。"
    tea_draft "素织。"
    tea_draft "优秀。"
    tea_draft "木子米。"
    tea_draft "有进步。"
    tea_draft "凌宁。"

    show tea_draft angry

    with vpunch

    tea_draft "你练的是波浪二代吗。"

    show lingning casual depressed

    l "老师我尽力了。"

    show tea_draft strict

    tea_draft "下课别走。"

    show lingning casual depressed

    l "是。"

    show suzhi casual smile at right with dissolve

    s "这就是报应。"

    m "太惨了。"

    show lingning casual ashamed

    l "你们还笑。"

    play sound audio.se_bell

    "下课铃响了。"

    show tea_draft normal at center with dissolve

    tea_draft "今天就到这里。"
    tea_draft "作业画一页直线。"
    tea_draft "明天交。"

    show tea_draft strict

    tea_draft "凌宁留堂。"

    show lingning casual depressed

    l "是。"

    # ==========================================
    # 【场景二：食堂 - 午饭时间】
    # ==========================================

    scene bg dining_inside with fade

    play music audio.bgm_break_time fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.3

    hide lingning with dissolve
    hide suzhi with dissolve

    m "我们在外面等你。"

    show suzhi casual normal at right with dissolve

    s "食堂见。"

    show lingning casual depressed at left with dissolve

    l "谢了。"

    hide lingning with dissolve

    show suzhi casual normal at center with moveinright

    m "那家伙真可怜。"

    s "谁让他吊儿郎当。"

    m "其实他挺聪明的。"

    show suzhi casual normal

    s "聪明不用正地方。"

    m "也是。"

    s "走吧。"
    s "先去占位。"

    m "今天吃什么。"

    s "你请客。"

    m "为什么。"

    show suzhi casual smile

    s "因为你欠我的。"

    m "欠什么。"

    s "鸡蛋。"

    m "那是你给我的。"

    s "所以你要回礼。"

    m "这逻辑。"

    show suzhi casual angry

    s "有意见？"

    m "没有。"
    m "想吃什么。"

    show suzhi casual smile

    s "红烧肉。"

    m "你又不怕胖。"

    show suzhi casual angry

    s "你才胖。"

    m "我错了。"

    show suzhi casual smile

    s "再加一个鸡腿。"

    m "行。"
    m "今天大出血。"

    s "这就是得罪我的下场。"

    m "我什么时候得罪你了。"

    show suzhi casual angry

    s "刚才。"
    s "你说我胖。"

    m "我没说。"

    s "你暗示了。"

    m "冤枉。"

    show suzhi casual smile

    s "不接受反驳。"

    m "好吧。"

    show suzhi casual normal

    m "食堂人好多。"

    s "赶紧排队。"
    s "红烧肉窗口。"

    m "我去挤。"

    s "小心点。"
    s "别洒了。"

    m "放心。"
    m "为了鸡腿。"

    show suzhi casual smile

    s "还有红烧肉。"

    m "拼了。"

    play sound audio.se_foot_stomp

    m "让一让。"
    m "谢谢。"
    m "阿姨。"
    m "两份红烧肉。"
    m "两个鸡腿。"

    show aunt happy at left with dissolve

    aunt "好嘞。"
    aunt "小伙子能吃。"

    show aunt normal

    m "不是我一个人。"

    aunt "那也够多的。"

    m "朋友胃口好。"

    show aunt happy

    aunt "给你多加一勺汁。"

    m "谢谢阿姨。"

    hide aunt with dissolve
    show suzhi casual normal at right with dissolve

    s "拿到了吗。"

    m "任务完成。"

    show suzhi casual smile

    s "不错。"
    s "奖励你一个鸡腿。"

    m "本来就是我的。"

    s "我让给你的。"

    m "行行。"
    m "你说了算。"

    show lingning casual tired at left with moveinleft

    l "我来了。"
    l "老师终于放过了我。"
    l "你们已经开始吃了。"

    show suzhi casual normal

    s "谁让你慢。"

    show lingning casual depressed

    l "我受了那么多苦。"
    l "你们不等我。"

    m "你的饭在那边。"
    m "自己打。"

    show lingning casual surprised

    l "没钱了。"
    l "行行好。"

    m "拿去。"
    m "饭卡。"

    show lingning casual happy

    l "恩人。"
    l "我要吃最贵的。"

    show suzhi casual gloomy

    s "脸皮真厚。"

    show lingning casual pose

    l "这是劫后余生的庆祝。"
    l "等我回来。"

    m "快去吧。"
    m "红烧肉快没了。"

    show lingning casual surprised

    l "我这就去。"

    hide lingning with moveoutleft

    show suzhi casual normal

    s "这家伙。"
    s "真拿他没办法。"

    m "就这个性子。"
    m "习惯就好。"

    show suzhi casual normal

    s "嗯。"
    s "吃肉。"

    m "你也多吃点。"

    show suzhi casual smile

    s "自然。"
    s "不用你说。"

    show lingning casual happy at left with moveinleft

    l "满载而归。"
    l "阿姨多给了我一个狮子头。"
    l "说我辛苦了。"

    show suzhi casual normal

    m "阿姨知道你是被留堂的。"
    m "同情你。"

    show lingning casual pose

    l "不管是同情还是欣赏。"
    l "肉是真的。"
    l "开动。"

    show suzhi casual smile

    s "慢点吃。"
    s "没人抢。"

    show lingning casual happy

    l "好吃。"
    l "这是我应得的。"
    l "上午的屈辱被治愈了。"

    m "你要求真低。"

    l "知足常乐。"
    l "吃完这顿饭。"
    l "我就忘了画线的事。"

    show suzhi casual normal

    s "明天还要画。"

    show lingning casual surprised

    l "明天的事明天说。"

    m "赞同。"

    show suzhi casual gloomy

    s "你们男生都这样。"

    m "这叫乐观。"

    s "这叫逃避。"

    show lingning casual happy

    l "都一样。"
    l "下午没课吧。"

    m "没有。"

    show lingning casual pose

    l "自由了。"

    show suzhi casual normal

    s "我要去图书馆。"

    m "又预习？"

    s "复习制图。"
    s "今天的内容要巩固。"

    show lingning casual happy

    l "太勤奋了。"
    l "不像某人。"

    m "你说谁。"

    show lingning casual happy

    l "说你。"
    l "你下午准备干什么。"

    m "回宿舍睡觉。"

    show lingning casual happy

    l "好主意。"
    l "我也睡。"

    show suzhi casual gloomy

    s "你们两个。"
    s "没救了。"

    m "劳逸结合。"

    show lingning casual pose

    l "说得对。"
    l "素织也回去休息吧。"

    show suzhi casual angry

    s "不要。"
    s "我去图书馆。"

    show suzhi casual normal

    m "那晚上我再去找你俩。"

    s "晚上有选修课。"

    m "对。"
    m "土木概论。"

    s "别迟到。"

    m "知道了。"

    show lingning casual happy

    l "我会叫他的。"

    show suzhi casual smile

    s "你更不靠谱。"

    show lingning casual surprised

    l "怎么会。"
    l "我是靠谱的代名词。"

    show suzhi casual smile

    s "信你才怪。"

    m "好了好了。"
    m "吃完了。"
    m "走吧。"

    show lingning casual pose

    l "我去买奶茶。"
    l "你们要吗。"

    show suzhi casual normal

    s "不要。"
    s "糖分太高。"

    m "我要。"
    m "草莓味。"

    show lingning casual happy

    l "老样子。"
    l "素织真的不要？"

    s "不要。"

    show lingning casual surprised

    l "可惜。"
    l "那我买两杯。"
    l "自己喝。"

    m "会胖的。"

    show lingning casual pose

    l "本少爷代谢好。"
    l "不怕。"

    s "随你。"

    show suzhi casual normal

    s "我走了。"

    hide suzhi with moveoutright

    # ==========================================
    # 【场景三：回宿舍路上 / 宿舍 - 午后】
    # ==========================================

    scene bg black with fade

    stop sound fadeout 1.0
    play music audio.bgm_campus fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.2

    hide lingning with dissolve

    show lingning casual normal at center with dissolve

    l "她还真是干脆。"

    m "她一直这样。"

    show lingning casual happy

    l "你现在很了解她嘛。"

    m "一般般。"

    show lingning casual happy

    l "骗谁呢。"
    l "看你那眼神。"

    m "什么眼神。"

    show lingning casual pose

    l "黏糊糊的眼神。"

    m "别瞎说。"

    show lingning casual happy

    l "我没瞎说。"
    l "旁观者清。"

    m "奶茶还堵不住你的嘴。"

    show lingning casual surprised

    l "堵不住。"
    l "除非你给我加珍珠。"

    m "行。"
    m "加双份。"

    show lingning casual happy

    l "成交。"
    l "暂时不说了。"

    m "走吧。"
    m "回宿舍。"

    show lingning casual pose

    l "回去打游戏。"

    m "你不是要睡觉吗。"

    show lingning casual happy

    l "先打一把。"
    l "再睡。"

    m "随你。"

    show lingning casual normal

    l "今晚叫素织一起吃饭吗。"

    m "她有选修课。"

    l "我们也有。"
    l "一起吃呗。"

    m "看情况。"

    show lingning casual happy

    l "你就是怂。"
    l "想约就约。"

    m "我没有。"

    show lingning casual happy

    l "行。"
    l "你说没有就没有。"
    l "反正我信了。"

    m "你那语气明明是怀疑。"

    show lingning casual surprised

    l "哪有。"
    l "我语气很诚恳。"

    m "算了。"
    m "走吧。"

    show lingning casual normal

    l "走。"
    l "等等。"

    show lingning casual surprised

    l "我奶茶还没拿。"

    m "你事真多。"

    show lingning casual pose

    l "人生大事。"
    l "奶茶第一。"

    m "快拿。"

    show lingning casual happy

    l "拿到了。"
    l "回窝。"

    m "终于可以休息了。"

    show lingning casual tired

    l "上午太痛苦。"
    l "手还酸呢。"

    m "我也是。"
    m "制图课好累。"

    l "严老师太严格。"
    l "不过人不错。"

    m "确实。"
    m "教得也好。"

    show lingning casual depressed

    l "只是我手不听话。"

    m "多练就好了。"

    show lingning casual normal

    l "希望如此。"
    l "不然我要挂科。"

    m "不会的。"
    m "你努力就行。"

    show lingning casual happy

    l "那你教我。"

    m "行。"
    m "教你画线。"

    show lingning casual pose

    l "恩人。"
    l "下午就教。"

    m "下午要睡觉。"

    show lingning casual surprised

    l "睡觉不重要。"

    m "很重要。"

    show lingning casual depressed

    l "好吧。"
    l "晚上再教。"

    m "晚上上课。"

    l "那就下课。"

    m "你是真的急。"

    show lingning casual pose

    l "关乎荣誉。"
    l "必须急。"

    m "知道了。"
    m "下课教你。"

    show lingning casual happy

    l "赞。"
    l "先回去了。"

    m "嗯。"
    m "素织到图书馆了吧。"

    show lingning casual happy

    l "你看。"
    l "还说不想她。"

    m "我只是自言自语。"

    show lingning casual happy

    l "恩。"
    l "自言自语。"
    l "我懂。"

    m "闭嘴。"

    show lingning casual surprised

    l "闭了。"
    l "但我在心里说。"

    m "幼稚。"

    show lingning casual happy

    l "彼此彼此。"

    stop sound fadeout 1.0

    scene bg dorm_room_clean with fade

    play music audio.bgm_warm fadein 1.0
    play sound audio.se_door_kick volume 0.5

    show lingning casual tired at center with moveinright

    m "到了。"
    m "开门。"

    show lingning casual normal

    l "你开。"

    m "你没带钥匙？"

    show lingning casual surprised

    l "好像没带。"

    m "你真是。"
    m "什么事都忘。"

    show lingning casual happy

    l "因为有你。"
    l "你是我的备用钥匙。"

    m "我不是。"

    show lingning casual pose

    l "你是。"
    l "开门吧。"

    m "唉。"
    m "开了。"

    play sound audio.se_bump

    show lingning casual tired at center, running_shake with moveinright

    l "床。"
    l "我想你了。"

    m "别发神经。"

    show lingning casual depressed

    l "是真的想。"
    l "我的被子。"
    l "我的枕头。"

    m "睡吧。"
    m "别说话了。"

    show lingning casual tired

    l "睡。"
    l "晚上见。"

    m "晚上见。"

    # 第七章 完
    scene black with fade
    stop music fadeout 2.0
    centered "{size=60}第七章 完{/size}"

    jump chapter_8


# ==========================================
# 第八章：电脑实训课的相遇
# ==========================================
label chapter_8:

    # 【场景一：教学楼走廊 - 上课前】
    scene bg classroom_clean with fade
    play music audio.bgm_school fadein 1.0
    play sound audio.se_bell

    "上课铃声响了。"

    show suzhi casual normal at center with dissolve

    m "又是新课。"
    m "电脑实训。"
    m "在图书馆四楼。"

    show lingning casual surprised at left with moveinleft

    l "图书馆有电脑室吗。"

    s "有。"
    s "电子阅览室。"

    l "我都不知道。"

    s "你只知道奶茶店。"

    show lingning casual happy

    l "还有食堂。"

    show suzhi casual gloomy

    m "别说了。"
    m "快走吧。"
    m "图书馆离这儿远。"

    show lingning casual tired

    l "又要爬坡。"
    l "我恨坡。"

    show suzhi casual smile

    s "就当锻炼。"

    show lingning casual depressed

    l "军训已经锻炼够了。"

    show suzhi casual normal

    m "走吧走吧。"

    stop music fadeout 1.0

    # 【场景二：图书馆大门】
    scene bg library with fade
    play music audio.bgm_campus fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.3

    show lingning casual pose at left with dissolve
    show suzhi casual normal at center with dissolve

    l "知识的味道。"

    s "是灰尘的味道。"

    m "是机房的味道。"

    show lingning casual happy

    l "你们真没情调。"

    show suzhi casual normal

    s "四楼。"
    s "电梯还是楼梯。"

    m "楼梯。"
    m "电梯要等很久。"

    show lingning casual surprised

    l "我选电梯。"
    l "节约体力。"

    s "那你等吧。"
    s "我们走楼梯。"

    show lingning casual tired

    l "等等我。"
    l "我还是跟你们走。"

    show suzhi casual smile

    m "善变。"

    show lingning casual pose

    l "这是策略。"

    stop sound fadeout 1.0

    # 【场景三：电子阅览室门口】
    scene bg computer_lab with fade
    play music audio.bgm_classroom fadein 1.0

    m "好大。"

    s "比想象的大。"

    show lingning casual surprised at left with dissolve

    l "电脑好多。"
    l "都是新款的。"

    show suzhi casual normal at center

    m "找位置。"

    s "坐中间吧。"
    s "能看清楚投影。"

    m "行。"

    show lingning casual happy

    l "我坐素织那边。"

    show suzhi casual gloomy

    m "为什么。"

    l "离老师近。"
    l "我要好好学。"

    show suzhi casual smile

    s "难得。"

    show lingning casual pose

    l "我是认真的。"

    # 【场景四：实训课开始 - 老师】
    show tea_cad normal at center with dissolve
    hide lingning
    hide suzhi

    tea_cad "同学们好。"
    tea_cad "我是你们的电脑实训老师。"
    tea_cad "我姓周。"
    tea_cad "这门课叫工程制图实训。"
    tea_cad "说白了就是教你们用电脑画图。"
    tea_cad "之前学的都是手绘。"
    tea_cad "现在开始学软件。"

    show tea_cad smile

    tea_cad "这门课很重要。"
    tea_cad "以后你们做设计。"
    tea_cad "全靠电脑出图。"
    tea_cad "明白吗。"

    # 众学生回应
    play sound audio.se_footsteps_crowd volume 0.2
    "众学生" "明白。"

    show tea_cad normal

    tea_cad "今天先学基础。"
    tea_cad "打开电脑。"
    tea_cad "找到桌面上这个图标。"
    tea_cad "叫CAD。"
    tea_cad "点开。"

    hide tea_cad with dissolve

    # 【场景五：学生操作CAD】
    show lingning casual tired at left with dissolve
    show suzhi casual normal at center with dissolve

    l "这个软件好大。"
    l "要加载多久。"

    s "别急。"
    s "等就行了。"

    m "打开了。"
    m "界面好复杂。"

    show tea_cad strict at right with moveinright

    tea_cad "别慌。"
    tea_cad "今天只讲基本操作。"
    tea_cad "先学画线。"
    tea_cad "看投影。"
    tea_cad "鼠标点这里。"
    tea_cad "选定直线工具。"
    tea_cad "在绘图区点一下。"
    tea_cad "拖动。"
    tea_cad "再点一下。"
    tea_cad "线就画好了。"
    tea_cad "大家试试。"

    hide tea_cad with moveoutright

    show suzhi casual smile

    m "比手绘简单。"

    s "因为有电脑辅助。"

    show lingning casual happy

    l "我画出来了。"
    l "直的。"
    l "好直。"

    show suzhi casual gloomy

    s "那是因为电脑帮你直了。"

    show lingning casual pose

    l "工具就是给人用的。"

    m "横线画好了。"
    m "竖线怎么画。"

    show tea_cad normal at right with moveinright

    tea_cad "按F8。"
    tea_cad "开启正交模式。"
    tea_cad "这时只能画水平或垂直线。"
    tea_cad "对初学者很实用。"

    hide tea_cad with moveoutright

    show suzhi casual normal

    s "试试看。"
    s "真的只能画直线。"

    show lingning casual happy

    l "这功能真好。"
    l "再也不怕歪了。"

    show tea_cad normal at right with moveinright

    tea_cad "接下来学删除。"
    tea_cad "选中线条。"
    tea_cad "按Delete键。"
    tea_cad "就删掉了。"

    hide tea_cad with moveoutright

    m "简单。"

    s "实用。"

    show lingning casual tired

    l "我多画了几条。"
    l "想删。"
    l "按了没反应。"

    show tea_cad strict at right with moveinright

    tea_cad "因为你没选中。"
    tea_cad "要先点选。"
    tea_cad "再删除。"

    hide tea_cad with moveoutright

    show lingning casual surprised

    l "哦。"
    l "选中了。"
    l "删掉了。"

    show suzhi casual gloomy

    m "你没听课。"

    show lingning casual ashamed

    l "刚才走神了。"

    show suzhi casual normal

    s "正常。"
    s "你一直这样。"

    # 【场景六：矩形工具和图层】
    show tea_cad normal at center with dissolve
    hide lingning
    hide suzhi

    tea_cad "还有矩形工具。"
    tea_cad "点这里。"
    tea_cad "输入长和宽。"
    tea_cad "就能画出标准矩形。"
    tea_cad "不用手量尺寸。"

    hide tea_cad with dissolve

    show suzhi casual smile at center with dissolve

    m "真好用。"
    m "画了个正方形。"

    s "我画了个100乘50的矩形。"

    show lingning casual tired at left with dissolve

    l "我画的不知道多大。"
    l "没看输入栏。"

    show suzhi casual gloomy

    s "你乱画。"

    show lingning casual happy

    l "艺术就是这样。"

    show tea_cad normal at right with moveinright

    tea_cad "接下来教大家用图层。"
    tea_cad "图层就是透明的纸。"
    tea_cad "不同内容放不同层。"
    tea_cad "方便管理。"
    tea_cad "也方便修改。"
    tea_cad "这是专业习惯。"
    tea_cad "必须养成。"

    hide tea_cad with moveoutright

    show suzhi casual normal

    m "有点难。"
    m "但能理解。"

    s "很实用。"
    s "我建了三个层。"

    show lingning casual happy

    l "我建了五个。"
    l "虽然不知道干什么用。"

    show suzhi casual gloomy

    s "你乱建也没用。"

    show lingning casual pose

    l "先建了再说。"

    # 【场景七：自由练习】
    show tea_cad smile at center with dissolve
    hide lingning
    hide suzhi

    tea_cad "现在自由练习。"
    tea_cad "画一下刚才学的内容。"
    tea_cad "有问题举手。"

    hide tea_cad with dissolve

    show suzhi casual normal at center with dissolve

    m "图层怎么改名。"

    s "双击名字就行。"

    m "好了。"
    m "谢谢。"

    s "举手之劳。"

    show lingning casual surprised at left with dissolve

    l "我有问题。"
    l "鼠标怎么不听话。"

    show suzhi casual smile

    s "你鼠标垫歪了。"

    show lingning casual ashamed

    l "哦。"
    l "好了。"

    show suzhi casual normal

    s "你基本功太差。"

    show lingning casual pose

    l "练习嘛。"
    l "慢慢来。"

    # 【场景八：下课】
    show tea_cad normal at center with dissolve
    hide lingning
    hide suzhi

    tea_cad "时间差不多了。"
    tea_cad "今天的内容很重要。"
    tea_cad "回去复习。"
    tea_cad "下次学画圆。"
    tea_cad "下课。"

    hide tea_cad with dissolve

    stop music fadeout 1.0

    # 【场景九：课后】
    scene bg library with fade
    play music audio.bgm_daily fadein 1.0

    show lingning casual happy at left with dissolve

    l "终于结束了。"

    show suzhi casual normal at center

    m "你去哪。"

    s "等一下。"
    s "我有点事。"

    m "什么事。"

    s "我的图没保存。"
    s "要重新弄一下。"

    show lingning casual pose

    l "那我先走了。"
    l "奶茶店有活动。"
    l "买一送一。"
    l "我要去抢。"

    show suzhi casual smile

    m "你去吧。"
    m "我等他。"

    s "不用等我。"
    s "你先走吧。"

    show suzhi casual normal

    m "我等你。"
    m "反正也没事。"

    s "随便你。"

    m "你慢慢弄。"
    m "不急。"

    s "嗯。"
    s "保存好了。"

    m "那走。"

    s "等一下。"
    s "我想借两本书。"
    s "工程制图参考书。"
    s "在五楼的专业书库。"

    hide lingning with dissolve

    m "我陪你去。"

    s "不用。"
    s "我自己就行。"

    m "我今天还没借书。"
    m "也想看看。"

    show suzhi casual gloomy

    s "你平时不看书。"

    m "今天想看了。"

    s "随你。"

    stop music fadeout 1.0

    # 【场景十：五楼专业书库】
    scene bg library_shelves with fade
    play music audio.bgm_warm fadein 1.0

    show suzhi casual normal at center with dissolve

    s "书在那边。"
    s "TU开头的。"

    m "你对图书馆很熟。"

    s "来过几次。"
    s "找书很方便。"

    m "我还没来过五楼。"

    s "这边都是建筑类。"
    s "那边是结构类。"

    m "书好多。"
    m "看得眼花。"

    s "找这本。"
    s "CAD从入门到精通。"
    s "还有这本。"
    s "工程制图规范。"

    m "我也借一本。"
    m "就借这本。"

    show suzhi casual surprised

    s "你借一样的干嘛。"

    m "一起看。"

    show suzhi casual gloomy

    s "有病。"

    m "方便讨论。"

    show suzhi casual normal

    s "那你拿好。"
    s "别弄丢了。"

    m "放心。"

    # 【场景十一：发现白墨萱】
    show layer master at soft_shake

    m "嗯？"
    m "那边有人。"

    show suzhi casual surprised

    s "哪里。"

    m "书架尽头。"
    m "好像在打瞌睡。"

    show suzhi casual gloomy

    s "谁会在书库睡觉。"

    m "不知道。"
    m "去看看。"

    s "别多事。"

    m "万一是晕倒了。"

    show suzhi casual normal

    s "好吧。"
    m "走过去看看。"

    stop music fadeout 1.0
    hide suzhi with dissolve
    show layer master

    # 【场景十二：白墨萱登场】
    play music audio.bgm_awkward fadein 1.0

    show baimoxuan coat crazy at center with dissolve

    pause 0.5

    b "呼……"
    b "混凝土的配比。"
    b "水灰比0.35。"
    b "减水剂掺量0.8%。"
    b "坍落度……"
    b "坍落度要算……"

    show suzhi casual surprised at right with moveinright

    s "白墨萱？"
    s "你怎么在这儿睡。"

    b "嗯。"
    b "有人在呼唤我的名讳。"
    b "是正宫的气场。"
    b "还有巨人族的脚步。"

    show suzhi casual gloomy

    m "你在这睡了多久。"

    b "多久。"
    b "让我确认一下时间线。"
    b "下午一点进来。"
    b "现在是。"
    b "根据窗外光照强度推算。"
    b "大约四点。"
    b "三个小时。"
    b "不算久。"

    show suzhi casual angry

    s "你在这睡了三个小时？"

    b "不是睡。"
    b "是深度思考。"
    b "我在推算一个公式。"

    m "什么公式。"

    b "高层建筑风荷载的临界值。"
    b "算到一半。"
    b "内存不足。"
    b "就进入了低功耗模式。"

    show suzhi casual normal

    s "低功耗模式。"
    s "说人话就是睡着了。"

    b "不准确。"
    b "是战略性休息。"

    m "你吃饭了吗。"

    b "饭。"
    b "上次摄入营养物质。"
    b "是昨晚的泡面。"
    b "还有今天早上的薄荷糖。"

    show suzhi casual surprised

    s "你一天没吃饭？"

    b "进食会占用思考时间。"
    b "效率优先。"

    show suzhi casual angry

    m "不行。"
    m "你得吃东西。"
    m "现在就去。"

    b "现在食堂没开。"

    m "小卖部有面包。"

    b "面包。"
    b "碳水化合物加防腐剂。"
    b "营养价值低。"

    show suzhi casual gloomy

    s "总比饿死强。"

    b "说得对。"
    b "生存优先。"
    b "但在去之前。"
    b "我需要借这摞书。"

    m "这摞书。"
    m "这也太多了。"
    m "十几本。"
    m "你能拿得动吗。"

    b "理论上能。"
    b "前提是我今天吃过饭。"
    b "现在不行。"
    b "缺乏ATP。"

    show suzhi casual normal

    s "我们帮你拿。"
    s "但你得先去吃东西。"

    b "协议达成。"
    b "这是双赢。"

    m "你借这么多书干嘛。"

    b "研究。"
    b "我的魔塔需要理论支撑。"

    show suzhi casual surprised

    s "魔塔？"

    b "就是那个。"
    b "我说过的。"
    b "巴比伦塔。"
    b "以现代高层建筑结构的形式。"
    b "重现于世。"

    show suzhi casual normal

    s "你还真是执着。"

    b "这是我的课题。"
    b "我的生存意义。"

    m "但是这些书。"
    m "有些是大三才学的。"

    b "知识不分年级。"
    b "大一能学懂的。"
    b "就不要等大三。"
    b "时间有限。"
    b "人类寿命太短。"

    show suzhi casual smile

    s "你这想法。"
    s "有点道理。"
    s "但身体更重要。"

    b "身体是容器。"
    b "知识是内容。"
    b "容器要维护。"
    b "但不能本末倒置。"

    show suzhi casual gloomy

    m "说不过你。"
    m "书给我一半。"

    b "谢谢。"
    b "巨人族的力量派上用场了。"

    show suzhi casual angry

    m "别叫我巨人。"

    b "好的巨人。"

    show suzhi casual gloomy

    s "她根本不想改。"

    b "这是客观描述。"
    b "你身高超过平均值两个标准差。"
    b "符合巨人定义。"

    m "随你吧。"

    show suzhi casual normal

    s "走吧。"
    s "先去自助借书机。"

    stop music fadeout 1.0

    # 【场景十三：自助借书机】
    scene bg library_counter with fade
    play music audio.bgm_daily_warm fadein 1.0

    show baimoxuan coat crazy at center with dissolve

    b "滴。"
    b "滴。"
    b "滴。"
    b "十二本。"
    b "借阅成功。"

    show suzhi casual surprised at right with dissolve

    m "借书证一次只能借十本。"
    m "你怎么借了十二本。"

    b "我有两张证。"
    b "一张是我的。"
    b "一张是室友的。"
    b "她借给我用的。"

    show suzhi casual normal

    s "你室友不管你吗。"

    b "她管不了。"
    b "她说我是异次元生物。"
    b "放弃了干预。"
    b "选择观察。"

    m "心态真好。"

    b "是的。"
    b "她叫赵晴晴。"
    b "是个好人。"
    b "经常帮我打饭。"

    show suzhi casual smile

    s "难怪你能活到现在。"

    b "人类的延续依赖社会合作。"
    b "这是演化优势。"

    show suzhi casual normal

    m "好了。"
    m "现在去小卖部。"

    stop music fadeout 1.0

    # 【场景十四：小卖部】
    scene bg shop with fade
    play music audio.bgm_break_time fadein 1.0

    show baimoxuan coat crazy at center with dissolve

    b "这个。"
    b "全麦面包。"
    b "还有纯牛奶。"
    b "蛋白质加碳水。"
    b "营养均衡。"

    show suzhi casual normal at right with dissolve

    m "你不买点零食吗。"

    b "零食。"
    b "反式脂肪酸。"
    b "添加剂。"
    b "不合算的营养来源。"

    show suzhi casual gloomy

    s "你连吃东西都算。"

    b "当然。"
    b "身体是研究工具。"
    b "工具需要定期保养。"
    b "输入合格燃料。"

    m "你活得好累。"

    b "不累。"
    b "这是我的常态。"

    show suzhi casual smile

    s "快吃吧。"
    s "吃完回去休息。"

    b "不能休息。"
    b "晚上还要做实验。"

    m "什么实验。"

    b "结构模型加载实验。"
    b "在土木实验楼。"
    b "晚上七点开始。"

    show suzhi casual surprised

    s "你才大一。"
    s "怎么做实验。"

    b "我申请了课外创新项目。"
    b "指导老师特批的。"

    m "你太厉害了。"

    b "不厉害。"
    b "只是愿意花时间。"
    b "面包吃完了。"
    b "牛奶喝完了。"
    b "感谢你们的能源补给。"
    b "我要去实验室了。"

    show suzhi casual normal

    s "等一下。"
    s "这摞书。"
    s "我们帮你送过去吧。"

    b "不用。"
    b "实验室不远。"
    b "我的能量值恢复到正常水平的百分之七十二。"
    b "足以搬运这些文献。"

    m "真的不用？"

    b "真的。"
    b "你们已经提供了足够的帮助。"
    b "作为回报。"
    b "这个给你们。"

    # 白墨萱递出便签
    play sound audio.se_book_drop

    b "我从口袋里掏出一张便签。"

    m "这是什么。"

    b "我整理的学习笔记。"
    b "关于CAD的常用快捷键。"
    b "刚才在书库里。"
    b "听到你们在讨论实训课。"
    b "这个应该对你们有帮助。"

    show suzhi casual surprised

    s "你刚才不是在睡觉吗。"

    b "低功耗模式。"
    b "听觉依然在线。"
    b "这是人类演化的本能。"
    b "用来防范危险。"

    m "谢谢。"

    s "谢谢。"

    b "不客气。"
    b "再见。"
    b "巨人。"
    b "还有正宫。"

    show suzhi casual angry

    s "别叫那个。"
    s "听到了吗。"

    b "听到了。"
    b "但保留称呼权。"
    b "这是观察者命名体系的一部分。"

    show suzhi casual gloomy

    s "你。"
    s "算了。"
    s "跟她说理说不通。"

    hide baimoxuan with moveoutright

    m "她走了。"
    m "真快。"

    show suzhi casual normal

    s "这个人。"
    s "越想越神奇。"

    m "其实她人不错。"

    s "我知道。"
    s "只是太奇怪了。"

    m "奇怪的善良。"
    m "你看这个笔记。"
    m "写得好详细。"
    m "每个快捷键都有注释。"

    show suzhi casual smile

    s "她确实很用心。"
    s "就是表达方式独特。"

    m "也许天才都这样。"

    show suzhi casual normal

    s "你把她当天才。"

    m "难道不是吗。"
    m "大一就能做创新项目。"
    m "能借大三大四的书看。"

    s "也是。"
    s "她确实不一样。"

    m "走吧。"
    m "书也借了。"
    m "饭也催她吃了。"
    m "任务完成。"

    s "嗯。"

    stop music fadeout 1.0

    # 【场景十五：凌宁来电】
    scene bg library with fade
    play music audio.bgm_daily fadein 1.0

    show suzhi casual normal at center with dissolve

    s "等等。"
    s "我手机响了。"
    s "是凌宁。"

    m "他干嘛。"

    s "接一下。"

    play sound audio.se_phone

    # 手机通话场景
    show lingning casual happy at left with dissolve

    l "喂。"
    l "素织。"
    l "那个奶茶活动太火爆了。"
    l "排队排了四十分钟。"
    l "你们还在图书馆吗。"

    s "在。"
    s "正要走。"

    l "那我去找你们。"
    l "我买了三杯。"
    l "草莓味给木子米。"
    l "红豆味给素织。"
    l "珍珠奶茶我自己。"

    show suzhi casual surprised

    s "你不是没钱了吗。"

    l "刚充了饭卡。"
    l "还发现了零钱。"
    l "藏在旧衣服口袋里。"
    l "贵族的好运。"

    show suzhi casual normal

    s "行。"
    s "我们在图书馆门口等你。"

    l "马上到。"

    s "挂了。"

    hide lingning with dissolve

    m "凌宁要来？"

    s "嗯。"
    s "买了奶茶。"
    s "有你喜欢的草莓味。"

    m "他还记得。"

    show suzhi casual smile

    s "那家伙记吃的最清楚。"

    m "也有你的。"

    s "红豆的。"
    s "其实我喜欢原味。"

    m "那你怎么不说。"

    show suzhi casual normal

    s "他好心买的。"
    s "说了浪费。"
    s "红豆也不难喝。"

    m "下次我帮你告诉他。"

    show suzhi casual gloomy

    s "不用。"
    s "小事而已。"

    # 【场景十六：凌宁到达】
    show lingning casual tired at left with moveinleft

    l "我来了。"
    l "累死了。"
    l "爬坡又爬楼梯。"
    l "奶茶差点洒了。"
    l "接住。"
    l "一人一杯。"

    m "谢谢。"

    s "谢谢。"

    show lingning casual happy

    l "不客气。"
    l "你们在图书馆这么久。"
    l "是不是又遇到谁了。"

    m "你猜。"

    show lingning casual surprised

    l "白墨萱。"
    l "对不对。"

    show suzhi casual surprised

    s "你怎么知道。"

    l "图书馆是她的领地。"
    l "上次就见她在这儿。"
    l "再加上你们这表情。"
    l "我就猜到了。"

    m "她在这儿睡了三个小时。"

    show lingning casual surprised

    l "睡？"
    l "在书库睡觉？"
    l "果然是她。"

    show suzhi casual normal

    s "她还一天没吃饭。"

    show lingning casual ashamed

    l "太不会照顾自己了。"
    l "下次遇到。"
    l "我请她吃饭。"
    l "贵族不能让女士饿着。"

    m "她会跟你讲营养学。"

    show lingning casual pose

    l "那我就跟她探讨。"
    l "说不定能学到东西。"

    show suzhi casual gloomy

    s "你想学？"

    show lingning casual happy

    l "不想。"
    l "但聊聊天总行。"
    l "她的世界观很有趣。"

    m "那确实。"

    m "走吧。"
    m "吸管插好。"
    m "边走边喝。"

    show lingning casual tired

    l "晚上还有课。"
    l "土木概论。"

    show suzhi casual normal

    s "我记得。"
    s "在阶梯教室。"

    m "现在还早。"
    m "先回宿舍吧。"

    show lingning casual happy

    l "好主意。"
    l "我要补个觉。"
    l "奶茶的咖啡因对我没用。"

    show suzhi casual gloomy

    s "你就是想睡。"

    show lingning casual pose

    l "诚实面对欲望。"
    l "这是贵族的品格。"

    show suzhi casual angry

    s "什么乱七八糟的。"

    m "素织呢。"
    m "也回宿舍吗。"

    show suzhi casual normal

    s "嗯。"
    s "回去放下书。"
    s "衣服也要换一件。"

    m "怎么了。"

    s "搬书搬的。"
    s "袖子有点灰。"

    m "都怪我让你帮忙。"

    show suzhi casual smile

    s "我自己要帮的。"
    s "不怪你。"

    show lingning casual happy

    l "你们互帮互助。"
    l "真是感人。"
    l "怎么没人帮我。"

    show suzhi casual normal

    s "你帮我们也行。"

    l "我帮了。"
    l "我买了奶茶。"
    l "这就是帮助。"

    m "算。"
    m "当然算。"

    show lingning casual pose

    l "那就对了。"
    l "扯平。"

    show suzhi casual gloomy

    s "别扯了。"
    s "快走吧。"

    show lingning casual happy

    l "走走走。"
    l "奶茶真好喝。"
    l "珍珠弹牙。"

    m "我的草莓味也不错。"

    show suzhi casual normal

    s "还行。"
    s "甜了点。"

    show lingning casual pose

    l "这就是青春的味道。"

    m "你又来了。"

    l "我说的是事实。"

    stop music fadeout 1.0

    # 【场景十七：路上聊天】
    scene bg campus_road_blur with fade
    play music audio.bgm_campus fadein 1.0

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    l "对了。"
    l "白墨萱说要研究什么来着。"

    s "高层建筑风荷载。"

    show lingning casual surprised

    l "完全不懂。"

    m "我也不懂。"

    show suzhi casual normal

    s "以后会学到的。"

    l "她还说要建巴比伦塔。"

    s "那是比喻。"

    show lingning casual pose

    l "有梦想是好事。"
    l "虽然听起来太远。"

    m "她说的时候眼神很亮。"
    m "不是那种说大话的感觉。"

    show suzhi casual smile

    s "确实。"
    s "她大概真的能做到。"

    show lingning casual happy

    l "那我要提前交好关系。"
    l "万一以后她真的建出什么。"
    l "我可以去参观。"

    show suzhi casual gloomy

    m "目的不纯。"

    show lingning casual pose

    l "实用主义。"
    l "这也是贵族品格。"

    show suzhi casual angry

    s "你什么都能说成品格。"

    show lingning casual happy

    l "当然。"
    l "只要我愿意。"

    # 【场景十八：回到宿舍区】
    scene bg dorm_room_clean with fade
    stop music fadeout 1.0

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    m "到了。"
    m "各自回窝吧。"

    s "晚上教室见。"

    l "记得叫我们。"

    show suzhi casual gloomy

    s "是你叫我。"

    show lingning casual surprised

    l "好吧。"
    l "我叫你。"
    l "木子米我叫他。"

    m "定好闹钟。"
    m "上次差点迟到。"

    show lingning casual pose

    l "有我呢。"

    m "就是你最不靠谱。"

    show lingning casual happy

    l "这次保证。"

    show suzhi casual normal

    s "信你最后一次。"

    show lingning casual pose

    l "荣誉担保。"

    m "行。"
    m "晚上见。"

    s "晚上见。"

    stop music fadeout 2.0

    # 第八章 完
    scene black with fade
    centered "{size=60}第八章 完{/size}"

    return


label chapter_9:

    # 【场景一：宿舍傍晚】
    scene bg dorm_boys_night with fade
    play music audio.bgm_daily fadein 1.0

    "傍晚。"
    "宿舍里的灯还没完全亮起来。"
    "窗外的天色已经沉了下去。"

    m "几点了。"
    m "六点二十。"
    m "土木概论七点上课。"
    m "还来得及。"

    play sound audio.se_phone

    "手机震了一下。"

    s_phone "醒了吗。"
    s_phone "别迟到。"

    m_phone "醒着。"
    m_phone "我看起来像会迟到的人吗。"

    s_phone "像。"

    m_phone "你说话真直接。"

    s_phone "事实。"
    s_phone "凌宁也没回我消息。"
    s_phone "你去叫他。"

    m_phone "收到。"

    nvl clear

    m "凌宁。"
    m "起床。"
    m "上课了。"

    show lingning casual tired at center with dissolve

    l "再五分钟。"
    l "贵族需要充足睡眠。"

    m "你下午已经睡了一个小时。"

    show lingning casual depressed

    l "那是预热。"
    l "真正的睡眠还没开始。"

    m "土木概论也要开始了。"

    show lingning casual surprised

    l "什么。"
    l "已经这个点了？"

    m "六点二十。"

    show lingning casual tired

    l "完了。"
    l "我的灵魂还在午睡。"

    m "把灵魂带上。"
    m "走。"

    stop music fadeout 1.0

    # 【场景二：宿舍楼下】
    scene bg dorm_room_clean with fade
    play music audio.bgm_campus fadein 1.0

    show suzhi casual normal at center with dissolve

    s "你们终于下来了。"

    show lingning casual tired at left with moveinleft

    l "不是终于。"
    l "是准时。"

    show suzhi casual gloomy

    s "距离迟到只差十分钟。"

    m "十分钟也是时间。"

    show suzhi casual angry

    s "你们两个还挺骄傲。"

    show lingning casual pose

    l "压力越大。"
    l "越能体现贵族从容。"

    show suzhi casual normal

    s "从容地迟到？"

    l "那叫优雅地抵达。"

    m "别优雅了。"
    m "快走。"

    stop music fadeout 1.0

    # 【场景三：通往教学楼的路】
    scene cg campus_road_blur with fade
    play music audio.bgm_school fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.3

    show lingning casual tired at left with dissolve
    show suzhi casual normal at center with dissolve

    l "晚上上课。"
    l "很不人道。"

    s "大学课表就是这样。"

    m "土木概论。"
    m "听名字应该不难。"

    show suzhi casual gloomy

    s "你最好别这么想。"

    m "为什么。"

    s "越是概论。"
    s "越容易什么都讲一点。"
    s "然后什么都考一点。"

    show lingning casual surprised

    l "这不是概论。"
    l "这是总攻。"

    m "别吓我。"

    show suzhi casual normal

    s "也不一定。"
    s "先听听看。"

    play sound audio.se_phone

    "手机又震了一下。"

    m "白墨萱发消息了。"

    s "她有你微信？"

    m "下午帮她搬书的时候加的。"
    m "她说。"
    m "土木概论教室在哪里。"

    show suzhi casual surprised

    s "她也上这节？"

    l "命运的齿轮开始转动。"

    show suzhi casual gloomy

    s "你少来。"

    m_phone "阶梯教室。"
    m_phone "三教二楼。"
    m_phone "跟人流走。"

    b "收到。"
    b "如果我迷路。"
    b "说明人流的导向性不足。"

    nvl clear

    m "她说得好正式。"

    s "她一直这样。"

    stop sound fadeout 1.0

    # 【场景四：阶梯教室】
    scene bg classroom_full with fade
    play music audio.bgm_classroom fadein 1.0
    play sound audio.se_bell

    "上课铃响前。"
    "阶梯教室里已经坐了不少人。"

    show suzhi casual normal at center with dissolve
    show lingning casual happy at left with dissolve

    l "这里视野不错。"
    l "像小型议会厅。"

    s "你能不能正常一点。"

    m "坐中间吧。"
    m "别太靠后。"

    show lingning casual depressed

    l "靠后比较安全。"

    s "安全什么。"

    l "老师点不到。"

    show suzhi casual angry

    s "这就是你所谓的贵族品格？"

    show lingning casual pose

    l "战略纵深。"

    m "行了。"
    m "就这排。"

    hide lingning with dissolve
    hide suzhi with dissolve

    "教室前门被推开。"

    show baimoxuan coat crazy at center with moveinright

    b "坐标确认。"
    b "三教二楼阶梯教室。"
    b "人类聚集密度较高。"
    b "空气质量一般。"

    show suzhi casual surprised at right with dissolve

    s "你真的来了。"

    b "当然。"
    b "土木概论。"
    b "是所有土木人的共同起源。"
    b "我不能缺席。"

    m "你实验不做了？"

    b "延期了。"
    b "加载仪器被老师借走。"
    b "命运给了我听课的机会。"

    show lingning casual happy at left with dissolve

    l "欢迎加入我们的学习小组。"

    b "学习小组？"
    b "人员构成。"
    b "正宫。"
    b "巨人。"
    b "自称贵族。"
    b "很有研究价值。"

    show suzhi casual angry

    s "别乱起代号。"

    b "好的。"
    b "素织。"

    m "为什么只有我还是巨人。"

    b "因为客观事实不会因为抗议而改变。"

    show lingning casual pose

    l "我对自称贵族这个分类没有意见。"

    show suzhi casual gloomy

    s "你还挺满意。"

    stop music fadeout 1.0

    # 【场景五：土木概论课开始】
    play music audio.bgm_school fadein 1.0

    "老师走上讲台。"

    show suzhi casual normal at right
    show lingning casual tired at left
    show baimoxuan coat crazy at center

    unknown "同学们晚上好。"
    unknown "我是你们土木概论课的老师。"
    unknown "这门课不讲太深。"
    unknown "但会让你们知道。"
    unknown "土木工程到底是在做什么。"

    m "听起来挺正经。"

    s "安静。"

    unknown "很多人以为土木就是搬砖。"
    unknown "也有人以为土木就是画图。"
    unknown "都不准确。"
    unknown "土木工程。"
    unknown "是把人的生活空间。"
    unknown "变成真实结构的学科。"

    show baimoxuan coat crazy:
        ease 0.3 zoom 1.05

    b "漂亮。"

    show baimoxuan coat crazy:
        ease 0.3 zoom 1.0

    show suzhi casual surprised

    s "你小声点。"

    b "这句话可以写进序章。"

    l "什么序章。"

    b "我的塔。"
    b "需要一个序章。"

    m "你连建筑物都有剧情？"

    b "伟大的建筑都需要叙事。"

    unknown "今天先讲三个问题。"
    unknown "第一。"
    unknown "建筑为什么不会倒。"
    unknown "第二。"
    unknown "桥为什么能跨过河。"
    unknown "第三。"
    unknown "工程师为什么不能只靠想象。"

    show lingning casual surprised

    l "第三个问题在针对我。"

    show suzhi casual gloomy

    s "你还有自知之明。"

    # 【场景六：老师提问】
    unknown "我问一个简单问题。"
    unknown "如果让你们设计一座高楼。"
    unknown "最先考虑什么。"

    "教室安静了一瞬。"

    m "最先考虑。"
    m "地基？"

    s "荷载。"

    l "外观。"

    show suzhi casual gloomy

    s "你果然。"

    b "风。"

    unknown "后排那位同学。"
    unknown "你说风。"
    unknown "为什么。"

    show baimoxuan coat crazy:
        ease 0.2 zoom 1.08

    b "高度增加后。"
    b "水平风荷载对结构侧移影响显著。"
    b "如果只考虑竖向承重。"
    b "会低估整体稳定问题。"
    b "尤其是高宽比较大的建筑。"
    b "风致振动会影响舒适度。"
    b "甚至影响安全储备。"

    show baimoxuan coat crazy:
        ease 0.2 zoom 1.0

    "教室里安静了。"

    show lingning casual surprised

    l "她真的会。"

    show suzhi casual normal

    s "她不是在开玩笑。"

    unknown "说得不错。"
    unknown "虽然有些内容超纲。"
    unknown "但方向是对的。"
    unknown "高层建筑不能只看它站不站得住。"
    unknown "还要看它晃不晃。"
    unknown "人能不能接受。"

    m "原来楼也会晃。"

    s "会。"
    s "只是幅度很小。"

    l "那住高楼的人。"
    l "岂不是每天都在坐船。"

    show suzhi casual gloomy

    s "你这个比喻。"
    s "怪怪的。"

    b "某种程度上。"
    b "也可以这样理解。"

    show lingning casual happy

    l "看。"
    l "学术认证。"

    # 【场景七：课堂小作业】
    unknown "下课前。"
    unknown "给大家布置一个小作业。"
    unknown "不用交很多字。"
    unknown "画一张你理解中的土木工程。"
    unknown "可以是桥。"
    unknown "可以是楼。"
    unknown "也可以是道路。"
    unknown "下周带来。"
    unknown "我会抽几份展示。"

    show lingning casual depressed

    l "画画？"
    l "这不是我的强项吗。"

    show suzhi casual normal

    s "你刚才不是很自信吗。"

    l "我自信。"
    l "但我画出来的东西。"
    l "老师不一定看得懂。"

    m "那就是抽象派。"

    show lingning casual pose

    l "土木抽象主义。"

    show suzhi casual angry

    s "别发明新流派。"

    b "我可以画塔。"

    m "巴比伦塔？"

    b "不。"
    b "概念验证版。"
    b "比例一比一千。"
    b "平面。"
    b "立面。"
    b "剖面。"
    b "加结构体系说明。"

    show suzhi casual surprised

    s "老师说不用很多字。"

    b "我可以少写。"
    b "只写三页。"

    m "这叫少？"

    b "对我的计划来说。"
    b "是摘要。"

    play sound audio.se_bell

    unknown "今天就到这里。"
    unknown "下课。"

    stop music fadeout 1.0

    # 【场景八：下课后】
    scene bg classroom_clean with fade
    play music audio.bgm_daily_warm fadein 1.0

    show suzhi casual normal at center with dissolve
    show lingning casual tired at left with dissolve
    show baimoxuan coat crazy at right with dissolve

    l "我饿了。"
    l "我的大脑已经被概论抽干。"

    s "你明明睡了一半。"

    show lingning casual surprised

    l "我那叫闭目理解。"

    m "你闭目理解的时候。"
    m "还点了两次头。"

    show lingning casual pose

    l "说明我认可老师。"

    show suzhi casual gloomy

    s "你那是快睡着了。"

    b "睡眠有助于记忆整合。"
    b "但课堂睡眠效率不高。"
    b "建议回宿舍睡。"

    l "白墨萱。"
    l "你说话有时候很温柔。"

    b "这是生物学建议。"
    b "不包含感情色彩。"

    show lingning casual depressed

    l "更伤人了。"

    m "去小卖部吗。"
    m "食堂估计没什么了。"

    s "可以买点面包。"

    b "我不去了。"
    b "我要去图书馆还一本书。"

    show suzhi casual surprised

    s "你下午刚借。"
    s "现在就还？"

    b "借错了。"
    b "那本是道路工程。"
    b "我现在需要结构动力学。"

    m "跨度太大了吧。"

    b "知识之间没有墙。"
    b "只有门。"

    show lingning casual happy

    l "这句好。"
    l "像校训。"

    s "校训不是这个。"

    b "可以当我的个人校训。"

    # 【场景九：夜晚图书馆门口】
    scene bg library with fade
    play music audio.bgm_night fadein 1.0
    play sound audio.se_crickets volume 0.4

    show baimoxuan coat crazy at right with dissolve
    show suzhi casual normal at center with dissolve
    show lingning casual tired at left with dissolve

    l "为什么我们也跟来了。"

    m "因为你说顺路买吃的。"

    l "买吃的在小卖部。"
    l "图书馆没有吃的。"

    s "那你现在可以去。"

    show lingning casual ashamed

    l "一个人去没意思。"

    b "群体行动可以降低夜间移动风险。"
    b "你的选择合理。"

    show lingning casual happy

    l "你看。"
    l "她懂我。"

    show suzhi casual gloomy

    s "她只是给你的懒找理论依据。"

    b "准确。"

    l "不要准确。"

    stop sound fadeout 1.0

    # 【场景十：图书馆大厅】
    scene bg library_counter with fade
    play music audio.bgm_warm fadein 1.0

    show baimoxuan coat crazy at center with dissolve

    b "还书。"
    b "借书。"
    b "流程闭环。"

    play sound audio.se_bell

    "自助借还机发出提示音。"

    show suzhi casual normal at right with dissolve

    s "这次借几本。"

    b "三本。"
    b "我控制了。"

    m "你管三本叫控制。"

    b "和十二本相比。"
    b "降幅百分之七十五。"

    show lingning casual pose at left with dissolve

    l "数据很有说服力。"

    show suzhi casual gloomy

    s "你别帮她。"

    b "另外。"
    b "我想邀请你们参与我的小项目。"

    m "什么项目。"

    b "下周概论作业。"
    b "我想做一个四人合作版。"
    b "主题是。"
    b "我们理解中的校园土木。"

    show suzhi casual surprised

    s "老师不是说个人作业吗。"

    b "可以个人提交。"
    b "但素材可以共同采集。"
    b "每个人画自己的理解。"
    b "最后拼成一个系列。"

    l "听起来很有仪式感。"

    m "具体怎么做。"

    b "明天傍晚。"
    b "在校园里走一圈。"
    b "看路。"
    b "看桥。"
    b "看楼。"
    b "看排水沟。"

    show lingning casual surprised

    l "排水沟也算？"

    s "当然算。"
    s "市政工程。"

    b "素织理解正确。"
    b "奖励一枚概念徽章。"

    show suzhi casual gloomy

    s "不要奇怪的奖励。"

    m "我觉得可以。"
    m "反正作业也要做。"

    show lingning casual tired

    l "明天傍晚。"
    l "那我晚饭怎么办。"

    s "走完再吃。"

    l "太残忍了。"

    b "可以携带能量补给。"
    b "面包。"
    b "牛奶。"
    b "巧克力。"

    show lingning casual happy

    l "我批准这个项目。"

    show suzhi casual angry

    s "你批准有什么用。"

    l "增加士气。"

    # 【场景十一：素织的小提醒】
    scene bg rest_area_sunset with fade
    play music audio.bgm_warm_guitar fadein 1.0

    show suzhi casual normal at center with dissolve

    "从图书馆出来后。"
    "凌宁跑去小卖部买夜宵。"
    "白墨萱抱着书。"
    "先一步回了宿舍。"

    m "明天你真的要去吗。"

    s "去。"
    s "作业总得做。"

    m "我还以为你会嫌麻烦。"

    show suzhi casual gloomy

    s "我是嫌麻烦。"
    s "但白墨萱说得也没错。"
    s "多看看。"
    s "总比坐在宿舍瞎画好。"

    m "你对她印象变好了？"

    show suzhi casual normal

    s "她很奇怪。"
    s "但不是坏人。"
    s "而且她认真。"

    m "你也很认真。"

    show suzhi casual surprised

    s "我？"

    m "嗯。"
    m "下午借书也是。"
    m "刚才听课也是。"
    m "你都很认真。"

    show suzhi casual shy

    s "只是正常上课。"
    s "别乱夸。"

    m "我说实话。"

    show suzhi casual gloomy

    s "那也别说得这么突然。"

    m "哦。"

    pause 0.5

    s "不过。"
    s "谢谢。"

    m "不用谢。"

    show suzhi casual normal

    s "明天记得带笔。"
    s "还有速写本。"

    m "我没有速写本。"

    show suzhi casual gloomy

    s "那就买。"

    m "知道了。"

    s "还有。"
    s "别只顾着看热闹。"
    s "真要画。"

    m "我会画的。"

    show suzhi casual smile

    s "最好是。"

    stop music fadeout 1.0

    # 【场景十二：凌宁归来】
    scene bg shop with fade
    play music audio.bgm_break_time fadein 1.0

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    l "我回来了。"
    l "战利品丰富。"
    l "烤肠。"
    l "饭团。"
    l "还有酸奶。"

    m "你买这么多。"

    show lingning casual pose

    l "为明天的项目提前储备。"

    s "你明天就吃完了。"

    l "那就明天再买。"
    l "储备是动态的。"

    show suzhi casual gloomy

    s "你只是想吃。"

    l "不要拆穿贵族的后勤体系。"

    m "给我一个饭团。"

    l "十块。"

    m "小卖部卖六块。"

    l "包含跑腿费。"

    show suzhi casual angry

    s "他就在你旁边。"
    s "你跑什么腿。"

    l "精神跑腿。"

    m "算了。"
    m "我自己买。"

    show lingning casual depressed

    l "别啊。"
    l "八块。"

    s "六块。"

    l "成交。"

    show lingning casual happy

    l "素织砍价好厉害。"

    s "不是砍价。"
    s "是纠正。"

    # 【场景十三：回宿舍路上】
    scene bg playground_night with fade
    play music audio.bgm_night fadein 1.0
    play sound audio.se_crickets volume 0.4

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    l "明天校园采集。"
    l "听起来像社团活动。"

    m "我们没有社团。"

    l "那就叫临时土木观察社。"

    s "不要随便成立社团。"

    l "社长我来当。"

    m "你先把作业画完再说。"

    show lingning casual pose

    l "社长负责方向。"
    l "细节交给成员。"

    show suzhi casual gloomy

    s "那你什么都不干。"

    l "我负责精神建设。"

    m "白墨萱负责理论。"
    m "素织负责认真。"
    m "你负责精神建设。"
    m "那我负责什么。"

    show lingning casual surprised

    l "负责长得高。"

    show suzhi casual smile

    s "负责搬东西。"

    m "怎么又回到巨人了。"

    show lingning casual happy

    l "团队定位清晰。"
    l "这是好事。"

    s "你别笑太大声。"
    s "晚上操场有人。"

    l "好。"
    l "低调。"

    pause 0.5

    play sound audio.se_phone

    "手机屏幕亮起。"

    b "临时土木观察社。"
    b "名称不错。"
    b "我已记录。"

    m "她怎么知道。"

    show suzhi casual surprised

    s "群消息。"
    s "凌宁刚才发群里了。"

    show lingning casual ashamed

    l "手滑。"

    m "你把社名发出去了？"

    l "还有成员分工。"

    show suzhi casual angry

    s "你发了什么。"

    l "理论担当白墨萱。"
    l "纪律担当素织。"
    l "搬运担当木子米。"
    l "灵魂担当凌宁。"

    m "搬运担当。"

    show suzhi casual gloomy

    s "还挺准确。"

    m "别认可啊。"

    b "补充。"
    b "巨人担当更准确。"

    m "她还补刀。"

    show lingning casual happy

    l "今晚的群聊很有活力。"

    s "把手机收起来。"
    s "走路看路。"

    m "嗯。"

    stop sound fadeout 1.0
    stop music fadeout 1.0

    # 【场景十四：夜色收束】
    scene bg dorm_boys_night with fade
    play music audio.bgm_warm fadein 1.0

    "回到宿舍。"
    "桌上的CAD教材还摊着。"
    "下午借来的书压在一边。"
    "书页边缘带着图书馆淡淡的灰尘味。"

    m "土木观察社。"
    m "听起来还真像那么回事。"

    play sound audio.se_phone

    "手机屏幕上。"
    "群聊又跳出一条消息。"

    s_phone "明天傍晚五点半。"
    s_phone "宿舍楼下集合。"
    s_phone "别迟到。"

    b "收到。"
    b "我会携带测距工具。"

    l "我会携带能量补给。"

    m_phone "我携带自己。"

    s_phone "你携带速写本。"

    m_phone "知道了。"

    nvl clear

    m "速写本。"
    m "测距工具。"
    m "能量补给。"
    m "还有一个奇怪的临时社团。"

    "我把手机扣在桌面上。"
    "窗外的操场灯还亮着。"
    "远处偶尔传来笑声。"
    "大学生活好像就是这样。"
    "一节课。"
    "一次偶遇。"
    "一句玩笑。"
    "就能把明天变成新的事件。"

    m "那就看看吧。"
    m "我们理解中的土木工程。"
    m "到底会画成什么样。"

    stop music fadeout 2.0

    # 第九章 完
    scene black with fade
    centered "{size=60}第九章 完{/size}"

    return
# ==========================================
# 第十章新增：社团百团大战 / 临时占位素材
# ==========================================
# 角色新增
# 小北：动漫社社员，cos装登场。后续可以替换正式立绘。
define kb = Character("小北", color="#ba68c8")
define club_senior = Character("社团学长", color="#ffb74d")
define club_sister = Character("社团学姐", color="#f06292")
define anime_senior = Character("动漫社学姐", color="#ce93d8")

# 临时占位立绘：先保证脚本能跑，正式素材到位后把 Text 替换成图片 Transform 即可。
image xiaobei cosplay normal = Transform(Text("小北\ncosplay normal", size=64, color="#ffffff", outlines=[(3, "#5e3570", 0, 0)]), xalign=0.5, yalign=0.5)
image xiaobei cosplay smile = Transform(Text("小北\ncosplay smile", size=64, color="#ffffff", outlines=[(3, "#5e3570", 0, 0)]), xalign=0.5, yalign=0.5)
image xiaobei cosplay pose = Transform(Text("小北\ncosplay pose", size=64, color="#ffffff", outlines=[(3, "#5e3570", 0, 0)]), xalign=0.5, yalign=0.5)
image xiaobei cosplay shy = Transform(Text("小北\ncosplay shy", size=64, color="#ffffff", outlines=[(3, "#5e3570", 0, 0)]), xalign=0.5, yalign=0.5)

# 素织下午换装用新形态，占位。正式图建议放：images/char/suzhi/suzhi cosplay *.png
image suzhi cosplay normal = Transform(Text("素织\ncosplay normal", size=64, color="#ffffff", outlines=[(3, "#ef5350", 0, 0)]), xalign=0.5, yalign=0.5)
image suzhi cosplay shy = Transform(Text("素织\ncosplay shy", size=64, color="#ffffff", outlines=[(3, "#ef5350", 0, 0)]), xalign=0.5, yalign=0.5)
image suzhi cosplay angry = Transform(Text("素织\ncosplay angry", size=64, color="#ffffff", outlines=[(3, "#ef5350", 0, 0)]), xalign=0.5, yalign=0.5)
image suzhi cosplay smile = Transform(Text("素织\ncosplay smile", size=64, color="#ffffff", outlines=[(3, "#ef5350", 0, 0)]), xalign=0.5, yalign=0.5)

# 集邮卡CG占位：正式可以替换成拍照图或重绘图。
image cg stamp_card = Transform(Text("2026社团文化节集邮卡", size=70, color="#ffffff", outlines=[(3, "#1565c0", 0, 0)]), xalign=0.5, yalign=0.5)

label chapter_10:

    # 【场景一：周末上午】
    scene bg dorm_room_morning with fade
    play music audio.bgm_daily fadein 1.0

    "周末上午。"
    "窗帘缝里挤进来的光。"
    "像一条强制开机的进度条。"

    play sound audio.se_phone

    "手机连续震了三下。"

    s_phone "起床。"
    s_phone "五点半集合。"
    s_phone "现在已经九点了。"

    m_phone "你这提醒跨度是不是有点大。"

    s_phone "怕你睡到下午。"

    m_phone "我没有那么离谱。"

    s_phone "你昨天说要早起画桥。"

    m_phone "桥会理解我的。"

    s_phone "桥不会。"
    s_phone "桥只会受力。"

    m_phone "你已经被土木概论污染了。"

    nvl clear

    m "昨天说好的。"
    m "今天要去校园里找土木素材。"
    m "但现在。"
    m "我只想找枕头素材。"

    play sound audio.se_phone

    l "重大情报。"
    l "今天操场百团大战。"
    l "有集邮卡。"
    l "盖满能抽奖。"

    m_phone "什么奖。"

    l "未知。"
    l "但未知本身就是贵族的浪漫。"

    s_phone "你只是想凑热闹。"

    l "准确。"

    m_phone "那土木观察社怎么办。"

    s_phone "先观察社团。"
    s_phone "也是观察。"

    m "她说得好有道理。"
    m "我甚至没办法反驳。"

    stop music fadeout 1.0

    # 【场景二：操场入口】
    scene bg playground_morning with fade
    play music audio.bgm_school fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.4

    "操场入口。"
    "横幅从主席台一路拉到跑道边。"
    "人群像被风吹散的便利贴。"
    "每个摊位前都挤着不同颜色的热闹。"

    show suzhi casual normal at center with dissolve

    s "这边。"

    show lingning casual happy at left with moveinleft

    l "百团大战。"
    l "听起来像大学版本的群雄割据。"

    m "其实就是社团招新。"

    show lingning casual pose

    l "不要破坏史诗感。"

    show suzhi casual gloomy

    s "你先把报名表从脸上拿下来。"

    l "刚刚被风糊上的。"
    l "这说明我与社团活动有缘。"

    m "也可能说明你站得太靠前。"

    show suzhi casual normal

    s "先去领集邮卡。"
    s "盖几个章就走。"

    m "几个？"

    s "看情况。"

    l "不。"
    l "既然是集邮。"
    l "就要全收集。"

    m "你这种人玩开放世界很可怕。"

    stop sound fadeout 1.0

    # 【场景三：集邮卡】
    scene cg stamp_card with fade
    play music audio.bgm_daily_funny fadein 1.0

    "入口处的志愿者递来一张浅蓝色的卡片。"
    "卡片上印着社团文化节集邮格。"
    "每个格子旁边都有小小的社团名。"
    "天文社。"
    "音乐社。"
    "心理社。"
    "书法社。"
    "话剧社。"
    "动漫社。"
    "电竞社。"
    "魔方社。"
    "手工社。"
    "志愿者协会。"
    "足球社。"
    "羽毛球社。"
    "乒乓球社。"
    "健美操社。"
    "还有一些被印章和光反射挡住的名字。"

    m "好多。"

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    l "这是命运清单。"

    s "这是集邮卡。"

    l "差不多。"
    l "盖满它。"
    l "我们就完成了大学第一项伟业。"

    m "我以为第一项伟业是不要挂科。"

    show suzhi casual gloomy

    s "那个难度更高。"

    m "别这么诚实。"

    show lingning casual pose

    l "出发。"
    l "第一站。"
    l "离我们最近的摊位。"

    stop music fadeout 1.0

    # 【场景四：天文社】
    scene bg playground with fade
    play music audio.bgm_campus fadein 1.0

    "最近的摊位摆着小型望远镜。"
    "桌布上贴着星空图。"
    "旁边还放着几张月球照片。"

    club_senior "同学。"
    club_senior "对宇宙感兴趣吗？"

    show lingning casual happy at left with dissolve

    l "当然。"
    l "我一直认为我的精神起源于更高维度。"

    club_senior "呃。"
    club_senior "我们主要晚上观星。"

    m "他晚上主要睡觉。"

    show lingning casual depressed

    l "睡眠也是一种深空探索。"

    show suzhi casual normal at center with dissolve

    s "盖章。"
    s "谢谢。"

    play sound audio.se_splat

    "红色印章落在卡片左上角。"

    m "第一枚。"

    l "宇宙承认了我们。"

    s "只是天文社承认你来过。"

    # 【场景五：音乐社与书法社】
    scene bg rest_area with fade
    play sound audio.se_footsteps_crowd volume 0.4

    "再往前走。"
    "左边是音乐社。"
    "吉他声和键盘声混在一起。"
    "右边是书法社。"
    "墨香在风里轻轻散开。"

    show suzhi casual normal at center with dissolve
    show lingning casual happy at left with dissolve

    club_sister "音乐社了解一下。"
    club_sister "可以学吉他。"
    club_sister "也可以一起排练。"

    l "我会。"

    m "你会什么。"

    l "欣赏。"

    club_sister "也可以。"

    s "你别把人家学姐整不会了。"

    play sound audio.se_splat

    "第二枚章。"

    m "音乐社。"

    "旁边书法社的学长正低头写字。"
    "宣纸上落下两个大字。"
    "加油。"

    club_senior "同学。"
    club_senior "要不要写一个？"

    s "他写字一般。"

    m "你为什么直接替我评价。"

    s "节省时间。"

    l "让我来。"

    "凌宁拿起毛笔。"
    "沉思三秒。"
    "在纸上写下一个歪歪扭扭的‘贵’。"

    club_senior "这是……"

    l "贵族的贵。"

    s "像虫子爬过。"

    m "挺抽象的。"

    play sound audio.se_splat

    "第三枚章。"
    "书法社。"

    stop sound fadeout 1.0

    # 【场景六：心理社】
    scene bg library with fade
    play music audio.bgm_warm fadein 1.0

    "心理社的摊位很安静。"
    "桌上摆着彩色卡片。"
    "每张卡片上都有一个问题。"

    club_sister "抽一张吧。"
    club_sister "看看你现在最需要什么。"

    show suzhi casual normal at center with dissolve
    show lingning casual tired at left with dissolve

    m "我抽到了。"
    m "睡眠。"

    s "很准。"

    l "我抽到了。"
    l "勇气。"

    s "你需要的是常识。"

    l "常识会限制贵族。"

    club_sister "那这位同学呢？"

    show suzhi casual surprise

    s "我？"

    "素织低头抽了一张。"
    "卡片上写着。"
    "偶尔也可以依赖别人。"

    show suzhi casual shy

    s "这个不准。"

    m "我觉得挺准。"

    show suzhi casual angry

    s "闭嘴。"

    play sound audio.se_splat

    "第四枚章。"
    "心理社。"

    stop music fadeout 1.0

    # 【场景七：电竞社与魔方社】
    scene bg computer_lab with fade
    play music audio.bgm_daily_funny fadein 1.0

    "电竞社摊位前围着一圈人。"
    "屏幕上角色技能乱飞。"
    "旁边魔方社的桌子上。"
    "一排魔方被拧得整整齐齐。"

    show lingning casual happy at left with dissolve
    show suzhi casual normal at center with dissolve

    club_senior "电竞社。"
    club_senior "五分钟solo。"
    club_senior "赢了送贴纸。"

    l "让我来。"

    m "你会玩？"

    l "不会。"
    l "但气势不能输。"

    scene bg computer_lab with hpunch

    "五分钟后。"

    show lingning casual ashamed at left with dissolve
    show suzhi casual gloomy at center with dissolve

    l "对方不讲武德。"

    m "你开局走进防御塔。"

    s "塔很讲武德。"
    s "它一直打你。"

    play sound audio.se_splat

    "第五枚章。"
    "电竞社。"

    "魔方社的学长递来一个三阶魔方。"

    club_senior "试试？"

    m "我可以。"

    "我接过魔方。"
    "转了三下。"
    "把一面也打乱了。"

    s "你是怎么做到越复原越乱的。"

    m "这叫结构重组。"

    l "很土木。"

    play sound audio.se_splat

    "第六枚章。"
    "魔方社。"

    # 【场景八：体育区】
    scene bg stadium_grandstand with fade
    play music audio.bgm_break_time fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.4

    "体育类社团集中在跑道另一侧。"
    "足球社在颠球。"
    "羽毛球社在拉高远球。"
    "乒乓球社的桌子被围得水泄不通。"
    "健美操社的音响放得很响。"

    show suzhi casual normal at center with dissolve
    show lingning casual happy at left with dissolve

    club_senior "足球社了解一下。"

    l "我擅长战略部署。"

    m "翻译一下。"

    s "他不跑。"

    club_senior "守门也行。"

    show lingning casual surprised

    l "守门？"
    l "以一人之躯面对全场火力。"
    l "这不是守门。"
    l "这是王城最后的城墙。"

    m "你要是真这么有觉悟。"
    m "体育课就不会请假了。"

    play sound audio.se_splat

    "第七枚章。"
    "足球社。"

    "羽毛球社的学姐把球拍递给素织。"

    club_sister "同学要不要试一下？"

    show suzhi casual smile

    s "可以。"

    "她轻轻一挥。"
    "羽毛球越过球网。"
    "准确落在线内。"

    m "好标准。"

    show suzhi casual normal

    s "以前打过一点。"

    l "一点。"
    l "等于人类高质量一点。"

    play sound audio.se_splat

    "第八枚章。"
    "羽毛球社。"

    "乒乓球社和健美操社的章也很快盖上。"
    "卡片上的红色印记越来越密。"

    m "已经一半了吧。"

    l "不。"
    l "真正的战斗才刚刚开始。"

    s "你能不能别每十分钟就热血一次。"

    stop sound fadeout 1.0

    # 【场景九：志愿者协会与手工社】
    scene bg rest_area_sunset with fade
    play music audio.bgm_warm_guitar fadein 1.0

    "中午过后。"
    "阳光开始变得偏白。"
    "我们在志愿者协会摊位领了宣传册。"
    "又在手工社摊位前停下。"

    show suzhi casual normal at center with dissolve
    show lingning casual tired at left with dissolve

    club_sister "可以做一个小挂件。"
    club_sister "做好了就能盖章。"

    m "这个听起来简单。"

    "十分钟后。"
    "我手里出现了一个看不出物种的毛绒球。"

    s "这是猫吗？"

    m "本来是。"

    l "现在像土豆。"

    m "至少它很稳定。"

    s "别什么都往土木上靠。"

    play sound audio.se_splat

    "第十一枚章。"
    "手工社。"

    "志愿者协会的章在旁边。"
    "红色的‘奉献’两个字印得很正。"

    m "还差几个？"

    show lingning casual happy

    l "话剧社。"
    l "还有。"
    l "动漫社。"

    show suzhi casual gloomy

    s "你为什么说动漫社的时候停顿了。"

    l "因为那是最终关卡。"

    m "不就是动漫社吗。"

    l "你不懂。"
    l "那是另一个次元的大门。"

    s "你今天中二浓度超标。"

    # 【场景十：话剧社】
    scene bg classroom_clean with fade
    play music audio.bgm_awkward fadein 1.0

    "话剧社占了教学楼一楼的空教室。"
    "门口贴着手写海报。"
    "即兴表演体验。"
    "体验后盖章。"

    show lingning casual surprised at left with dissolve
    show suzhi casual normal at center with dissolve

    m "体验？"

    club_sister "对。"
    club_sister "抽一个题目。"
    club_sister "三十秒表演。"

    l "这种场合。"
    l "正适合我。"

    s "我有种不好的预感。"

    "凌宁抽出纸条。"
    "上面写着。"
    "被雨淋湿的王子。"

    show lingning casual pose

    l "为什么。"
    l "为什么命运要在今日将我放逐。"
    l "这雨。"
    l "不是落在我的肩上。"
    l "是落在王国的心脏。"

    "教室安静了。"

    m "他进入状态了。"

    show suzhi casual gloomy

    s "不如说他平时就这样。"

    club_sister "很好。"
    club_sister "情绪很足。"

    play sound audio.se_splat

    "第十二枚章。"
    "话剧社。"

    show lingning casual happy

    l "我感觉被认可了。"

    s "你不要被错误地鼓励。"

    stop music fadeout 1.0

    # 【场景十一：动漫社门口】
    scene bg library with fade
    play music audio.bgm_stealth_happy fadein 1.0
    play sound audio.se_footsteps_crowd volume 0.4

    "动漫社的摊位在活动室门口。"
    "门框上挂着彩色纸花。"
    "桌上摆着立牌、徽章和手绘海报。"
    "走廊里比操场还热闹。"

    show suzhi casual normal at center with dissolve
    show lingning casual happy at left with dissolve

    s "盖完这个就结束。"

    l "不。"
    l "结束往往意味着开始。"

    m "你能不能先用人类语言说话。"

    unknown "欢迎来到动漫社。"

    hide suzhi
    hide lingning

    show xiaobei cosplay normal at center with dissolve

    "声音从门内传来。"
    "一个穿着cos服的女生站在活动室门口。"
    "衣摆随着她转身的动作轻轻晃了一下。"
    "阳光从窗边斜着落下来。"
    "刚好落在她的发饰和眼角。"

    kb "你们是来集邮的吗？"

    m "啊。"
    m "是。"

    show xiaobei cosplay smile

    kb "那先盖章。"
    kb "然后可以进来看看。"
    kb "今天有社团展示。"

    play sound audio.se_splat

    "最后一枚章落下。"
    "动漫社。"

    m "谢谢。"

    kb "不用谢。"
    kb "你们也可以报名。"

    m "报名？"

    show xiaobei cosplay pose

    kb "动漫社不只是看动画。"
    kb "也有绘画、剪辑、配音、cos、摄影、后期。"
    kb "还有社团展演。"

    "她说话的时候很自然。"
    "像是在介绍一件自己真的喜欢的事。"
    "我原本只是想把集邮卡盖满。"
    "可视线却一直没能从她身上移开。"

    m "摄影。"
    m "后期。"

    kb "嗯。"
    kb "如果会拍照或者修图。"
    kb "很欢迎。"

    "我忽然想起昨天的土木作业。"
    "观察。"
    "记录。"
    "把看见的东西变成作品。"
    "这好像也不是完全无关。"

    show suzhi casual gloomy at right with dissolve
    show lingning casual happy at left with dissolve

    s "你看得太认真了。"

    m "我是在了解社团方向。"

    l "方向很明确。"
    l "他已经被异世界召唤了。"

    show xiaobei cosplay shy

    kb "也没有那么夸张啦。"

    m "我可以看看报名表吗？"

    show suzhi casual surprise

    s "你真要加？"

    m "先看看。"

    l "一般说先看看的人。"
    l "已经输了。"

    stop sound fadeout 1.0

    # 【场景十二：动漫社活动室】
    scene bg classroom_desk with fade
    play music audio.bgm_warm fadein 1.0

    "活动室里摆着几张拼在一起的桌子。"
    "墙上贴着往届活动照片。"
    "角落里堆着道具箱。"
    "几套cos服被整齐地挂在衣架上。"

    show xiaobei cosplay normal at center with dissolve

    kb "这个是报名表。"
    kb "填专业、联系方式和想参加的方向就行。"

    m "方向。"

    kb "摄影也可以写。"
    kb "新生不用马上确定。"
    kb "先来玩也行。"

    show lingning casual happy at left with dissolve

    l "听起来很适合我。"

    m "你想参加什么方向。"

    show lingning casual pose

    l "精神领袖。"

    kb "欸？"

    show suzhi casual gloomy at right with dissolve

    s "不用管他。"
    s "他平时就这样。"

    m "我填摄影和后期吧。"

    "笔尖落在纸上。"
    "动漫社。"
    "摄影。"
    "后期。"
    "写下去的时候。"
    "我居然有一点紧张。"

    kb "欢迎加入。"

    show xiaobei cosplay smile

    "小北把一枚社团徽章放到我手心。"

    kb "下午有一个小型cos体验。"
    kb "如果你们有时间。"
    kb "可以来帮忙拍照。"

    m "下午？"

    s "我们不是还要画土木作业吗。"

    l "素材来源增加了。"
    l "二次元建筑与现实结构的交汇。"

    s "你别乱给作业升华。"

    m "下午来看看也行。"
    m "拍两张就走。"

    show suzhi casual gloomy

    s "你每次说两张。"
    s "最后都不是两张。"

    m "这次一定。"

    "素织看了我一眼。"
    "叹了口气。"

    show suzhi casual normal

    s "行。"
    s "但别影响作业。"

    m "知道。"

    # 【场景十三：下午再访】
    scene bg classroom_full with fade
    play music audio.bgm_bright_violin fadein 1.0

    "下午。"
    "动漫社活动室外的人比上午更多。"
    "有人举着反光板。"
    "有人整理假发。"
    "还有人在角落里检查道具。"

    show xiaobei cosplay smile at center with dissolve

    kb "你们来了。"

    m "说好来拍照。"

    kb "正好。"
    kb "我们缺一个临时摄影。"

    show lingning casual happy at left with dissolve

    l "看。"
    l "命运开始结算了。"

    show suzhi casual normal at right with dissolve

    s "你不要给别人添麻烦。"

    kb "不会。"
    kb "其实还有一套备用服。"
    kb "如果有人愿意试试的话。"

    "小北的视线落到素织身上。"

    show suzhi casual surprise

    s "我？"

    kb "嗯。"
    kb "你的气质很合适。"

    m "确实。"

    show suzhi casual angry

    s "你确实什么。"

    l "我同意。"
    l "素织拥有成为主角的压迫感。"

    s "你们两个闭嘴。"

    kb "只是试穿。"
    kb "不想的话也没关系。"

    "素织低头看着那套服装。"
    "沉默了一会儿。"

    show suzhi casual shy

    s "只拍几张。"
    s "不要乱传。"

    m "当然。"

    l "我以贵族之名保证。"

    s "你的保证最不可靠。"

    # 【场景十四：素织cos占位登场】
    scene bg classroom_desk with fade
    play music audio.bgm_love fadein 1.0

    "十分钟后。"
    "活动室的门被轻轻推开。"

    show suzhi cosplay normal at center with dissolve

    "素织换好了衣服。"
    "和平时利落的样子不太一样。"
    "多了一点不自然的拘谨。"
    "也多了一点让人移不开眼的明亮。"

    s "看什么。"

    m "没。"
    m "挺合适的。"

    show suzhi cosplay shy

    s "别说这种奇怪的话。"

    show xiaobei cosplay smile at left with dissolve

    kb "很好看。"
    kb "真的很适合。"

    show lingning casual surprised at right with dissolve

    l "这是。"
    l "现实世界的隐藏剧情。"

    show suzhi cosplay angry

    s "凌宁。"

    l "我什么都没说。"

    m "你已经说了很多。"

    kb "那我们去窗边拍吧。"
    kb "光线比较好。"

    "我举起相机。"
    "取景框里。"
    "素织站在窗边。"
    "午后的光落在她肩上。"
    "她有些不自在地移开视线。"
    "但嘴角却没有真的生气。"

    m "看这边。"

    show suzhi cosplay shy

    s "快点拍。"

    play sound audio.se_phone

    "快门声响起。"

    m "好了。"

    s "给我看看。"

    "她凑过来看屏幕。"
    "距离突然变近。"
    "空气也像被按下了暂停键。"

    s "……还行。"

    m "只是还行？"

    show suzhi cosplay smile

    s "比你平时靠谱。"

    m "那评价还挺高。"

    show xiaobei cosplay smile

    kb "这张可以做社团宣传图。"

    show suzhi cosplay angry

    s "不行。"
    s "至少要先给我审核。"

    kb "当然。"

    show lingning casual happy

    l "我宣布。"
    l "今日百团大战。"
    l "最大收获。"
    l "不是印章。"
    l "是新世界的大门。"

    m "你这么说也没错。"

    show suzhi cosplay shy

    s "你也别跟着他乱说。"

    # 【场景十五：傍晚收束】
    scene bg playground_sunset with fade
    play music audio.bgm_warm_guitar fadein 1.0

    "傍晚。"
    "百团大战慢慢收摊。"
    "操场上的音响声小了下去。"
    "集邮卡上的红章已经盖满。"
    "我的口袋里多了一枚动漫社徽章。"
    "相机里多了几十张照片。"
    "还有几张。"
    "我没敢多看。"

    show suzhi cosplay normal at center with dissolve
    show lingning casual happy at left with dissolve
    show xiaobei cosplay smile at right with dissolve

    kb "今天辛苦啦。"
    kb "之后社团群里会发活动通知。"

    m "嗯。"
    m "我会看。"

    s "作业也要看。"

    m "知道。"
    m "土木观察社不会倒闭。"

    l "今天的观察成果很丰富。"
    l "社团摊位结构。"
    l "人流组织。"
    l "临时建筑。"
    l "以及cos服装与个体气质之间的复杂关系。"

    show suzhi cosplay angry

    s "最后一个删掉。"

    kb "你们关系真好。"

    show suzhi cosplay shy

    s "没有。"

    m "一般好。"

    l "非常好。"

    s "你闭嘴。"

    "风从操场另一头吹过来。"
    "把横幅吹得轻轻晃动。"
    "我低头看着盖满章的卡片。"
    "从天文社到动漫社。"
    "从只是路过到写下报名表。"
    "今天好像什么都没计划。"
    "却又什么都发生了。"

    m "大学生活。"
    m "还真容易被一张集邮卡改变方向。"

    show xiaobei cosplay smile

    kb "那就下次社团见。"

    m "下次见。"

    stop music fadeout 2.0

    # 第十章 完
    scene black with fade
    centered "{size=60}第十章 完{/size}"

    return
