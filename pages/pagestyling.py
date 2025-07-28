def set_dropdown_style(widget):
    dropdown_style = """
        QComboBox {
            border: 1px solid transparent;
            border-radius: 6px;
            padding: 10px 15px;
            background-color: #424141;
            font-size: 14px;
            color: #ffffff;
            min-height: 20px;
        }
        QComboBox#unitclasses {
            border: 1px solid #ff8c00;
            border-radius: 6px;
            padding: 10px 15px;
            background-color: #2c2c2c;
            font-size: 20px;
            color: #ffffff;
            min-height: 20px;
        }
        QComboBox#unitTypeDrop {
            border: 1px solid #ff8c00;
            border-radius: 6px;
            padding: 10px 15px;
            background-color: #2c2c2c;
            font-size: 20px;
            color: #ffffff;
            min-height: 20px;
        }
        QComboBox#beam_unit_drop {
            border: 1px solid #ff8c00;
            border-radius: 6px;
            padding: 10px 15px;
            background-color: #2c2c2c;
            font-size: 20px;
            color: #ffffff;
            min-height: 20px;
        }
        QComboBox:hover {
            border: 1px solid #ff8c00;
        }
        QComboBox:focus {
            background-color: #333333;
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border: none;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
            background-color: transparent;
        }
        QComboBox::down-arrow {
            image: none;
            width: 12px;
            height: 1px;
            background-color: #ffffff;
            margin: 0px;
        }
        QComboBox::down-arrow:hover {
            background-color: #ff8c00;
        }
        QComboBox QAbstractItemView {
            border: 1px solid #444444;
            border-radius: 6px;
            background-color: #2c2c2c;
            selection-background-color: #ff8c00;
            selection-color: #ffffff;
            font-size: 14px;
            padding: 2px;
            min-width: 200px;
            outline: none;
        }
        QComboBox QAbstractItemView::item {
            height: 25px;
            padding: 6px 10px;
            border: none;
            color: #ffffff;
        }
        QComboBox QAbstractItemView::item:hover {
            background-color: #404040;
            color: #ff8c00;
        }
        QComboBox QAbstractItemView::item:selected {
            background-color: #ff8c00;
            color: #ffffff;
        }
    """
    widget.setStyleSheet(dropdown_style)

def set_lineEdit_style(widget):
    line_edit_style = """ 
        QLineEdit {
            border: 1px solid transparent;
            padding: 20px;
            font-size: 30px;
        }
        QLineEdit:hover {
            border-bottom: 1px solid #ff8c00;      
        }
        QLineEdit#inputLineEdit {
            border: 1px solid transparent;
            padding: 20px;
            font-size: 35px;
        }

        QLineEdit#inputLineEdit:hover, QLineEdit#inputLineEdit:focus {
            border-bottom: 1px solid #ff8c00;      
        }
        QLineEdit#length_lineEdit {
            padding: 10px;
            font-size: 20px;
            border-bottom: 1px solid #ff8c00;
        }
        QLineEdit#modulus_lineEdit {
            padding: 10px;
            font-size: 20px;
            border-bottom: 1px solid #ff8c00;

        }
        QLineEdit#inertia_lineEdit {
            padding: 10px;
            font-size: 20px;
            border-bottom: 1px solid #ff8c00;

        }
    """
    widget.setStyleSheet(line_edit_style)

def setLabelStyle(widget):
    label_style = """

        QLabel {
            padding: 15px;
            font-size: 15px;
        }
        QLabel#length_label {
            font-size: 14px;
        
        }
        
        QLabel#modulus_label {
            font-size: 12px;


        }
        QLabel#inertia_label {
            font-size: 12px;

        }
        QLabel#modelheader {
            font-size: 17px;
        }


"""
    widget.setStyleSheet(label_style)

def setButtonStyle(widget):
    button_style = """

        QPushButton {
            padding: 10px;
            font-size: 13px;
            font-weight: oblique;
            background-color: #454545;
            border-radius: 3px;
        
        }
        QPushButton:checked {
            border: 1px solid #ff8c00;
        }

        QPushButton#makeBeamButton {
            font-size: 15px;
            background-color: #ff8c00;
        }
        QPushButton#makeBeamButton:hover {
            font-size: 15px;
            background-color: #ff8c00;
            border: 1px solid white;
        }


        QPushButton#pinned_support_btn {
            background-color: #ff8c00;
            padding: 2px;
        }
        QPushButton#pinned_support_btn:hover {
            font-size: 15px;
            background-color: #ff8c00;
            border: 1px solid white;
        }


        QPushButton#roller_support_btn {
            background-color: #ff8c00;
            padding: 2px;
        }
        QPushButton#roller_support_btn:hover {
            font-size: 15px;
            background-color: #ff8c00;
            border: 1px solid white;
        }

        
        QPushButton#fixed_support_btn {
            background-color: #ff8c00;
            padding: 2px;
        }
        QPushButton#fixed_support_btn:hover {
            font-size: 15px;
            background-color: #ff8c00;
            border: 1px solid white;
        }

"""
    widget.setStyleSheet(button_style)