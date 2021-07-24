# import tkinter
from tkinter import *
import tkinter.messagebox
import struct
import socket
import numpy as np
from PIL import Image, ImageTk
import threading
import re
from cv2 import cv2
import os

root = Tk()

# 放缩大小
scale = 1

# 原传输画面尺寸
fixw, fixh = 0, 0

# 放缩标志
wscale = False

# 屏幕显示画布
showcan = None

# socket缓冲区大小
bufsize = 10240

# 线程
th = None

# socket
soc = None

# socks5

socks5 = None


# 初始化socket
def SetSocket():
    global soc, host_en

    def byipv4(ip, port):
        return struct.pack(">BBBBBBBBH", 5, 1, 0, 1, ip[0], ip[1], ip[2], ip[3], port)

    def byhost(host, port):
        d = struct.pack(">BBBB", 5, 1, 0, 3)
        blen = len(host)
        d+=struct.pack(">B", blen)
        d+=host.encode()
        d+=struct.pack(">H", port)
        return d
    host = host_en.get()
    if host is None:
        tkinter.messagebox.showinfo('提示', 'Host设置错误！')
        return
    hs = host.split(":")
    if len(hs) != 2:
        tkinter.messagebox.showinfo('提示', 'Host设置错误！')
        return
    if socks5 is not None:
        ss = socks5.split(":")
        if len(ss) != 2:
            tkinter.messagebox.showinfo('提示', '代理设置错误！')
            return
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((ss[0], int(ss[1])))
        soc.sendall(struct.pack(">BB", 5, 0))
        recv = soc.recv(2)
        if recv[1] != 0:
            tkinter.messagebox.showinfo('提示', '代理回应错误！')
            return
        if re.match(r'^\d+?\.\d+?\.\d+?\.\d+?:\d+$', host) is None:
            # host 域名访问
            hand = byhost(hs[0], int(hs[1]))
            soc.sendall(hand)
        else:
            # host ip访问
            ip = [int(i) for i in hs[0].split(".")]
            port = int(hs[1])
            hand = byipv4(ip, port)
            soc.sendall(hand)
        # 代理回应
        rcv = b''
        while len(rcv)!=10:
            rcv += soc.recv(10-len(rcv))
        if rcv[1] != 0:
            tkinter.messagebox.showinfo('提示', '代理回应错误！')
            return
    else:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((hs[0], int(hs[1])))


def SetScale(x):
    global scale, wscale
    scale = float(x) / 100
    wscale = True

# def ShowProxy():
#     # 显示代理设置
#     global root
#     def set_s5_addr():
#         global socks5
#         socks5 = s5_en.get()
#         if socks5 == "":
#             socks5 = None
#         pr.destroy()
#     pr = tkinter.Toplevel(root)
#     s5v = tkinter.StringVar()
#     s5_lab = tkinter.Label(pr, text="Socks5 Host:")
#     s5_en = tkinter.Entry(pr, show=None, font=('Arial', 14), textvariable=s5v)
#     s5_btn = tkinter.Button(pr, text="OK", command=set_s5_addr)
#     s5_lab.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0)
#     s5_en.grid(row=0, column=1, padx=10, pady=10, ipadx=40, ipady=0)
#     s5_btn.grid(row=1, column=0, padx=10, pady=10, ipadx=30, ipady=0)
#     s5v.set("127.0.0.1:8888")


# 快捷命令
def Shut_win():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 1, 0, 0))

def Win_keyboard():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 2, 0, 0))

def Camera():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 3, 0, 0))

def Paint():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 4, 0, 0))

def Task():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 5, 0, 0))

def Sleep():
    global soc
    soc.sendall(struct.pack('>BBHH', 4, 6, 0, 0))

def View():
    # global root
    pr = Toplevel(root)
    pr.title("function")
    pr.geometry('400x350')
    canvas = Canvas(pr, width=400, height=135, bg='ghostwhite')
    image_file = PhotoImage(file='picture.png')
    image = canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    frame1 = Frame(pr)
    frame2 = Frame(pr)
    frame3 = Frame(pr)
    function_1=Button(frame1, text="    关 机    ", command=Shut_win)
    function_2=Button(frame1, text="    休 眠    ", command=Sleep)
    function_3=Button(frame2, text="   摄像头   ", command=Camera)
    function_4=Button(frame2, text="   画图板   ", command=Paint)
    function_5=Button(frame3, text="任务管理器", command=Task)
    function_6 = Button(frame3, text="   软键盘   ", command=Win_keyboard)
    # pr.destroy()
    function_1.pack(padx=10, pady=10,side=tkinter.LEFT)
    function_2.pack(padx=40, pady=10,side=tkinter.RIGHT)
    function_3.pack(padx=10, pady=15,side=tkinter.LEFT)
    function_4.pack(padx=40, pady=15,side=tkinter.RIGHT)
    function_5.pack(padx=10, pady=20,side=tkinter.LEFT)
    function_6.pack(padx=40, pady=20, side=tkinter.RIGHT)
    frame1.pack(expand="yes")
    frame2.pack(expand="yes")
    frame3.pack(expand="yes")
    pr.mainloop()


