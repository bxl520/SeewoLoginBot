# 希沃白板图像识别登录工具

## 项目简介
本项目是一个用于希沃白板自动登录的Python脚本工具，通过图像识别和模拟鼠标操作实现自动登录功能，旨在简化希沃白板的登录流程，提高使用效率。

## 功能特点
- 自动检测并终止希沃白板软件进程（`EasiNote.exe`）。
- 自动启动希沃白板软件。
- 实时截取屏幕图像，通过模板匹配识别登录按钮并模拟鼠标点击。
- 自动输入账号和密码，完成登录操作。

## 使用方法

### 环境依赖
- Python 3.x
- 必须安装以下Python库：
  - OpenCV (`cv2`)
  - NumPy (`numpy`)
  - PyAutoGUI (`pyautogui`)
  - psutil
  - pyscreeze
  - pillow

安装依赖库：
```bash
pip install opencv-python numpy pyautogui psutil pyscreeze pillow
```

# 配置步骤
## 1. 设置希沃白板软件路径：
在代码第28行中，找到`exe_path = ""`，填入希沃白板软件的安装路径，例如：
```python
exe_path = r"C:\Program Files\Seewo\EasiNote\in\EasiNote.exe"
```

## 2. 准备登录按钮模板图片：
将该图片放置在脚本运行目录下，或者在代码第78行中指定正确的图片路径：
```python
template = cv2.imread(r'path_to_check_in_button.png')
```

## 3. 配置账号和密码：
在代码第96行和第100行中找到以下部分，填入你的希沃白板账号和密码：
```python
pg.write("your_account")  # 输入账号
pg.write("your_password")  # 输入密码
```
## 4. 配置点击坐标
在代码第找到代码94、98、101、103行找到以下代码，填入自己电脑分辨率对应坐标
```python
pg.click(x,y) #点击账号登录
pg.click(x,y) #点击密码框
pg.click(x,y) #点击同意条款
pg.click(x,y) #点击登陆
```

# 运行脚本
运行脚本前，请确保希沃白板软件已正确安装，并且上述配置已完成。运行脚本
```bash
python 希沃白板图像识别登录_github.py
```
脚本运行后，将自动完成以下操作：
1. 检测并终止希沃白板软件进程。
2. 启动希沃白板软件。
3. 截取屏幕图像，识别登录按钮并模拟点击。
4. 输入账号和密码，完成登录操作

## 注意事项
- 请确保屏幕分辨率与脚本中定义的坐标一致。如果分辨率不同，需要根据实际情况调整鼠标点击的坐标。
- 如果希沃白板软件的界面布局或按钮样式发生变化，可能需要重新截取模板图片并更新脚本。
- 本工具仅供学习和研究使用，请勿用于任何非法或未经授权的操作。