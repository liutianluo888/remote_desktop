# 1 绪论
## 1.1研究背景及意义
   随着计算机应用技术的发展，图形化界面已经成为各种不同计算设备所必不可少的功能。与此同时基于图形化用户界面的远程控制也应运而生，并且得到越来越广泛的应用，这其中包括：远程办公、远程教学、产品演示、远程配置、高危地带远程作业等等。这种技术趋势一方面为远程图形界面访问在宽范围上的应用提供了硬件条件，另一方面促使了对这种应用的需求的产生。计算机网络的迅速发展和广泛应用源于人们对信息资源共享的需求，远程桌面控制指的是这样一类应用：用户通过使用计算机网络中的某台主机，以交互式图形界面的形式对另一台主机进行全权访问与控制。远程控制作为在网络环境下一种典型的应用，使用户在操作终端机器与实际的设备分离，使用者不再需要局限于实际设备所处的位置，而通过远程控制软件就可以对设备进行各种方面的控制和操作，获得远程设备的状态，向远程设备下达各种控制命令并且能够即时得到对操作的反馈信息。<br>
   
  在传统的远程控制领域，以对计算机简单的管理和控制需求而言，通过远程桌面控制软件实现对个人计算机的控制也以更加便捷的方式满足了用户简单的管理操控远程计算机的需求。<br>
  
## 1.2国内外相关技术研究现状
  远程桌面控制协议设计的目的就是为了突破地域的限制，让用户可以随时随地通过网络连接操作自己的远程主机。不仅达到了便携、灵活的优点，而且实现了资源的共享。客户端只需要很少的投入，通常只是很低配置的计算机，就可以利用远程桌面控协议接入数据中心进行复杂的计算和大型应用软件的部署，因为所有的计算过程都在服务端完成，客户端只是充当了显示和输入的作用。<br>
  
  为了方便对计算机的管理需要，远程控制技术在桌面操作系统诞生之前的DOS时代就已经开始。而随着网络的发展以及桌面操作系统的成熟，远程控制方面的技术引起了更多的关注，从最初仅仅支持远程访问文件系统到后来可以自 由控制服务器端操作。通过远程控制软件，可以进行很多方面的远程控制，包括 获取远程电脑屏幕图像、窗口及进程列表：记录并提取远程主机键盘事件；可以打开、关闭目标电脑的任意目录并实现资源共享；提取拨号网络及普通程序的密码；激活、中止远端程序进程：管理远端电脑的文件和文件夹；关闭或者重新启动远端电脑中的操作系统；修改 windows 注册表；通过远端电脑上、下载文件和捕获音频、视频信号等。这些管理可以是一对一模式，也可以是一对多模式，即可以用一台计算机控制远程的一 台计算机或者多台计算机。这样，远程控制的应用便可以扩展到更多领域，如远程办公、远程技术支持、远程交流、远程维护和管理、远程监视等等。<br>
  
  随着桌面云市场的迅猛发展。国内外各大云计算服务提供商都纷纷推出基于 各种远程桌面控制协议实现的桌面云服务。其中以Microsoft的RDP协议，citrix 的ICA协议，vmware的PCOIP协议，开源的SPICE协议最为出名。Microsoft的RDP协议最初也是从citrix购买的。Microsoft在其基础上做了不断的优化改进，从RDP7.1开始支持RemoteFX。RemoteFX可以给每个桌面提供一个虚拟图形处理器支持2D、3D图形加速，使得RDP协议拥有了非凡的用户视觉效果体验。相较于RDP协议，citrix的ICA协议功能更加完善。ICA协议不仅能够实现带宽控制，而且还具有平台无关性。<br>
  
  近年来VMware也推出了自己的PCoIP协议，PCoIP协议是专门为桌面虚拟 化环境设计的，目的就是为了给用户带来高分比率和高流畅度的虚拟桌面图像。相较于以上的三种协议，VNC更加简洁轻便。VNC是虚拟网络计算机的缩写。VNC作为一款应用于远程桌面控制的软件，其设计初衷并非应用于桌面虚拟化环境。最开始VNC只是作为一款终端连接软件使用，客户端和服务端都是对等的实体物理机，通过VNC客户端与服务端可以进行一般的远程终端控制。因此，VNC设计上采为尽量简单的方式，除了对鼠标、键盘的支持外，对外设并未支持转向功能，也没有对音频播放进行处理。VNC是基于RFB（Remote Frame Buffer）远程帧缓冲的协议。RFB协议工作在帧缓冲层，对于操作系统如何渲染生成图像并不关心，仅仅是简单的“截图-编码-重绘”，所以对于不同的操作系统平台VNC都能很好的运行使用。RFB协议是真正意义上的“瘦客户机”协议。减少对客户端处理工作的需求是RFB协议设计的特点，因为尽量简单的客户端处理逻辑可以降低对硬件配置的要求，使得RFB协议可以运行在众多的终端设备之上。RFB协议对于客户端是无状态的。<br>
  
