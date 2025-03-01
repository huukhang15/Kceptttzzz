import requests
import time
import subprocess
import random
import re
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pystyle import Write, Colors
import subprocess, sys; [subprocess.check_call([sys.executable, "-m", "pip", "install", lib]) for lib in ["requests", "selenium", "pystyle"] if __import__(lib, globals(), locals(), [], 0) is None]
from datetime import datetime
import unicodedata
#========= Cấu hình link =========#
TIKTOK_URL = "https://www.tiktok.com/"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

class TikTokLogin:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "referer": "https://www.tiktok.com/",
            "authority": "www.tiktok.com"
        }

    def login_with_cookie(self, cookies_str):
        for cookie in cookies_str.split(';'):
            if '=' in cookie:
                name, value = cookie.split('=', 1)
                self.session.cookies.set(name.strip(), value.strip(), domain='.tiktok.com')

        response = self.session.get("https://www.tiktok.com/passport/web/account/info/", headers=self.headers)

        if response.status_code == 200:
            data = response.json().get('data', {})
            username = data.get('username', 'N/A')
            nickname = data.get('nickname', 'N/A')
            profile_url = f"https://www.tiktok.com/@{username}"

            profile_response = self.session.get(profile_url, headers=self.headers)
            followers_count = re.search(r'"followerCount":(\d+)', profile_response.text)
            following_count = re.search(r'"followingCount":(\d+)', profile_response.text)

            result = {
                'success': True,
                'username': username,
                'nickname': nickname,
                'follower_count': followers_count.group(1) if followers_count else 'N/A',
                'following_count': following_count.group(1) if following_count else 'N/A'
            }

            # Kiểm tra nếu tất cả thông tin chính đều là 'N/A'
            if (result['username'] == 'N/A' and 
                result['nickname'] == 'N/A' and 
                result['follower_count'] == 'N/A' and 
                result['following_count'] == 'N/A'):
                return {
                    'success': False,
                    'message': 'Cookie đã die vui lòng nhập lại'
                }

            return result
        return {'success': False, 'message': 'Cookie không hợp lệ hoặc đã hết hạn'}

#========= Khởi chạy Brave (Incognito Mode) =========#
def chay_brave():
    try:
        subprocess.Popen(f'"{BRAVE_PATH}" --incognito --remote-debugging-port=9222', shell=True)
        time.sleep(3)
    except Exception as e:
        print(f"Lỗi khi khởi chạy Brave: {str(e)}")

#========= Cấu hình Selenium =========#
def setup_driver():
    try:
        options = Options()
        options.binary_location = BRAVE_PATH
        options.add_argument("--mute-audio")
        options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=options)
        driver.get(TIKTOK_URL)
        return driver
    except Exception as e:
        print(f"Lỗi khi khởi tạo driver: {str(e)}")
        return None

