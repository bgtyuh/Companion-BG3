from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from ui.layouts import FlowLayout  # Importer le FlowLayout personnalisé
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont

class ItemCard(QWidget):
    def __init__(self, item_name, image_path, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        # Image de l'item
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path).scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Nom de l'item
        self.name_label = QLabel(item_name, self)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.name_label.setWordWrap(True)  # Permet le retour à la ligne

        # Calculer la hauteur dynamique en fonction de la longueur du texte
        self.name_label.adjustSize()
        text_height = self.name_label.sizeHint().height()
        total_height = 100 + text_height + 10  # Image height + text height + margin

        # Ajouter les widgets au layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)

        self.setLayout(layout)
        self.setFixedSize(120, total_height)  # Ajuste la hauteur de la carte dynamiquement


class ItemsDisplayWidget(QWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent)

        # Trier les items par rareté
        sorted_items = self.sort_items_by_rarity(items)

        # Créer le layout principal
        main_layout = QVBoxLayout()

        for rarity, items_in_rarity in sorted_items.items():
            # Ajouter un label pour la catégorie de rareté
            rarity_label = QLabel(f"Rareté : {rarity.capitalize()}")
            rarity_label.setFont(QFont("Arial", 12, QFont.Bold))
            main_layout.addWidget(rarity_label)

            # Ajouter les items de cette rareté au FlowLayout
            flow_layout = FlowLayout(spacing=10)
            for item in items_in_rarity:
                item_name = item['name']
                image_path = f"ressources/icons/{item['image_path']}"
                card = ItemCard(item_name, image_path)
                flow_layout.addWidget(card)

            # Encapsuler chaque section dans un widget pour gérer le spacing
            section_widget = QWidget()
            section_widget.setLayout(flow_layout)
            main_layout.addWidget(section_widget)

            # Ajouter une ligne de séparation après chaque groupe de rareté
            separator = QFrame()
            separator.setFrameShape(QFrame.HLine)
            separator.setFrameShadow(QFrame.Sunken)
            main_layout.addWidget(separator)

        # Configurer le QScrollArea pour contenir tous les items
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_widget = QWidget()
        scroll_area_widget.setLayout(main_layout)
        scroll_area.setWidget(scroll_area_widget)

        # Ajouter le QScrollArea à la fenêtre principale
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        self.setLayout(layout)

    def sort_items_by_rarity(self, items):
        """Trie les items par rareté."""
        sorted_items = {}
        for item in items:
            rarity = item['rarity']
            if rarity not in sorted_items:
                sorted_items[rarity] = []
            sorted_items[rarity].append(item)
        return sorted_items
