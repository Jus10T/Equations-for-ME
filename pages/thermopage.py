from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame

class ThermoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        #layout
        unit_layout = QVBoxLayout()
        self.setLayout(unit_layout)
        unit_layout.setContentsMargins(20, 10, 20, 20)
        unit_layout.setSpacing(10)

        #heading
        title = QLabel("Thermodynamcics")
        title.setStyleSheet("font-size:37px; font-weight: bold;")

        line1 = QFrame()
        line1.setFrameShape(QFrame.Shape.HLine)
        line1.setFrameShadow(QFrame.Shadow.Sunken)
        line1.setLineWidth(3)

        #add
        unit_layout.addWidget(title)
        unit_layout.addWidget(line1)
        unit_layout.addStretch()