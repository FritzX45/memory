from PyQt5.QtWidgets import (QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt

menu_line = QVBoxLayout()
test_btn = QPushButton("Розпочати тестування")
create_btn = QPushButton("Бестиарій")
new_btn = QPushButton("Щось тут має бути")

test_btn.setFixedSize(200, 50)
create_btn.setFixedSize(200, 50)
new_btn.setFixedSize(200, 50)

menu_line.addWidget(test_btn, alignment=Qt.AlignHCenter)
menu_line.addWidget(create_btn, alignment=Qt.AlignHCenter)
menu_line.addWidget(new_btn, alignment=Qt.AlignHCenter)