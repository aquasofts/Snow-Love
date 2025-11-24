# ==========================================
# 主界面特效定义
# ==========================================

# 1. 背景缓慢平移特效
transform main_menu_bg_pan:
    xalign 0.5 yalign 0.5
    linear 30.0 xalign 0.45
    linear 30.0 xalign 0.55
    repeat

# 2. 标题文字入场特效
transform title_fade_in:
    alpha 0.0 yoffset -30
    easein 2.0 alpha 1.0 yoffset 0

# 3. 看板娘呼吸特效
transform character_breathing:
    yalign 1.0 xalign 0.15
    zoom 1.0
    easein 2.0 zoom 1.005
    easeout 2.0 zoom 1.0
    repeat

# 4. 按钮悬停特效 (柔和缩放)
transform yuzu_hover_soft:
    on idle:
        easein 0.2 zoom 1.0 alpha 0.95
    on hover:
        easein 0.2 zoom 1.05 alpha 1.0

# 5. 按钮入场
transform button_slide_in_elastic(delay_time):
    xoffset 200 alpha 0.0
    pause delay_time
    easein_back 0.6 xoffset 0 alpha 0.9

# ==========================================
# 屏幕：Main Menu
# ==========================================
screen main_menu():

    tag menu

    # --- 1. 背景层 ---
    add "images/bg/school_gate.jpg":
        fit "cover"
        at main_menu_bg_pan

    # 稍微加一点亮色蒙版，让画面更通透
    add Solid("#ffffff20") 

    # --- 2. [修改] 装饰层 (枫叶) ---
    # 图标改为 🍂，颜色改为橙红色 (#ff9800)
    add SnowBlossom(Text("🍂", color="#ff9800", size=25), count=15, border=50, xspeed=20, yspeed=60, start=5)

    # --- 3. 角色层 ---
    add "suzhi casual normal":
        at character_breathing

    # --- 4. UI 层 (右侧布局) ---
    vbox:
        xalign 0.92
        yalign 0.55
        spacing 20

        # --- 标题部分 ---
        text "雪 之 恋":
            font "gui/font/MaShanZheng-Regular.ttf"
            size 160
            color "#ffffff"
            # 保持之前的强发光描边
            outlines [(6, "#26c6da", 0, 0), (4, "#4dd0e1", 2, 2), (2, "#ffffff", 0, 0)]
            text_align 1.0
            xalign 1.0
            at title_fade_in

        null height 60

        # --- 菜单按钮组 ---
        
        # 1. 开始游戏
        button:
            style "yuzu_mm_button"
            action Start()
            at [button_slide_in_elastic(0.2), yuzu_hover_soft]
            text "开始游戏" style "yuzu_mm_text"

        # 2. 读取进度
        button:
            style "yuzu_mm_button"
            action ShowMenu("load")
            at [button_slide_in_elastic(0.3), yuzu_hover_soft]
            text "读取进度" style "yuzu_mm_text"

        # 3. 环境设置
        button:
            style "yuzu_mm_button"
            action ShowMenu("preferences")
            at [button_slide_in_elastic(0.4), yuzu_hover_soft]
            text "环境设置" style "yuzu_mm_text"
        
        # 4. 关于
        button:
            style "yuzu_mm_button"
            action ShowMenu("about")
            at [button_slide_in_elastic(0.5), yuzu_hover_soft]
            text "关于作品" style "yuzu_mm_text"

        # 5. 退出
        button:
            style "yuzu_mm_button_quit"
            action Quit(confirm=not main_menu)
            at [button_slide_in_elastic(0.6), yuzu_hover_soft]
            text "退出游戏" style "yuzu_mm_text_quit"

# ==========================================
# 样式定义
# ==========================================

style yuzu_mm_button:
    xsize 300
    ysize 70
    xalign 1.0
    
    # [修改] 使用 Solid 生成纯白背景
    # #fffffff0 是非常高不透明度的白色
    background Frame(Solid("#fffffff0"), 10, 10)
    # 悬停时完全不透明纯白
    hover_background Frame(Solid("#ffffff"), 10, 10)

    padding (0, 0) 

style yuzu_mm_button_quit is yuzu_mm_button:
    # 退出按钮带一点点淡红色调的白
    background Frame(Solid("#fff0f0f0"), 10, 10)
    hover_background Frame(Solid("#ffebee"), 10, 10)

style yuzu_mm_text:
    font "gui/font/MiSans-Bold.ttf"
    size 38
    # 文字颜色保持蓝灰色，配合白色背景很清晰
    color "#546e7a"
    hover_color "#26c6da"
    xalign 0.5
    yalign 0.5
    text_align 0.5

style yuzu_mm_text_quit is yuzu_mm_text:
    color "#e57373"
    hover_color "#d32f2f"