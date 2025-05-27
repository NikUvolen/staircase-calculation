# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_results.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Allresult(object):
    def setupUi(self, Allresult):
        if not Allresult.objectName():
            Allresult.setObjectName(u"Allresult")
        Allresult.resize(1707, 801)
        Allresult.setStyleSheet(u"font: 16px \"Comic Sans MS\";\n"
"color: white;\n"
"\n"
"background-color: #100A29;")
        self.centralwidget = QWidget(Allresult)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"margin:5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QWidget(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"font-weight:700;\n"
"font-size:28px;")
        self.verticalLayout_3 = QVBoxLayout(self.Title)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.Title)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.Title)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.Title)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"        background-color: #681E76;\n"
"        color: white;\n"
"        padding: 5px;\n"
"        border: none;\n"
"        font-weight: bold;\n"
"		height:30px;\n"
"    }\n"
"    \n"
"QHeaderView {\n"
"        background-color: transparent;\n"
"		font-size:16px;\n"
"}")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.frame)

        Allresult.setCentralWidget(self.centralwidget)

        self.retranslateUi(Allresult)

        QMetaObject.connectSlotsByName(Allresult)
    # setupUi

    def retranslateUi(self, Allresult):
        Allresult.setWindowTitle(QCoreApplication.translate("Allresult", u"All result", None))
        self.label_5.setText(QCoreApplication.translate("Allresult", u"Results", None))
        self.label_6.setText(QCoreApplication.translate("Allresult", u"Calculation", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Allresult", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Allresult", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Allresult", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Allresult", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Allresult", u"\u0423\u0433\u043e\u043b/\u0440\u0430\u0434\u0438\u0443\u0441", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Allresult", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Allresult", u"\u0428\u0430\u0433 \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Allresult", u"\u042d\u0440\u043e\u0433\u043e\u043d\u043e\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u043e\u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Allresult", u"\u0422\u0438\u043f \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u044b", None));
    # retranslateUi