def ShowScreen():
    global showcan, root, soc, th, wscale
    if showcan is None:
        wscale = True
        showcan = tkinter.Toplevel(root)
        th = threading.Thread(target=run)
        th.start()
    else:
        soc.close()
        showcan.destroy()


def New():
    os.popen('client.exe')

def Preferences():
    infor = Toplevel(root)
    infor.title("Preferences")
    infor.geometry('400x150')
    infor.resizable(0, 0)
    val = StringVar()
    host_lab = Label(infor, text="Host:  ")
    host_en = Entry(infor, show=None, font=('Arial', 14), textvariable=val)
    sca_lab = Label(infor, text="Scale:")
    sca = Scale(infor, from_=10, to=100, orient=HORIZONTAL, length=100,
                showvalue=100, resolution=0.1, tickinterval=90, command=SetScale)
    host_lab.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0)
    host_en.grid(row=0, column=1, padx=0, pady=0, ipadx=40, ipady=0)
    sca_lab.grid(row=1, column=0, padx=10, pady=10, ipadx=0, ipady=0)
    sca.grid(row=1, column=1, padx=0, pady=0, ipadx=100, ipady=0)
    sca.set(80)
    val.set('127.0.0.1:8888')

def set():
    global root
    sca.set(80)
    val.set('127.0.0.1:8888')


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


root.title("remote-desktop")
root.geometry('400x400')
# root.config(bg='blue')
# def cut(event=None):
#     val.event_generate("<<Cut>>")
# def copy(event=None):
#     val.event_generate("<<Copy>>")
# def paste(event=None):
#     val.event_generate('<<Paste>>')
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label="New connection",command=New)
filemenu.add_separator()
filemenu.add_command(label="Preferences",command=Preferences)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

viewmenu=Menu(menubar,tearoff=False)
viewVar=IntVar()
viewmenu.add_radiobutton(label="Light",command=Light_view,variable=viewVar,value=1)
viewmenu.add_radiobutton(label="Dark",command=Dark_view,variable=viewVar,value=2)
viewmenu.add_separator()
viewmenu.add_command(label="Set",command=set)
viewmenu.add_separator()
viewmenu.add_command(label="Show function",command=View)
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
frame2 = Frame(root)
frame3 = Frame(root)
# frame_4=Frame(root,width=200,height=200)

