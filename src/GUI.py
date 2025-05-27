from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QHeaderView, QTableWidgetItem
from PySide6.QtGui import QDoubleValidator, QPixmap, QColor

from gui.main_ui import Ui_MainWindow
from gui.result_ui import Ui_Dialog as ui_result_gui
from gui.db_results_ui import Ui_Allresult as ui_result_table_gui
from src import Calc, DB


calc = Calc()
db = DB()

class resultsTable(QMainWindow):
    def __init__(self):
        super(resultsTable, self).__init__()
        self.ui = ui_result_table_gui()
        self.ui.setupUi(self)
        self.table = self.ui.tableWidget

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.update_table()

    def update_table(self):
        for row in reversed(range(self.table.rowCount())):
            self.table.removeRow(row)

        data = db.get_items()
        rows = len(data)
        cols = len(data[0][1:]) if rows > 0 else 0
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        for row_idx, row_data in enumerate(reversed(data)):
            for col_idx, cell_data in enumerate(row_data[1:]):
                item = QTableWidgetItem(str(cell_data) if cell_data != 'None' else '-')
                item.setTextAlignment(Qt.AlignHCenter)
                if col_idx == 7:
                    if .60 <= float(cell_data) <= .66:
                        item.setBackground(QColor(0, 116, 57))
                    else:
                        item.setBackground(QColor(166, 40, 0))
                self.table.setItem(row_idx, col_idx, item)

    def show_table(self):
        self.update_table()
        self.show()


class ResultWindow(QMainWindow):
    def __init__(self):
        super(ResultWindow, self).__init__()
        self.ui = ui_result_gui()
        self.ui.setupUi(self)

        self.check_color: dict = {
            'bad': "#A62800",
            'good': '#007439'
        }

    def _calculate(self, data: dict) -> dict:
        calc.set_stair_type(data['type'])
        calc.set_step_height(data['stepHeight'])
        calc.set_stair_width(data['width'])
        calc.set_stair_height(data['height'])
        calc.set_area(data['area'])
        if calc._current_stair_type in (calc.stairs_types[2], calc.stairs_types[-1]):
            calc.set_angle(data['radiusAngle'])
        else:
            calc.set_angle(None)
        calc.set_r(data['radiusAngle'] if calc._current_stair_type == calc.stairs_types[-2] else None)

        return calc.calc()

    def load_result(self, data: dict):
        result: dict = self._calculate(data)
        db.add_item(data, result)

        self.ui.step_count_label.setText('Ступеней в марше' if calc._current_stair_type == calc.stairs_types[1] else 'Количество ступеней')
        self.ui.step_count.setText(str(result['numOfSteps']))
        self.ui.step_hight.setText(str(result['stepHeight']))
        self.ui.step_pitch.setText(str(result['stepPitch']))
        check_status = 'good' if result['checkStatus'] else 'bad'
        check_result = round(result['checkValue'], 2)
        self.ui.result_label.setStyleSheet(f"""
            font-size: 18px;
            border: none;
            background-color:{self.check_color[check_status]};
            border-radius: 8px;
        """)
        if result['checkStatus']:
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
        self.result_table_window = resultsTable()

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
        
        if stair_type in calc.stairs_types[2:]:
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
        self.ui.btn_results.clicked.connect(self.result_table_window.show_table)

    def get_data(self) -> dict:
        try:
            stair_w = float(self.ui.stair_w.text().replace(',', '.'))
            stair_h = float(self.ui.stair_h.text().replace(',', '.'))
            area = float(self.ui.area.text().replace(',', '.'))
            stair_type = self.ui.stair_type.currentText()
            step_h = float(self.ui.step_h.text().replace(',', '.'))
            if stair_type in calc.stairs_types[2:]:
                radius_angle = float(self.ui.radius_angle.text().replace(',', '.'))
            else:
                radius_angle = None

            return {
                'width': stair_w,
                'height': stair_h,
                'area': area,
                'type': stair_type,
                'stepHeight': step_h,
                'radiusAngle': radius_angle
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