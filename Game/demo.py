from Sence import index
import cocos


# 初始化导演
cocos.director.director.init(width=640, height=480, caption="dog and cat")

# 将背景层  添加到场景
bg = index.Game_BG()
main_scence = cocos.scene.Scene(bg)
# 添加菜单
mainmenu = index.main_menu()
main_scence.add(mainmenu)
# 启动场景
cocos.director.director.run(main_scence)
