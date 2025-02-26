# =yright: reportUnusedImport=false
# pyright: reportUndefinedVariable=false
import json
import os
import time
import datetime
import socket
import subprocess
import uuid
import re
import html
from time import sleep, strftime
from datetime import date, datetime
from pystyle import Colors, Colorate, Center, Anime, Box, _MakeColors
from pystyle import Write, Colors
from termcolor import colored
from weakref import proxy
Defaut="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue      # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"
xduong = '\033[1;94m'
do2 = '\033[1;91m'
tim2 = '\033[0;95m'
xl = '\033[1;32m'
vang3 = '\033[1;93m'
den = '\033[1;47;30m'
xn2 = '\033[1;96m'
do = '\033[1;31m'
hong = '\033[1;35m'
luc = '\033[1;92m'
trang = '\033[1;97m'
tim = '\033[0;35m'
vang2 = '\033[1;33m'
gray = '\033[0;90m'
bblack = '\033[1;30m',
bred = '\033[1;31m',
bgreen = '\033[1;32m',
byellow = '\033[1;33m',
bblue = '\033[1;34m',
bpurple = '\033[1;35m',
bcyan = ' \033[1;36m',
bwhite = '\033[1;37m',
lamd = "\033[1;34m"
orange = "\033[1;33m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
BLUE_DARK = '\033[34m'
BLUE_LIGHT = '\033[36m'
RESET = '\033[0m'
#========màu=========
black_to_white = ["m;m;m"]
black_to_red = ["m;0;0"]
black_to_green = ["0;m;0"]
black_to_blue = ["0;0;m"]

white_to_black = ["n;n;n"]
white_to_red = ["255;n;n"]
white_to_green = ["n;255;n"]
white_to_blue = ["n;n;255"]

red_to_black = ["n;0;0"]
red_to_white = ["255;m;m"]
red_to_yellow = ["255;m;0"]
red_to_purple = ["255;0;m"]

green_to_black = ["0;n;0"]
green_to_white = ["m;255;m"]
green_to_yellow = ["m;255;0"]
green_to_cyan = ["0;255;m"]

blue_to_black = ["0;0;n"]
blue_to_white = ["m;m;255"]
blue_to_cyan = ["0;m;255"]
blue_to_purple = ["m;0;255"]

yellow_to_red = ["255;n;0"]
yellow_to_green = ["n;255;0"]

purple_to_red = ["255;0;n"]
purple_to_blue = ["n;0;255"]

cyan_to_green = ["0;255;n"]
cyan_to_blue = ["0;n;255"]
dynamic_colors = [
        black_to_white, black_to_red, black_to_green, black_to_blue,
        white_to_black, white_to_red, white_to_green, white_to_blue,

        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,

        yellow_to_red, yellow_to_green,
        purple_to_red, purple_to_blue,
        cyan_to_green, cyan_to_blue
    ]

red_to_blue = _MakeColors._makergbcol(red_to_purple, purple_to_blue)
red_to_green = _MakeColors._makergbcol(red_to_yellow, yellow_to_green)

green_to_blue = _MakeColors._makergbcol(green_to_cyan, cyan_to_blue)
green_to_red = _MakeColors._makergbcol(green_to_yellow, yellow_to_red)

blue_to_red = _MakeColors._makergbcol(blue_to_purple, purple_to_red)
blue_to_green = _MakeColors._makergbcol(blue_to_cyan, cyan_to_green)

for color in dynamic_colors:
    _col = 20000000
    reversed_col = 22000000
    dbl_col = 2000000
    dbl_reversed_col = 22000000

    content = color[0]
    color.pop(0)

    for _ in range(12):
        if 'm' in content:
            result = content.replace('m', str(_col))
            color.append(result)
        elif 'n' in content:
            result = content.replace('n', str(reversed_col))
            color.append(result)
        _col += 2000000
        reversed_col -= 22000000

    for _ in range(12):
        if 'm' in content:
            result = content.replace('m', str(dbl_reversed_col))
            color.append(result)
        elif 'n' in content:
            result = content.replace('n', str(dbl_col))
            color.append(result)
        dbl_col += 2000000
        dbl_reversed_col -= 22000000

try:
	import re,requests,os,sys,random
except:
	os.system("pip install requests")
	import re,requests,os,sys,random

try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box

try:
    from bs4 import BeautifulSoup
except:
     os.system("pip install bs4")

try:
    from termcolor import colored
except:
    os.system("pip install termcolor")
os.system("pip install git")        

    # ====Màu====
