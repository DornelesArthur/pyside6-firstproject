import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

# Slot Example for Menu Bar
@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('Action has been triggered')
    return inner
    # status_bar.showMessage('')
    # print('Action has been triggered')

# Another Slot Example
@Slot()
def another_slot_example(checked):
    print(f'Is marked? {checked}')
    # status_bar.showMessage(f'Is marked? {checked}')

# Another Slot Example
@Slot()
def third_slot_example(action):
    def inner():
        another_slot_example(action.isChecked())
    return inner

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
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot_example)
second_action.hovered.connect(third_slot_example(second_action))

button.clicked.connect(third_slot_example(second_action))

window.show()
app.exec()