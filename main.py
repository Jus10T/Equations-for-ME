import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from src.ui.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    
    app.setApplicationName("Tools For ME")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("ME Tools")
    
    app.setWindowIcon(QIcon('Equations-for-ME/icons/gearcalc.png'))
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
