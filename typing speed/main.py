from mainscreen import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import time
import random

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        textList = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet quod doloremque accusantium rem? Deserunt, rerum? Voluptatem eos labore ipsum error nihil ducimus ad laboriosam eius ullam veritatis aspernatur, sint consectetur odio voluptate repudiandae nesciunt est rerum facere corrupti voluptatum exercitationem placeat. Laborum, distinctio eos vitae est numquam, natus sint recusandae itaque laudantium maxime asperiores a explicabo officiis eligendi unde neque? Sint quidem distinctio doloribus doloremque error. Consequatur voluptatibus quibusdam, aperiam, aut officiis provident iusto quas recusandae facilis autem quisquam inventore voluptatem. Quae similique sint fuga iusto? Enim doloribus suscipit quas.","A Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum","Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda quasi totam, expedita deserunt adipisci quas, modi porro fuga corrupti ipsa perferendis architecto deleniti nisi eaque cumque repudiandae nemo atque voluptas incidunt, saepe perspiciatis laudantium officia sunt. Perferendis ea repellendus corrupti natus fuga, laudantium unde ratione. Expedita, veniam enim perferendis amet tempore architecto sit et rerum necessitatibus facere. Pariatur quam, voluptate nihil modi ab nisi ducimus optio eaque corrupti praesentium porro laudantium, excepturi totam est similique, velit molestiae impedit? Fuga consequatur vero, distinctio asperiores quidem esse."]
        self.text = textList[random.randint(0,2)]
        self.ui.start.clicked.connect(self.start)
    
    def start(self):
        self.begining_time = time.time()
        self.ui.admintext.setText(self.text)
        self.ui.start_2.clicked.connect(self.finish)

    def finish(self):
        self.endTime = time.time()
        correct_word = 0
        text = self.text.split(" ")
        user_text = self.ui.usertext.toPlainText().split(" ")
        if len(user_text) > len(text):
            rangeNum = len(text)
        else:
            rangeNum = len(user_text)
        for a in range(rangeNum):
            if text[a] == user_text[a]: 
                correct_word += 1
        self.ui.word.setText(str(correct_word))
        self.ui.time.setText(str(int(self.endTime-self.begining_time)))

def start():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec())

start()
