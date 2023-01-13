class MyWidget(QWidget):  # 主窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.center()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.clicktime = 0
        self.onlist = []
        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        if not os.path.exists(fulldir2):
            cont = codecs.open('tarlist.txt', 'r', encoding='utf-8').read()
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write(cont)

    def everytimefirst(self):
        cont = codecs.open('showlist.txt', 'r', encoding='utf-8').read()
        self.showlist = cont.split('☆')
        self.totalnum = len(self.showlist)
        if self.totalnum / 5 <= 1:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(190)
            if self.totalnum == 0:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(240)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt1.setText('None')
            if self.totalnum == 1:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(240)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt1.setText('None')
            if self.totalnum == 2:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(454)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
            if self.totalnum == 3:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(668)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
            if self.totalnum == 4:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(882)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
            if self.totalnum == 5:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(1096)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
        if 1 < self.totalnum / 5 <= 2:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(350)
            self.setFixedWidth(1096)
            if self.totalnum == 6:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
            if self.totalnum == 7:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
            if self.totalnum == 8:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
            if self.totalnum == 9:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
            if self.totalnum == 10:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
        if 2 < self.totalnum / 5 <= 3:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(510)
            self.setFixedWidth(1096)
            if self.totalnum == 11:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
            if self.totalnum == 12:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
            if self.totalnum == 13:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
            if self.totalnum == 14:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
            if self.totalnum == 15:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
        if 3 < self.totalnum / 5 <= 4:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(670)
            self.setFixedWidth(1096)
            if self.totalnum == 16:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
            if self.totalnum == 17:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
            if self.totalnum == 18:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
            if self.totalnum == 19:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt19.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
                self.bt19.setText(self.showlist[18])
            if self.totalnum == 20:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt19.setVisible(True)
                self.bt20.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
                self.bt19.setText(self.showlist[18])
                self.bt20.setText(self.showlist[19])
        if self.totalnum / 5 > 4:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(690)
            self.setFixedWidth(1096)
            self.all_invisible()
            self.widg2.setVisible(True)
            self.widg3.setVisible(True)
            self.widg4.setVisible(True)
            self.bt1.setVisible(True)
            self.bt2.setVisible(True)
            self.bt3.setVisible(True)
            self.bt4.setVisible(True)
            self.bt5.setVisible(True)
            self.bt6.setVisible(True)
            self.bt7.setVisible(True)
            self.bt8.setVisible(True)
            self.bt9.setVisible(True)
            self.bt10.setVisible(True)
            self.bt11.setVisible(True)
            self.bt12.setVisible(True)
            self.bt13.setVisible(True)
            self.bt14.setVisible(True)
            self.bt15.setVisible(True)
            self.bt16.setVisible(True)
            self.bt17.setVisible(True)
            self.bt18.setVisible(True)
            self.bt19.setVisible(True)
            self.bt20.setVisible(True)
            self.bt1.setText(self.showlist[0])
            self.bt2.setText(self.showlist[1])
            self.bt3.setText(self.showlist[2])
            self.bt4.setText(self.showlist[3])
            self.bt5.setText(self.showlist[4])
            self.bt6.setText(self.showlist[5])
            self.bt7.setText(self.showlist[6])
            self.bt8.setText(self.showlist[7])
            self.bt9.setText(self.showlist[8])
            self.bt10.setText(self.showlist[9])
            self.bt11.setText(self.showlist[10])
            self.bt12.setText(self.showlist[11])
            self.bt13.setText(self.showlist[12])
            self.bt14.setText(self.showlist[13])
            self.bt15.setText(self.showlist[14])
            self.bt16.setText(self.showlist[15])
            self.bt17.setText(self.showlist[16])
            self.bt18.setText(self.showlist[17])
            self.bt19.setText(self.showlist[18])
            self.bt20.setText(self.showlist[19])
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.center()

    def setUpMainWindow(self):
        self.bt1 = QPushButton('', self)
        self.bt1.setFixedSize(200, 150)
        self.bt1.clicked.connect(self.clickplus1)
        self.bt1.setVisible(False)

        self.bt2 = QPushButton('', self)
        self.bt2.setFixedSize(200, 150)
        self.bt2.clicked.connect(self.clickplus2)
        self.bt2.setVisible(False)

        self.bt3 = QPushButton('', self)
        self.bt3.setFixedSize(200, 150)
        self.bt3.clicked.connect(self.clickplus3)
        self.bt3.setVisible(False)

        self.bt4 = QPushButton('', self)
        self.bt4.setFixedSize(200, 150)
        self.bt4.clicked.connect(self.clickplus4)
        self.bt4.setVisible(False)

        self.bt5 = QPushButton('', self)
        self.bt5.setFixedSize(200, 150)
        self.bt5.clicked.connect(self.clickplus5)
        self.bt5.setVisible(False)

        self.bt6 = QPushButton('', self)
        self.bt6.setFixedSize(200, 150)
        self.bt6.clicked.connect(self.clickplus6)
        self.bt6.setVisible(False)

        self.bt7 = QPushButton('', self)
        self.bt7.setFixedSize(200, 150)
        self.bt7.clicked.connect(self.clickplus7)
        self.bt7.setVisible(False)

        self.bt8 = QPushButton('', self)
        self.bt8.setFixedSize(200, 150)
        self.bt8.clicked.connect(self.clickplus8)
        self.bt8.setVisible(False)

        self.bt9 = QPushButton('', self)
        self.bt9.setFixedSize(200, 150)
        self.bt9.clicked.connect(self.clickplus9)
        self.bt9.setVisible(False)

        self.bt10 = QPushButton('', self)
        self.bt10.setFixedSize(200, 150)
        self.bt10.clicked.connect(self.clickplus10)
        self.bt10.setVisible(False)

        self.bt11 = QPushButton('', self)
        self.bt11.setFixedSize(200, 150)
        self.bt11.clicked.connect(self.clickplus11)
        self.bt11.setVisible(False)

        self.bt12 = QPushButton('', self)
        self.bt12.setFixedSize(200, 150)
        self.bt12.clicked.connect(self.clickplus12)
        self.bt12.setVisible(False)

        self.bt13 = QPushButton('', self)
        self.bt13.setFixedSize(200, 150)
        self.bt13.clicked.connect(self.clickplus13)
        self.bt13.setVisible(False)

        self.bt14 = QPushButton('', self)
        self.bt14.setFixedSize(200, 150)
        self.bt14.clicked.connect(self.clickplus14)
        self.bt14.setVisible(False)

        self.bt15 = QPushButton('', self)
        self.bt15.setFixedSize(200, 150)
        self.bt15.clicked.connect(self.clickplus15)
        self.bt15.setVisible(False)

        self.bt16 = QPushButton('', self)
        self.bt16.setFixedSize(200, 150)
        self.bt16.clicked.connect(self.clickplus16)
        self.bt16.setVisible(False)

        self.bt17 = QPushButton('', self)
        self.bt17.setFixedSize(200, 150)
        self.bt17.clicked.connect(self.clickplus17)
        self.bt17.setVisible(False)

        self.bt18 = QPushButton('', self)
        self.bt18.setFixedSize(200, 150)
        self.bt18.clicked.connect(self.clickplus18)
        self.bt18.setVisible(False)

        self.bt19 = QPushButton('', self)
        self.bt19.setFixedSize(200, 150)
        self.bt19.clicked.connect(self.clickplus19)
        self.bt19.setVisible(False)

        self.bt20 = QPushButton('', self)
        self.bt20.setFixedSize(200, 150)
        self.bt20.clicked.connect(self.clickplus20)
        self.bt20.setVisible(False)

        self.widg1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(self.bt1)
        blay1.addWidget(self.bt2)
        blay1.addWidget(self.bt3)
        blay1.addWidget(self.bt4)
        blay1.addWidget(self.bt5)
        blay1.addStretch()
        self.widg1.setLayout(blay1)

        self.widg2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(self.bt6)
        blay2.addWidget(self.bt7)
        blay2.addWidget(self.bt8)
        blay2.addWidget(self.bt9)
        blay2.addWidget(self.bt10)
        blay2.addStretch()
        self.widg2.setLayout(blay2)

        self.widg3 = QWidget()
        blay3 = QHBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addStretch()
        blay3.addWidget(self.bt11)
        blay3.addWidget(self.bt12)
        blay3.addWidget(self.bt13)
        blay3.addWidget(self.bt14)
        blay3.addWidget(self.bt15)
        blay3.addStretch()
        self.widg3.setLayout(blay3)

        self.widg4 = QWidget()
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addStretch()
        blay4.addWidget(self.bt16)
        blay4.addWidget(self.bt17)
        blay4.addWidget(self.bt18)
        blay4.addWidget(self.bt19)
        blay4.addWidget(self.bt20)
        blay4.addStretch()
        self.widg4.setLayout(blay4)

        widg0 = QWidget()
        blay0 = QVBoxLayout()
        blay0.setContentsMargins(20, 20, 20, 20)
        blay0.addStretch()
        blay0.addWidget(self.widg1)
        blay0.addWidget(self.widg2)
        blay0.addWidget(self.widg3)
        blay0.addWidget(self.widg4)
        blay0.addStretch()
        widg0.setLayout(blay0)

        blay = QHBoxLayout()
        blay.setContentsMargins(0, 0, 0, 0)
        blay.addStretch()
        blay.addWidget(widg0)
        blay.addStretch()
        self.setLayout(blay)

    def clickplus1(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setDisabled(True)
        self.bt1.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt1.text()
            if gettext == 'None':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                button_action.setChecked(False)
                action3.setChecked(False)
            if gettext != 'None':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.onlist.append(gettext)
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus2(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt2.setDisabled(True)
        self.bt2.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt2.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus3(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt3.setDisabled(True)
        self.bt3.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt3.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus4(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt4.setDisabled(True)
        self.bt4.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt4.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus5(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt5.setDisabled(True)
        self.bt5.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt5.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus6(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt6.setDisabled(True)
        self.bt6.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt6.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus7(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt7.setDisabled(True)
        self.bt7.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt7.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus8(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt8.setDisabled(True)
        self.bt8.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt8.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus9(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt9.setDisabled(True)
        self.bt9.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt9.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus10(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt10.setDisabled(True)
        self.bt10.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt10.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus11(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt11.setDisabled(True)
        self.bt11.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt11.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus12(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt12.setDisabled(True)
        self.bt12.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt12.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus13(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt13.setDisabled(True)
        self.bt13.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt13.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus14(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt14.setDisabled(True)
        self.bt14.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt14.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus15(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt15.setDisabled(True)
        self.bt15.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt15.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus16(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt16.setDisabled(True)
        self.bt16.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt16.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus17(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt17.setDisabled(True)
        self.bt17.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt17.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus18(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt18.setDisabled(True)
        self.bt18.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt18.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus19(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt19.setDisabled(True)
        self.bt19.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt19.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def clickplus20(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt20.setDisabled(True)
        self.bt20.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        if self.clicktime < ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.clicktime += 1
            gettext = self.bt20.text()
            self.onlist.append(gettext)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
        if self.clicktime == ncount:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.showhide()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.cancel()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            action3.setChecked(False)
            button_action.setChecked(False)

    def showhide(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.clicktime = 0
        self.hidelist = list(set(self.showlist) - set(self.onlist))
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        for t in range(len(self.hidelist)):
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            pattern0 = re.compile(r'(.*?)\n~')
            result0 = pattern0.findall(self.hidelist[t])
            result0 = ''.join(result0)

            pattern = re.compile(r'~(.*?)~')
            result = pattern.findall(self.hidelist[t])
            result = int(''.join(result))
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()

            if result0 == 'Finder':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                cmd = f"""osascript -e '''
                tell application "Finder"
                    try
                        set collapsed of window {result} to true
                    on error errorMessage
                        tell application "Finder" to activate
                        delay 0.1
                        tell application "System Events" to tell process "Finder"
                            keystroke "m" using command down
                        end tell
                    end try
                end tell
                '''"""
                os.system(cmd)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if result0 != 'Finder':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                cmd = f"""osascript -e '''
                tell application "System Events"
                    tell application "{result0}"
                        try
                            set miniaturized of window {result} to true
                        on error errorMessage
                            tell application "{result0}" to activate
                            delay 0.1
                            tell application "System Events" to tell process "{result0}"
                                keystroke "m" using command down
                            end tell
                        end try
                    end tell
                end tell'''"""
                os.system(cmd)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
        for i in range(len(self.onlist)):
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            pattern0 = re.compile(r'(.*?)\n~')
            result0 = pattern0.findall(self.onlist[i])
            result0 = ''.join(result0)

            pattern = re.compile(r'~(.*?)~')
            result = pattern.findall(self.onlist[i])
            result = ''.join(result)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()

            if result0 == 'Finder':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                cmd = f"""osascript -e '''
                tell application "Finder"
                    try
                        set collapsed of window {result} to false
                    on error errorMessage
                        reopen
                        activate
                    end try
                end tell
                '''"""
                os.system(cmd)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if result0 != 'Finder':
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                cmd = f"""osascript -e '''
                tell application "{result0}"
                    try
                        set miniaturized of window {result} to false
                        activate
                    on error errorMessage
                        reopen
                        activate
                    end try
                end tell'''"""
                os.system(cmd)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
        self.onlist = []
        self.hidelist = []

    def all_invisible(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setVisible(False)
        self.bt2.setVisible(False)
        self.bt3.setVisible(False)
        self.bt4.setVisible(False)
        self.bt5.setVisible(False)
        self.bt6.setVisible(False)
        self.bt7.setVisible(False)
        self.bt8.setVisible(False)
        self.bt9.setVisible(False)
        self.bt10.setVisible(False)
        self.bt11.setVisible(False)
        self.bt12.setVisible(False)
        self.bt13.setVisible(False)
        self.bt14.setVisible(False)
        self.bt15.setVisible(False)
        self.bt16.setVisible(False)
        self.bt17.setVisible(False)
        self.bt18.setVisible(False)
        self.bt19.setVisible(False)
        self.bt20.setVisible(False)
        self.widg2.setVisible(False)
        self.widg3.setVisible(False)
        self.widg4.setVisible(False)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

    def restorebutton(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setDisabled(False)
        self.bt2.setDisabled(False)
        self.bt3.setDisabled(False)
        self.bt4.setDisabled(False)
        self.bt5.setDisabled(False)
        self.bt6.setDisabled(False)
        self.bt7.setDisabled(False)
        self.bt8.setDisabled(False)
        self.bt9.setDisabled(False)
        self.bt10.setDisabled(False)
        self.bt11.setDisabled(False)
        self.bt12.setDisabled(False)
        self.bt13.setDisabled(False)
        self.bt14.setDisabled(False)
        self.bt15.setDisabled(False)
        self.bt16.setDisabled(False)
        self.bt17.setDisabled(False)
        self.bt18.setDisabled(False)
        self.bt19.setDisabled(False)
        self.bt20.setDisabled(False)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt2.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt3.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt4.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt5.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt6.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt7.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt8.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt9.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt10.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt11.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt12.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt13.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt14.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt15.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt16.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt17.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt18.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt19.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt20.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')

    def activate(self):  # 设置窗口显示
        if action3.isChecked():
            self.restorebutton()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.everytimefirst()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.show()
            self.center()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFocus()
            self.raise_()
            self.activateWindow()
            button_action.setChecked(True)
        if not action3.isChecked():
            self.cancel()
            button_action.setChecked(False)

    def key_activate(self):  # 设置窗口显示
        if button_action.isChecked():
            self.restorebutton()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.everytimefirst()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.show()
            self.center()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFocus()
            self.raise_()
            self.activateWindow()
            action3.setChecked(True)
        if not button_action.isChecked():
            self.cancel()
            action3.setChecked(False)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        qr.moveCenter(cp)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        xy = str(qr.topLeft()).replace('PyQt6.QtCore.QPoint(', '').replace(')', '').split(', ')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.move(int(xy[0]), int(xy[1]))
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

    def cancel(self):  # 设置取消键的功能
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.close()
        self.restorebutton()

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()