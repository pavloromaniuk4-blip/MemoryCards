#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from PyQt5.QtGui import QFont
from random import shuffle, randint

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question("Скільки планет мае в солнічний системі?", "Вісім", "Плутон", "Не знаю", "Навушники"))
questions_list.append(Question("Скільки мае глубину до ядра земли?", "6371 км", "1215 км", "Не знаю", "0 км"))
questions_list.append(Question("Хто любить школу?", "Я", "Бобр", "Ніхто", "Мама"))
questions_list.append(Question("Як перекладается слово `змінна` ?", "variable", "zminna", "variant", "string"))

app = QApplication([]) 
#створення віджетів головного вікна
window = QWidget()
window.resize(400, 300) 
window.setWindowTitle("Опрос")

RadioButtonsGroup = QGroupBox('Варіанти')
question = QLabel("Хто любить школу?")
question1 = QRadioButton('Бобр')
question2 = QRadioButton('Я')
question3 = QRadioButton('Ніхто')
question4 = QRadioButton("Мама")
Button = QPushButton("Відповідь")

RadioGroup = QButtonGroup()
RadioGroup.addButton(question1)
RadioGroup.addButton(question2)
RadioGroup.addButton(question3)
RadioGroup.addButton(question4)

ResultGroupBox = QGroupBox("Результат")
result = QLabel("Результат", alignment=Qt.AlignmentFlag.AlignCenter)
correct = QLabel("Правильна Відповідь", alignment=Qt.AlignmentFlag.AlignCenter)

result_lineV1 = QVBoxLayout()
result_lineV1.addWidget(result, alignment=Qt.AlignmentFlag.AlignCenter)
result_lineV1.addWidget(correct, alignment=Qt.AlignmentFlag.AlignCenter)
ResultGroupBox.setLayout(result_lineV1)
ResultGroupBox.hide()

font = QFont("Arial", 20, QFont.Bold)
font_Button = QFont("Times New Roman", 10, QFont.Bold)
question.setFont(font)
result.setFont(font)
correct.setFont(font)

Button.setFont(font_Button)


layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout2.addWidget(question1, alignment=Qt.AlignmentFlag.AlignCenter)
layout2.addWidget(question2, alignment=Qt.AlignmentFlag.AlignCenter)
layout3.addWidget(question3, alignment=Qt.AlignmentFlag.AlignCenter)
layout3.addWidget(question4, alignment=Qt.AlignmentFlag.AlignCenter)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioButtonsGroup.setLayout(layout1)

RadioButtonsGroup.setLayout(layout1)

MainHline1 = QHBoxLayout()
MainHline2 = QHBoxLayout()
MainHline3 = QHBoxLayout()

MainHline1.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)
MainHline2.addWidget(RadioButtonsGroup, alignment=Qt.AlignmentFlag.AlignCenter)
MainHline2.addWidget(ResultGroupBox, alignment=Qt.AlignmentFlag.AlignCenter)
MainHline3.addWidget(Button, alignment=Qt.AlignmentFlag.AlignCenter)

Mainvline1 = QVBoxLayout()
Mainvline1.addLayout(MainHline1, stretch=1)
Mainvline1.addLayout(MainHline2, stretch=8)
Mainvline1.addStretch(1)
Mainvline1.addLayout(MainHline3, stretch=5)
Mainvline1.addSpacing(5)

window.setLayout(Mainvline1)

def show_result():
    RadioButtonsGroup.hide()
    ResultGroupBox.show()    
    Button.setText("Next запитання")

def show_question():
    RadioButtonsGroup.show()
    ResultGroupBox.hide()    
    Button.setText("Відповідь")

    RadioGroup.setExclusive(False)
    question1.setChecked(False)
    question2.setChecked(False)
    question3.setChecked(False)
    question4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [question1, question2, question3, question4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.text)
    correct.setText("Правильна відповідь:" + q.right_answer)
    show_question()

def right_wrong():
    window.total+=1
    if RadioGroup.checkedButton() is None:
        return
    if answers[0].isChecked():
        result.setText("Корект")
        window.score+=1
    else:
        result.setText("Фолс")
    show_result()
    rating = window.score/window.total * 100
    print("Даю відповідей: ", window.total)
    print("Правильних відповідей: ", window.score)
    print("Успівність: ", rating, "%")


def next_question():
    random_question = randint(0, len(questions_list) - 1)
    q = questions_list[random_question]
    ask(q)
    
def button_OK():
    if Button.text() == "Відповідь":
        right_wrong()
    else:
        next_question()


Button.clicked.connect(button_OK)
window.score = 0
window.total = 0
window.show()
app.exec_()