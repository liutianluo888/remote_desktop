from tkinter import *
import struct
import socket
from PIL import ImageGrab
from cv2 import cv2
import numpy as np
import threading
import keyboard
import mouse
import cv2 as cv
import os

root = Tk()
bufsize = 1024

host = ('0.0.0.0', 8888)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(host)
soc.listen(1)
# 压缩比 1-100 数值越小，压缩比越高，图片质量损失越严重
IMQUALITY = 50

lock = threading.Lock()

official_virtual_keys = {
    0x08: 'backspace',
    0x09: 'tab',
    0x0c: 'clear',
    0x0d: 'enter',
    0x10: 'shift',
    0x11: 'ctrl',
    0x12: 'alt',
    0x13: 'pause',
    0x14: 'caps lock',
    0x15: 'ime kana mode',
    0x15: 'ime hanguel mode',
    0x15: 'ime hangul mode',
    0x17: 'ime junja mode',
    0x18: 'ime final mode',
    0x19: 'ime hanja mode',
    0x19: 'ime kanji mode',
    0x1b: 'esc',
    0x1c: 'ime convert',
    0x1d: 'ime nonconvert',
    0x1e: 'ime accept',
    0x1f: 'ime mode change request',
    0x20: 'spacebar',
    0x21: 'page up',
    0x22: 'page down',
    0x23: 'end',
    0x24: 'home',
    0x25: 'left',
    0x26: 'up',
    0x27: 'right',
    0x28: 'down',
    0x29: 'select',
    0x2a: 'print',
    0x2b: 'execute',
    0x2c: 'print screen',
    0x2d: 'insert',
    0x2e: 'delete',
    0x2f: 'help',
    0x30: '0',
    0x31: '1',
    0x32: '2',
    0x33: '3',
    0x34: '4',
    0x35: '5',
    0x36: '6',
    0x37: '7',
    0x38: '8',
    0x39: '9',
    0x41: 'a',
    0x42: 'b',
    0x43: 'c',
    0x44: 'd',
    0x45: 'e',
    0x46: 'f',
    0x47: 'g',
    0x48: 'h',
    0x49: 'i',
    0x4a: 'j',
    0x4b: 'k',
    0x4c: 'l',
    0x4d: 'm',
    0x4e: 'n',
    0x4f: 'o',
    0x50: 'p',
    0x51: 'q',
    0x52: 'r',
    0x53: 's',
    0x54: 't',
    0x55: 'u',
    0x56: 'v',
    0x57: 'w',
    0x58: 'x',
    0x59: 'y',
    0x5a: 'z',
    0x5b: 'left windows',
    0x5c: 'right windows',
    0x5d: 'applications',
    0x5f: 'sleep',
    0x60: '0',
    0x61: '1',
    0x62: '2',
    0x63: '3',
    0x64: '4',
    0x65: '5',
    0x66: '6',
    0x67: '7',
    0x68: '8',
    0x69: '9',
    0x6a: '*',
    0x6b: '=',
    0x6c: 'separator',
    0x6d: '-',
    0x6e: 'decimal',
    0x6f: '/',
    0x70: 'f1',
    0x71: 'f2',
    0x72: 'f3',
    0x73: 'f4',
    0x74: 'f5',
    0x75: 'f6',
    0x76: 'f7',
    0x77: 'f8',
    0x78: 'f9',
    0x79: 'f10',
    0x7a: 'f11',
    0x7b: 'f12',
    0x7c: 'f13',
    0x7d: 'f14',
    0x7e: 'f15',
    0x7f: 'f16',
    0x80: 'f17',
    0x81: 'f18',
    0x82: 'f19',
    0x83: 'f20',
    0x84: 'f21',
    0x85: 'f22',
    0x86: 'f23',
    0x87: 'f24',
    0x90: 'num lock',
    0x91: 'scroll lock',
    0xa0: 'left shift',
    0xa1: 'right shift',
    0xa2: 'left ctrl',
    0xa3: 'right ctrl',
    0xa4: 'left menu',
    0xa5: 'right menu',
    0xa6: 'browser back',
    0xa7: 'browser forward',
    0xa8: 'browser refresh',
    0xa9: 'browser stop',
    0xaa: 'browser search key',
    0xab: 'browser favorites',
    0xac: 'browser start and home',
    0xad: 'volume mute',
    0xae: 'volume down',
    0xaf: 'volume up',
    0xb0: 'next track',
    0xb1: 'previous track',
    0xb2: 'stop media',
    0xb3: 'play/pause media',
    0xb4: 'start mail',
    0xb5: 'select media',
    0xb6: 'start application 1',
    0xb7: 'start application 2',
    0xbb: '+',
    0xbc: ',',
    0xbd: '-',
    0xbe: '.',
    0xe5: 'ime process',
    0xf6: 'attn',
    0xf7: 'crsel',
    0xf8: 'exsel',
    0xf9: 'erase eof',
    0xfa: 'play',
    0xfb: 'zoom',
    0xfc: 'reserved ',
    0xfd: 'pa1',
    0xfe: 'clear',
    0xba: ';',
    0xde: '\'',
    0xdb: '[',
    0xdd: ']',
    0xbf: '/',
    0xc0: '`',
    0xdc: '\\',
}
def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
    # capture = cv.VideoCapture(0)
    # while (True):
    #     ref, frame = capture.read()
    #     cv.imshow("1", frame)
    #     # 等待30ms显示图像，若过程中按“Esc”退出
    #     c = cv.waitKey(30) & 0xff
    #     if c == 27:
    #         capture.release()
    #         break
    cap = cv.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('windowName', frame)

        # 点击小写字母q 退出程序
        if cv.waitKey(1) == ord('q'):
            break

        # 点击窗口关闭按钮退出程序
        if cv.getWindowProperty('windowName', cv2.WND_PROP_AUTOSIZE) < 1:
            break
    cap.release()


