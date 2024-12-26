import nuke
import os
import json
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFileDialog, QPushButton, QLineEdit

def set_prod_path():

    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            
            hbox = QHBoxLayout()
            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            vbox = QVBoxLayout()

            label = QLabel("Select Production Path for Shot Builder")
            self.path_space = QLineEdit()

            browse_button = QPushButton("Browse Path")
            cancel_button = QPushButton("Cancel")
            set_path_button = QPushButton("Set Path")

            hbox.addWidget(label)
            
            hbox1.addWidget(self.path_space)
            hbox1.addWidget(browse_button)

            hbox2.addWidget(set_path_button)
            hbox2.addWidget(cancel_button)
            
            vbox.addLayout(hbox)
            vbox.addLayout(hbox1)
            vbox.addLayout(hbox2)

            self.setLayout(vbox)
            self.setMinimumSize(400, 100)
            self.setMaximumSize(400, 100)

            browse_button.clicked.connect(self.browse_operation)
            set_path_button.clicked.connect(self.set_path_operation)
            cancel_button.clicked.connect(self.cancel_operation)

        def cancel_operation(self):
            self.close()

        def browse_operation(self):
            dir_browser = QFileDialog()
            dir_browser.directory()

            self.selected_dir = dir_browser.getExistingDirectory()

            if self.selected_dir:
                self.path_space.clear()
                self.path_space.setText(self.selected_dir)

        def set_path_operation(self):
            user_dir = os.path.expanduser(r"~")
            prod_path_record_dir = os.path.join(user_dir, "production_path_record")

            os.makedirs(prod_path_record_dir, exist_ok= True)

            prod_path_record_file = os.path.join(prod_path_record_dir, "production_path.json")

            with open(prod_path_record_file, "w") as file:
                json.dump(self.path_space.text(), file)
            
            self.close()

    global window

    window = MainWindow()
    window.show()