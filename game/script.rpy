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

    s "你走路不看路的吗？"

    m "（揉着肩膀）抱歉抱歉，刚才光顾着看那边的猴山了……"

    "我低下头，发现地上掉了一个精致的挂件。"
    m "啊，你的东西掉了。"

    "我捡起挂件，递了过去。"

    s "（一把夺过，仔细检查了一下）……啧，还好没摔坏。这可是限量版的。"

    m "那个，真的不好意思。我不是故意的。"

    show suzhi casual normal

    s "（叹气）算了，看在你态度诚恳的份上。"
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

    j "全体都有！立正——！向右看齐！"

    m "（嘶……这九月的太阳怎么比昨天还毒。）"
    m "（土木工程系的方队……应该是这里吧。）"

    "我急匆匆地跑入队伍末尾。"

    m "报告！"
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

    s "……是你？！"
    m "……是你？！"

    # 恢复场景
    scene bg playground 
    
    show suzhi camo surprised at center
    with fade

    s "（惊讶地指着我）那个动物园的冒失鬼？"
    m "（惊讶地指着她）那个脾气很冲的……"

    j "那边那两个！干什么呢！眉来眼去的！出列！"

    show suzhi camo embarrassed with vpunch

    m "（尴尬地小声说）完蛋……"
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
    e "（声音不大，但透着一股冷冽的穿透力）第三排那个戴眼镜的，眼神乱飘什么？"
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
    
    l "木子米……我恐怕已到极限了……今日的阳光真是无情啊。"
    l "若此刻能有一杯加冰的柠檬水，当是人间至福……"

    m "别说话了，凌宁。再坚持五分钟，少尉看表了。"

    l "五分钟？这简直度日如年。看着那位教官冷峻的面容，我只觉得比烈日还要难熬。。"
    l "我现在……哪怕是一口普通的自来水，也会感激涕零的"
    show instructor cold at center with dissolve
    hide lingning

    e "全体都有！稍息！"
    e "（摘下墨镜，露出一双锐利的眼睛，环视一周）讲一下。"
    e "上午的训练，整体表现尚可，但个别同学意志力薄弱。"
    e "记住，你们是未来的工程师，连这点苦都吃不了，以后怎么去工地？"
    e "鉴于刚才有人乱动，延长十五分钟站姿体验。"

    show lingning camo weak at right with dissolve
    l "哎……天亡我也。"

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
    e "解散！休息二十分钟！"
    hide instructor with dissolve

    show lingning camo tired at center
    l "水……我的生命之源，我来了。"

    # (凌宁虽然极度口渴，但依然保持着快步走的姿态，而不是像其他人那样狂奔，木子米紧随其后)
    # (画面切换：放水区)
    # (此时，一个穿着蓝色保洁服的大妈正背对着学生们，手里拿着一个巨大的黑色塑料袋。她动作麻利地拿起地上的水瓶，拧开盖子，哗啦一声倒掉里面的水，然后将瓶子踩扁扔进袋子)
    
    hide lingning
    show auntie working at center
    # 音效：倒水声
    play sound audio.se_pour_water

    show lingning camo surprised at left with vpunch
    l "天哪……？"

    # (木子米也停下了脚步，愣住了)
    # (只见大妈并没有停手，她拿起半瓶还剩很多的矿泉水，那是凌宁特意用手帕擦拭过瓶身的，毫不犹豫地倒进了旁边的排水沟)
    play sound audio.se_pour_water

    l "且慢！阿姨！请手下留情！"

    a "啥？"

    l "那是我的水……我才刚刚买来，才喝了一小口。你为何要将它倒掉？"

    a "这地儿不让乱扔垃圾。我看这瓶子都在地上晒半天了，寻思是没人要的。"

    l "怎会是没人要的？我们在那训练呢，瓶子当然在地上晒着了"

    # (周围的同学也围了过来，因为极度的干渴和疲惫，大家的情绪都像火药桶一样)
    stu_a "就是啊，我那瓶也是满的！"
    stu_b "怎么这样啊，我们累死累活的，连口水都不让喝？"
    stu_c "这大妈是不是为了卖瓶子赚钱疯了啊？"

    # (素织也走了过来，手里拿着空瓶子，显然她原本也想来喝水，却发现自己的水也没了)
    show suzhi camo normal at right
    s "阿姨，我们在训练，水瓶放在这是为了休息时喝。"
    s "您不问一声就倒掉，是不是太过分了？"
    a "我看这水都被太阳晒热了，塑料瓶晒久了有毒！"
    a "再说，这一地乱七八糟的，领导检查看见了要扣俺工资的！"
    l "即便有毒，那也是我们自己的选择！您……您怎么能这样不近人情？"
    l "我们真的快要渴晕过去了"
    l "……扣工资并非小事, 但这也不是您随意处置他人财物的理由啊！"
    a "你这学生咋说话呢！俺这是为了你们好！"
    a "这一地的瓶子，哪瓶是谁的你们分得清吗？万一喝错了传染病咋整？"

    m "（眼看局势要失控）凌宁，冷静点。"

    l "木子米，这让我如何冷静？这简直是……简直是不可理喻！"

    # (就在这时，一道挺拔的身影挡住了阳光)
    show instructor cold at center with dissolve
    hide auntie
    hide suzhi
    hide lingning

    e "吵什么？很有精神嘛。"
    
    show lingning camo weak at left
    l "教官，这位阿姨将我们的饮用水全部处理掉了，我们在试图……讲道理。"

    e "（冷冷地扫了一眼满地的空瓶和大妈手里的袋子，眉头微皱）行了。多大点事？没水了再去买。"
    e "（目光如炬地盯着凌宁）对着长辈大声喧哗，这就是你的教养？你的军人风度呢？"

    l "我……并非有意喧哗，只是……"

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
    
    l "真是令人郁闷。我实在无法理解，那位阿姨为何要这般固执。还有那位少尉，虽说军令如山，但也太不通人情了……"

    # (砰的一声，宿舍门被踢开)
    play sound audio.se_door_kick
    with vpunch

    m "（抱着那个巨大的不锈钢保温桶）凌宁，拿碗来！"

    show lingning casual surprised at center
    l "木子米？你抱着这庞然大物是何意？莫非是食堂的存货？"

    m "抢什么抢。这是“赔偿”。"

    l "赔偿？"

    m "那个大妈给的。绿豆汤，冰糖的。"

    l "真的吗？她会有这般好意？……不会有什么问题吧？"

    m "喝不喝？不喝我给隔壁寝室了。"

    l "嗯？！……啊，真是舒畅！天哪，竟是冰镇的！"
    l "这绿豆熬得恰到好处，口感绵密，甜度适中……"

    # (木子米把事情的原委，包括大妈擦地、担心暴晒水质变质的事情，原原本本地讲了一遍)
    
    show lingning casual ashamed at center
    
    # (宿舍里渐渐安静下来，凌宁捧着空碗，白皙的脸庞泛起了一丝红晕，表情变得非常惭愧)

    l "呃……你是说，她是担心水质变坏才倒掉的？"

    m "嗯。而且她怕我们中暑，特意熬的汤，结果被你急切的样子吓得不敢拿出来。"

    l "这……这让我显得像是无理取闹的纨绔子弟一般。"
    l "哎，我今日的举止实在是有失风度，竟误解了一位长辈的好意。"
    l "真是……太失礼了"

    m "行了，明天见到人家，知道该咋办了吧？"

    show lingning casual happy at center
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
    
    l "阿姨……请留步。"

    a "干啥？"

    l "（突然非常标准地鞠了一躬）真的非常抱歉！"
    l "昨日是我鲁莽了，言语多有冒犯，请您原谅！"
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

    s "看来，误会解除了？"

    # (木子米转头，发现素织不知何时站在了他身边，手里拿着一瓶水)
    show suzhi camo normal at center with dissolve

    m "是啊。有时候，眼睛看到的并不一定是真相。大家只是立场不同罢了。"

    s "听说是你昨天晚上去跟阿姨沟通的？"

    m "碰巧遇到了而已。"

    show suzhi camo smile at center
    s "（看不出来，你这人虽然看着呆呆的，办事还挺靠谱的。"
    s "连那个冷冰冰的少尉刚才都夸了我们班风气不错。"

    # (CG图：素织的特写。阳光透过树叶洒在她脸上，那原本清冷的眸子里，此刻倒映着木子米的影子，带着一丝认可和温柔)
    scene cg suzhi_camo_smile with dissolve

    s "喏，这个给你。"

    m "这是？"

    s "昨天看你水也没了，今天多买了一瓶。"
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
    l "啊……这清晨的寒气，简直是在侵蚀我的灵魂。"

    # 立绘出现：凌宁。虽然穿着迷彩服，但他的扣子扣得一丝不苟
    show lingning camo weak at center with dissolve

    l "木子米，你看我的脸色是否有些苍白？这几日的紫外线虽然强烈，但这早晨的寒风更是肌肤的大敌。"

    m "（整理着腰带）看起来挺红润的，凌宁。赶紧吧，迟到一分钟，少尉的眼神能把你冻成冰雕。"

    show lingning camo tired
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

    e "（拿着扩音器，声音穿透力极强）全体都有！立正！"
    e "经过一周的适应性训练，你们已经初步具备了军人的模样。但是，这还不够！"
    e "下周五，将举行全校新生军训汇报表演。这是检验你们成果的时刻，也是展现土木系风采的时刻！"

    # 台下一阵骚动
    play sound audio.se_footsteps_crowd # 模拟骚动声

    e "安静！"
    e "为了保证汇演效果，从今天开始，我们将重新编队。所有人将被打散，重新划分为三个部分："
    e "第一，分列式方队。这是最精锐的部队，将代表系里走过主席台，接受检阅。要求动作标准，身材匀称，意志力强！"
    e "第二，合唱团。负责在看台上唱军歌，展现气势。"
    e "第三，观训营。身体素质无法适应高强度训练的，进入观训营。"

    # 少尉顿了顿
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

    l "木子米，虽然我的双腿在抗议，但身为七尺男儿，若连挑战都不敢面对，岂不是有辱斯文？"

    m "凌宁？你想进方队？"

    l "自然。荣誉即吾命。哪怕是倒下，我也要倒在冲锋的路上……或者正步的路上。"

    m "好，那我们一起。"

    # 【场景三：操场中央 - 选拔现场 - 上午】
    scene bg playground with fade
    play music audio.bgm_march fadein 1.0
    
    # 音效：整齐的踏步声
    play sound audio.se_foot_stomp

    show instructor cold at center
    e "第一排，出列！正步走！"
    
    # 几名男生踢着正步走过
    e "停！第三个，顺拐了，去合唱团。第五个，罗圈腿太严重，去合唱团。第一个，留下。"

    # 残酷的筛选在继续
    e "下一组！"
    hide instructor

    # 轮到女生组了
    show suzhi camo normal at center with dissolve

    m "（即使在一群穿着同样迷彩服的女生中，素织依然很显眼。）"
    m "（她的动作很利落，没有多余的晃动。）"

    e "正步——走！"
    play sound audio.se_foot_stomp

    # 素织踢腿带风，摆臂定格准确
    show suzhi camo angry # 表现凛冽的英气

    e "（眼中闪过一丝赞赏，但很快掩饰住）停！"
    e "第二个（指素织），不错。踢腿高度标准，落地有声。入列，第一排面。"

    s "（大声）是！"

    # 素织出列，站在了象征“精锐”的指定区域
    hide suzhi
    show suzhi camo normal at right
    # 眼神交互
    # 素织微微侧头，似乎在人群中寻找着什么
    
    m "（该我了。）"
    hide suzhi

    show instructor cold at center
    e "下一组！正步——走！"

    m "（绷直脚尖。）"
    m "（压住重心。）"
    m "（不要晃动。）"
    m "（我感觉全身的肌肉都在紧绷，每一次砸地都震得脚底发麻。）"

    e "停！"
    # 教官走到面前
    e "（上下打量）眼镜扶好。眼神再犀利点，别像没睡醒一样。"
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
    e "下一组！"

    # 凌宁上场了
    # 切换到凌宁机械舞CG
    stop music fadeout 0.5
    play music audio.bgm_humorous fadein 0.5
    show cg lingning_mechanical with vpunch

    e "停！"
    e "（皱眉）那个白净的男生，你在跳机械舞吗？"

    l "报告教官！我正在努力控制肌肉的平衡，试图达到力与美的统一！"

    e "（忍住笑）很有想法。但是正步需要的是爆发力，不是优雅。"
    e "你的协调性还得练练。去合唱团吧，那边可能更适合你的……气质。"
    l "（如遭雷击，摇摇欲坠）教官……能不能再给我一次机会？我可以……"

    e "服从命令！"
    l "（行了一个有些悲壮的军礼）是……"

    hide cg lingning_mechanical
    scene bg playground
    show lingning camo tired at center

    # 凌宁垂头丧气地走向合唱团区域
    l "（投来了一个“你要连我的份一起努力”的哀怨眼神）"

    # 【场景四：分列式方队训练区 - 下午】
    scene bg playground_sunset with fade
    stop music fadeout 1.0
    play music audio.bgm_depressing_piano fadein 1.0

    # 字幕：分列式方队正式成立
    centered "分列式方队正式成立"

    show instructor cold at center
    e "恭喜你们，留到了最后。"
    e "但不要高兴得太早。从现在起，你们不再是个体，而是一个整体。"
    e "方队的要求只有一个：整齐划一。"
    e "一人出错，全队受罚！"

    # 接下来的几个小时，是枯燥到令人发指的单兵动作定型
    e "右腿踢出！定住！谁敢动！"
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

    e "（立刻捕捉到）女生方队第一排排头！晃什么！腿软了？"

    s "（咬牙，大声）报告！没有！"

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
    s "是你啊。没事。"

    m "（指了指她的脚）刚才定型的时候，我看你有点抖。是不是鞋磨脚？"

    show suzhi camo embarrassed
    s "（沉默了一会儿，偏过头）新鞋都这样。而且……作为排头，我不能让人觉得我娇气。"

    m "没人觉得你娇气。能坚持下来已经很厉害了。"

    show suzhi camo normal
    s "（自嘲地笑了一下）刚才害大家多站了两分钟，肯定有人在心里骂我。"

    m "（坐到她旁边，保持着礼貌的距离）那是教官严厉，不怪你。而且……"
    m "你刚才把腿抬高纠正姿势的时候，真的很帅。"

    # 素织愣了一下，转过头看着木子米
    show suzhi camo smile
    s "帅？你是第一个用这个词形容女生的。"

    m "在这里，这可是最高评价。"

    # 素织轻轻笑了一声，原本紧绷的肩膀放松了下来
    s "你也不赖。男生方队在后面，我也听到了，你们那个踢腿的声音，挺响的。"

    m "哈哈，那是为了掩盖我们整齐度不够的事实，用音量凑数。"

    # 凌宁突然出现
    show lingning casual pose at left with moveinleft
    
    l "噢，多么和谐的画面。而我，一个被流放到合唱团的孤独灵魂，只能在远处吟唱悲伤的旋律。"

    m "凌宁！你来慰问我们了？"

    l "（递过饮料，姿态依然优雅）拿去吧，这是合唱团的福利。"
    l "我们在树荫下练声，看着你们在烈日下挥洒汗水，"
    l "我的良心深受谴责……大约有一秒钟那么久。"
    show suzhi camo smile
    s "（接过饮料，对凌宁点头）谢谢。你的室友挺有趣的。"

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

    s "有什么？"

    m "有那个把你水倒掉的阿姨的扫帚？"

    show suzhi camo smile
    s "（噗嗤一声笑了出来）什么烂比喻。"

    m "有用就行。再来！预备——踢！"
    
    play sound audio.se_foot_stomp

    s "这次呢？"

    m "完美。声音很实。"

    show suzhi camo smile
    s "（深吸一口气，脸上露出了满意的神色）谢谢。感觉找到了。"

    m "（看着月光下的素织，她额前的碎发被汗水打湿，眼神却比星星还亮）"
    m "那个……汇演的时候，我们方队就在你们后面。"
    
    s "嗯？"

    m "我会看着你的背影走的。所以……你只要大胆往前走就好。如果排头稳了，我们后面也就稳了。"

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
    
    l "（敷着面膜，躺在床上发出含糊的声音）木子米，你回来得甚晚。莫非是与那位佳人有了什么月下之约？"

    m "（疲惫地爬上床）只是加练而已。别乱想。"

    l "呵，加练。年轻人的借口总是如此拙劣又可爱。不过……"
    l "（翻了个身）我看那位素织小姐，对你也并非无意。她的眼神，比这面膜里的精华还要浓郁。"

    m "睡你的觉吧，合唱团的大歌星。"

    l "哼，明日我要去竞选领唱。即便不能在跑道上挥洒汗水，我也要在看台上用歌声征服全场。晚安，我的步兵朋友。"

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

    e "停——！都给我停下！"

    # 音效：刺耳电流声 -> 模拟哨声
    play sound audio.se_whistle
    with soft_shake

    e "土木系的！你们是在梦游吗？那个排面，歪得像贪吃蛇一样！"
    e "尤其是第三列！脚抬高！砸地要有声音！ "
    e "中午还想不想吃饭了？我看你们是精神太好了，不饿是吧？ "
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

    e "全停！ 现在是11点40分，距离正式汇演还有40分钟。 为了保持这种紧绷的状态，为了防止你们吃饱了犯困——"
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
    
    s "（压低声音，气声）喂，木子米。活着吗？"

    m "（虚弱）快……不行了……这是谋杀……"

    s "想不想吃东西？"

    m "（瞬间睁大眼）想！做梦都想！"
    m "但是教官那个阎王就在那边盯着……"
    # 表情变化：狡黠/微笑
    show suzhi camo smile

    s "跟我来。 我昨天观察过了，那边的凉亭就能直接跑掉，"
    s "从凉亭穿过去就是食堂。 来回只需要五分钟。"

    m "越狱？！在这时候？"
    m "素织，你可是标兵啊！要是被抓到……"

    # 表情变化：愤怒/锐利 -> angry
    show suzhi camo angry

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
    s "（用力吞咽）太好吃了……木子米。"
    s "这绝对是我这辈子吃过最好吃的手抓饼。"
    s "里面加的这根烤肠简直是世界珍宝。"
    m "（猛点头）那是因为这是“违禁品”。"

    m "这就是“自由”的味道啊！"

    m "还有这孜然味，简直是救命的仙丹。"

    m "真没想到。 那个“优等生”素织，居然会带头违反纪律，还在这啃大饼。"

    s "规则是死的，人是活的。"
    s "如果不吃饱，哪有力气把那面锦旗扛回来？"
    s "我又不是铁做的机器人。"
    s "而且……"

    m "而且？"

    s "（移开视线）刚才解散的时候，我看你脸色发白，嘴唇都在抖。 "

    s "我怕你待会儿晕倒在主席台前……那样不仅丢我们土木系的人"
    s "还……挺让人担心的。"
    m "心脏……好像漏跳了一拍。 胃里暖暖的，心里也暖暖的。"
    m "（挠头，傻笑）原来是专门为了照顾我这个“病号”啊？"

    s "（声音提高八度）少自作多情！我是为了集体的荣誉！ "
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
    
    l "好！！！太棒了！！！ 木子米！素织小姐！看到了吗！那是第一名！"
    l "太优雅了！这才是土木人的魂！这才是优雅的极致！"

    # 立绘：教官 微笑（虽然素材是cold，但文字描述了）
    show instructor cold at left
    
    e "哼，算你们这群小兔崽子没给我丢人。排头兵！出列领奖！"

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

    s "呼…… 累死我了……感觉腿已经离家出走了，现在连站起来的力气都没有。"
    s "（把锦旗小心翼翼地交给路过的班长，然后毫无形象地瘫坐在地上）" # 文字演出

    # 木子米没有立绘，只有对话
    m "恭喜啊，排头兵。 刚才那个特写，如果拍下来绝对能当明年学校的招生简章封面。标题就叫“热血青春”。"


    # 表情变化：微笑
    show suzhi camo smile

    s "（接过水，仰头喝了一大口，转头看着木子米）你也一样。"
    s "刚才踢正步的时候，我能感觉到后面的节奏很稳。"
    s "就像有一堵墙在后面推着我一样。"
    s "如果没有你们在后面撑着，我这第一排也不敢走得那么大步。"

    m "（耸耸肩，笑）那是，毕竟吃了你的手抓饼。"
    m "这就是“拿人手短，吃人嘴软”，总得卖力气还债吧。"
    # 表情变化：娇羞/笑
    show suzhi camo embarrassed with soft_shake

    s "（扑哧一笑，轻轻锤了一下木子米的肩膀）就知道吃。满脑子都是手抓饼。"

    # 短暂沉默
    stop sound fadeout 2.0
    
    # 表情变化：正常/温柔
    show suzhi camo normal

    s "（抬头看着天空，长舒一口气）不过……终于结束了。 这半个月，简直像过了一年那么长。"

    m "是啊，结束了。 但这只是军训结束了。明天开始，就是真正的大学生活了。"

    show suzhi camo smile

    s "（轻声，眼神温柔）嗯。 希望以后的日子，也能像今天这样。"
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
    l "（超大声）啊！这是何等残酷的宿命！我的刘海……竟向左偏离了0.5度！"

    # 镜头切回中心 (或者切到说话人位置)
    # 如果需要瞬间切回，不需要 linear；如果需要滑回，加上 linear 0.5
    camera:
        xalign 0.5

    m "（惊醒）怎、怎么了？！"

    # 凌宁：日常 Pose 从右侧移入
    show lingning casual pose at right with moveinright
    
    l "早安，我的战友。"
    l "不，今日起，请称呼我为——“寻觅真理的贵族学者”。"
    l "你看，这瓶“皇家定型喷雾”，能否挽救我这不听话的发梢？"

    # 描述性动作
    m "（死鱼眼，重新倒回枕头上）"
    
    m "现在才七点半……"
    m "第一节课是八点。"
    m "你能不能让我再享受三分钟？"

    l "No, no, no，木子米，你太松懈了。"
    l "军训是肉体的磨炼，而大学课堂，是灵魂的战场！"
    l "尤其是第一节课！那是决定你在班级女生心中地位的“首秀”！"
    l "你是想做一个默默无闻的路人A，还是像我一样，成为照亮教室的恒星？"

    m "（内心）这家伙……绝对是那种会在开学典礼上扔玫瑰花的类型。"
    m "（内心）而且……白色西装？你是去上高数课还是去参加婚礼？"

    # 旁白或动作描述
    "（叹气，爬下床）"

    m "如果你所谓的“恒星”是指像个反光板一样闪瞎别人的眼睛，那你赢了。"
    m "话说，我们要去哪个教室？"

    l "（自信满满）作为情报通，我早已调查清楚。"
    l "就在——那个很高的楼。"

    m "……哈？"

    l "长春工程学院有哪个楼高？"
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

    l "（气喘吁吁，双手向后像忍者一样摆动）"
    l "木子米！慢……慢一点！"
    l "风！风会把我的发型吹乱的！"
    
    # 特写凌宁的滑稽感，稍微放大一点
    show lingning casual run at center, running_shake:
        zoom 1.1
    
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
    
    l "（绝望的哀嚎）四楼？！"
    
    # 音乐淡出，预示着接下来是爬楼梯的痛苦或转场
    stop music fadeout 2.0
    
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

    l "看来，只有那个位置了。"
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
    s "（眉头微微一皱，脸颊泛起一丝红晕，小声喊道）"
    s "呆子！看什么看！"
    s "这边……有个空位。"

    # 木子米发现占座的水杯
    "我这才发现，素织旁边的桌子上放着一个粉色的水杯，显然是帮人占座的。"

    # 凌宁复活，凑过来
    show lingning casual happy at left with moveinleft

    l "（凑到耳边）哦~ 多么感人的战友情。"
    l "去吧，木子米。"
    l "那个位置属于你。"
    l "我就牺牲一下，去第一排沐浴知识（粉笔灰）的洗礼了。"

    m "（感动）凌宁……你真是个好人。"
    m "下辈子我一定做牛做马报答你。"

    # 凌宁潇洒离开
    # 切换凌宁立绘为普通的或得意的，然后消失
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
    s "别误会。"
    s "本来是给……给室友占的。"

    # 切换表情：傲娇/生气
    show suzhi casual angry at center
    s "但是她突然说要陪男朋友坐后面。"
    s "这位置空着也是空着，要是坐个不认识的男生，我会不自在。"
    s "与其那样，不如……不如让你这个“熟人”坐这。"
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
    s "很……很奇怪吗？"

    show suzhi casual shy at center
    s "是不是太……太花里胡哨了？"
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

    s "（蚊子叫般的声音）……笨蛋。"
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

    s "（压低声音）喂。"
    s "第一节课就睡？你是不想活了吗？"
    s "那个“杀手王”已经盯你两次了。"
    play music audio.bgm_daily_funny fadein 1.0
    m "（擦了擦嘴角的口水）抱歉……"
    m "但这真的比安眠药还管用。你怎么能听得这么津津有味的？"

    show suzhi casual normal
    s "（指了指笔记本）这哪里津津有味了？"
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
    s "因为这只猪睡相很难看。"
    s "和你刚才一模一样。这叫……艺术写生。"

    m "你这就是单纯的报复吧！"
    m "把笔给我，我要行使肖像权，给这只猪画上眼镜！"

    # --- 第六幕：触电 ---

    # 切换回傲娇/护食状态
    show suzhi casual angry
    s "不给！这是我的创作！"
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

    s "（声音颤抖）……好好听课。"
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
    s "（看到木子米）哎，你居然买到了？"

    # 我去小卖部的时候，草莓味的已经卖光了。
    s "我去小卖部的时候，草莓味的已经卖光了。"

    # 只剩下……香菜味的酸奶。
    # 简直是黑暗料理。
    show suzhi casual angry
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
    s "（白眼翻到天上去）想得美。"

    # 我自己有水。
    s "我自己有水。"

    # (素织刚想从兜里掏纸巾擦手，结果因为手太滑，没拿住，一张纸巾都没带出来)
    "（素织刚想从兜里掏纸巾擦手，结果因为手太滑，没拿住，一张纸巾都没带出来）"

    # 素织：
    # 啧。
    show suzhi casual gloomy
    s "啧。"

    # 忘带纸了。
    s "忘带纸了。"

    # 喂，木子米，借张纸。
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
    s "（握紧了拳头，额头上蹦出一个红色的井字）这是我昨天刚买的新衣服！！！"

    # 而且黏糊糊的难受死了！！！
    s "而且黏糊糊的难受死了！！！"

    # 你给我……去死吧！！！
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
    l "（此时正拿着一杯咖啡路过，看到这一幕，优雅地抿了一口）"

    # 哦~
    l "哦~"

    # 这就是所谓的“打情骂俏”吗？
    l "这就是所谓的“打情骂俏”吗？"

    # 青春啊，真是充满了甜腻的草莓味。
    l "青春啊，真是充满了甜腻的草莓味。"

    # 只不过……
    # （看着木子米被逼到墙角）
    show lingning casual pose
    l "只不过……（看着木子米被逼到墙角）"

    # 愿主保佑你，我的朋友。
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
    s "你在看哪？！变态！"

    # 镜头复原
    show suzhi shirt shy at center:
        ease 0.2 zoom 1.0

    m "（立刻转头，疯狂搓衣服）我看衣服！我在看衣服的纹理！我在思考纤维的构造！"

    # 素织：(哼了一声，有些别扭地把腿并拢)
    s "（哼了一声，有些别扭地把腿并拢）……喂。"
    s "刚才……虽然是你弄脏的。但……你挡在前面的时候，没被烫到吧？"
    s "那两个人拿着好像是热豆浆。"

    # 木子米：(一愣，看了看自己的手背，确实有一块红了)
    m "（一愣，看了看自己的手背，确实有一块红了）啊，没事。皮糙肉厚的。"
    m "只要你的脸没事就行。要是毁容了，我可赔不起一辈子的饭票。"

    # 素织：(愣住) (脸瞬间爆红，头顶冒出蒸汽)
    # 使用 Flash 模拟脸瞬间爆红的冲击感
    show suzhi shirt shy at slight_shake
    with flash

    s "谁……谁要你赔一辈子！谁要吃你的饭票！"
    s "你……你这个笨蛋！不可理喻！"

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
    s "（……笨蛋。）"
    s "（这种话……怎么能随随便便说出口啊。）"
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

    l "这就是青春的试炼！接下来，我们将前往那个神秘的——“图书馆”。听说那里有一位“魔女”正在等待着命运的羔羊。"

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
    l "出来了吗？ 比我预想的时间要短了三分钟。"
    
    # 凌宁表情微调：带着一种看透红尘的微笑
    show lingning casual happy
    l "看来在那个封闭的空间里，你们并没有进行关于宇宙真理的深层探讨。"

    # 木子米：（满头黑线） 你在门口站岗干什么？
    # 木子米没有立绘，通常为第一人称视角或画外音
    m "（满头黑线） 你在门口站岗干什么？ 这反而更可疑好不好！ 路过的每个人都在看你！"

    # 凌宁：（优雅地摊手）
    show lingning casual pose
    l "我在守护你们的隐私。 要知道，青春的冲动就像暴风雨中的蝴蝶，脆弱而美丽。"
    l "若是被俗人打扰了这“清洗罪孽（指洗衣服）”的神圣仪式，岂不可惜？"

    # 素织：（脸还是红的，听到凌宁的话，额头又冒出了井字）
    # 在素织头上显示生气符号
    show icon_angry_mark at left:
        yoffset -350 # 调整符号位置到头顶
        xoffset 100
    with vpunch # 配合震动加强语气

    # 为了表现愤怒，虽然她是羞涩姿态，但语气是愤怒的
    s "凌宁！ 你再胡说八道，我就把你那天晚上敷面膜的照片发到新生群里！"

    hide icon_angry_mark # 隐藏生气符号

    # 凌宁：（脸色瞬间变得苍白，优雅崩塌）
    # 使用 casual surprised (惊讶/被吓到) 或 ashamed (羞愧)
    show lingning casual surprised with soft_shake
    
    l "唔！这……这是犯规的战术！"
    
    show lingning casual ashamed
    l "素织小姐，请务必手下留情！那是我身为贵族的最后尊严！"

    # (内心独白) 木子米： 看来，就算是贵族，也有怕被社会性死亡的时候。
    m "（看来，就算是贵族，也有怕被社会性死亡的时候。 不过…… 看着这两个人像小学生一样斗嘴。）"
    m "（这种感觉，居然还不赖。）"

    # 木子米： 行了，别贫了。 下一节课是什么？
    m "行了，别贫了。 下一节课是什么？"

    # 凌宁：（恢复正经，推了推不存在的眼镜）
    show lingning casual pose with dissolve
    l "没有课了。 但是，身为土木系的精英，我们有一个必须攻略的副本。"
    l "那就是—— 第十一节流通过程与物质交换中心。"

    # 木子米： 说人话。
    m "说人话。"

    # 凌宁： 食堂。 抢饭。
    show lingning casual happy
    l "食堂。 抢饭。"

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
    
    l "这……这不符合美学。 在如此拥挤的环境中进食，还要为了一个鸡腿而此时此刻，这有辱斯文。"
    l "我决定去买面包。"

    # 素织： （眼神犀利）
    # 使用 suzhi casual angry 表现气场全开 (假设此时已穿好外套或无视服装bug，使用常规立绘表达情绪)
    show suzhi casual angry at left with moveinleft

    s "（眼神犀利，盯着远处的“特色盖浇饭”窗口） 不行！ 为了下午的英语分级考试，必须吃米饭补充碳水。"
    s "凌宁你去看包占座。 木子米，你跟我走！"

    # 木子米： 哈？我也要去挤？
    m "哈？我也要去挤？"

    # 素织： （一把拽住木子米的袖子，气场全开）
    # 播放撞击声或接触声
    play audio audio.se_bump_sfx
    
    # 素织逼近
    show suzhi casual angry at center with move

    s "少废话！ 你是肉盾！ 我们要执行“钳形攻势”！" 
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
    s "……笨蛋。"
    s "这都要护住我……逞什么强"
    # 【演出效果：回到现实】
    # 恢复音量和噪音
    $ renpy.music.set_volume(1.0, delay=0.2, channel='music')
    play sound audio.se_market loop volume 0.8

    # 木子米：（听到声音，低头）
    m "（听到声音，低头） 你说啥？ 太吵了听不见！ "
    m "阿姨问你要什么菜！快喊！"

    # 素织：（回过神，脸一红）
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
    l "所以说，智者不入爱河，贵族不抢饭桌。 虽然我依然很饿，但我保持了风度。"

    # 素织：（戳着盘子里的土豆）
    # 表情切换为犹豫/羞涩
    show suzhi casual shy
    "（素织戳着盘子里的土豆，看了看木子米那副惨兮兮的样子）"
    
    pause 0.5
    
    s "……喂。"

    m "嗯？"

    # 素织夹肉动作
    # 播放一个小音效模拟夹菜/放碗里的声音
    play audio audio.se_bump 
    with soft_shake # 屏幕轻微震动表现动作迅速

    # 素织：（动作飞快地丢进木子米的碗里）
    # 恢复正常表情掩饰害羞，或者保持羞涩但嘴硬
    show suzhi casual normal 
    s "（夹起自己盘子里最大的一块牛肉，动作飞快地丢进木子米的碗里）" 
    s "我不喜欢吃太肥的。 帮你解决垃圾。 别多想。"

    # 木子米内心吐槽
    m "（看着碗里那块明明是半肥半瘦、口感最好的牛肉）"
    m "（这哪里肥了？这明明是极品好吗！素织同学，你的傲娇属性已经暴露无遗了啊！）"

    # 木子米：（抬头，坏笑）
    m "（抬头，坏笑） 哦？是吗？ 那既然是垃圾，我就勉为其难地……"

    # 素织：（瞪眼）
    show suzhi casual angry
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

    s "咳！咳咳！ 谁……谁有爱意了！"
    s "吃饭都堵不住你的嘴！ 变态！"

    # 凌宁：（看着两人，默默地把手里的面包捏扁了）
    # 表情切换为郁闷/死鱼眼
    show lingning casual depressed with dissolve
    
    l "（看着两人，默默地把手里的面包捏扁了）"
    l "我觉得…… 我应该在车底，不应该在这里。"
    
    # 柠檬味时刻
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
    l "（压低声音） 这就是知识的殿堂。 空气中都弥漫着墨水的芬芳。 我要去找几本关于西方建筑美学的书，陶冶一下情操。"

    # 木子米： 你是去找画册看图吧？
    m "你是去找画册看图吧？"

    # 素织： 我也去找几本专业书。
    s "我也去找几本专业书。 土木概论老师推荐的那几本，据说很难抢。"
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
    unknown "（眼神空洞，语速极快） 混凝土的坍落度……骨料的级配…… 不行……这个公式不对……"
    unknown "根据魔女的法则……这里应该加一点蜥蜴的尾巴…… 啊不对，是加减水剂……"

    # (内心独白) 木子米
    m "（……蜥蜴的尾巴？ 这家伙在说什么？ 这是土木系的学生？还是霍格沃茨的交换生？）"

    # 木子米：（小心翼翼地）
    m "（小心翼翼地） 那个……同学？ 你没事吧？书掉地上了。"

    # 神秘女生：（猛地抬头）
    # 播放惊悚或悬疑的小音效
    play music audio.bgm_stealth_happy fadein 0.5 # 切换BGM表现古怪氛围

    unknown "（猛地抬头，眼镜反过一道寒光） （声音阴森） 观测者……？"
    unknown "你看到了？ 你看到了我的“禁忌炼成阵”？"

    # 木子米：（看了一眼地上的书堆）
    m "（看了一眼地上的书堆，确实摆得像个魔法阵） 不……我只是看到你在乱扔公物。"

    # 神秘女生：（推了推眼镜，突然换了一副表情，变得像小动物一样可怜）
    # 因为没有特定表情差分，通过震动或位置移动表现情绪变化
    show baimoxuan coat crazy at center:
        yoffset 0
        linear 0.2 yoffset 10
    
    unknown "（推了推眼镜，突然换了一副表情，变得像小动物一样可怜） 呜……学长？还是同级？"
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
    b "我是为了……建造巴比伦塔！"
    b "通往神域的塔！ 谢谢你，巨人族的好心人。 吾名 {color=#a3a3a3}白墨萱{/color} 。 你可以称呼我为——“结构力学的魔女”。"

    # 木子米：（满头黑线）
    m "（满头黑线） 我是木子米。 建议你少看点轻小说，多睡会觉。 你的黑眼圈都快掉到下巴了。"

    # 白墨萱：（突然凑近）
    show baimoxuan coat crazy:
        ease 0.3 zoom 1.2 yoffset 50 # 镜头拉近效果

    b "（突然凑近木子米，鼻子耸动了一下） 嗯？ 这股味道…… 是草莓牛奶？"
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

    s "木。子。米。"

    # 木子米：（僵硬地回头）
    # 屏幕剧烈震动一下
    with vpunch
    m "（僵硬地回头） 嗨……素织。 你听我解释，这是……"

    # 素织：（目光在白墨萱和木子米之间来回扫视）
    s "（目光在白墨萱和木子米之间来回扫视，看着白墨萱抓着木子米衣角的手）" 
    s "我就离开十分钟。 你就开始勾搭……奇怪的小学妹了？ 还真是“乐于助人”啊。"

    # 白墨萱：（看着素织，歪了歪头）
    # 白墨萱完全读不懂空气
    b "（看着素织，歪了歪头） 哦？ 正宫的气场？ 防御力很强，但攻击性过高。 容易产生裂缝（指感情破裂）。"
    b "需要加固。"

    # 素织：（额头青筋暴起）
    # 加上生气符号
    show icon_angry_mark at left:
        xoffset 100 yoffset -350
    with vpunch

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
    
    b "（挥着小手，面无表情） 走好。 作为报酬，我会为你祈祷……" 
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
    with soft_shake # 手机震动效果

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
    
    centered "{size=60}第五章 完{/size}"

    return