import cocos


# 背景层
class Game_BG(cocos.layer.Layer):
    def __init__(self):
        super(Game_BG, self).__init__()
        d_width, d_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite('index.png')
        background.position = d_width // 2, d_height // 2
        self.add(background)


# 自定义菜单类
class main_menu(cocos.menu.Menu):
    def __init__(self):
        super(main_menu, self).__init__()

        # 也可以改变图片项的大小
        # 改变字体
        self.font_item['font_size'] = 66
        # 选中时
        self.font_item_selected['font_size'] = 66
        # 改变颜色 rgba
        self.font_item['color'] = (255, 255, 255, 25)
        # 选中时
        self.font_item_selected['color'] = (25, 255, 255, 255)

        menu_start = cocos.menu.ImageMenuItem('start.png', self.menu_start_callback)
        menu_setting = cocos.menu.ImageMenuItem('setting.png', self.menu_setting_callback)
        help_setting = cocos.menu.ImageMenuItem('help.png', self.menu_help_callback)
        # 创建菜单（添加项的列表，自定义布局位置）
        self.create_menu([menu_start, menu_setting, help_setting],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(500, 339), (500, 220), (500, 100)]),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out())

    def menu_start_callback(self):
        print("开始游戏")

    def menu_help_callback(self):
        pass

    def menu_setting_callback(self):
        pass


