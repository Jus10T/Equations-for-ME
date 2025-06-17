from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        home_layout = QVBoxLayout()
        home_layout.addWidget(QLabel("Home Page"))
        self.setLayout(home_layout)