# 2 理论及关键技术
## 2.1远程控制相关理论
  远程桌面控制系统是指系统的使用者利用计算机等终端通过网络连接被控 制的终端，将被控终端系统的桌面环境显示到自己的终端之上，以达到通过本地 终端对远程终端的配置，修改，或者访问外部设备等工作。以往远程控制往往发生在两台或多台计算机之间，通常由于网络的情况，最初也只应用于局域网中的电脑之间。远程并不代表距离上的远近，而是指通过网络而不是直接控制电脑的方式。因此远程控制必须通过网络才能进行。本地终端作为主控端，同时也是客户端，发出操作指令；而远程被控制的终端则被称为被控端或者服务器端，对指令进行相应。如今远程控制已经不仅仅局限于远程电脑桌面控制，而如今通过终端远程控制各种电器设备都已经成为可能。远程控制功能主要由软件实现，远程控制软件通常由客户端程序和服务器程序组成，客户端安装在主控端，服务器安装在被控端，使用时双方建立连接，客户端发送远程控制命令，控制服务器的操作。在远程桌面控制应用中，主控端设备需要通过网络在具体的技术基础上实现 远端服务器的屏幕图像输出，而采用的桌面共享技术则是保证主控端高效截取被 控端主机的屏幕信息的关键。 桌面共享出现在操作系统 GUI 之后，其目的就是在一些场合可以远程显示服务器屏幕的显示内容，或者以一种虚拟终端的概念出现，使远端用户感觉就坐在主机前操作。现在流行的操作系统都提供一定的用户图形界面。桌面作为计算机信息显示的主要方式，是对用户极为重要的人机交互接口。 常见的屏幕共享技术可以分为以下几类：主要为利用操作系统底层的 GUI 矢量指令；利用屏幕复制和无失真压缩算法；利用屏幕复制和特殊的有失真压缩算法等方式。<br>
  
  对于远程桌面控制系统而言，在主控端显示被控端的桌面是功能实现的关键 点之一。图像显示的一个重要概念是分辨率。分辨率就是屏幕图像的精密度，是 指显示器所能显示的像素的多少。由于屏幕上的点、线和面都是由像素组成的， 显示器可显示的像素越多，画面就越精细，同样的屏幕区域内能显示的信息也越 多，所以分辨率是个非常重要的性能指标之一。可以把整个图像想象成是一个大 型的棋盘，而分辨率的表示方式就是所有经线和纬线交叉点的数目。<br>
  
