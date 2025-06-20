import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QFrame, 
                             QStackedWidget, QLabel, QPushButton)

from pages.thermopage import ThermoPage
from pages.unitspage import UnitSolverPage
from pages.beampage import BeamPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setup_Window()


        
    

    def setup_Window(self):
         self.setGeometry(100,100,1000,700)
         self.setWindowTitle("Tools For ME")


    def setupUI(self):
         central_widget = QWidget()
         self.setCentralWidget(central_widget)

         #main layout
         main_layout = QHBoxLayout(central_widget)
         main_layout.setContentsMargins(25, 25, 25, 25)
         main_layout.setSpacing(15)


         #create sidebar and add to layout
         self.sidebar_widget = self.create_sidebar()
         main_layout.addWidget(self.sidebar_widget, stretch= 1)
         

         #add content area to layout
         self.main_content_widget = self.create_content_area()
         main_layout.addWidget(self.main_content_widget, stretch= 5)


         #styling
         self.setStyleSheet("""

            
            QLabel#sidebarHeadingtext {
                font-family: 'Segoe UI';
                font-size: 30px;
                font-weight: bold;
                border-radius: 5;
                color: #6b6969;
                                            
        
                            }
        

                            """)


    

    def create_sidebar(self):
        #frame
        sidebar = QFrame()
        sidebar.setFrameStyle(QFrame.Shape.StyledPanel)
        sidebar.setMaximumWidth(275)
        sidebar.setMinimumWidth(270)
        #sidebar V layout
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(5,5,5,5)
        sidebar_layout.setSpacing(10)

        #sidebar heading H layout
        sidebar_heading_layout = QHBoxLayout()
        sidebar_heading_layout.setContentsMargins(5, 10, 20, 0)
        sidebar_heading_layout.setSpacing(15)

        #side heading text
        sidebar_heading_text = QLabel("Tools")
        sidebar_heading_text.setObjectName("sidebarHeadingtext")
        sidebar_heading_text.setAlignment(Qt.AlignmentFlag.AlignLeft)
        sidebar_heading_text.setMaximumHeight(40)


        #heading pixmap
        sidebar_icon = QLabel()
        sidebar_icon.setPixmap(QPixmap("Equations-for-ME\gearcalc.ico"))

        #add icon and text to horizontal
        sidebar_heading_layout.addWidget(sidebar_icon)
        sidebar_heading_layout.addWidget(sidebar_heading_text)
        sidebar_heading_layout.addStretch()


        #add H to V
        sidebar_layout.addLayout(sidebar_heading_layout)


        #add line
        navline = QFrame()
        navline.setFrameShape(QFrame.Shape.HLine)
        navline.setLineWidth(0)
        navline.setContentsMargins(0,25, 25, 0)
        navline.setStyleSheet("""
                              
                              color: gray;
                              background: qlineargradient(
                                x1:0, y1:0, x2:1, y2:0,
                                stop:0 #FF9122,   /* Left color */
                                stop:1 #7B7A79    /* Right color */
    );
                              
                              
                              """)

        sidebar_layout.addWidget(navline)
        



        #create sidebar buttons
        self.unitbutton = QPushButton("- Units")
        self.thermobutton  = QPushButton("- Thermodynamics")
        self.beamsbutton = QPushButton("- Beams")

        #button style    
        buttons = [self.unitbutton, self.thermobutton, self.beamsbutton]

        buttonstyle = """
            QPushButton {
            padding: 10px;
            text-align: left;
            font-size: 17px;
            font-weight: oblique;
            font-family: 'Segoe UI';
            color: #969393;
                }
            


            QPushButton:hover {
                background-color: #f3893c;
                color: 'white';
                }

        """

        for button in buttons:
            button.setStyleSheet(buttonstyle)


        #add buttons to layout
        sidebar_layout.addWidget(self.unitbutton)
        sidebar_layout.addWidget(self.thermobutton)
        sidebar_layout.addWidget(self.beamsbutton)

        #connect buttons to page switching
        self.unitbutton.clicked.connect(lambda: self.main_content_stack.setCurrentIndex(0))
        self.thermobutton.clicked.connect(lambda: self.main_content_stack.setCurrentIndex(1))
        self.beamsbutton.clicked.connect(lambda: self.main_content_stack.setCurrentIndex(2))

        #add stretch after buttons
        sidebar_layout.addStretch()



    
        return sidebar


    def create_content_area(self):
        #create frame and stack
        content_frame = QFrame()
        self.main_content_stack = QStackedWidget()

        content_frame.setFrameStyle(QFrame.Shape.StyledPanel)


        #make main layout and add stack to it
        center_layout = QVBoxLayout(content_frame)
        center_layout.addWidget(self.main_content_stack)

        #create pages
        self.unitpage = UnitSolverPage()
        self.thermopage = ThermoPage()
        self.beampage = BeamPage()

        #add pages to stack
        self.main_content_stack.addWidget(self.unitpage)
        self.main_content_stack.addWidget(self.thermopage)
        self.main_content_stack.addWidget(self.beampage)

        return content_frame



    def switchPage(self, index):
        self.main_content_stack.setCurrentIndex(index)



def main():
    app = QApplication([])
   
    app.setWindowIcon(QIcon(('Equations-for-ME\gearcalc.png')))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()