canvas = Canvas(root, width=400, height=135, bg='ghostwhite')
image_file = PhotoImage(file='picture.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
Label(root, text='Welcome',font=('Arial', 16)).pack()

val = StringVar()
host_lab = Label(frame1, text="Host:  ")
host_en = Entry(frame1, show=None, font=('Arial', 14), textvariable=val)
sca_lab = Label(frame2, text="Scale:")
sca = Scale(frame2, from_=10, to=100, orient=HORIZONTAL, length=400,
                    showvalue=100, resolution=0.1, tickinterval=10, command=SetScale)
show_btn = Button(frame3, text="  Show  ", command=ShowScreen)
function_btn=Button(frame3, text="Function", command=View)

host_lab.pack(side=tkinter.LEFT)
host_en.pack(fill="x")
sca_lab.pack(side=tkinter.LEFT)
sca.pack(fill="x")
show_btn.pack(padx=10, pady=10,side=tkinter.LEFT)
function_btn.pack(padx=40, pady=10,side=tkinter.RIGHT)

frame1.pack(fill="x",expand="yes",padx=20, pady=20)
frame2.pack(fill="x",expand="yes",padx=10, pady=10)
frame3.pack(expand="yes")
# frame_4.pack()
# def popup(event):
#     viewmenu.post(event.x_root,event.y_root)
#
#
# frame_4.bind("<Button-3>",popup)


# proxy_btn = tkinter.Button(root, text="Proxy",bg="black",fg="blue",command=ShowProxy)
# host_lab.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0)
# host_en.grid(row=0, column=1, padx=0, pady=0, ipadx=40, ipady=0)
# proxy_btn.pack()
# sca_lab.grid(row=1, column=0, padx=10, pady=10, ipadx=0, ipady=0)
# sca.grid(row=1, column=1, padx=0, pady=0, ipadx=100, ipady=0)
# proxy_btn.grid(row=2, column=0, padx=0, pady=10, ipadx=30, ipady=0)
# proxy_btn.place(x=100,y=100,anchor='nw')
# proxy_btn.pack()
# show_btn.grid(row=2, column=1, padx=0, pady=10, ipadx=30, ipady=0)

def BindEvents(canvas):
    global soc, scale
    '''
    处理事件
    '''
    def EventDo(data):
        soc.sendall(data)
    # 鼠标左键

    def LeftDown(e):
        return EventDo(struct.pack('>BBHH', 1, 100, int(e.x/scale), int(e.y/scale)))

    def LeftUp(e):
        return EventDo(struct.pack('>BBHH', 1, 117, int(e.x/scale), int(e.y/scale)))
    canvas.bind(sequence="<1>", func=LeftDown)
    canvas.bind(sequence="<ButtonRelease-1>", func=LeftUp)

    # 鼠标右键
    def RightDown(e):
        return EventDo(struct.pack('>BBHH', 3, 100, int(e.x/scale), int(e.y/scale)))

    def RightUp(e):
        return EventDo(struct.pack('>BBHH', 3, 117, int(e.x/scale), int(e.y/scale)))
    canvas.bind(sequence="<3>", func=RightDown)
    canvas.bind(sequence="<ButtonRelease-3>", func=RightUp)

    # 鼠标滚轮
    def Wheel(e):
        if e.delta < 0:
            return EventDo(struct.pack('>BBHH', 2, 0, int(e.x/scale), int(e.y/scale)))
        else:
            return EventDo(struct.pack('>BBHH', 2, 1, int(e.x/scale), int(e.y/scale)))
    canvas.bind(sequence="<MouseWheel>", func=Wheel)

    # 键盘
    def KeyDown(e):
        return EventDo(struct.pack('>BBHH', e.keycode, 100, int(e.x/scale), int(e.y/scale)))
    def KeyUp(e):
        return EventDo(struct.pack('>BBHH', e.keycode, 117, int(e.x/scale), int(e.y/scale)))
    canvas.bind(sequence="<KeyPress>", func=KeyDown)
    canvas.bind(sequence="<KeyRelease>", func=KeyUp)


def run():
    global wscale, fixh, fixw, soc, showcan
    SetSocket()
    lenb = soc.recv(5)
    imtype, le = struct.unpack(">BI", lenb)
    imb = b''
    while le > bufsize:
        t = soc.recv(bufsize)
        imb += t
        le -= len(t)
    while le > 0:
        t = soc.recv(le)
        imb += t
        le -= len(t)
    data = np.frombuffer(imb, dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    h, w, _ = img.shape
    fixh, fixw = h, w
    imsh = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    imi = Image.fromarray(imsh)
    imgTK = ImageTk.PhotoImage(image=imi)
    cv = tkinter.Canvas(showcan, width=w, height=h, bg="white")
    cv.focus_set()
    BindEvents(cv)
    cv.pack()
    cv.create_image(0, 0, anchor=tkinter.NW, image=imgTK)
    h = int(h * scale)
    w = int(w * scale)
    while True:
        if wscale:
            h = int(fixh * scale)
            w = int(fixw * scale)
            cv.config(width=w, height=h)
            wscale = False
        try:
            lenb = soc.recv(5)
            imtype, le = struct.unpack(">BI", lenb)
            imb = b''
            while le > bufsize:
                t = soc.recv(bufsize)
                imb += t
                le -= len(t)
            while le > 0:
                t = soc.recv(le)
                imb += t
                le -= len(t)
            data = np.frombuffer(imb, dtype=np.uint8)
            ims = cv2.imdecode(data, cv2.IMREAD_COLOR)
            if imtype == 1:
                # 全传
                img = ims
            else:
                # 差异传
                img = img + ims
            imt = cv2.resize(img, (w, h))
            imsh = cv2.cvtColor(imt, cv2.COLOR_RGB2RGBA)
            imi = Image.fromarray(imsh)
            imgTK.paste(imi)
        except:
            showcan = None
            ShowScreen()
            return

root.mainloop()

# if __name__ == '__main__':
#     view()
