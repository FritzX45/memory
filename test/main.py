from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QMessageBox
from layout import *
from menu import *
from data import *
from study import *
from random import choice

q = choice(quest_list)
q.show_data(questionLb, result_answ, rbtn_list)

timer = QTimer()
timer.setInterval(1000)

def list_click():
    for q in quest_list:
        if q.question == qw_list.currentItem().text():
            q.show_data_study(pict_lb, ans_lb)
            break

def ok_click():
    global q
    if okey_btn.text() == "Відповісти":
        if button_group.checkedButton():
            q.chek_result(rbtn_list, result)
            show_result()
    else:
        q = choice(quest_list)
        q.show_data(questionLb, result_answ, rbtn_list)
        show_question()

def show_data():
    pass 
def check_result():
    pass

def start_study():
    timer.start()
    qw_list.clear()
    for q in quest_list:
        qw_list.addItem(q.question)
    menu_window.hide()
    study_window.show()

def back_to_menu():
    main_window.hide()
    study_window.hide()
    menu_window.show()

def timer_handler():
    time_lb.setText(str(int(time_lb.text())+1))
    if int(time_lb.text()) >= 600:
        m = QMessageBox()
        m.setWindowTitle("Час вичерпано!")
        m.setText("Досить навчатись")
        if m.exec_() == 1024:
            timer.stop()
            back_to_menu()

def start_test():
    menu_window.hide()
    main_window.show()

def crate_test():
    main_window.hide()
    crate_test.show()

test_btn.clicked.connect(start_test)
okey_btn.clicked.connect(ok_click)
create_btn.clicked.connect(start_study)
menu_btn.clicked.connect(back_to_menu)
qw_list.itemClicked.connect(list_click)
timer.timeout.connect(timer_handler)
#create_btn.clicked.connect(crate_test)

main_window = QWidget()
main_window.setWindowTitle('Memory card')
main_window.resize(600, 500)
main_window.move(0, 0)

menu_window = QWidget()
menu_window.setWindowTitle('Memory card menu')
menu_window.resize(400, 400)
menu_window.move(0, 0)

#crate_window = QWidget()
#crate_window.setWindowTitle('Crate test menu')
#crate_window.resize(400, 600)
#crate_window.move(0, 0)


menu_window.show()

menu_window.setLayout(menu_line)
main_window.setLayout(layout_card)

study_window = QWidget()
study_window.resize(700, 400)
study_window.setWindowTitle("Memory Card Study")
# study_window.move(0, 0)
study_window.setLayout(study_line)

#main_window.show()



app.exec_()