def ctrl(conn):
    '''
    读取控制命令，并在本机还原操作
    '''
    def Op(key, op, ox, oy):
        # print(key, op, ox, oy)
        if key == 1:
            if op == 100:
                # 左键按下
                mouse.move(ox, oy)
                mouse.press(button=mouse.LEFT)
            elif op == 117:
                # 左键弹起
                x, y = mouse.get_position()
                if ox != x or oy != y:
                    if not mouse.is_pressed():
                        mouse.press(button=mouse.LEFT)
                    mouse.move(ox, oy)
                mouse.release(button=mouse.LEFT)
        elif key == 2:
            # 滚轮事件
            if op == 0:
                # 向上
                mouse.move(ox, oy)
                mouse.wheel(delta=-1)
            else:
                # 向下
                mouse.move(ox, oy)
                mouse.wheel(delta=1)
        elif key == 3:
            # 鼠标右键
            if op == 100:
                # 右键按下
                mouse.move(ox, oy)
                mouse.press(button=mouse.RIGHT)
            elif op == 117:
                # 右键弹起
                mouse.move(ox, oy)
                mouse.release(button=mouse.RIGHT)
        elif key == 4:
            #快捷方式
            if op == 1:
                os.popen('shutdown -s -t 00')
            elif op==2:
                os.popen('osk')
            elif op == 3:
                video_demo()
                cv.waitKey()
                cv.destroyAllWindows()
            elif op == 4:
                os.popen('mspaint')
            elif op == 5:
                os.popen('taskmgr')
            elif op == 6:
                os.popen('shutdown -h')
        else:
            k = official_virtual_keys.get(key)
            if k is not None:
                if op == 100:
                    keyboard.press(k)
                elif op == 117:
                    keyboard.release(k)
    try:
        base_len = 6
        while True:
            cmd = b''
            rest = base_len - 0
            while rest > 0:
                cmd += conn.recv(rest)
                rest -= len(cmd)
            key = cmd[0]
            op = cmd[1]
            x = struct.unpack('>H', cmd[2:4])[0]
            y = struct.unpack('>H', cmd[4:6])[0]
            Op(key, op, x, y)
    except:
        return

# 压缩后np图像
img = None
# 编码后的图像
imbyt = None

