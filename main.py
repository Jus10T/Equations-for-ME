import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QFrame, QListWidget, QListWidgetItem,
                             QStackedWidget, QLabel)

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        home_layout = QVBoxLayout()
        home_layout.addWidget(QLabel("Home Page"))
        self.setLayout(home_layout)

class UnitSolverPage(QWidget):
    def __init__(self):
        super().__init__()
        unit_layout = QVBoxLayout()
        unit_layout.addWidget(QLabel("Unit Solver"))
        self.setLayout(unit_layout)

class ThermoPage(QWidget):
    def __init__(self):
        super().__init__()
        thermo_layout = QVBoxLayout()
        thermo_layout.addWidget(QLabel("Thermo"))
        self.setLayout(thermo_layout)

class BeamPage(QWidget):
    def __init__(self):
        super().__init__()
        beam_layout = QVBoxLayout()
        beam_layout.addWidget(QLabel("Beam Deflection Solver"))
        self.setLayout(beam_layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setup_Window()
        self.sidelist.currentRowChanged.connect(self.switchPage)
        self.sidelist.setCurrentRow(0)


    def setup_Window(self):
         self.setGeometry(100,100,800,600)
         self.setWindowTitle("Equations For ME")

        

    

    def setupUI(self):
         central_widget = QWidget()
         self.setCentralWidget(central_widget)

         #main layout
         main_layout = QHBoxLayout(central_widget)
         main_layout.setContentsMargins(10, 10, 10, 10)

         #create sidebar and add to layout
         sidebar_widget = self.create_sidebar()
         main_layout.addWidget(sidebar_widget, stretch= 1)
         self.sidelist.setMaximumWidth(250)
         self.sidelist.setMaximumWidth(200)

         #add content area to layout
         main_content_widget = self.create_content_area()
         main_layout.addWidget(main_content_widget, stretch= 4)
    

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFrameStyle(QFrame.Shape.StyledPanel)
        #sidebar layout
        sidebar_layout = QVBoxLayout(sidebar)

        #sidebar heading
        sidebar_heading = QLabel("ME Tools")
        sidebar_layout.addWidget(sidebar_heading)

        #sidebar list
        self.sidelist = QListWidget()        
        self.sidelist.addItem(QListWidgetItem("Home"))
        self.sidelist.addItem(QListWidgetItem("Unit Conversion"))
        self.sidelist.addItem(QListWidgetItem("Thermodynamics"))
        self.sidelist.addItem(QListWidgetItem("Beam Deflection Calculator"))




        sidebar_layout.addWidget(self.sidelist)


        return sidebar


    def create_content_area(self):
        #create frame and stack
        content_frame = QFrame()
        self.main_content_stack = QStackedWidget()

        content_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        #content_frame.setStyleSheet("border: 1px solid gray;")


        #make main layout and add stack to it
        center_layout = QVBoxLayout(content_frame)
        center_layout.addWidget(self.main_content_stack)

        #create pages
        self.homepage = HomePage()
        self.unitpage = UnitSolverPage()
        self.thermopage = ThermoPage()
        self.beampage = BeamPage()

        #add pages to stack
        self.main_content_stack.addWidget(self.homepage)
        self.main_content_stack.addWidget(self.unitpage)
        self.main_content_stack.addWidget(self.thermopage)
        self.main_content_stack.addWidget(self.beampage)

        return content_frame



    def switchPage(self, index):
        self.main_content_stack.setCurrentIndex(index)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()