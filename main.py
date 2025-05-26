import sys
import random 
from PySide6.QtCore import Qt, QRectF
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QDoubleValidator, QPixmap, QImage, QPainter

from gui.main_ui import Ui_MainWindow
from src import Calc

class ExpanseTracker(QMainWindow):
    def __init__(self):
        super(ExpanseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_inputs()
        self.setup_connections()

        self.load_image('./images/AlekseiAnoshko.jpg')

        self.calc = Calc()

    def setup_inputs(self):
        self.ui.stair_w.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.stair_h.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.area.setValidator(QDoubleValidator(0.0, 1000.0, 2))

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(self.calculate)

    def get_data(self) -> dict:
        try:
            stair_w = float(self.ui.stair_w.text().replace(',', '.'))
            stair_h = float(self.ui.stair_h.text().replace(',', '.'))
            area = float(self.ui.area.text().replace(',', '.'))
            stair_type = self.ui.stair_type.currentText()
            
            return {
                'width': stair_w,
                'height': stair_h,
                'area': area,
                'type': stair_type
            }
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения")
            return None
    
    def load_image(self, image_path: str):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(
                self.ui.image.width(),
                self.ui.image.height(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.image.setPixmap(scaled_pixmap)
            self.ui.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def calculate(self):
        data = self.get_data()
        self.calc.calc(
            stair_type=data['type'],
            stair_widht=data['width'],
            stair_height=data['height'],
            area=data['area']
        )

    def generate_number(self):
        print(self.ui.stair_w.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpanseTracker()
    window.show()

    sys.exit(app.exec())