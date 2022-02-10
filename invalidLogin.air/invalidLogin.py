# -*- encoding=utf8 -*-
__author__ = "sampadrout"

from airtest.core.api import *
from airtest.report.report import *
from tqdm import tqdm
import requests
import os

ST.LOG_FILE = "log.txt"
set_logdir(r'log')

auto_setup(__file__)

PWD = os.path.dirname(__file__)
PKG = "com.gsn.worldwinner"

APK_URL = 'https://cdn.skillprod.worldwinner.com/AppPackages/Android/WorldWinner.apk'
APK = PWD+'/app/WorldWinner.apk'
# stream true is required
response = requests.get(APK_URL, stream=True)
# total file size
t = int(response.headers.get('content-length', 0))
block_size = 1024**2 #1 Mbit
progress_bar = tqdm(total=t, unit='iB', unit_scale=True)
with open(APK, 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()
if ( t != 0 ) and ( progress_bar.n != t ) : print("ERROR downloading file!")

if PKG not in device().list_app():
    install(APK)
else:
	stop_app("com.gsn.worldwinner")
	clear_app("com.gsn.worldwinner")
	uninstall("com.gsn.worldwinner")
	install(APK)

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

simple_report(__file__,logpath=True,logfile=r"log/log.txt",output=r"log/report.html")