BLUE_LIGHT = '\033[38;5;159m'  # Xanh dương rất nhạt
BLUE_SOFT = '\033[38;5;123m'   # Xanh dương nhạt
BLUE_MEDIUM = '\033[38;5;75m'  # Xanh dương vừa
BLUE_STRONG = '\033[38;5;33m'  # Xanh dương đậm
BLUE_DARK = '\033[38;5;18m'
banner = f"""
{BLUE_LIGHT}██╗  ██╗██╗███╗   ██╗██████╗  ██████╗███████╗██████╗ ████████╗███████╗
{BLUE_SOFT}██║ ██╔╝██║████╗  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝╚══███╔╝
{BLUE_MEDIUM}█████╔╝ ██║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝   ██║     ███╔
{BLUE_STRONG}██╔═██╗ ██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔═══╝    ██║    ███╔╝
{BLUE_DARK}██║  ██╗██║██║ ╚████║██████╔╝╚██████╗███████╗██║        ██║   ███████╗
{RESET}╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝╚══════╝╚═╝        ╚═╝   ╚══════╝
                   ╔════════════════════════════╗ {xn2}
                      [1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook: Huukhang.info\t {trang}        
                      Telegram: @nhk1510z\t           {hong}
                      Gmail   : huukhangz.info\t              {do2}
                   ╚════════════════════════════╝  {vang3}
"""
thanhxau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanhdep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➽ "
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➽"
banner1 = fr"""

 ██ ▄█▀ ▄████▄  ▓█████  ▄████▄   ██▓███  ▄▄▄█████▓▒███████▒
 ██▄█▒ ▒██▀ ▀█  ▓█   ▀ ▒██▀ ▀█  ▓██░  ██▒▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░
▓███▄░ ▒▓█    ▄ ▒███   ▒▓█    ▄ ▓██░ ██▓▒▒ ▓██░ ▒░░ ▒ ▄▀▒░ 
▓██ █▄ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▄█▓▒ ▒░ ▓██▓ ░   ▄▀▒   ░
▒██▒ █▄▒ ▓███▀ ░░▒████▒▒ ▓███▀ ░▒██▒ ░  ░  ▒██▒ ░ ▒███████▒
▒ ▒▒ ▓▒░ ░▒ ▒  ░░░ ▒░ ░░ ░▒ ▒  ░▒▓▒░ ░  ░  ▒ ░░   ░▒▒ ▓░▒░▒
░ ░▒ ▒░  ░  ▒    ░ ░  ░  ░  ▒   ░▒ ░         ░    ░░▒ ▒ ░ ▒
░ ░░ ░ ░           ░   ░        ░░         ░      ░ ░ ░ ░ ░
░  ░   ░ ░         ░  ░░ ░                          ░ ░    
       ░               ░                          ░        
                  |_нãy_вấм_хυốɴɢ_dòɴɢ_|
"""

red_to_green = Colors.red_to_green
green_to_blue = Colors.green_to_blue
blue_to_red = Colors.blue_to_red
rainbow = _MakeColors._makerainbow(
    red_to_green, green_to_blue, blue_to_red)
for _col in (
        red_to_blue, red_to_green,
        green_to_blue, green_to_red,
        blue_to_red, blue_to_green
    ): dynamic_colors.append(_col)
dynamic_colors.append(rainbow)
Anime.Fade(Center.Center(banner1), rainbow, Colorate.Vertical, enter=True)
#========banner2============
def banner2():  
    # ====Màu====
    BLUE_LIGHT = '\033[38;5;159m'  # Xanh dương rất nhạt
    BLUE_SOFT = '\033[38;5;123m'   # Xanh dương nhạt
    BLUE_MEDIUM = '\033[38;5;75m'  # Xanh dương vừa
    BLUE_STRONG = '\033[38;5;33m'  # Xanh dương đậm
    BLUE_DARK = '\033[38;5;18m'    # Xanh dương đậm tối

    # ====Cấu hình====
    data_machine = []  # Giữ nguyên biến này nếu bạn dùng sau này
    time = datetime.now().strftime("%H:%M")
    today = date.today()
    now = datetime.now()
    thu = now.strftime("%A")
    ngay_hom_nay = now.strftime("%d")
    thang_nay = now.strftime("%m")
    nam_ = now.strftime("%Y")
    lines = [
        # ASCII art hiện tại
        ("██╗  ██╗██╗███╗   ██╗██████╗  ██████╗███████╗██████╗ ████████╗███████╗\n", BLUE_LIGHT),
        ("██║ ██╔╝██║████╗  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔==╝╚══███╔╝\n", BLUE_LIGHT),
        ("█████╔╝ ██║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝   ██║     ███╔╝\n", BLUE_MEDIUM),
        ("██╔═██╗ ██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔═══╝    ██║    ███╔╝\n", BLUE_STRONG),
        ("██║  ██╗██║██║ ╚████║██████╔╝╚██████╗███████╗██║        ██║   ███████╗\n", BLUE_DARK),
        ("╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝╚══════╝╚═╝        ╚═╝   ╚══════╝\n", BLUE_LIGHT),
        (f"➽ Facebook:NguyenHuuKhang.Profile           ➩ Gmail:huukhangz.info\n", BLUE_LIGHT),
        (f"➽ Telegram:@nhk1510z                        ➩ Ngày:{ngay_hom_nay}/{thang_nay}/{nam_}|{time}\n", BLUE_STRONG),
        ('====================================================================== \n', BLUE_STRONG),
    ]

    # In từng dòng với Write.Print
    for text, color in lines:
        Write.Print(text, color, interval=0.0001)

def git():
    while True:
        banner2()
        print(f"Chọn [")
        print(f"Chọn 2 để ăn ngon (file)")
        chon = input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m')
        if chon == "1":
            os.system("clear")
            banner2()
            print("Ngủ ngon")
            break
        elif chon == "2":
            os.system("clear")
            banner2()
            exec(requests.get('https://raw.githubusercontent.com/huukhang15/Kcepttzz/master/new.py').text, globals())
            break
git()
