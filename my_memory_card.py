from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QVBoxLayout, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Что закончилось в 1945 году ???', '2 Мировая Война', '1944 год', 'Скидка на пельмени', 'Бизнес Ивонгая' ))
questions_list.append(Question('2000*30:30000+8-5*20=?', '90', '43', '100', 'Я не умею считать :(' ))
questions_list.append(Question('Горячая(тёплая) вода замерзает быстрее чем холодная?', 'Да', 'Нет, не может быть', 'Когда как', 'Тёплая вода замерзает быстрее всех' ))

app = QApplication([])
window = QWidget()

button = QPushButton('Ответить')
lb_Question = QLabel('Что закончилось в 1945 году ???')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('2 Мировая Война')
rbtn_2 = QRadioButton('1944 год')
rbtn_3 = QRadioButton('Скидка на пельмени')
rbtn_4 = QRadioButton('Бизнес Ивонгая')
rbtn_5 = QRadioButton('20 Век')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_V = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()

layout_h1.addWidget(rbtn_1)
layout_h1.addWidget(rbtn_2)
layout_h2.addWidget(rbtn_3)
layout_h2.addWidget(rbtn_4)

layout_V.addLayout(layout_h1)
layout_V.addLayout(layout_h2)

RadioGroupBox.setLayout(layout_V)

AnsGroupBox = QGroupBox('Результат')
lb_res = QLabel("Результат")
lb_correct = QLabel("Правильный")
col1 =QVBoxLayout()
col1.addWidget(lb_res)
col1.addWidget(lb_correct)

AnsGroupBox.setLayout(col1)


line1 = QHBoxLayout()
line1.addWidget(RadioGroupBox)
line1.addWidget(AnsGroupBox)
AnsGroupBox.hide()

collum = QVBoxLayout()
collum.addWidget(lb_Question)
collum.addLayout(line1)
collum.addWidget(button)

window.setLayout(collum)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Слудующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4,]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_res.setText(res)
    show_result()

def check_anwer():
    if answers[0].isChecked():
        show_correct('Поздравляю, вы получаете (ещё) пачку пельмений')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно, вы получаете 2 леща')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len (questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_anwer()
    else:
        next_question()

window.cur_question = -1
button.clicked.connect(click_OK)
next_question()

window.show()
app.exec()