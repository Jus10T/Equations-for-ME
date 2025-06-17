from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class UnitSolverPage(QWidget):
    def __init__(self):
        super().__init__()
        unit_layout = QVBoxLayout()
        unit_layout.addWidget(QLabel("Unit Solver"))
        self.setLayout(unit_layout)