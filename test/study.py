from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QListWidget, QFormLayout)

menu2_btn = QPushButton("Меню")
time_lb = QLabel("0")

study_line1 = QHBoxLayout()
study_line1.addWidget(menu2_btn)
study_line1.addStretch(5)
study_line1.addWidget(QLabel("час навчання"))
study_line1.addStretch(1)
study_line1.addWidget(time_lb)
study_line1.addStretch(1)

qw_list = QListWidget()

form = QFormLayout()
ans_lb = QLabel("--")
pict_lb = QLabel("--")
form.addRow("Відповідь:", ans_lb)
form.addRow(pict_lb)

study_line2 = QHBoxLayout()

study_line2.addWidget(qw_list, stretch=7)
study_line2.addStretch(1)
study_line2.addLayout(form, stretch=7)

study_line = QVBoxLayout()
study_line.addLayout(study_line1)
study_line.addLayout(study_line2)