from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ThermoPage(QWidget):
    def __init__(self):
        super().__init__()
        thermo_layout = QVBoxLayout()
        thermo_layout.addWidget(QLabel("Thermo"))
        self.setLayout(thermo_layout)