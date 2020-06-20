import sys

# importing PyQt5 modules

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from LoopThread import LoopThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot

class Tictactoe(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(250, 250, 400, 100)
        self.setWindowTitle("Tic-Tac-Toe Game")
        self.show()


        self.loop_thread = LoopThread()
        self.loop_thread.signal.connect(self.thread_slot)

        oImage = QImage("TTT6.jpg")
        sImage = oImage.scaled(QSize(300, 200))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.setWindowIcon(QIcon("TTTBALL.png"))  # sets the icon for the window

        self.label = QLabel('Test', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)

        self.gameCharacter = QtGui.QIcon()

        self.Xscr = 0
        self.Oscr = 0

        # Title
        self.title = QLabel("TIC-TAC-TOE")
        self.title.setFont(QFont("Ariel", 35, QtGui.QFont.Bold))
        self.title.setStyleSheet("color: white;")

        # setting picture(symbol)
        self.pic_label = QLabel()
        pixmap = QPixmap().scaled(75, 75)
        self.pic_label.setPixmap(pixmap)

        # CREATING LABELS

        self.edit = QTextEdit()  # creating text edit
        self.edit.setFont(QFont("Ariel", 13))  # setting the font size that will appear on the text edit
        self.edit.setStyleSheet("color: white;  background-image: url(TTT2.jpg);")  # set background picture and color to the text edit
        self.edit.setReadOnly(True)
        # self.edit.QScrollBar(True)

        self.cross = QPixmap("cross.gif")
        self.nought = QPixmap("nought.gif")

        self.my_symbol = QLabel("MY SYMBOL:")  # creating MY_SYMBOL label
        self.my_symbol.setFont(QFont("Ariel", 8, QtGui.QFont.Bold))
        self.my_symbol.setStyleSheet("color: white;")

        self.line = QLineEdit()  # creating line edit
        self.line.resize(10, 10)

        self.server = QLabel("SERVER :")  # creating SERVER label
        self.server.setFont(QFont("Ariel", 8, QtGui.QFont.Bold))
        self.server.setStyleSheet("color: white;")

        self.messages = QLabel("SERVER MESSAGES:")  # creating SERVER MESSAGES label
        self.messages.setFont(QFont("Ariel", 9, QtGui.QFont.Bold))
        self.messages.setStyleSheet("color: white;")

        self.board = QLabel("GAME BOARD")
        self.board.setFont(QFont("Ariel", 12, QtGui.QFont.Bold))
        self.board.setStyleSheet("color: white;")

        self.radiobtn1 = QRadioButton("smile")
        self.radiobtn1.setStyleSheet("color: orange")
        self.radiobtn1.setFont(QFont("Ariel", 14, QtGui.QFont.Bold))
        self.radiobtn1.toggled.connect(self.pic1)

        self.radiobtn2 = QRadioButton("glow")
        self.radiobtn2.setStyleSheet("color: red")
        self.radiobtn2.setFont(QFont("Ariel", 14, QtGui.QFont.Bold))
        self.radiobtn2.toggled.connect(self.pic1)
        self.radiobtn2.toggled.connect(self.pic2)

        self.btn_connect = QPushButton()  # creating connect button
        self.btn_connect.setText("CONNECT")
        self.btn_connect.clicked.connect(self.click_connect)
        # self.btn_connect.clicked.connect(self.click_connect)

        self.btn1 = QPushButton()  # creating button 1
        self.btn1.setIcon(QtGui.QIcon("blank.gif"))
        self.btn1.setIconSize(QtCore.QSize(80, 80))
        self.btn1.clicked.connect(self.click1)  # connecting button to method

        self.btn2 = QPushButton()  # creating button 2
        self.btn2.setIcon(QtGui.QIcon("blank.gif"))
        self.btn2.setIconSize(QtCore.QSize(80, 80))
        self.btn2.clicked.connect(self.click2)  # connecting button to method

        self.btn3 = QPushButton()  # creating button 3
        self.btn3.setIcon(QtGui.QIcon("blank.gif"))
        self.btn3.setIconSize(QtCore.QSize(80, 80))
        self.btn3.clicked.connect(self.click3)  # connecting button to method

        self.btn4 = QPushButton()  # creating button 4
        self.btn4.setIcon(QtGui.QIcon("blank.gif"))
        self.btn4.setIconSize(QtCore.QSize(80, 80))
        self.btn4.clicked.connect(self.click4)  # connecting button to method

        self.btn5 = QPushButton()  # creating button 5
        self.btn5.setIcon(QtGui.QIcon("blank.gif"))
        self.btn5.setIconSize(QtCore.QSize(80, 80))
        self.btn5.clicked.connect(self.click5)  # connecting button to method

        self.btn6 = QPushButton()  # creating button 6
        self.btn6.setIcon(QtGui.QIcon("blank.gif"))
        self.btn6.setIconSize(QtCore.QSize(80, 80))
        self.btn6.clicked.connect(self.click6)  # connecting button to method

        self.btn7 = QPushButton()  # creating button 7
        self.btn7.setIcon(QtGui.QIcon("blank.gif"))
        self.btn7.setIconSize(QtCore.QSize(80, 80))
        self.btn7.clicked.connect(self.click7)  # connecting button to method

        self.btn8 = QPushButton()  # creating button 8
        self.btn8.setIcon(QtGui.QIcon("blank.gif"))
        self.btn8.setIconSize(QtCore.QSize(80, 80))
        self.btn8.clicked.connect(self.click8)  # connecting button to method

        self.btn9 = QPushButton()  # creating button 9
        self.btn9.setIcon(QtGui.QIcon("blank.gif"))
        self.btn9.setIconSize(QtCore.QSize(80, 80))
        self.btn9.clicked.connect(self.click9)  # connecting button to method

        self.quit_btn = QPushButton()  # creating quit  button
        self.quit_btn.setText("QUIT")
        self.quit_btn.clicked.connect(quit)  # connecting button to method

        # self.new_game = QPushButton()
        # self.new_game.setText("New Game")

        # ADDING TO GRID


        grid = QGridLayout()  # creating a grid layout


        grid.addWidget(self.title, 0, 1)  # adding Tictactoe Title

        grid.addWidget(self.server, 2, 0)  # adding server label
        grid.addWidget(self.my_symbol, 3, 0)  # adding  my symbol label
        grid.addWidget(self.line, 2, 1)  # adding line edit
        grid.addWidget(self.btn_connect, 2, 2)  # adding connect button

        grid.addWidget(self.board, 1, 4)

        grid.addWidget(self.btn1, 2, 3)  # adding button 1
        grid.addWidget(self.btn2, 2, 4)  # adding button 2
        grid.addWidget(self.btn3, 2, 5)  # adding button 3

        grid.addWidget(self.btn4, 3, 3)  # adding button 4
        grid.addWidget(self.btn5, 3, 4)  # adding button 5
        grid.addWidget(self.btn6, 3, 5)  # adding button 6

        grid.addWidget(self.btn7, 4, 3)  # adding button 7
        grid.addWidget(self.btn8, 4, 4)  # adding button 8
        grid.addWidget(self.btn9, 4, 5)  # adding button 9

        grid.addWidget(self.messages, 4, 0)
        grid.addWidget(self.edit, 5, 0, 1, 3)  # adding text edit
        grid.addWidget(self.quit_btn, 5, 4)  # adding quit button.

        grid.addWidget(self.radiobtn1,1, 1)
        grid.addWidget(self.radiobtn2,1, 2)
        # grid.addWidget(self.new_game, 5, 5)

        grid.addWidget(self.pic_label, 3, 1)  # adding picture

        self.setLayout(grid)  # setting the grid layout     `

        self.positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # create METHODS for when each button is clicked it will write and show on the text edit that the button is clicked
    # These Methods will also be connected to their respective buttons [ method click1 >> btn1]

    # METHODS

    def instruct(self):
        QMessageBox.information(self, "instructions", "some instructions")

    def pic1(self):  #adding a a background image 1
        oImage = QImage("smile.jpg")
        sImage = oImage.scaled(QSize(300, 200))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def pic2(self):  #adding a a background image 2
        oImage = QImage("tictacglo2.jpg")
        sImage = oImage.scaled(QSize(300, 200))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def click1(self):  # function for button 1
        try:
            self.loop_thread.send_message(self.positions[0])
        except Exception as r:
            print(r)

    def click2(self):  # function for button 2
        try:
            self.loop_thread.send_message(self.positions[1])
        except Exception as r:
            print(r)

    def click3(self):  # function for button 3
        try:
            self.loop_thread.send_message(self.positions[2])
        except Exception as r:
            print(r)

    def click4(self):  # function for button 4
        try:
            self.loop_thread.send_message(self.positions[3])
        except Exception as r:
            print(r)

    def click5(self):  # function for button 5
        try:
            self.loop_thread.send_message(self.positions[4])
        except Exception as r:
            print(r)

    def click6(self):  # function for button 6
        try:
            self.loop_thread.send_message(self.positions[5])
        except Exception as r:
            print(r)

    def click7(self):  # function for button 7
        try:
            self.loop_thread.send_message(self.positions[6])
        except Exception as r:
            print(r)

    def click8(self):  # function for button 8
        try:
            self.loop_thread.send_message(self.positions[7])
        except Exception as r:
            print(r)

    def click9(self):  # function for button 9
        try:
            self.loop_thread.send_message(self.positions[8])
        except Exception as r:
            print(r)

    def click_connect(self):  # function for connect button
        self.loop_thread.connect_(self.line.displayText())
        self.loop_thread.start()
        self.edit.append("server connection established")
        self.btn_connect.setEnabled(False)


    # Handles message from and to a server and their functions
    def handle_gui(self, msg):
        if msg == "new game,O":
            self.icon = self.nought
            self.pic_label.setPixmap(self.icon)
            self.edit.append(msg[:8] + "\n")
        elif msg == "new game,X":
            self.icon = self.cross
            self.pic_label.setPixmap(self.icon)
            self.edit.append(msg[:8] + "\n")

        elif msg == "your move":
            # print("your move")
            self.edit.append(msg)
            # self.new_game.setEnabled(False)  # Disables the new game button
            self.btn_connect.setEnabled(False)  # Disable the connect button
            self.btn1.setEnabled(True)  # Disable the board while the other player is playing
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)
            self.btn4.setEnabled(True)
            self.btn5.setEnabled(True)
            self.btn6.setEnabled(True)
            self.btn7.setEnabled(True)
            self.btn8.setEnabled(True)
            self.btn9.setEnabled(True)

        elif msg == "opponents move":
            # print("opponents move")
            self.edit.append(msg)
            # self.ng_button.setEnabled(False)
            self.btn_connect.setEnabled(False)
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn9.setEnabled(False)


        elif msg[:10] == "valid move":  #Allowed moves
            symbol = msg[-3]
            playPosition = msg[-1]
            if symbol == "X":
                self.gameCharacter = QtGui.QIcon("cross.gif")
            elif symbol == "O":
                self.gameCharacter = QtGui.QIcon("nought.gif")

            if playPosition == "0":
                self.btn1.setIcon(self.gameCharacter)
                self.btn1.setIconSize(QSize(55, 50))
            elif playPosition == "1":
                self.btn2.setIcon(self.gameCharacter)
                self.btn2.setIconSize(QSize(55, 50))
            elif playPosition == "2":
                self.btn3.setIcon(self.gameCharacter)
                self.btn3.setIconSize(QSize(55, 50))
            elif playPosition == "3":
                self.btn4.setIcon(self.gameCharacter)
                self.btn4.setIconSize(QSize(55, 50))
            elif playPosition == "4":
                self.btn5.setIcon(self.gameCharacter)
                self.btn5.setIconSize(QSize(55, 50))
            elif playPosition == "5":
                self.btn6.setIcon(self.gameCharacter)
                self.btn6.setIconSize(QSize(55, 50))
            elif playPosition == "6":
                self.btn7.setIcon(self.gameCharacter)
                self.btn7.setIconSize(QSize(55, 50))
            elif playPosition == "7":
                self.btn8.setIcon(self.gameCharacter)
                self.btn8.setIconSize(QSize(55, 50))
            elif playPosition == "8":
                self.btn9.setIcon(self.gameCharacter)
                self.btn9.setIconSize(QSize(55, 50))

        elif msg == "invalid move":
            self.edit.append(msg)

        # score values to be implemented in the beta
        elif msg[:9] == "game over":
            self.edit.append(msg[:9])
            if msg[-1] == "T":
                self.edit.append("It's a tie!")
            elif msg[-1] == "X":
                self.Xscr += 1
                self.edit.append("Shape " + str(msg[-1]) + " Won!")
            elif msg[-1] == "O":
                self.Oscr += 1
                self.edit.append("Shape " + str(msg[-1]) + " Won!")
            # else:
            #     self.edit.append("Shape " + str(msg[-1]) + " Won!")


        elif msg == "play again":
            done = QMessageBox.question(self, 'Message', "Game over. Do you want to play again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if done == QMessageBox.Yes:
                self.edit.clear()
                self.loop_thread.send_message("y")  #if the user presses yes the game will clear everythinng and restart
                self.btn1.setIcon(QtGui.QIcon("blank.gif"))
                self.btn2.setIcon(QtGui.QIcon("blank.gif"))
                self.btn3.setIcon(QtGui.QIcon("blank.gif"))
                self.btn4.setIcon(QtGui.QIcon("blank.gif"))
                self.btn5.setIcon(QtGui.QIcon("blank.gif"))
                self.btn6.setIcon(QtGui.QIcon("blank.gif"))
                self.btn7.setIcon(QtGui.QIcon("blank.gif"))
                self.btn8.setIcon(QtGui.QIcon("blank.gif"))
                self.btn9.setIcon(QtGui.QIcon("blank.gif"))
            else:
                self.loop_thread.send_message("n")

        elif msg == "exit game":
            self.edit.append(msg)

    def thread_slot(self, msg):
        self.handle_gui(msg)


def main():

    app = QApplication(sys.argv)
    oxo = Tictactoe()
    oxo.show()
    sys.exit(app.exec())

main()
