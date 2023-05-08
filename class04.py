import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

# Slot Example for Menu Bar
def slot_example(status_bar):
    status_bar.showMessage('Action has been triggered')
    # status_bar.showMessage('')
    # print('Action has been triggered')

# Create app
app = QApplication(sys.argv)
# Window
window = QMainWindow()
# Central Widget
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('This is App Window Title')

# Simple buttons
button = QPushButton('Button text')
button.setStyleSheet('font-size: 50px')

button2 = QPushButton('Another Button')

button3 = QPushButton('Another Button Again')

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)

layout.addWidget(button2, 1, 2, 1, 1)

layout.addWidget(button3, 3, 1, 1, 2)

# Status bar 
status_bar = window.statusBar()
status_bar.showMessage('Show message')

# Menu bar
menu_bar = window.menuBar()
first_menu = menu_bar.addMenu('Something in the menu')
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(lambda :slot_example(status_bar))

window.show()
app.exec()