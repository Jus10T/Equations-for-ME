from asyncio.windows_events import NULL
import os
from PyQt6.QtWidgets import QComboBox, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView

from units.unit_factors import beam_dropdown_units
from pages.pagestyling import set_dropdown_style

class ThermoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # Layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setContentsMargins(20, 10, 20, 20)
        main_layout.setSpacing(10)

        # Top layout for dropdowns and zoom buttons
        top_layout = QHBoxLayout()

        # Existing unit dropdown
        self.unit_drop = QComboBox()
        self.unit_drop.addItems(list(beam_dropdown_units.keys()))
        set_dropdown_style(self.unit_drop)
        top_layout.addWidget(self.unit_drop)

        #set of tables drop
        self.table_catalog = QComboBox()
        self.table_catalog.addItems(["Unit Conversion Factors", "Thermodynamics Tables", 
                                    "Ideal Gas Model Summary", "Psychrometric Charts", "Isentropic / Ideal / k = 1.4 (9.2)" ])
        set_dropdown_style(self.table_catalog)
        top_layout.addWidget(self.table_catalog)

        # Spacer to push zoom buttons to the right
        top_layout.addStretch(1)

        # Zoom buttons
        self.zoom_out_button = QPushButton("-")
        self.zoom_out_button.setStyleSheet("QPushButton {font-size: 20px;}")
        self.zoom_in_button = QPushButton("+")
        self.zoom_in_button.setStyleSheet("QPushButton {font-size: 20px;}")

        self.zoom_out_button.setFixedSize(50, 50)
        self.zoom_in_button.setFixedSize(50, 50)
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.zoom_in_button.clicked.connect(self.zoom_in)

        top_layout.addWidget(self.zoom_out_button)
        top_layout.addWidget(self.zoom_in_button)
        
        main_layout.addLayout(top_layout)

        #pdf viewer
        self.pdf_doc = QPdfDocument(self)
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.pdf_doc)
        self.pdf_view.setPageMode(QPdfView.PageMode.MultiPage)

        #(table, unit)
        self.pdf_map = {
            "Unit Conversion Factors": "UnitConversionMoranShapiro.pdf",
            "Thermodynamics Tables": {
                "Metric / SI": "SITables.pdf",
                "English": "EnglishTables.pdf"
            },
            "Ideal Gas Model Summary": "idealSummary.pdf",
            "Psychrometric Charts": "PsychrometricCharts.pdf",
            "Isentropic / Ideal / k = 1.4 (9.2)": "Table 9-2.pdf"
        }

        # Connect dropdowns to handler
        self.unit_drop.currentIndexChanged.connect(self.update_pdf)
        self.table_catalog.currentIndexChanged.connect(self.update_pdf)

        self.update_pdf()

        main_layout.addWidget(self.pdf_view)
    
    def zoom_in(self):
        zoom_factor = self.pdf_view.zoomFactor()
        self.pdf_view.setZoomFactor(zoom_factor * 1.1)

    def zoom_out(self):
        zoom_factor = self.pdf_view.zoomFactor()
        self.pdf_view.setZoomFactor(zoom_factor / 1.1)

    def update_pdf(self):
        table = self.table_catalog.currentText()
        unit = self.unit_drop.currentText()
        pdf_file = None

        if table == "Thermodynamics Tables":
            # Only use unit dropdown for Thermodynamics Tables
            pdf_file = self.pdf_map[table].get(unit)
        else:
            # Ignore unit dropdown for other tables
            pdf_file = self.pdf_map.get(table)

        if pdf_file:
            pdf_dir = os.path.dirname(os.path.abspath(__file__))
            pdf_path = os.path.join(pdf_dir, 'thermopdfs', pdf_file)
            if os.path.exists(pdf_path):
                self.pdf_doc.load(pdf_path)
            else:
                self.pdf_doc.load("")  # Clear if file not found
        else:
            self.pdf_doc.load("")  # Clear if no mapping


        