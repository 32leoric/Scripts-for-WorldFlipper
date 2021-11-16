# -*- encoding=utf8 -*-
__author__ = "32yy"

import sys
from airtest.core.api import *

auto_setup(__file__)

t = 0 #计数，看看刷了几次
target = "多人猫头鹰"  #你要刷的目标，格式人数+目标，举例：单人雪人王，多人猫头鹰，多人螃蟹
pic_folder = "pic/"   #基础图片目录
random_member = False #多人模式是否招野人，默认不要，要招野人改True
use_ruby_or_not = True  #是否用钻石买体力，可以用改True

#以下是目前支持刷的内容
single_player_mission = ["雪人王"]
multi_player_mission = ["猫头鹰", "螃蟹"]

multi_player = "多人" in target

def touch_if_exists(p, th=0.8):
    if exists(Template(p, threshold=th, rgb=True, record_pos=(-0.441, -0.636), resolution=(810, 1440))):
        touch(Template(p, threshold=th, rgb=True, record_pos=(-0.441, -0.636), resolution=(810, 1440)))
        
def game_start():
    touch(exists(Template(pic_folder + r"弹射世界app图标.png", record_pos=(-0.174, -0.221), resolution=(810, 1440))))

    touch(wait(Template(pic_folder + r"点击开始.png", rgb=True, record_pos=(-0.015, 0.658), resolution=(810, 1440)), timeout=600,
               interval=0.1))

    if exists(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440))):
        touch(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))

def buy_energy(use_ruby = False):
    if use_ruby == True:
        touch(Template(pic_folder + r"星石买体力.png", threshold=0.8, rgb=True, record_pos=(-0.169, 0.391), resolution=(810, 1440)))
        sleep(1.0)
        touch(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))
        sleep(1.0)
        touch(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))
        
def enter_mission(target):
    
    if "多人" in target:    
        touch(wait(Template(pic_folder + r"领主战.png", record_pos=(0.353, 0.646), resolution=(810, 1440)), timeout = 60))
        target = target.strip("多人")
        
    else:
        touch(wait(Template(pic_folder + r"活动.png", record_pos=(-0.344, 0.648), resolution=(810, 1440)), timeout = 60))
        target = target.strip("单人")
        
    target = target + '/' + target
    while not exists(Template(pic_folder + target + '1.png', record_pos=(-0.193, 0.431), resolution=(810, 1440))):
        swipe((400, 1200), (400, 600), duration=2)

    sleep(2.0)
    touch(Template(pic_folder + target + '1.png', record_pos=(-0.193, 0.431), resolution=(810, 1440)))
    sleep(1.0)
    touch(Template(pic_folder + target + '2.png', record_pos=(0.084, -0.251), resolution=(810, 1440)))
    
def kai_fang():
    touch(Template(pic_folder + r"多人游戏.png", record_pos=(-0.063, 0.36), resolution=(810, 1440)))
    if exists(Template(pic_folder + r"领主加成点数询问.png", record_pos=(0.001, -0.094), resolution=(810, 1440))):
        touch(Template(pic_folder + r"是.png", record_pos=(0.227, 0.256), resolution=(810, 1440)))
        
