import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 50px')

button2 = QPushButton('Another Button')

button3 = QPushButton('Another Button Again')

main_widget = QWidget()

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
main_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)

layout.addWidget(button2, 1, 2, 1, 1)

layout.addWidget(button3, 3, 1, 1, 2)


main_widget.show()
app.exec()