import sys
import os
import random

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox

class SecureFileEraser(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initializes the UI"""

        self.setWindowTitle("Secure File Eraser")
        self.setGeometry(200, 200, 400, 300)

        app_font = QFont("", 12)
        self.setFont(app_font)

        layout = QVBoxLayout()

        self.label = QLabel("Select a file to securely delete")
        self.label.setStyleSheet("color : #FF0000; font-size: 14px ; font-weight:bold ")
        layout.addWidget(self.label)

        self.select_button = QPushButton("Select File")
        self.select_button.setStyleSheet("""
        
                QPushButton {
                background-color: #FF0000;
                color: white
                border-radius: 5px;
                padding: 10px;
                font-size: bold;
                }
                QPushButton:hover {
                background-color: #950c02;
               }
        """
        )
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.delete_button = QPushButton("Delete Securely")
        self.delete_button.setStyleSheet("""
                    QPushButton {
                        background-color: #660000;
                        color: white;
                        border-radius: 5px;
                        padding: 10px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #330000;
                    }
                """
                                        )
        self.delete_button.clicked.connect(
            lambda: self.securely_delete(self.file_path) if hasattr(self, 'file_path') else None)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

        # Apply overall window styling
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: white;
            }
            """
            )


        pass

    def select_file(self):
        """Opens a file dialog for choosing the file to delete"""
        pass

    def securely_delete(self, file_path):
        """overwrites and deletes the file"""
        pass
