from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from ui.layouts import FlowLayout  # Importer le FlowLayout personnalisé
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont

class ItemCard(QWidget):
    def __init__(self, item_name, image_path, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path).scaled(100, 100, aspectRatioMode=1)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.name_label = QLabel(item_name, self)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        self.setLayout(layout)
        self.setFixedSize(120, 150)
        print(item_name, image_path)

class ItemsDisplayWidget(QWidget):
    def __init__(self, items, item_type, parent=None):
        super().__init__(parent)
        flow_layout = FlowLayout()
        for item in items:
            item_name = item['name']
            image_path = f"ressources/icons/{item_type}/{item['image_path']}"
            card = ItemCard(item_name, image_path)
            flow_layout.addWidget(card)
        self.setLayout(flow_layout)
