from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from controllers.build_controller import get_all_builds, get_build_levels

class ShowBuildsWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.build_list = QListWidget()
        self.build_list.itemClicked.connect(self.display_build_levels)
        layout.addWidget(self.build_list)

        self.build_detail = QLabel("Sélectionnez un build pour voir les détails.")
        layout.addWidget(self.build_detail)

        self.setLayout(layout)

        # Charger la liste des builds
        self.load_builds()

    def load_builds(self):
        builds = get_all_builds()
        for build in builds:
            item = QListWidgetItem(f"{build[1]} ({build[2]} {build[3]})")
            item.setData(1, build[0])  # Stocke l'ID du build dans l'item
            self.build_list.addItem(item)

    def display_build_levels(self, item):
        build_id = item.data(1)
        levels = get_build_levels(build_id)
        detail_text = f"Détails pour {item.text()}:\n"
        for level in levels:
            detail_text += f"--- Niveau {level[0]} ---\n"
            detail_text += f"Sorts : {level[1]}\n"
            detail_text += f"Dons : {level[2]}\n"
            detail_text += f"Sous-classe : {level[3]}\n"
            detail_text += f"Multiclassage : {level[4]}\n\n"
        self.build_detail.setText(detail_text)
