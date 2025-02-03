import cv2
import time
import psutil
import subprocess
import numpy as np
import pyautogui as pg
#还要安装pyscreeze和pillow

def kill_process_by_name(process_name):
    # 获取当前系统中所有进程的列表
    for proc in psutil.process_iter():
        try:
            # 检查进程名是否匹配
            if process_name.lower() in proc.name().lower():
                # 尝试终止进程
                proc.terminate()
                print(f"已终止进程：{proc.pid} ({proc.name()})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # 如果进程不存在或无法访问，则忽略该进程
            pass

# 替换为你想要杀死的进程名
# 例如：'notepad.exe' 对于Windows系统或 'gnome-terminal' 对于Linux系统
target_process_name = 'EasiNote.exe'
kill_process_by_name(target_process_name)

#启动软件#
exe_path = ""
# 填入希沃白板路径
subprocess.Popen(exe_path)

# 程序名，这里替换为你想要检测的程序名
program_name = 'EasiNote.exe'
def check_process(program_name):
    while True:
        for proc in psutil.process_iter():
            try:
                # 检查进程名是否匹配
                if program_name.lower() in proc.name().lower():
                    print(f"程序 {proc.name()} 正在运行，PID: {proc.pid}")
                    return proc.pid  # 返回进程ID，如果找到了匹配的进程
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        # 如果进程不存在，等待一秒后继续检测
        time.sleep(1)

# 主程序
if __name__ == "__main__":
    check_process(program_name)

# 模板匹配的函数
def template_matching(img, template):
    # 转换为灰度图像
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)

    # 如果找到了匹配的位置
    if len(loc[0]) > 0:
        pt = loc[::-1][0][0]  # 获取第一个匹配的位置
        return True, pt
    else:
        return False, (-1, -1)

# 循环识别
while True:
    # 截取屏幕图像
    screenshot = pg.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 加载打卡按钮的图片样本
    template = cv2.imread(r'') # 填入'check_in_button.png'图片的路径

    # 模板匹配
    found, pt = template_matching(screenshot, template)
    
    if found:
        print("已点击登录")
        # 模拟鼠标点击
        pg.click(353,1763)  # 点击'登录'
        break
    else:
        print("白板未打开，等待2秒后重试...")
        time.sleep(1)

#输入账号密码
time.sleep(1)
pg.click(1140,253) #点击账号登录
time.sleep(0.5)
pg.write("") #输入账号
time.sleep(0.5)
pg.click(948,477) #点击密码框
time.sleep(0.5)
pg.write("") #输入密码
pg.click(1317,1278) #点击同意条款
time.sleep(0.5)
pg.click(1627,952) #点击登陆
print("完成登录")

# 注根据自己的屏幕分辨率来调整坐标

#surface pro5坐标；登录353，1763;同意1317,1278;登录1627,952