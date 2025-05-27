# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import gui.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 480)
        MainWindow.setMinimumSize(QSize(860, 480))
        MainWindow.setMaximumSize(QSize(860, 480))
        MainWindow.setStyleSheet(u"font: 16px \"Comic Sans MS\";\n"
"\n"
"color: white;\n"
"\n"
"background-color: #100A29;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 811, 380))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.balance_frame = QFrame(self.layoutWidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stair_type_frame = QHBoxLayout()
        self.stair_type_frame.setObjectName(u"stair_type_frame")
        self.stair_type_label = QLabel(self.balance_frame)
        self.stair_type_label.setObjectName(u"stair_type_label")
        self.stair_type_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_type_frame.addWidget(self.stair_type_label)

        self.stair_type = QComboBox(self.balance_frame)
        self.stair_type.addItem("")
        self.stair_type.addItem("")
        self.stair_type.addItem("")
        self.stair_type.addItem("")
        self.stair_type.addItem("")
        self.stair_type.setObjectName(u"stair_type")
        self.stair_type.setEnabled(True)
        self.stair_type.setMinimumSize(QSize(300, 0))
        self.stair_type.setMaximumSize(QSize(300, 16777215))
        self.stair_type.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stair_type.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0441\u0442\u0438\u043b\u044c ComboBox */\n"
"QComboBox {\n"
"    border: 2px solid #681E76;\n"
"    border-radius: 8px;\n"
"    padding: 5px 25px 5px 10px;\n"
"    selection-background-color: #C33278;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* \u041e\u0431\u043b\u0430\u0441\u0442\u044c \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 25px;\n"
"    border-left: 1px solid #681E76;\n"
"}\n"
"\n"
"/* Unicode-\u0441\u0442\u0440\u0435\u043b\u043a\u0430 \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/arrow.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QComboBox:fo"
                        "cus {\n"
"    border-color: #C33278;\n"
"}\n"
"\n"
"/* \u0412\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0438\u0439 \u0441\u043f\u0438\u0441\u043e\u043a */\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #681E76;\n"
"    selection-background-color: #C33278;\n"
"}")

        self.stair_type_frame.addWidget(self.stair_type)

        self.label_10 = QLabel(self.balance_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(25, 16777215))
        self.label_10.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_type_frame.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.stair_type_frame)

        self.stair_w_frame = QHBoxLayout()
        self.stair_w_frame.setObjectName(u"stair_w_frame")
        self.stare_w_label = QLabel(self.balance_frame)
        self.stare_w_label.setObjectName(u"stare_w_label")
        self.stare_w_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_w_frame.addWidget(self.stare_w_label)

        self.stair_w = QLineEdit(self.balance_frame)
        self.stair_w.setObjectName(u"stair_w")
        self.stair_w.setMaximumSize(QSize(300, 16777215))
        self.stair_w.setFocusPolicy(Qt.StrongFocus)
        self.stair_w.setAutoFillBackground(False)
        self.stair_w.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")

        self.stair_w_frame.addWidget(self.stair_w)

        self.label_7 = QLabel(self.balance_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(25, 16777215))
        self.label_7.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_w_frame.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.stair_w_frame)

        self.stair_h_frame = QHBoxLayout()
        self.stair_h_frame.setObjectName(u"stair_h_frame")
        self.stair_h_label = QLabel(self.balance_frame)
        self.stair_h_label.setObjectName(u"stair_h_label")
        self.stair_h_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_h_frame.addWidget(self.stair_h_label)

        self.stair_h = QLineEdit(self.balance_frame)
        self.stair_h.setObjectName(u"stair_h")
        self.stair_h.setMaximumSize(QSize(300, 16777215))
        self.stair_h.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")

        self.stair_h_frame.addWidget(self.stair_h)

        self.label_8 = QLabel(self.balance_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(25, 16777215))
        self.label_8.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.stair_h_frame.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.stair_h_frame)

        self.area_frame = QHBoxLayout()
        self.area_frame.setObjectName(u"area_frame")
        self.area_frame_2 = QLabel(self.balance_frame)
        self.area_frame_2.setObjectName(u"area_frame_2")
        self.area_frame_2.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.area_frame.addWidget(self.area_frame_2)

        self.area = QLineEdit(self.balance_frame)
        self.area.setObjectName(u"area")
        self.area.setMaximumSize(QSize(300, 16777215))
        self.area.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")

        self.area_frame.addWidget(self.area)

        self.label_9 = QLabel(self.balance_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(25, 16777215))
        self.label_9.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.area_frame.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.area_frame)

        self.step_h_frame = QHBoxLayout()
        self.step_h_frame.setObjectName(u"step_h_frame")
        self.stap_h_label = QLabel(self.balance_frame)
        self.stap_h_label.setObjectName(u"stap_h_label")
        self.stap_h_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.step_h_frame.addWidget(self.stap_h_label)

        self.step_h = QLineEdit(self.balance_frame)
        self.step_h.setObjectName(u"step_h")
        self.step_h.setMaximumSize(QSize(300, 16777215))
        self.step_h.setFocusPolicy(Qt.StrongFocus)
        self.step_h.setAutoFillBackground(False)
        self.step_h.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")

        self.step_h_frame.addWidget(self.step_h)

        self.label_18 = QLabel(self.balance_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(25, 16777215))
        self.label_18.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.step_h_frame.addWidget(self.label_18)


        self.verticalLayout.addLayout(self.step_h_frame)

        self.radius_angle_frame = QHBoxLayout()
        self.radius_angle_frame.setObjectName(u"radius_angle_frame")
        self.radius_angle_label = QLabel(self.balance_frame)
        self.radius_angle_label.setObjectName(u"radius_angle_label")
        self.radius_angle_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.radius_angle_frame.addWidget(self.radius_angle_label)

        self.radius_angle = QLineEdit(self.balance_frame)
        self.radius_angle.setObjectName(u"radius_angle")
        self.radius_angle.setMaximumSize(QSize(300, 16777215))
        self.radius_angle.setFocusPolicy(Qt.StrongFocus)
        self.radius_angle.setAutoFillBackground(False)
        self.radius_angle.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")

        self.radius_angle_frame.addWidget(self.radius_angle)

        self.label_22 = QLabel(self.balance_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(25, 16777215))
        self.label_22.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.radius_angle_frame.addWidget(self.label_22)


        self.verticalLayout.addLayout(self.radius_angle_frame)


        self.horizontalLayout_5.addWidget(self.balance_frame)

        self.image = QLabel(self.layoutWidget)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(260, 260))
        self.image.setMaximumSize(QSize(260, 260))
        self.image.setStyleSheet(u"border: 2px solid #681E76;\n"
"border-radius: 8px;\n"
"overflow: hidden;")

        self.horizontalLayout_5.addWidget(self.image)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777202, 16777215))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font-weight: 700;\n"