#========= Xử lý cookie =========#
def dang_nhap_tiktok():
    """
    Hàm xử lý đăng nhập TikTok bằng cookie.
    Returns:
        list: Danh sách các cookie đã được xử lý
    """
    tiktok_login = TikTokLogin()  # Khởi tạo đối tượng TikTokLogin
    cookie_file = 'cookietiktok.txt'

    while True:  # Vòng lặp chính để quay lại từ đầu khi có lỗi
        os.system('cls')  # Xóa terminal
        banner2()  # Hiển thị banner
        try:
            cookie_final = ''
            
            # Kiểm tra và tạo file cookie nếu chưa tồn tại
            if not os.path.exists(cookie_file):
                with open(cookie_file, 'w', encoding='utf-8') as f:
                    f.write('')
            
            # Đọc cookie cũ từ file
            with open(cookie_file, 'r', encoding='utf-8') as f:
                cookie_cu = f.read().strip()
            
            # Xử lý trường hợp có cookie cũ
            if cookie_cu:
                while True:
                    su_dung_cu = input(f"{trang}Bạn muốn sử dụng cookie cũ không (Y/N): ").strip().upper()
                    if su_dung_cu == 'Y':
                        print("\033[F\033[K", end="")
                        for _ in range(15): print(f"{xl}Sử dụng cookie cũ thành công.{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                        cookie_final = cookie_cu
                        break
                    elif su_dung_cu == 'N':
                        print("\033[F\033[K", end="")
                        # Nhập và lưu cookie mới
                        cookie_final = input(f"{trang}Nhập cookie mới của bạn: ").strip()
                        if "=" not in cookie_final:
                            for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                            continue
                        with open(cookie_file, 'w', encoding='utf-8') as f:
                            f.write(cookie_final)
                            for _ in range(15): print(f"{xl}Cookie mới đã được lưu.{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                        break
                    else:
                        print("\033[F\033[K", end="")
                        for _ in range(5): print(f"{red}Vui lòng nhập đúng lựa chọn!{RESET}", end="\r", flush=True); time.sleep(0.2); print(" " * 40, end="\r", flush=True); time.sleep(0.2)
                print(" " * 50, end="\r")
            else:
                # Nhập và lưu cookie mới nếu không có cookie cũ
                while True:
                    cookie_final = input(f"{trang}Nhập cookie mới của bạn: ").strip()
                    if "=" not in cookie_final:
                        for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                        continue
                    with open(cookie_file, 'w', encoding='utf-8') as f:
                        f.write(cookie_final)
                        for _ in range(15): print(f"{xl}Cookie mới đã được lưu.{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                    break
            
            # Kiểm tra cookie bằng TikTokLogin
            result = tiktok_login.login_with_cookie(cookie_final)
            if not result['success']:
                for _ in range(15): print(f"{red}{result['message']}{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                time.sleep(1)  
                continue  
            
            # Xử lý cookie thành list nếu thành công
            cookies = [c.strip() for c in cookie_final.split(';') if "=" in c]
            if not cookies:
                for _ in range(15): print(f"{red}Cookie không tồn tại hoặc hết hạn{RESET}", end="\r"); time.sleep(0.2); print(" " * 40, end="\r"); time.sleep(0.2)
                time.sleep(5)  
                continue  
                
            return cookies
            
        except Exception as e:
            print(f"Lỗi khi xử lý cookie: {str(e)}")
            time.sleep(5)  
            continue  

#========= Gán cookie vào Brave và kiểm tra đăng nhập =========#
def gan_cookie_vao_brave(driver, cookies):
    driver.get(TIKTOK_URL)
    for cookie in cookies:
        name, value = cookie.split('=', 1)
        driver.add_cookie({'name': name.strip(), 'value': value.strip(), 'domain': '.tiktok.com'})
    driver.refresh()

def nhap_nhay():
    for _ in range(5):  # Số lần nhấp nháy
        print("Đang quay lại menu chính.....", end="\r")
        time.sleep(0.2)  # Giảm thời gian xuống 0.2 giây
        print(" " * 40, end="\r")
        time.sleep(0.2)
def docdanhsach():
    while True:
        try:
            print(f"{trang}Nhập đường dẫn chứa file danh sách following:")
            duongdanfile = input(f"{trang}Nhập: ").strip()
            duongdanfile = ''.join(c for c in duongdanfile if unicodedata.category(c) != 'Cf')

            usernames = []
            with open(duongdanfile, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.startswith("Username: "):
                        username = line.replace("Username: ", "").strip()
                        if username != "N/A":
                            usernames.append(username)

            if usernames:  # Nếu có username hợp lệ, return danh sách
                print(f"{trang}Số lượng username đọc được: {len(usernames)}")
                print("="*50)
                return usernames
            else:
                print("File không chứa username hợp lệ. Vui lòng nhập lại.")
        except FileNotFoundError:
            print("\033[F\033[K", end="")  # Xóa dòng nhập sai
            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")  # Xóa thông báo lỗi
            print(f"{red}Bạn đã nhập sai đường dẫn,vui lòng nhập lại!!", end="\r", flush=True)  # In lỗi mà không xuống dòng
            time.sleep(2)  # Hiển thị lỗi trong 2 giây
            print(" " * 50, end="\r")
            continue
def countdown_timer(seconds, message):
    for i in range(seconds, 0, -1):
        print(f"\r{message} {i} giây...", end='', flush=True)
        time.sleep(1)
    print('\r' + ' ' * 80, end='\r')
def unfollowtheo_danhsach(driver, usernames):
    delay_min = int(input('Nhập Delay Min: '))
    delay_max = int(input('Nhập Delay Max: '))
    jobs_to_rest = int(input('Sau bao nhiêu nhiệm vụ thì kích hoạt chống block: '))
    rest_time = int(input(f'Sau {jobs_to_rest} nhiệm vụ thì nghỉ ngơi bao nhiêu giây: '))
    print(f"\033[97m════════════════════════════════════════════════════════")

    count_success = 0
    failed_accounts = []
    account_thaydoiusername = []
    consecutive_failures = 0  # Biến đếm số tài khoản thất bại liên tiếp
    task_count = 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    failed_file = f"failed_unfollow_{timestamp}.txt"

    # Định nghĩa các selector
    FOLLOW_BUTTON = '[data-e2e="follow-button"]:not([aria-label*="Following"])'
    FOLLOWING_BUTTON = '[data-e2e="follow-button"][aria-label*="Following"]'

    for user in usernames:
        user_url = f"https://www.tiktok.com/@{user}"
        print(f"{trang}✨ Đang xử lý: {user_url}\033[0m")
        

        try:
            driver.get(user_url)
            time.sleep(2)

            # Kiểm tra tài khoản không tồn tại hoặc đổi username
            error_messages = [
                "//p[contains(text(), \"Couldn't find this account\")]",
                "//p[contains(text(), 'Không tìm thấy tài khoản này')]",
                "//div[contains(text(), \"Couldn't find this account\")]"
            ]
            account_not_found = False
            for xpath in error_messages:
                try:
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    if element.is_displayed():
                        print(f"\033[31m⚠️ {user} không tồn tại hoặc đã đổi username, bỏ qua...\033[0m")
                        print(f"\033[97m════════════════════════════════════════════════════════\033[0m")
                        account_thaydoiusername.append(user)
                        account_not_found = True
                        break
                except TimeoutException:
                    continue

            if account_not_found:
                continue

            # Kiểm tra đã follow chưa
            try:
                follow_button = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, FOLLOW_BUTTON))
                )
                if follow_button.is_displayed():
                    print(f"\033[33m✅ Bạn đã follow {user} rồi, bỏ qua !!!\033[0m")
                    print(f"\033[97m════════════════════════════════════════════════════════\033[0m")
                    consecutive_failures = 0  # Reset nếu đã follow
                    continue
            except (NoSuchElementException, TimeoutException):
                pass

            # Thử follow với tối đa 3 lần
            retry = 0
            while retry < 3:
                try:
                    following_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, FOLLOWING_BUTTON))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", following_button)
                    following_button.click()
                    driver.refresh()
                    time.sleep(2)

                    try:
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, FOLLOW_BUTTON))
                        )
                        count_success += 1
                        task_count += 1
                        print(f"{xl}✅ Bạn đã unfollow {user} ({count_success})\033[0m")
                        print(f"\033[97m════════════════════════════════════════════════════════\033[0m")
                        consecutive_failures = 0  # Reset khi follow thành công
                        break
                    except TimeoutException:
                        retry += 1
                        print(f"{yellow}⚠️ Thử lại unfollow {user} lần {retry}\033[0m")

                except Exception as e:
                    print(f"{red}❌ Lỗi khi thử unfollow {user}: {str(e)}\033[0m")
                    break

            if retry == 3:
                print(f"\033[31m❌ Hiện tại không thể unfollow {user} được.\033[0m")
                print(f"\033[97m════════════════════════════════════════════════════════\033[0m")
                failed_accounts.append(user)
                consecutive_failures += 1  # Tăng khi thất bại hoàn toàn với user
                if consecutive_failures == 3:
                    print(f"\033[31m❌ Acc đã bị block chức năng unfollow, vui lòng thử lại sau...\033[0m")
                    print(f"\033[97m════════════════════════════════════════════════════════\033[0m")
                    break  # Thoát vòng lặp lớn nếu bị block

            # Chống block: nghỉ sau số nhiệm vụ nhất định
            if task_count % jobs_to_rest == 0 and task_count > 0:
                for remaining in range(int(rest_time), 0, -1):
                    sys.stdout.write(f"\r{yellow}⏳ Còn [{remaining}] giây...    \033[0m")
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\r" + " " * 50 + "\r")  # Ghi đè bằng khoảng trắng để xóa dòng
                sys.stdout.flush()

            # Đoạn code delay random với countdown
            delay = random.uniform(delay_min, delay_max)
            for remaining in range(int(delay), 0, -1):
                sys.stdout.write(f"\r{trang}⏳ Còn [{remaining}] giây...    \033[0m")
                sys.stdout.flush()
                time.sleep(1)
            # Thêm 0.1 giây cuối nếu delay có phần thập phân
            if delay % 1 > 0:
                time.sleep(delay % 1)
            sys.stdout.write("\r" + " " * 50 + "\r")  # Ghi đè bằng khoảng trắng để xóa dòng
            sys.stdout.flush()

        except Exception as e:
            print(f"{red}❌ Lỗi bất ngờ khi xử lý {user}: {str(e)}\033[0m")
            failed_accounts.append(user)

    # Ghi danh sách tài khoản thất bại vào file
    unique_accounts = set(failed_accounts)
    with open(failed_file, 'w', encoding='utf-8') as f:
        for account in unique_accounts:
            f.write(f"Username: {account}\n")

    # Tổng kết
    print(f"{trang}📊 Tổng kết:\033[0m")
    print(f"{trang} Đã lưu danh sách tài khoản follow thất bại vào file: {failed_file}")
    print(f"{xl}✅ Số tài khoản đã follow thành công: {count_success}\033[0m")
    print(f"{red}❌ Số tài khoản không thể follow: {len(failed_accounts)}\033[0m")
    print(f"{yellow}🔄 Số tài khoản có thể đã đổi username: {len(account_thaydoiusername)}\033[0m")
