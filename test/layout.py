from PyQt5 . QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QSpinBox, QVBoxLayout, QPushButton, QGroupBox, QButtonGroup, QRadioButton

app = QApplication([])

def show_result():
    group_box.hide()
    group_box2.show()
    okey_btn.setText('Наступне питання')

def show_question():
    button_group.setExclusive(False)
    for rb in rbtn_list:
        rb.setChecked(False)
    button_group.setExclusive(True)
    group_box2.hide()
    group_box.show()
    okey_btn.setText("Відповісти")




menu_btn = QPushButton('Меню')
rest_btn = QPushButton('Відпочити')
rest_spin = QSpinBox()
rest_spin.setValue(30)

line1 = QHBoxLayout()
line1.addWidget(menu_btn, alignment=Qt.AlignLeft)
line1.addStretch(1)
line1.addWidget(rest_btn, alignment=Qt.AlignRight)
line1.addWidget(rest_spin, alignment=Qt.AlignRight)
line1.addWidget(QLabel('хвилин'), alignment=Qt.AlignRight)

questionLb = QLabel('Яблуко')
line2 = QHBoxLayout()
line2.addWidget(questionLb, alignment=Qt.AlignCenter)
group_box = QGroupBox('Варіанти відповідей')
button_group = QButtonGroup()

rbtn_list = []

for i in range (4):
    r = QRadioButton('Варіанти')
    rbtn_list.append(r)
    button_group.addButton(r)

layout_group = QHBoxLayout()
line1_group = QVBoxLayout()
line2_group = QVBoxLayout()

line1_group.addWidget(rbtn_list[0])
line1_group.addWidget(rbtn_list[1])
line2_group.addWidget(rbtn_list[2])
line2_group.addWidget(rbtn_list[3])

layout_group.addLayout(line1_group)
layout_group.addLayout(line2_group)

group_box.setLayout(layout_group)

group_box2 = QGroupBox("Результат теста")
result = QLabel("вірно/невірно")

okey_btn = QPushButton('Відповідь')

result_answ = QLabel('Вірна відповідь:')
layout_group2 = QVBoxLayout()
layout_group2.addWidget(result, alignment=Qt.AlignTop | Qt.AlignLeft)
layout_group2.addWidget(result_answ, alignment=Qt.AlignHCenter)
group_box2.hide()

line3 = QHBoxLayout()
line3.addStretch(1)
line3.addWidget(okey_btn, stretch= 2)
line3.addStretch(1)

radiobutton1 = QRadioButton()
radiobutton2 = QRadioButton()
radiobutton3 = QRadioButton()

layout_card = QVBoxLayout()
layout_card.addLayout(line1)
layout_card.addStretch(1)
layout_card.addLayout(line2)
layout_card.addStretch(1)
layout_card.addWidget(group_box, stretch= 5)
layout_card.addWidget(group_box2, stretch= 5)
layout_card.addStretch(1)
layout_card.addLayout(line3)
layout_card.addStretch(1)


question = QLabel('apple')