from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ShowBuildsWidget(QWidget):
    def __init__(self, builds):
        super().__init__()

        layout = QVBoxLayout()

        # Ajouter un label pour chaque build
        for build in builds:
            build_label = QLabel(f"{build[1]} ({build[2]} {build[3]}) - Niveau {build[5]}")
            layout.addWidget(build_label)

        self.setLayout(layout)