if __name__ == "__main__":
    chay_brave()
    driver = setup_driver()
    if driver:
        cookies = dang_nhap_tiktok()
        if cookies:
            gan_cookie_vao_brave(driver, cookies)
            time.sleep(3)
            tiktok_login = TikTokLogin()
            cookie_final = '; '.join(cookies)
            result = tiktok_login.login_with_cookie(cookie_final)
            if result['success']:
                os.system('cls')
                banner2()
                print("===== Đăng nhập thành công ! =====")
                print(f"Username: {result['username']}")
                print(f"Link tài khoản: https://www.tiktok.com/@{result['username']}")
                print(f"Số người theo dõi: {result['follower_count']}")
                print(f"Số người đang theo dõi: {result['following_count']}")
                print(f"=" * 29)
                usernames = docdanhsach()
                unfollowtheo_danhsach(driver, usernames)
            else:
                print(result['message'])
    elif KeyboardInterrupt:
            print(f"{trang}📊 Cảm ơn bạn đã sử dụng tôi<3333\033[0m")
            print(f"{trang}📊 Tổng kết:\033[0m")
            print(f"{trang} Đã lưu danh sách tài khoản follow thất bại vào file: {failed_file}")
            print(f"{xl}✅ Số tài khoản đã follow thành công: {count_success}\033[0m")
            print(f"{red}❌ Số tài khoản không thể follow: {len(failed_accounts)}\033[0m")
            print(f"{yellow}🔄 Số tài khoản có thể đã đổi username: {len(account_thaydoiusername)}\033[0m")
        
                
