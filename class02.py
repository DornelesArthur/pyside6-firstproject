import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 50px')
button.show()

button2 = QPushButton('Another Button')
button2.show()

app.exec()