def call_members(random_member):
    touch(Template(pic_folder + r"招募选项（全黑）.png", rgb=True, record_pos=(0.0, 0.189), resolution=(810, 1440)))
    touch(Template(pic_folder + r"招募.png", rgb=True, record_pos=(-0.007, 0.262), resolution=(810, 1440)))
    if random_member:
        if exists(Template(pic_folder + r"随机招募（否）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.201, 0.159), resolution=(810, 1440))):
            touch(Template(pic_folder + r"随机招募（否）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.201, 0.159), resolution=(810, 1440)))
            
    else:
        if exists(Template(pic_folder + r"随机招募（是）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.209, 0.159),
                       resolution=(810, 1440))):
            touch(Template(pic_folder + r"随机招募（是）.png", threshold=0.9500000000000002, rgb=True, target_pos=1, record_pos=(-0.209, 0.159),
                       resolution=(810, 1440)))
    touch(Template(pic_folder + r"开始招募.png", record_pos=(0.235, 0.389), resolution=(810, 1440)))

def fail_process(target):
    touch(Template(pic_folder + r"返回主菜单.png", record_pos=(-0.254, 0.821), resolution=(810, 1440)))
    enter_mission(target)    
    
def multi_mission_process(target):
    
    if exists(Template(pic_folder + r"橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        if exists(Template(pic_folder + r"空位.png", record_pos=(0.321, -0.426), resolution=(810, 1440))):
            sleep(10.0)

    while not exists(Template(pic_folder + r"橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        sleep(5.0)
        if not exists(Template(pic_folder + r"灰色挑战按钮.png", rgb=True, record_pos=(-0.002, 0.4), resolution=(810, 1440))):
            break   
        touch(Template(pic_folder + r"发表情.png", record_pos=(-0.4, -0.7), resolution=(810, 1440)))
        touch(Template(pic_folder + r"赞.png", record_pos=(-0.062, -0.706), resolution=(810, 1440)))  # 可以改成你想要的

    if exists(Template(pic_folder + r"橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440))):
        if exists(Template(pic_folder + r"空位.png", record_pos=(0.321, -0.426), resolution=(810, 1440))):
            sleep(10.0)
        touch(Template(pic_folder + r"橙色挑战按钮.png", rgb=True, record_pos=(0.023, 0.614), resolution=(810, 1440)))
        
    touch_if_exists(pic_folder + r"自动（关）.png")
    touch_if_exists(pic_folder + r"技能自动（关）.png")

    while not exists(Template(pic_folder + r"返回房间.png", record_pos=(0.201, 0.78), resolution=(810, 1440))):        
        temp = 5
        while temp > 0:
            touch((400, 1350))
            sleep(0.5)
            temp -= 1
        
    while exists(Template(pic_folder + r"关注.png", rgb=True, record_pos=(0.301, 0.312), resolution=(810, 1440))):
        touch(Template(pic_folder + r"关注.png", rgb=True, record_pos=(0.301, 0.312), resolution=(810, 1440)))
        sleep(1.0)
        touch(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(0.227, 0.252), resolution=(810, 1440)))
        sleep(1.0)

    touch(wait(Template(pic_folder + r"返回房间.png", rgb=True, record_pos=(0.195, 0.779), resolution=(810, 1440)), timeout=20))

    if exists(Template(pic_folder + r"没体力了.png", record_pos=(0.012, -0.64), resolution=(810, 1440))):
        buy_energy(use_ruby = use_ruby_or_not)
        
def single_mission_process(target):
    touch(Template(pic_folder + r"单人挑战.png", record_pos=(0.007, 0.63), resolution=(810, 1440)))
    sleep(10.0)
    touch_if_exists(pic_folder + r"自动（关）.png")
    touch_if_exists(pic_folder + r"自动（一倍速）.png", th = 0.95)
    touch_if_exists(pic_folder + r"技能自动（关）.png")

    while not exists(Template(pic_folder + r"再次挑战.png", record_pos=(0.201, 0.78), resolution=(810, 1440))):        
        touch_if_exists(pic_folder + r"继续.png")
        if exists(Template(pic_folder + r"放弃.png", threshold=0.8, rgb=True, record_pos=(-0.441, -0.636), resolution=(810, 1440))):
            touch(Template(pic_folder + r"放弃.png", threshold=0.8, rgb=True, record_pos=(-0.441, -0.636), resolution=(810, 1440)))
            touch(Template(pic_folder + r"好.png", threshold=0.8, rgb=True, record_pos=(-0.441, -0.636), resolution=(810, 1440)))
            fail_process(target)
            failed = 1
            break
        touch((600, 900))
        sleep(0.5)
    if failed == 1:
        failed = 0
        return
    touch(Template(pic_folder + r"再次挑战.png", record_pos=(0.201, 0.78), resolution=(810, 1440)))
    if exists(Template(pic_folder + r"没体力了.png", record_pos=(0.012, -0.64), resolution=(810, 1440))):
        buy_energy(use_ruby = use_ruby_or_not)

####################################################

if target.strip("单人") not in single_player_mission and target.strip("多人") not in multi_player_mission:
    print("猫猫没听懂你要打啥呢")

if exists(Template(pic_folder + r"弹射世界app图标.png", record_pos=(-0.174, -0.221), resolution=(810, 1440))):
    game_start()

enter_mission(target)

if multi_player:
    kai_fang()
    call_members(random_member)

while True:
    if multi_player:
        multi_mission_process(target)
    else:
        single_mission_process(target)
        
    t += 1

print("执行完毕！")
           
print(t)
