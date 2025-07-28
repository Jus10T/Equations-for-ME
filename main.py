import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QFrame, QSplitter,
                             QStackedWidget, QLabel, QPushButton)

from pages.thermopage import ThermoPage
from pages.unitspage import UnitSolverPage
from pages.beams.beampage import BeamPage



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setup_Window()
        self.update_sidebar_styles(0)

    def setup_Window(self):
         self.setGeometry(25,25,1400,700)
         self.setWindowTitle("Tools For ME")


    def setupUI(self):
         central_widget = QWidget()
         self.setCentralWidget(central_widget)
         central_widget.setObjectName("centralwidget")

         #main layout
         main_layout = QHBoxLayout(central_widget)
         main_layout.setContentsMargins(25, 25, 25, 25)
         main_layout.setSpacing(15)
         splitter = QSplitter(Qt.Orientation.Horizontal)
         
        


         #create sidebar and add to layout
         self.sidebar_widget = self.create_sidebar()
         splitter.addWidget(self.sidebar_widget)
         

         #add content area to layout
         self.main_content_widget = self.create_content_area()
         splitter.addWidget(self.main_content_widget)
         main_layout.addWidget(splitter)


         #styling
         self.setStyleSheet("""
                            

            QWidget#centralwidget {
                background: qlineargradient(
                                x1:0, y1:0, x2:0, y2:1,
                                stop:0 #333231,   
                                stop:1 #000000,   
                            );
                            
                            }

            
            QLabel#sidebarHeadingtext {
                font-size: 30px;
                border-radius: 5;
                color: white;
                                                
                            }
        
                             """)


    

    def create_sidebar(self):
        #frame
        sidebar = QFrame()
        sidebar.setFrameStyle(QFrame.Shape.StyledPanel)
        sidebar.setMaximumWidth(275)
        #sidebar V layout
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(5,5,5,5)
        sidebar_layout.setSpacing(10)

        #sidebar heading H layout
        sidebar_heading_layout = QHBoxLayout()
        sidebar_heading_layout.setContentsMargins(5, 10, 20, 0)
        sidebar_heading_layout.setSpacing(10)

        #side heading text
        sidebar_heading_text = QLabel("Tools")
        sidebar_heading_text.setObjectName("sidebarHeadingtext")
        sidebar_heading_text.setAlignment(Qt.AlignmentFlag.AlignLeft)
        sidebar_heading_text.setMaximumHeight(40)


        #heading pixmap
        sidebar_icon = QLabel()
        sidebar_icon.setPixmap(QPixmap("Equations-for-ME\icons\gearcalc.ico"))

        #add icon and text to horizontal
        sidebar_heading_layout.addWidget(sidebar_icon)
        #sidebar_heading_layout.addWidget(sidebar_heading_text)
        #sidebar_heading_layout.addStretch()
        sidebar_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #add H to V
        sidebar_layout.addLayout(sidebar_heading_layout)



        #create sidebar buttons
        self.unitbutton = QPushButton("- Units")
        self.thermobutton  = QPushButton("- Thermodynamics")
        self.beamsbutton = QPushButton("- Beams")

        #for button style    
        self.sidebuttons = [self.unitbutton, self.thermobutton, self.beamsbutton]

        

        #add buttons to layout
        sidebar_layout.addWidget(self.unitbutton)
        sidebar_layout.addWidget(self.thermobutton)
        sidebar_layout.addWidget(self.beamsbutton)

        #connect buttons to page switching
        self.unitbutton.clicked.connect(lambda: self.switchPage(0))
        self.thermobutton.clicked.connect(lambda: self.switchPage(1))
        self.beamsbutton.clicked.connect(lambda: self.switchPage(2))

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
    
    

    def update_sidebar_styles(self, active_index):
        for i, button in enumerate(self.sidebuttons):
            if i == active_index:
                button.setStyleSheet(""" 
                    QPushButton {
                        padding: 10px;
                        text-align: left;
                        font-size: 15px;
                        font-weight: oblique;
                        background-color: #454545;


                    }
            


                    QPushButton:hover {
                        border: 1px solid #ff8c00;
                        border-radius: 4px;

                        }
                """)
            else:
                button.setStyleSheet(""" 
                    QPushButton {
                        padding: 10px;
                        text-align: left;
                        font-size: 15px;
                        font-weight: oblique;
                        font-family: 'Segoe UI';
                        color: white;
                        border-radius: 4px;

                        }
            


                    QPushButton:hover {
                        border: 1px solid #ff8c00;
                        border-radius: 4px;
                        color: 'white';
                        }
                """)



    def switchPage(self, index):
        self.main_content_stack.setCurrentIndex(index)
        self.update_sidebar_styles(index)



def main():
    app = QApplication([])
   
    app.setWindowIcon(QIcon(('Equations-for-ME\icons\gearcalc.png')))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()