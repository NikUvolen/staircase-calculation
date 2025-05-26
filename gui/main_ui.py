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
import gui.res_main_window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 435)
        MainWindow.setMinimumSize(QSize(860, 435))
        MainWindow.setMaximumSize(QSize(860, 435))
        MainWindow.setStyleSheet(u"font-family: Consolas;\n"
"font-size: 16px;\n"
"\n"
"color: white;\n"
"\n"
"background-color: #100A29;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 100, 811, 320))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.balance_frame = QFrame(self.widget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.balance_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.label)

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

        self.horizontalLayout.addWidget(self.stair_w)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.balance_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.label_3)

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

        self.horizontalLayout_3.addWidget(self.stair_h)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.balance_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_2)

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

        self.horizontalLayout_2.addWidget(self.area)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.balance_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: none;")

        self.horizontalLayout_4.addWidget(self.label_4)

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
        self.stair_type.setStyleSheet(u"/* \u041e\u0431\u044b\u0447\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 */\n"
"QComboBox {\n"
"    border: 2px solid #681E76;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    selection-background-color: #C33278;\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QComboBox:focus {\n"
"    border: 2px solid #C33278;  /* \u0421\u0438\u043d\u0438\u0439 \u0430\u043a\u0446\u0435\u043d\u0442\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u0412\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0438\u0439 \u0441\u043f\u0438\u0441\u043e\u043a */\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #681E76;\n"
"    selection-background-color: #C33278;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.stair_type)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.balance_frame)

        self.image = QLabel(self.widget)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(260, 260))
        self.image.setMaximumSize(QSize(260, 260))
        self.image.setStyleSheet(u"border: 2px solid #681E76;\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.image)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
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
        icon.addFile(u":/icon/icons8-calculator-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.Title = QFrame(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 20, 225, 71))
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Staircase Calculation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None))
        self.stair_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043f\u0440\u044f\u043c\u043e\u0439 \u043c\u0430\u0440\u0448", None))
        self.stair_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0434\u0432\u0430 \u043f\u0440\u044f\u043c\u044b\u0445 \u043c\u0430\u0440\u0448\u0435\u0439", None))
        self.stair_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0443\u0433\u043b\u043e\u0432\u0430\u044f", None))
        self.stair_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0432\u0438\u043d\u0442\u043e\u0432\u0430\u044f", None))
        self.stair_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0432\u043e\u0440\u043e\u0442\u043d\u0430\u044f", None))

        self.image.setText(QCoreApplication.translate("MainWindow", u"<image>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Staircase ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Calculation", None))
    # retranslateUi

