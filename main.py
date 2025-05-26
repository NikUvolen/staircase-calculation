import sys
import random 
from PySide6.QtCore import Qt, QRectF
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QDoubleValidator, QPixmap, QImage, QPainter, QIcon

from gui.main_ui import Ui_MainWindow
from gui.result_ui import Ui_Dialog
from src import Calc


calc = Calc()
class ResultWindow(QMainWindow):
    def __init__(self):
        super(ResultWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.check_color: dict = {
            'bad': '#A62800',
            'good': '#007439'
        }
    
    def load_result(self, data: dict):
        result = calc.calc(data['type'], data['width'], data['height'], data['area'])
        print(result)
        self.ui.step_count.setText(str(result[0]))
        self.ui.step_hight.setText(str(result[1]))
        self.ui.step_pitch.setText(str(result[2]))
        check_status = 'good' if result[4] else 'bad'
        check_result = round(result[3], 2)
        self.ui.result_label.setStyleSheet(f"""
            font-size: 18px;
            border: none;
            background-color:{self.check_color[check_status]};
            border-radius: 8px;
        """)
        if result[4]:
            self.ui.result_label.setText(f'Эргономическое соотношение {check_result}')
        else:
            self.ui.result_label.setText(f'Эргономическое соотношение {check_result}')
        self.show()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.result_window = ResultWindow()

        self.setup_inputs()
        self.setup_connections()

        self.images_links: dict = {
            calc.stairs_types[0]: 'images/direct_march.jpg',
            calc.stairs_types[1]: 'images/two_straight_march.jpg',
            calc.stairs_types[2]: 'images/corner.jpg',
            calc.stairs_types[3]: 'images/screw.jpg',
            calc.stairs_types[4]: 'images/turning.jpg',
        }

        self._additional_layout(self.ui.stair_type.currentText(), self.ui.radius_angle_frame)
        self._change_combo_image(self.ui.stair_type.currentText())

    def _additional_layout(self, stair_type: str, layout):
        def hide_or_show(needHide: bool):
            for idx in range(layout.count()):
                item = layout.itemAt(idx)
                if item.widget():
                    if needHide:
                        item.widget().hide()
                    else:
                        item.widget().show()
        
        if stair_type in calc.stairs_types[-2:]:
            if stair_type == calc.stairs_types[-2]:
                self.ui.radius_angle_label.setText('Радиус окружности')
                self.ui.label_22.setText('м')
            else:
                self.ui.radius_angle_label.setText('Угол поворота')
                self.ui.label_22.setText('°')
            hide_or_show(needHide=False)
        else:
            hide_or_show(needHide=True)
            

    def setup_inputs(self):
        self.ui.stair_w.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.stair_h.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.area.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.step_h.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.ui.radius_angle.setValidator(QDoubleValidator(0.0, 1000.0, 2))

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(lambda x: self.result_window.load_result(self.get_data()))
        self.ui.stair_type.currentTextChanged.connect(
            lambda stair_type: self._additional_layout(stair_type, self.ui.radius_angle_frame)
        )
        self.ui.stair_type.currentTextChanged.connect(
            lambda stair_type: self._change_combo_image(stair_type)
        )

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
    
    def _change_combo_image(self, stair_type: str):
        self.load_image(self.images_links[stair_type])

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./gui/icons/calc.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())