from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MechanicsPage(QWidget):
    def __init__(self):
        super().__init__()
        mechanics_layout = QVBoxLayout()
        mechanics_layout.addWidget(QLabel("Beam Deflection Solver"))
        self.setLayout(mechanics_layout)