|标屏	|分辨率	|率宽屏	|分辨率
|:----:  |:----: |:----: |:----:
|QVGA	|320*240	|WQVGA	|400*240|
|VGA	|640*480	|WVGA	|800*480|
|SVGA	|800*600	|WSVGA	|1024*600|
|XGA	|1024*768	|WXGA	|1280*800|
|XGA+	|1152*864	|WXGA+	|1366*768|
|SXGA	|1280*1024	|WSXGA	|1440*900|
|SXGA+	|1400*1050	|WSXGA+	|1680*1050|
|UXGA	|1600*1200	|WUXGA	|1900*1200|
|QXGA	|2048*1536	|WQXGA	|2560*1600|
## 2.2相关协议
### 2.2.1 RDP协议
RDP是由 MicroSoft 公司开发的应用层协议，该协议是对国际电信联盟发布的一个国际标准的多通道会议协议T.120的一个扩展，它是微软 Windows-based TerminalServices 应用的协议。终端服务的工作原理是客户机和服务器通过TCP/IP协议和标准的局域网架构联系。通过客户端终端，将客户机的输入传递到终端服务器上，再把服务器上的显示传递回客户端。客户端不需要具有计算能力，至多只需要提供一定的缓存能力。由表2-2可以看出，RDP协议是基于标准TCP连接，经过多层将数据流传输于客户端与服务器之间。并通过多层协议使得协议从功能上可以适用于更多的远程控制应用环境。在这一协议下，客户端桌面共享的显示更新策略是由服务器定时发送更新信息的。<br>


|RDP层	|应用程序共享 Application Sharing
|:----:  |:----: 
|SEC层	|加密解密Security Layer
|MCS层	|普通会议控制 Generic Conference Control
|GCC层	|多点通信服务 Multipoint Communication Service
|ISO层	|传输服务 ISO DP 8073
|TCP层	|TCP服务 TCP Service|
### 2.2.2 RFB协议
RFB是一个用于远程访问图形用户界面的简单协议。由于RFB协议工作在帧缓冲层，不涉及上层操作系统的图像渲染接口，因此适用于所有窗口系统。用户使用的远程终端称为RFB客户端，引起帧缓冲改变的终端称为RFB服务器端。RFB 协议设计时主要考虑的是尽量减少对客户端的需求，尽可能简化客户端的任务，因此RFB协议中客户端不需要完成复杂运算，只需将服务器发送过来的桌面图片在本地进行重绘，并且将用户操作的事件回传给服务器即可。在服务器端保存着本地Framebuffer信息以及客户端FrameBuffer信息，若客户端的操作导致了本地FrameBuffer的变化，服务器会判断当前FrameBuffer与客户端的 Framebuffer是否有变化，若有变化，则将变化的部分回送给客户端。RFB 协议主要涉及图像显示协议，输入协议，像素数据表示，协议扩展，协议消息几部分，其工作流程分为初次握手阶段和正常协议交互阶段。
## 2.3 图像压缩
两种远程控制领域较常用的协议中，无论是服务器主动定时向客户端发送显示内容更新，还是等待客户端发送更新请求的方式，都涉及到传输过程中对图像传输内容的压缩。在RFB协议中，显示协议通过帧缓冲刷新机制，每次更新只发送图像发生改动的矩阵，并对矩阵进行压缩，而且在传输过程中只需要传输桌面截图的子集的压缩。对数据的压缩包括对图像的压缩以及对压缩后数据流的压缩两部分。图像压缩的实质就是以较少的比特通过有损或者无损的方式来表示原本的像素矩阵的技术。图像数据之所以能被压缩，就是因为数据中存在着冗余。图像数据的冗余主要表现为：图像中相邻像素间的相关性引起的空间冗余；图像序列中不同帧之间存在相关性引起的时间冗余；不同彩色平面或频谱带的相关性引起的频谱冗余。数据压缩的目的就是通过去除这些数据冗余来减少表示数据所需 的比特数。由于图像数据量的庞大,在存储、传输、处理时非常困难,因此图像数 据的压缩就显得非常重要。