"    background-color: #681E76;  /* \u0412\u0430\u0448 \u0446\u0432\u0435\u0442 \u0438\u0437 \u0434\u0438\u0437\u0430\u0439\u043d\u0430 */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C33278;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/calc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.Title = QFrame(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 10, 225, 81))
        self.Title.setStyleSheet(u"font-weight:700;\n"
"font-size:28px;")
        self.verticalLayout_3 = QVBoxLayout(self.Title)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.Title)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.Title)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_6)

        self.btn_results = QPushButton(self.centralwidget)
        self.btn_results.setObjectName(u"btn_results")
        self.btn_results.setGeometry(QRect(600, 30, 231, 40))
        self.btn_results.setMinimumSize(QSize(0, 40))
        self.btn_results.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_results.setAcceptDrops(False)
        self.btn_results.setStyleSheet(u"QPushButton {\n"
"	font-weight: 700;\n"
"    background-color: #681E76;  /* \u0412\u0430\u0448 \u0446\u0432\u0435\u0442 \u0438\u0437 \u0434\u0438\u0437\u0430\u0439\u043d\u0430 */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C33278;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_results.setIcon(icon1)
        self.btn_results.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Staircase Calculation", None))
        self.stair_type_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.stair_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043f\u0440\u044f\u043c\u043e\u0439 \u043c\u0430\u0440\u0448", None))
        self.stair_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0434\u0432\u0430 \u043f\u0440\u044f\u043c\u044b\u0445 \u043c\u0430\u0440\u0448\u0435\u0439", None))
        self.stair_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0443\u0433\u043b\u043e\u0432\u0430\u044f", None))
        self.stair_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0432\u0438\u043d\u0442\u043e\u0432\u0430\u044f", None))
        self.stair_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0432\u043e\u0440\u043e\u0442\u043d\u0430\u044f", None))

        self.label_10.setText("")
        self.stare_w_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.stair_h_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.area_frame_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u043c\u00b2 ", None))
        self.stap_h_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.step_h.setText(QCoreApplication.translate("MainWindow", u"0,17", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.radius_angle_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.radius_angle.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"<image>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Staircase ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Calculation", None))
        self.btn_results.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432", None))
    # retranslateUi

