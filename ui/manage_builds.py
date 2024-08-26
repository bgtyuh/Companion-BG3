import os
import sqlite3

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem, QMessageBox

from controllers.build_controller import get_all_builds, delete_build
from ui.modify_build import ModifyBuildWidget


class ManageBuildsWidget(QWidget):
    def __init__(self, parent):
        """Initialise le widget pour gérer les builds existants."""
        super().__init__(parent)

        layout = QVBoxLayout()

        self.build_list = QListWidget()
        self.build_list.setIconSize(QSize(32, 32))  # Définit la taille des icônes dans la liste
        self.build_list.itemClicked.connect(self.show_build_options)
        layout.addWidget(self.build_list)

        # Bouton de retour au menu principal
        back_button = QPushButton("Retour au menu principal")
        back_button.clicked.connect(self.return_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

        self.load_builds()

    def load_builds(self):
        """Charge et affiche tous les builds depuis la base de données."""
        builds = get_all_builds()
        self.build_list.clear()
        for build in builds:
            class_icon_path = f"ressources/icons/class_images/{build[7]}" if build[7] else None
            subclass_icon_path = f"ressources/icons/class_images/{build[8]}" if build[8] else None

            # Vérification de l'existence des fichiers d'icônes
            class_icon = QIcon(class_icon_path) if class_icon_path and os.path.exists(class_icon_path) else QIcon()
            subclass_icon = QIcon(subclass_icon_path) if subclass_icon_path and os.path.exists(
                subclass_icon_path) else None

            item_text = f"{build[1]} - {build[2]} ({build[3]}) - {build[4]} - {build[5]} - {build[6]}"
            item = QListWidgetItem(class_icon, item_text)

            if subclass_icon:
                item.setIcon(subclass_icon)  # Utilise l'icône de la sous-classe si elle est présente

            item.setData(1, build[0])  # Stocke l'ID du build dans l'item
            self.build_list.addItem(item)

    def show_build_options(self, item):
        """Affiche des options pour modifier ou supprimer le build sélectionné."""
        build_id = item.data(1)
        msg_box = QMessageBox()
        msg_box.setText("Que voulez-vous faire avec ce build ?")
        msg_box.addButton(QPushButton("Modifier"), QMessageBox.AcceptRole)
        msg_box.addButton(QPushButton("Supprimer"), QMessageBox.RejectRole)
        msg_box.addButton(QPushButton("Annuler"), QMessageBox.DestructiveRole)

        choice = msg_box.exec_()

        if choice == QMessageBox.AcceptRole:
            self.modify_build(build_id)
        elif choice == QMessageBox.RejectRole:
            self.confirm_delete_build(build_id)

    def confirm_delete_build(self, build_id):
        """Demande confirmation pour supprimer le build."""
        confirm_box = QMessageBox()
        confirm_box.setText("Voulez-vous vraiment supprimer ce build ?")
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_box.setDefaultButton(QMessageBox.No)

        result = confirm_box.exec_()

        if result == QMessageBox.Yes:
            delete_build(build_id)
            self.load_builds()

    def modify_build(self, build_id):
        """Affiche l'interface de modification pour le build sélectionné."""
        build_data = self.get_build_data(build_id)
        modify_build_widget = ModifyBuildWidget(self, build_id, build_data)
        self.parent().setCentralWidget(modify_build_widget)

    def get_build_data(self, build_id):
        """Récupère les données actuelles du build pour pré-remplir le formulaire de modification."""
        conn = sqlite3.connect('data/bg3_builds.db')
        cursor = conn.cursor()

        cursor.execute("SELECT race_name, class_name, subclass_name, weapon_name, armor_name, footwear_name FROM builds WHERE id = ?", (build_id,))
        build = cursor.fetchone()

        conn.close()

        return {
            'race_name': build[0],
            'class_name': build[1],
            'subclass_name': build[2],
            'weapon_name': build[3],
            'armor_name': build[4],
            'footwear_name': build[5]
        }

    def return_to_main(self):
        """Retourne au menu principal."""
        self.parent().show_main_menu()