对于远程桌面面控制系统，传递的图像将会相当于一个图像序列，其中连续的帧动画之间会具有极大的相关性，因此在桌面图像的处理过程中，需要针对这一特性对传输的图像数据进行处理。数字图像中各个像素是不独立的，其相关性大。在图像画面上，经常有很多像素有相同或接近的灰度。就电视画面而言，同 一行中相邻两个像素或相邻两行间的像素，其相关系数可达0.9以上，而相邻两帧之间的相关性比帧内相关性一般说还要大些。因此，图像处理中信息压缩的潜力很大；数字图像处理的信息大多是二维信息，处理信息量很大。如一幅256×256低分辨率黑白图像，要求约64kbit的数据量；对高分辨率彩色512×512图像，则要求768kbit数据量；如果要处理 30 帧/秒的电视图像序列，则每秒要求500kbit～22.5Mbit数据量。因此对计算机的计算速度、存储容量等要求较高。

## 2.4数据压缩
数据压缩是指在不丢失信息的前提下，缩减数据量以减少存储空间，提高其 传输、存储和处理效率的一种技术方法。或按照一定的算法对数据进行重新组织， 减少数据的冗余和存储的空间。数据压缩包括有损压缩和无损压缩。数据压缩的理论基础是信息论。从信息的角度来看，压缩就是去除掉信息中的冗余，即去除掉确定的或可推知的信息，而保留不确定的信息，也就是用一种更接近信息本质的描述来代替原有的冗余的描述，这个本质的东西就是信息量。一种非常简单的压缩方法是行程长度编码，这种方法使用数据及数据长度这样简单的编码代替同样的连续数据，这是无损数据压缩的一个实例。这种方法经常用于办公计算机以更好地利用磁盘空间、或者更好地利用计算机网络中的带宽。对于电子表格、文本、可执行文件等这样的符号数据来说，无损是一个非常关键的要求，因为除了一些有限的情况，大多数情况下即使是一个数据位的变化都是无法接受的。<br>

