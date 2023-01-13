if __name__ == '__main__':
    w1 = window_about()  # about
    w2 = window_update()  # update
    w3 = MyWidget()
    w4 = window4()
    action1.triggered.connect(w1.activate)
    action2.triggered.connect(w2.activate)
    action3.triggered.connect(w3.activate)
    action4.triggered.connect(w4.activate)
    action5.triggered.connect(w4.onrunstart)
    button_action.triggered.connect(w3.key_activate)
    w1.setStyleSheet(style_sheet_ori)
    w2.setStyleSheet(style_sheet_ori)
    w4.setStyleSheet(style_sheet_ori)
    w3.setStyleSheet(style_sheet_cha)
    app.exec()
    