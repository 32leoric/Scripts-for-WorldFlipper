# -*- encoding=utf8 -*-
__author__ = "32yy"

from airtest.core.api import *

auto_setup(__file__)

times = 3  # 这是单次运行的循环次数

"""
使用网易Airtest实现的弹射世界脚本，当前是国服圣诞节版本，不是国服就不要问我为什么运行不了了。

脚本默认使用宝石回体，这个以后会优化。脚本导致的任何封号/少钻/其他问题，一律与32无关。

开游戏->选图->开房->招募->开->再开一次，遇到没关注的一律给关注

房主长时间不操作会被解散，所以每5s点个赞，不喜欢点赞的可以改成别的，把你想要的表情名字改成emoji.png就行。当然仅限系统给的四种表情。

关于自选要打的领主或者自动识别每日up，懒得截图就还没做，现在只支持打猫头鹰


"""
pic_folder = 'pic/'  #这是图片路径


def game_start():
    touch(exists(Template(r"pic/弹射世界app图标.png", record_pos=(-0.174, -0.221), resolution=(810, 1440))))

    touch(wait(Template(r"pic/点击开始.png", rgb=True, record_pos=(-0.015, 0.658), resolution=(810, 1440)), timeout=600,
               interval=0.1))

    if exists(Template(r"pic/好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440))):
        touch(Template(r"pic/好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))


def buy_energy():
    touch(Template(r"pic/星石买体力.png", threshold=0.8, rgb=True, record_pos=(-0.169, 0.391), resolution=(810, 1440)))
    touch(Template(r"pic/好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))
    touch(Template(r"pic/好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))


def enter_mission():
    touch(wait(Template(r"pic/领主战.png", record_pos=(0.353, 0.646), resolution=(810, 1440))))

    while not exists(Template(r"pic/猫头鹰图标.png", record_pos=(-0.193, 0.431), resolution=(810, 1440))):
        swipe((400, 1200), (400, 600), duration=2)

    sleep(2.0)
    touch(Template(r"pic/猫头鹰图标.png", record_pos=(-0.193, 0.431), resolution=(810, 1440)))

    touch(Template(r"pic/猫头鹰领主战.png", record_pos=(0.084, -0.251), resolution=(810, 1440)))


def kai_fang():
    touch(Template(r"pic/多人游戏.png", record_pos=(-0.063, 0.36), resolution=(810, 1440)))
    if exists(Template(r"pic/领主加成点数询问.png", record_pos=(0.001, -0.094), resolution=(810, 1440))):
        touch(Template(r"pic/是.png", record_pos=(0.227, 0.256), resolution=(810, 1440)))


def mission_process():
    if exists(Template(r"pic/招募选项（全黑）.png", rgb=True, record_pos=(0.0, 0.189), resolution=(810, 1440))):
        touch(Template(r"pic/招募.png", rgb=True, record_pos=(-0.007, 0.262), resolution=(810, 1440)))
        if random_member == 1:
            if exists(Template(r"pic/随机招募（否）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.201, 0.159), resolution=(810, 1440))):
                touch(Template(r"pic/随机招募（否）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.201, 0.159), resolution=(810, 1440)))
            
        else:
            if exists(Template(r"pic/随机招募（是）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.209, 0.159),
                       resolution=(810, 1440))):
                touch(Template(r"pic/随机招募（是）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.209, 0.159),
                       resolution=(810, 1440)))
        touch(Template(r"pic/开始招募.png", record_pos=(0.235, 0.389), resolution=(810, 1440)))

    if exists(Template(r"pic/橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        sleep(10.0)

    while not exists(Template(r"pic/橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        sleep(5.0)
        touch(Template(r"pic/发表情.png", record_pos=(-0.4, -0.7), resolution=(810, 1440)))
        touch(Template(r"pic/赞.png", record_pos=(-0.062, -0.706), resolution=(810, 1440)))  # 可以改成你想要的
        if not exists(Template(r"pic/灰色挑战按钮.png", rgb=True, record_pos=(-0.002, 0.4), resolution=(810, 1440))):
            break

    if exists(Template(r"pic/橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        touch(Template(r"pic/橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440)))

    touch(wait(Template(r"pic/继续.png", threshold=0.9, rgb=True, record_pos=(0.001, 0.781), resolution=(810, 1440)),
               timeout=300, interval=1))

    sleep(1.0)

    touch(wait(Template(r"pic/继续.png", threshold=0.9, rgb=True, record_pos=(0.001, 0.781), resolution=(810, 1440)),
               timeout=20, interval=1))

    sleep(1.0)

    touch(wait(Template(r"pic/继续.png", threshold=0.9, rgb=True, record_pos=(0.001, 0.781), resolution=(810, 1440)),
               timeout=20, interval=1))

    sleep(1.0)

    while exists(Template(r"pic/关注.png", rgb=True, record_pos=(0.301, 0.312), resolution=(810, 1440))):
        touch(Template(r"pic/关注.png", rgb=True, record_pos=(0.301, 0.312), resolution=(810, 1440)))
        sleep(2.0)
        touch(Template(r"pic/好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))
        sleep(2.0)

    touch(wait(Template(r"pic/返回房间.png", rgb=True, record_pos=(0.195, 0.779), resolution=(810, 1440)), timeout=20))

    if exists(Template(r"pic/回复药小.png", record_pos=(-0.309, -0.207), resolution=(810, 1440))):
        buy_energy()


if exists(Template(r"pic/弹射世界app图标.png", record_pos=(-0.174, -0.221), resolution=(810, 1440))):
    game_start()

enter_mission()

kai_fang()

while times > 0:
    times -= 1
    mission_process()

print("执行完毕！")


