class window_about(QWidget):  # 增加说明页面(About)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 说明页面内信息
        self.setUpMainWindow()
        self.resize(400, 380)
        self.center()
        self.setWindowTitle('About')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widg1 = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('olivemenu.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumWidth(100)
        l1.setMaximumHeight(100)
        l1.setScaledContents(True)
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(l1)
        blay1.addStretch()
        widg1.setLayout(blay1)

        widg2 = QWidget()
        lbl0 = QLabel('Olive', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(20)
        lbl0.setFont(font)
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(lbl0)
        blay2.addStretch()
        widg2.setLayout(blay2)

        widg3 = QWidget()
        lbl1 = QLabel('Version 0.1.8', self)
        blay3 = QHBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addStretch()
        blay3.addWidget(lbl1)
        blay3.addStretch()
        widg3.setLayout(blay3)

        widg4 = QWidget()
        lbl2 = QLabel('This app is open-sourced.', self)
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addStretch()
        blay4.addWidget(lbl2)
        blay4.addStretch()
        widg4.setLayout(blay4)

        widg5 = QWidget()
        lbl3 = QLabel('本软件开源。', self)
        blay5 = QHBoxLayout()
        blay5.setContentsMargins(0, 0, 0, 0)
        blay5.addStretch()
        blay5.addWidget(lbl3)
        blay5.addStretch()
        widg5.setLayout(blay5)

        widg6 = QWidget()
        lbl4 = QLabel('♥‿♥', self)
        blay6 = QHBoxLayout()
        blay6.setContentsMargins(0, 0, 0, 0)
        blay6.addStretch()
        blay6.addWidget(lbl4)
        blay6.addStretch()
        widg6.setLayout(blay6)

        widg7 = QWidget()
        lbl5 = QLabel('※\(^o^)/※', self)
        blay7 = QHBoxLayout()
        blay7.setContentsMargins(0, 0, 0, 0)
        blay7.addStretch()
        blay7.addWidget(lbl5)
        blay7.addStretch()
        widg7.setLayout(blay7)

        widg8 = QWidget()
        bt1 = QPushButton('The Author', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.intro)
        bt2 = QPushButton('Github Page', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.homepage)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg8.setLayout(blay8)

        widg9 = QWidget()
        bt3 = QPushButton('🍪\n¥5', self)
        bt3.setMaximumHeight(50)
        bt3.setMinimumHeight(50)
        bt3.setMinimumWidth(50)
        bt3.clicked.connect(self.donate)
        bt4 = QPushButton('🥪\n¥10', self)
        bt4.setMaximumHeight(50)
        bt4.setMinimumHeight(50)
        bt4.setMinimumWidth(50)
        bt4.clicked.connect(self.donate2)
        bt5 = QPushButton('🍜\n¥20', self)
        bt5.setMaximumHeight(50)
        bt5.setMinimumHeight(50)
        bt5.setMinimumWidth(50)
        bt5.clicked.connect(self.donate3)
        bt6 = QPushButton('🍕\n¥50', self)
        bt6.setMaximumHeight(50)
        bt6.setMinimumHeight(50)
        bt6.setMinimumWidth(50)
        bt6.clicked.connect(self.donate4)
        blay9 = QHBoxLayout()
        blay9.setContentsMargins(0, 0, 0, 0)
        blay9.addStretch()
        blay9.addWidget(bt3)
        blay9.addWidget(bt4)
        blay9.addWidget(bt5)
        blay9.addWidget(bt6)
        blay9.addStretch()
        widg9.setLayout(blay9)

        widg10 = QWidget()
        lbl6 = QLabel('© 2023 Ryan-the-hito. All rights reserved.', self)
        blay10 = QHBoxLayout()
        blay10.setContentsMargins(0, 0, 0, 0)
        blay10.addStretch()
        blay10.addWidget(lbl6)
        blay10.addStretch()
        widg10.setLayout(blay10)

        main_h_box = QVBoxLayout()
        main_h_box.addWidget(widg1)
        main_h_box.addWidget(widg2)
        main_h_box.addWidget(widg3)
        main_h_box.addWidget(widg4)
        main_h_box.addWidget(widg5)
        main_h_box.addWidget(widg6)
        main_h_box.addWidget(widg7)
        main_h_box.addWidget(widg8)
        main_h_box.addWidget(widg9)
        main_h_box.addWidget(widg10)
        main_h_box.addStretch()
        self.setLayout(main_h_box)

    def intro(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

    def homepage(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Olive')

    def donate(self):
        dlg = CustomDialog()
        dlg.exec()

    def donate2(self):
        dlg = CustomDialog2()
        dlg.exec()

    def donate3(self):
        dlg = CustomDialog3()
        dlg.exec()

    def donate4(self):
        dlg = CustomDialog4()
        dlg.exec()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def activate(self):  # 设置窗口显示
        self.show()
        self.raise_()
        self.activateWindow()