# 3 系统设计与实现
## 3.1 结构设计
![](https://github.com/liutianluo888/remote_desktop/blob/main/%E5%9B%BE%E7%89%871.png)  
图3-1 结构设计流程图
## 3.2 功能实现
### 3.2.1 客户端
1. 初始化socket。对主机ip进行打包，变成长度为4的数据。开始一个新的线程。
```   
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
```
2.图形界面的创建。创建一个GUI界面，填入名称，框以及滑动块。在host中输入要控制的主机的ip地址及端口，在下面通过滑动滑块可以调整控制屏幕的大小，转化为自己想要的显示屏幕大小。

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

3.创建了一个基于Canvas的框，鼠标事件和键盘事件都是在这个框内执行。首先是将服务端发来的数据（图片）长度解包，判断解包的长度与缓冲区的大小。如果缓冲区大小更大，说明还可以再接受一个图片。后将图片用unit8进行编码，计算图片的长和宽用于构建框。

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

4.鼠标操作与键盘操作。这里的操作是在上述的框中进行的。当客户端按鼠标左键时，根据上下这两部分代码，服务端也会产生一个按下鼠标左键的行为。同样，客户端按鼠标右键或滚动滚轮时，在服务端也会对应相应的操作。当客户端按键盘时，服务端也会有相应的操作。如若客户端按“a”键，服务端也会是一个按了“a”键的操作。这部分是客户端的代码，会将其对应服务发送给服务端，服务端对应代码进行接收并解析协议，执行操作。
```
def BindEvents(canvas):
    global soc, scale
    def EventDo(data):
        soc.sendall(data)
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
  ```

5.快捷方式。快捷命令函数与tkinter布局的界面上的触发事件绑定，触发事件后即向服务端发送相应的操作。

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

6.用户界面设置。使用tkinter进行窗口设置，root为主窗口，使用menu函数设置该窗口的菜单，并通过add_command函数设置菜单的相关功能，同时使用add_separator()函数为菜单栏添加分割线。在此处使用Canvas并添加图片以增添窗口的美观度。布局使用的是pack函数，这样可以随意改变窗口的大小而始终使元素位于中间位置。还使用了frame框架使相关元素保持一执性。

      root = Tk()
      root.title("remote-desktop")
      root.geometry('400x400')
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
      viewmenu.add_command(label="Show funtion",command=View)
      menubar.add_cascade(label="View",menu=viewmenu)

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
      root.mainloop()

7.窗口触发函数设置。Function窗口为二级窗口，使用Toplevel()进行设置，其格式设置方式与root基本相同，这里不再赘述。新窗口的打开调用命令行来完成。参照样式函数Preferences()使用grid进行布局，使得host与scale可以对齐。由于其位置固定，此处采用固定窗口设计。

      def View():
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

### 3.2.2 服务端
1. 对应于客户端的键盘操作。将键盘上所有字母，数字及操作对应的地址编码与操作或值相对应。比如当客户端按“tab”键时，通过以下函数可使服务端完成一个按“tab”键的操作。

```
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
           …… 

```
2.鼠标与键盘的执行。接收客户端发来的协议，对其进行解包，获得编码地址与op，key值。根据op值与key值判断进行的操作是鼠标左键按下或者弹起。或是鼠标右键按下或者弹起，或是滚轮的操作或是键盘输入，或是快捷方式。进行相应模块后，根据（x，y）值将鼠标移到相应位置并进行操作。如要进行关闭某个页面的操作，（x，y）可以定位到×的位置，op与key可以判断这是一个鼠标左键按下的操作，就可以完成关闭这个页面的操作。键盘输入和快捷方式与上述代码相对应，可以知道具体为什么操作，判断出来后即可执行相应操作。
```def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
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
 ```

3.进行图像加法。将截取的图片进行编码，将其打包并计算数据长度。将数据长度与数据都发送给客户端。计算第二张图片的大小为l1与两张图片的差值l2，如果l1>l2，则将差值图片发送给客户端，否则则直接把第二张图片发给客户端。
```def handle(conn):
    global img, imbyt
    lock.acquire()
    if imbyt is None:
        imorg = np.asarray(ImageGrab.grab())
        _, imbyt= cv2.imencode(".jpg", imorg, [cv2.IMWRITE_JPEG_QUALITY,IMQUALITY]
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
```

4.用户界面设置。使用方法与客户端基本相同，只是此处呈现本机IP地址，采用命令行获得，并切片提取IP进行展示。
```def Dark_view():
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
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

viewmenu=Menu(menubar,tearoff=False)
viewVar=IntVar()
viewmenu.add_radiobutton(label="Light",command=Light_view,variable=viewVar,value=1)
viewmenu.add_radiobutton(label="Dark",command=Dark_view,variable=viewVar,value=2)
menubar.add_cascade(label="View",menu=viewmenu)

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
```



# 4 系统测试及分析
## 4.1 系统运行环境
![](https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif) 
图4-1 系统运行环境
## 4.2 测试过程及结果
### 4.2.1软件安装
选择合适的路径来安装软件。












图4-2 安装路径选择
安装完成后选择“Finish”，结束安装过程。













图4-3 软件安装成功界面


图4-4 软件图标

### 4.2.2 界面展示
#### 4.2.2.1.客户端


1. 初始界面














图4-5 初始界面
2. 菜单栏介绍
1）“File”功能介绍
点击“New connection”即可新建一个连接。
点击“Preferences”，会出现如下图4-6所示的情况。
点击“Exit”即可退出程序，关闭该软件。







图4-6 “File”功能













图4-7 “Prefences”功能

2）“View”功能
点击“Light”即为“日间模式”，界面亮度改变，如图4-9所示。
点击“Dark”即为“夜间模式”，界面亮度改变，如图4-10所示。
点击“Set”即可将“Preference”中的默认参数设置到界面中。
点击“Show function”可以展示快捷功能，如图4-11所示。







图4-8 “View”功能













图4-9 “Light”功能













图4-10 “Dark”功能











图4-11 “Show function”功能
3）“Help”
点击“Technical support”，即可自动打开浏览器跳转到G码云，查看该软件所使用的相关库等技术支持。
点击“Service status”，即可获得当前服务的状态。
点击“Introductions”，即可获得关于该软件的简单说明
点击“About”，即可获得软件信息。







图4-12 “Help”功能




图4-13 “Technical support”功能








图4-14 “Service status”功能










图4-15 “Introductions”功能








图4-16 “About”功能
#### 4.2.2.2.服务端
1. 初始界面









图4-17 初始界面
2.菜单栏介绍
1）“File”功能（具体功能与客户端一致）






图4-18 “File”功能
2）“View”功能（具体功能与客户端一致）






图4-19 “View”功能
3）“Help”功能（具体功能与客户端一致）






图4-20 “Help”功能
### 4.2.3 功能测试
#### 4.2.3.1连接
如图4-21所示，可以发现两台主机可以正常连接，且“function”快捷功能界面可以正常打开。













图4-21 连接测试
并且，可以发现能够在客户端对服务端进行正常的键盘和鼠标操作。如图4-22所示，可以使用客户端的鼠标将服务端打开的文件关闭。











图4-22 鼠标操作
除此之外，如图4-23所示，可以使用客户端的键盘在服务端的文档上进行编辑。











图4-23 键盘操作
#### 4.2.3.2快捷功能
1. “关机”
可以发现服务端已关机，客户端呈现的界面如图4-24所示。









图4-24 “关机”操作
2. “休眠”
可以发现服务端已休眠，客户端呈现的界面如图4-25所示。








图4-25 “休眠”操作
3. “摄像头”
可以发现服务端打开了摄像头，如图4-26所示，客户端呈现的界面如图4-27所示。










图4-26 服务端摄像头状态







图4-27 “摄像头”操作
4. “画图板”
可以发现服务端打开了画图板，客户端呈现的界面如图4-28所示。









图4-28 “画图板”操作
5. “任务管理器”
可以发现服务端打开了任务管理器，客户端呈现的界面如图4-29所示。












图4-29 “任务管理器”操作
6. “软键盘”
可以发现服务端打开了软键盘，客户端呈现的界面如图4-30所示。









图4-30 “软键盘”操作
## 4.3 结果分析
从测试结果中可以看到，在远程控制下，我们可以对被控制电脑直接进行任何操作，且无需了解被控制电脑的账号和密码信息。同时，我们还添加了一些快捷指令，这样就可以更方便的对远程的电脑进行常见的操作，譬如关机等。
不足之处在于对网速有一定要求，只有在网络条件较好的情况下才能对被控制电脑流畅地执行操作，否则就会出现严重的卡顿现象，影响使用。其次，本次实验基于内网进行测试，server与client端需处于同一局域网下，否则则无法控制。这对于满足实际需要产生了一些局限性。
# 5 总结与展望
## 5.1总结
本次实验中，我们设计实现了一组远程控制软件，通过分别安装我们的server.exe及client.exe软件即可实现两台电脑间的远程控制。<br>
此软件相对于一些常见软件（如VNC）而言，存在一些优点，即我们的软件无须了解被控制端的账号和密码即可对其进行控制，也不需要被控制端关闭防火墙和360等安全软件。<br>
由此也可见，远程控制软件可以无声息的实现对电脑的所有控制。因此，我们也可以发现入侵检测系统的重要意义。现在远程控制软件层出不穷，其控制力可大可小，在方便我们生活的同时，也对我们的安全造成了一定的威胁。因此我们在平时对电脑的使用中，要重视其安全问题，保证我们的电脑和个人信息处于安全的环境，同时注意下载内容的安全，确保其不含木马病毒，只有这样，我们才能在保证安全的情况下保障需求。<br>
## 5.2展望
本实验是在内网中进行的，并没有进行内网穿透，即没有在两个网段中进行验证。而对于远程控制软件而言，大多数使用情景为一对一控制，并不适合直接将受控端部署在服务器上，这样来说我们的软件使用范围不大。在实际应用中，需要考虑如何使客户端和服务器端安装后即位于物联网中，这样才能真正实现我们远程控制的目的。<br>
