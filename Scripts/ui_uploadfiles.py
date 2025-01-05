# -*- coding: utf-8 -*-

# Form generated from reading UI file 'uploadfiles.ui'
# Created by: Qt User Interface Compiler version 5.15.2
# WARNING! All changes made in this file will be lost when recompiling UI file!

from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide2.QtGui import QCursor, QFont
from PySide2.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Ui_Upload(object):
    def setupUi(self, Upload):
        if not Upload.objectName():
            Upload.setObjectName("Upload")
        Upload.resize(370, 144)
        Upload.setMinimumSize(QSize(370, 120))
        Upload.setMaximumSize(QSize(370, 144))
        Upload.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout_4 = QVBoxLayout(Upload)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QWidget(Upload)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet(
            "background-color: rgb(140, 140, 140);\n" "border-radius: 5px;"
        )
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgba(0, 0, 0, 0.3);"
        )

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEndr = QLineEdit(self.frame)
        self.lineEndr.setObjectName("lineEndr")
        self.lineEndr.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 2px;\n" ""
        )

        self.horizontalLayout.addWidget(self.lineEndr)

        self.BuscarPlanilha = QPushButton(self.frame)
        self.BuscarPlanilha.setObjectName("BuscarPlanilha")
        self.BuscarPlanilha.setFont(font)
        self.BuscarPlanilha.setCursor(QCursor(Qt.PointingHandCursor))
        self.BuscarPlanilha.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgba(255, 255, 255, 0.5);\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 2px solid rgb(102, 102, 102);\n"
            "border-radius: 5px\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.BuscarPlanilha)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3.addWidget(self.frame)

        self.IniciarUpload = QPushButton(self.widget)
        self.IniciarUpload.setObjectName("IniciarUpload")
        self.IniciarUpload.setFont(font)
        self.IniciarUpload.setCursor(QCursor(Qt.PointingHandCursor))
        self.IniciarUpload.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgba(255, 255, 255, 0.5);\n"
            "border: 3px solid rgb(132, 132, 132);\n"
            "border-radius: 5px;\n"
            "margin: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: 2px solid rgb(102, 102, 102);\n"
            "border-radius: 5px\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.IniciarUpload)

        self.verticalLayout_4.addWidget(self.widget, 0, Qt.AlignVCenter)

        self.retranslateUi(Upload)

        QMetaObject.connectSlotsByName(Upload)

    # setupUi

    def retranslateUi(self, Upload):
        Upload.setWindowTitle(QCoreApplication.translate("Upload", "Form", None))
        self.label.setText(
            QCoreApplication.translate(
                "Upload", "Informe a planilha com arquivos a serem enviados", None
            )
        )
        self.BuscarPlanilha.setText(
            QCoreApplication.translate("Upload", "Buscar", None)
        )
        self.IniciarUpload.setText(
            QCoreApplication.translate("Upload", "Iniciar", None)
        )

    # retranslateUi
