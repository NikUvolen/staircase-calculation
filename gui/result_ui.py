# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 320)
        Dialog.setMinimumSize(QSize(480, 320))
        Dialog.setMaximumSize(QSize(480, 320))
        Dialog.setStyleSheet(u"font: 16px \"Comic Sans MS\";\n"
"\n"
"color: white;\n"
"\n"
"background-color: #100A29;")
        self.Title = QFrame(Dialog)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 0, 225, 81))
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

        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 100, 421, 209))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.StepCount = QHBoxLayout()
        self.StepCount.setObjectName(u"StepCount")
        self.step_count_label = QLabel(self.layoutWidget)
        self.step_count_label.setObjectName(u"step_count_label")
        self.step_count_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.StepCount.addWidget(self.step_count_label)

        self.step_count = QLineEdit(self.layoutWidget)
        self.step_count.setObjectName(u"step_count")
        self.step_count.setMaximumSize(QSize(220, 16777215))
        self.step_count.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")
        self.step_count.setReadOnly(True)

        self.StepCount.addWidget(self.step_count)


        self.verticalLayout.addLayout(self.StepCount)

        self.StepHight = QHBoxLayout()
        self.StepHight.setObjectName(u"StepHight")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.StepHight.addWidget(self.label_3)

        self.step_hight = QLineEdit(self.layoutWidget)
        self.step_hight.setObjectName(u"step_hight")
        self.step_hight.setMaximumSize(QSize(220, 16777215))
        self.step_hight.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")
        self.step_hight.setReadOnly(True)

        self.StepHight.addWidget(self.step_hight)


        self.verticalLayout.addLayout(self.StepHight)

        self.StepPitch = QHBoxLayout()
        self.StepPitch.setObjectName(u"StepPitch")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 18px;\n"
"border: none;")

        self.StepPitch.addWidget(self.label_2)

        self.step_pitch = QLineEdit(self.layoutWidget)
        self.step_pitch.setObjectName(u"step_pitch")
        self.step_pitch.setMaximumSize(QSize(220, 16777215))
        self.step_pitch.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #681E76;  /* \u041e\u0431\u044b\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C33278;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 (\u0441\u0438\u043d\u044f\u044f) */\n"
"}")
        self.step_pitch.setReadOnly(True)

        self.StepPitch.addWidget(self.step_pitch)


        self.verticalLayout.addLayout(self.StepPitch)

        self.result_label = QLabel(self.layoutWidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(0, 40))
        self.result_label.setMaximumSize(QSize(16777215, 40))
        self.result_label.setStyleSheet(u"font-size: 18px;\n"
"border: none;\n"
"background-color:#007439;\n"
"border-radius: 8px;")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calc result", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Result", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Calculation", None))
        self.step_count_label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0428\u0430\u0433 \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.result_label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u0432 \u043f\u0440\u0435\u0434\u0435\u043b\u0430\u0445 \u043d\u043e\u0440\u043c\u044b", None))
    # retranslateUi

