from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from controllers.weapon_controller import get_all_weapons, search_weapons

class ShowWeaponsWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.weapon_list = QListWidget()
        layout.addWidget(self.weapon_list)

        self.weapon_detail = QLabel("Sélectionnez une arme pour voir les détails.")
        layout.addWidget(self.weapon_detail)

        self.setLayout(layout)

        # Charger la liste des armes
        self.load_weapons()

    def load_weapons(self):
        weapons = get_all_weapons()
        for weapon in weapons:
            item = QListWidgetItem(f"{weapon[1]} - {weapon[2]}")
            item.setData(1, weapon[0])  # Stocke l'ID de l'arme dans l'item
            self.weapon_list.addItem(item)

    def display_weapon_details(self, item):
        weapon_id = item.data(1)
        # Ajoute ici la logique pour afficher les détails de l'arme
