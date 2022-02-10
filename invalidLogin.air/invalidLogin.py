# -*- encoding=utf8 -*-
__author__ = "sampadrout"

from airtest.core.api import *
from airtest.report.report import *
import os
import requests

ST.LOG_FILE = "log.txt"
set_logdir(r'invalidLogin.air/log')

auto_setup(__file__)

PWD = os.path.dirname(__file__)
PKG = "com.gsn.worldwinner"

APK_URL = "https://cdn.skillprod.worldwinner.com/AppPackages/Android/WorldWinner.apk"
APK_FILE = 'WorldWinner.apk'
requests.urlretrieve(APK_URL, APK_FILE)

APK = os.path.join(PWD, APK_FILE)

if PKG not in device().list_app():
    install(APK_FILE)
else:
	stop_app("com.gsn.worldwinner")

clear_app("com.gsn.worldwinner")

start_app("com.gsn.worldwinner")
sleep(120.0)
wait(Template(r"tpl1643712726718.png", record_pos=(-0.392, 0.391), resolution=(1080, 2280)))
touch(Template(r"tpl1643712726718.png", record_pos=(-0.392, 0.391), resolution=(1080, 2280)))
sleep(2.0)
wait(Template(r"tpl1643712777341.png", record_pos=(-0.003, 0.646), resolution=(1080, 2280)))
touch(Template(r"tpl1643712777341.png", record_pos=(-0.003, 0.646), resolution=(1080, 2280)))
sleep(2.0)
wait(Template(r"tpl1643712845653.png", record_pos=(-0.006, 0.083), resolution=(1080, 2280)))
touch(Template(r"tpl1643712845653.png", record_pos=(-0.006, 0.083), resolution=(1080, 2280)))
sleep(2.0)
wait(Template(r"tpl1643732972527.png", record_pos=(0.356, -0.722), resolution=(1080, 2280)))
touch(Template(r"tpl1643712871928.png", record_pos=(0.359, -0.724), resolution=(1080, 2280)))
wait(Template(r"tpl1643732993465.png", record_pos=(0.005, -0.041), resolution=(1080, 2280)))
touch(Template(r"tpl1643799280524.png", record_pos=(0.003, -0.087), resolution=(720, 1560)))

text("test")
wait(Template(r"tpl1643733007522.png", record_pos=(0.012, 0.181), resolution=(1080, 2280)))
touch(Template(r"tpl1643799296680.png", record_pos=(0.003, 0.146), resolution=(720, 1560)))

text("pwd")

touch(Template(r"tpl1643799846267.png", record_pos=(0.25, 0.493), resolution=(720, 1560)))

assert_exists(Template(r"tpl1643713169664.png", record_pos=(0.071, 0.29), resolution=(1080, 2280)), "Please fill in the test point.")

stop_app("com.gsn.worldwinner")
clear_app("com.gsn.worldwinner")
uninstall("com.gsn.worldwinner")

simple_report(__file__,logpath=True,logfile=r"invalidLogin.air/log/log.txt",output=r"invalidLogin.air/log/report.html")