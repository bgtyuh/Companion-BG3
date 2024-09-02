from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from ui.layouts import FlowLayout  # Importer le FlowLayout personnalisé
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolTip
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt

class ItemCard(QWidget):
    def __init__(self, item_name, image_path, card_size=100, image_size=100, item_properties="", parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.item_name = item_name
        self.item_properties = item_properties  # Store the properties for hover display

        # Set a fixed size for the card
        self.setFixedSize(card_size, card_size + 40)  # Adding extra space for text below the image

        # Image of the item
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path).scaled(image_size, image_size, aspectRatioMode=Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Item name
        self.name_label = QLabel(item_name, self)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.name_label.setWordWrap(True)  # Allow text wrapping

        # Add widgets to the layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)

        self.setLayout(layout)

    def enterEvent(self, event):
        """Display a tooltip or custom widget with item properties on hover."""
        QToolTip.showText(QCursor.pos(), self.item_properties, self)

    def leaveEvent(self, event):
        """Hide the tooltip when the mouse leaves the item."""
        QToolTip.hideText()
        event.accept()


class ItemsDisplayWidget(QWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent)

        # Calculate the image and card size based on the total number of items
        total_items = len(items)
        card_size = self.calculate_card_size(total_items)
        image_size = card_size  # The image size is equal to the calculated card size

        # Sort items by rarity
        sorted_items = self.sort_items_by_rarity(items)

        # Create the main layout
        main_layout = QVBoxLayout()

        for rarity, items_in_rarity in sorted_items.items():
            # Add a label for the rarity category
            rarity_label = QLabel(f"Rareté : {rarity.capitalize()}")
            rarity_label.setFont(QFont("Arial", 12, QFont.Bold))
            main_layout.addWidget(rarity_label)

            # Add the items of this rarity to the FlowLayout
            flow_layout = FlowLayout(spacing=10)
            for item in items_in_rarity:
                item_name = item['name']
                image_path = f"ressources/icons/{item['image_path']}"
                item_properties = f"Propriétés : {item.get('properties', 'Aucune')}"  # Example property string
                card = ItemCard(item_name, image_path, card_size, image_size, item_properties)
                flow_layout.addWidget(card)

            # Encapsulate each section in a widget to manage spacing
            section_widget = QWidget()
            section_widget.setLayout(flow_layout)
            main_layout.addWidget(section_widget)

            # Add a separation line after each rarity group
            separator = QFrame()
            separator.setFrameShape(QFrame.HLine)
            separator.setFrameShadow(QFrame.Sunken)
            main_layout.addWidget(separator)

        # Configure the QScrollArea to contain all items
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_widget = QWidget()
        scroll_area_widget.setLayout(main_layout)
        scroll_area.setWidget(scroll_area_widget)

        # Add the QScrollArea to the main window
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        self.setLayout(layout)


    def calculate_card_size(self, total_items, max_size=150, min_size=80):
        """Calculates the card size based on the total number of items."""
        if total_items <= 10:
            return max_size  # Max size for fewer items
        elif total_items >= 100:
            return min_size  # Min size for 100 or more items
        else:
            # Interpolated size between max_size and min_size
            return max_size - int((total_items - 10) * (max_size - min_size) / 90)

    def sort_items_by_rarity(self, items):
        """Trie les items par rareté."""
        sorted_items = {}
        for item in items:
            rarity = item['rarity']
            if rarity not in sorted_items:
                sorted_items[rarity] = []
            sorted_items[rarity].append(item)
        return sorted_items