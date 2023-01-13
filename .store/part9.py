class window4(QWidget):  # Customization settings
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.setUpMainWindow()
        self.resize(839, 475)
        self.center()
        self.setWindowTitle('Customization settings')
        self.setFocus()

    def setUpMainWindow(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl1 = QLabel('Number of side-by-side windows:', self)

        self.le1 = QLineEdit(self)
        ncount = codecs.open('multinum.txt', 'r', encoding='utf-8').read()
        self.le1.setText(ncount)

        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl2 = QLabel('Apps at running (copy and paste the apps you want to control from this frame to the one below):', self)

        self.te1 = QTextEdit(self)
        resp = applescript.tell.app("System Events", '''
            tell application "System Events"
                set processName to name of processes
                set processDic to processName
                return processDic
            end tell''')
        assert resp.code == 0, resp.err
        runnin = resp.out.replace(', ', '\n')
        runninlist = runnin.split('\n')
        runninlist.sort()
        runnin2 = '\n'.join(runninlist)
        self.te1.setText(runnin2)

        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl3 = QLabel('Apps to control (one app each line):', self)

        self.te2 = QTextEdit(self)
        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.te2.setText(cont)

        btn4_1 = QPushButton('Save', self)
        btn4_1.setMaximumHeight(20)
        btn4_1.setMinimumWidth(80)
        btn4_1.clicked.connect(self.saveapps)

        widg1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addWidget(lbl1)
        blay1.addWidget(self.le1)
        blay1.addStretch()
        widg1.setLayout(blay1)

        widg2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addWidget(lbl2)
        blay2.addStretch()
        widg2.setLayout(blay2)

        widg3 = QWidget()
        blay3 = QVBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addWidget(widg2)
        blay3.addWidget(self.te1)
        widg3.setLayout(blay3)

        widg4 = QWidget()
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addWidget(lbl3)
        blay4.addStretch()
        widg4.setLayout(blay4)

        widg5 = QWidget()
        blay5 = QVBoxLayout()
        blay5.setContentsMargins(0, 0, 0, 0)
        blay5.addWidget(widg4)
        blay5.addWidget(self.te2)
        widg5.setLayout(blay5)

        blay6 = QVBoxLayout()
        blay6.setContentsMargins(20, 20, 20, 20)
        blay6.addWidget(widg1)
        blay6.addWidget(widg3)
        blay6.addWidget(widg5)
        blay6.addWidget(btn4_1)
        self.setLayout(blay6)
        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.onTimer)

    def saveapps(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        with open('multinum.txt', 'w', encoding='utf-8') as f0:
            f0.write(self.le1.text())

        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = self.te2.toPlainText()
        with open(fulldir2, 'w', encoding='utf-8') as f0:
            f0.write(cont)
        self.close()

    def onrunstart(self):
        if action5.isChecked():
            self.counter = 5
            self.mytimer.start(1000)
        if not action5.isChecked():
            with open('showlist.txt', 'w', encoding='utf-8') as f0:
                f0.write('')

    def onTimer(self):
        if action5.isChecked():
            self.counter -= 1
            if self.counter == 0:
                self.mytimer.stop()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.onlist = []
                self.showlist0 = []
                resp = applescript.tell.app("System Events", '''
                    tell application "System Events"
                        set processName to name of processes
                        set processDic to processName
                        return processDic
                    end tell''')
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                assert resp.code == 0, resp.err
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                runlist = resp.out.split(', ')

                home_dir = str(Path.home())
                tarname1 = "OliveAppPath"
                fulldir1 = os.path.join(home_dir, tarname1)
                if not os.path.exists(fulldir1):
                    os.mkdir(fulldir1)
                tarname2 = "tarlist.txt"
                fulldir2 = os.path.join(fulldir1, tarname2)
                cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
                tarlist = cont.split('\n')
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()

                for i in range(len(tarlist)):
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    if tarlist[i] in runlist:
                        QApplication.processEvents()
                        QApplication.restoreOverrideCursor()
                        cmd = f'''
                        on count_windows_on_current_space(process_name)
                            tell application "System Events"
                                tell process process_name
                                    return count of windows
                                end tell
                            end tell
                        end count_windows_on_current_space
    
                        on name_windows_on_current_space(process_name)
                            tell application "System Events"
                                tell process process_name
                                    #return name of windows
                                    set names to name of windows
                                    set AppleScript's text item delimiters to "///"
                                    set strnam to names as text
                                    return strnam
                                end tell
                            end tell
                        end name_windows_on_current_space
    
                        tell application "{tarlist[i]}"
                            if my count_windows_on_current_space("{tarlist[i]}") > 0 then
                                try
                                    return my name_windows_on_current_space("{tarlist[i]}")
                                on error errorMessage
                                    return "F"
                                end try
                            end if
                        end tell'''
                        QApplication.processEvents()
                        QApplication.restoreOverrideCursor()
                        result = subprocess.run(['osascript', '-e', cmd], capture_output=True, encoding='UTF-8')
                        QApplication.processEvents()
                        QApplication.restoreOverrideCursor()
                        if result.stdout != '' and result.stdout != 'F':
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            multilist = result.stdout.replace('\n', '').split('///')
                            for n in range(len(multilist)):
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                if len(multilist[n]) > 15:
                                    QApplication.processEvents()
                                    QApplication.restoreOverrideCursor()
                                    multilist[n] = multilist[n][0:12] + '...'
                            for m in range(len(multilist)):
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                multilist[m] = str(tarlist[i]) + '\n~' + str(m + 1) + '~\n' + multilist[m]
                                self.showlist0.append(multilist[m])

                showcont = '☆'.join(self.showlist0)
                with open('showlist.txt', 'w', encoding='utf-8') as f0:
                    f0.write(showcont)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.counter = 5
                self.mytimer.start(1000)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def activate(self):  # 设置窗口显示
        resp = applescript.tell.app("System Events", '''
        tell application "System Events"
            set processName to name of processes
            set processDic to processName
            return processDic
        end tell''')
        assert resp.code == 0, resp.err
        runnin = resp.out.replace(', ', '\n')
        runninlist = runnin.split('\n')
        runninlist.sort()
        runnin2 = '\n'.join(runninlist)
        self.te1.setText(runnin2)

        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.te2.setText(cont)

        self.show()
        self.raise_()
        self.activateWindow()

style_sheet_cha = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QWidget{
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 20px;
}
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
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px solid gray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
'''
style_sheet_ori = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QPushButton{
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px solid gray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
'''