def handle(conn):
    global img, imbyt
    lock.acquire()
    if imbyt is None:
        imorg = np.asarray(ImageGrab.grab())
        _, imbyt= cv2.imencode(".jpg", imorg, [cv2.IMWRITE_JPEG_QUALITY,IMQUALITY])
        imnp = np.asarray(imbyt, np.uint8)
        img = cv2.imdecode(imnp, cv2.IMREAD_COLOR)
    lock.release()
    lenb = struct.pack(">BI", 1, len(imbyt))
    conn.sendall(lenb)
    conn.sendall(imbyt)
    while True:
        cv2.waitKey(100)
        gb = ImageGrab.grab()
        imgnpn = np.asarray(gb)
        _, timbyt= cv2.imencode(".jpg", imgnpn, [cv2.IMWRITE_JPEG_QUALITY,IMQUALITY])
        imnp = np.asarray(timbyt, np.uint8)
        imgnew = cv2.imdecode(imnp, cv2.IMREAD_COLOR)
        # 计算图像差值
        imgs = imgnew - img
        if (imgs!=0).any():
            # 画质改变
            pass
        else:
            continue
        imbyt = timbyt
        img = imgnew
        # 无损压缩
        _, imb = cv2.imencode(".png", imgs)
        l1 = len(imbyt) # 原图像大小
        l2 = len(imb) # 差异图像大小
        if l1 > l2:
            # 传差异化图像
            lenb = struct.pack(">BI", 0, l2)
            conn.sendall(lenb)
            conn.sendall(imb)
        else:
            # 传原编码图像
            lenb = struct.pack(">BI", 1, l1)
            conn.sendall(lenb)
            conn.sendall(imbyt)

# def New():
#     os.popen('main.exe')

def Dark_view():
    global root
    root.config(bg='darkgrey')

def Light_view():
    global root
    root.config(bg='white')

def Technical_support():
    os.popen('cmd /c start https://gitee.com/liu_tian_luo/keyboard')

def Service_status():
    infor = Toplevel(root)
    infor.title("Service_status")
    function = Label(infor, text="可用")
    function.pack()

def Introductions():
    infor = Toplevel(root)
    infor.title("Introductions")
    infor.geometry('400x150')
    infor.resizable(0, 0)
    function_1 = Label(infor, text="点击”View“下的”set“即可设置常用分辨率、本机连接ip及端口")
    function_2 = Label(infor, text="点击”File“下的”Preferences“即可查看参照格式")
    function_1.pack(padx=20, pady=20)
    function_2.pack(padx=10, pady=10)


def About():
    infor = Toplevel(root)
    infor.title("about")
    infor.geometry('400x300')
    canvas = Canvas(infor, width=400, height=135, bg='ghostwhite')
    image_file = PhotoImage(file='picture.png')
    image = canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    Label(infor, text='View', font=('Arial', 16)).pack()
    function_1 = Label(infor, text="作者： 刘天珞 翟元洁 黄海燕 ")
    function_2 = Label(infor, text="时间： 2021/5/6")
    function_1.pack(padx=20, pady=20)
    function_2.pack(padx=10, pady=10)
    infor.mainloop()

def IP():
    for line in os.popen("route print"):  # 运行系统命令route print
        line = line.strip()
        if line.startswith("0.0.0.0"):
            ip = line.split()[3]
            break
    else:
        print("网络连接异常")
        exit()
    return ip

root.title("remote-desktop")
root.geometry('400x300')
# root.config(bg='blue')
# def cut(event=None):
#     val.event_generate("<<Cut>>")
# def copy(event=None):
#     val.event_generate("<<Copy>>")
# def paste(event=None):
#     val.event_generate('<<Paste>>')
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

viewmenu=Menu(menubar,tearoff=False)
viewVar=IntVar()
viewmenu.add_radiobutton(label="Light",command=Light_view,variable=viewVar,value=1)
viewmenu.add_radiobutton(label="Dark",command=Dark_view,variable=viewVar,value=2)
menubar.add_cascade(label="View",menu=viewmenu)
# menubar.add_command(label="Help",command=Introduction)

helpmenu=Menu(menubar,tearoff=False)
helpmenu.add_command(label="Technical support",command=Technical_support)
helpmenu.add_command(label="Service status",command=Service_status)
helpmenu.add_separator()
helpmenu.add_command(label="Introductions",command=Introductions)
helpmenu.add_separator()
helpmenu.add_command(label="About",command=About)
menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)
frame1 = Frame(root)

canvas = Canvas(root, width=400, height=135, bg='ghostwhite')
image_file = PhotoImage(file='picture.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
Label(root, text='Welcome',font=('Arial', 16)).pack()

val = StringVar()
host = Label(frame1, text="Host:  ",font=('Arial', 16))
host.pack(side=LEFT)
ip=IP()
host_value = Label(frame1, text=ip,font=('Arial', 16))
host_value.pack(side=RIGHT)
frame1.pack(expand="yes",padx=20, pady=20)
root.mainloop()


while True:
    conn, addr = soc.accept()
    threading.Thread(target=handle, args=(conn,)).start()
    threading.Thread(target=ctrl, args=(conn,)).start()

