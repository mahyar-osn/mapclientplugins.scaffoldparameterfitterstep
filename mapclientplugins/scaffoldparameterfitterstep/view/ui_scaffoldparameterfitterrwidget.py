# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scaffoldparameterfitterrwidget.ui'
#
# Created: Sun Jul  7 15:23:42 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScaffoldParameterFitter(object):
    def setupUi(self, ScaffoldParameterFitter, shareableWidget):
        ScaffoldParameterFitter.setObjectName("ScaffoldParameterFitter")
        ScaffoldParameterFitter.resize(1982, 998)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScaffoldParameterFitter.sizePolicy().hasHeightForWidth())
        ScaffoldParameterFitter.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(ScaffoldParameterFitter)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(ScaffoldParameterFitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(418, 135))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 416, 956))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtGui.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setStyleSheet("QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.parameterFitPage = QtGui.QWidget()
        self.parameterFitPage.setGeometry(QtCore.QRect(0, 0, 395, 942))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameterFitPage.sizePolicy().hasHeightForWidth())
        self.parameterFitPage.setSizePolicy(sizePolicy)
        self.parameterFitPage.setObjectName("parameterFitPage")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.parameterFitPage)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scaffoldFrame = QtGui.QFrame(self.parameterFitPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaffoldFrame.sizePolicy().hasHeightForWidth())
        self.scaffoldFrame.setSizePolicy(sizePolicy)
        self.scaffoldFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.scaffoldFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scaffoldFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.scaffoldFrame.setObjectName("scaffoldFrame")
        self.gridLayout_7 = QtGui.QGridLayout(self.scaffoldFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scaffoldFrame_line_1 = QtGui.QFrame(self.scaffoldFrame)
        self.scaffoldFrame_line_1.setFrameShape(QtGui.QFrame.HLine)
        self.scaffoldFrame_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.scaffoldFrame_line_1.setObjectName("scaffoldFrame_line_1")
        self.gridLayout_7.addWidget(self.scaffoldFrame_line_1, 1, 0, 1, 1)
        self.scaffoldFrame_line_2 = QtGui.QFrame(self.scaffoldFrame)
        self.scaffoldFrame_line_2.setFrameShape(QtGui.QFrame.HLine)
        self.scaffoldFrame_line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.scaffoldFrame_line_2.setObjectName("scaffoldFrame_line_2")
        self.gridLayout_7.addWidget(self.scaffoldFrame_line_2, 3, 0, 1, 1)
        self.meshType_frame = QtGui.QFrame(self.scaffoldFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meshType_frame.sizePolicy().hasHeightForWidth())
        self.meshType_frame.setSizePolicy(sizePolicy)
        self.meshType_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshType_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshType_frame.setObjectName("meshType_frame")
        self.formLayout_4 = QtGui.QFormLayout(self.meshType_frame)
        self.formLayout_4.setContentsMargins(0, -1, 0, -1)
        self.formLayout_4.setObjectName("formLayout_4")
        self.meshType_label = QtGui.QLabel(self.meshType_frame)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setBold(True)
        self.meshType_label.setFont(font)
        self.meshType_label.setObjectName("meshType_label")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.meshType_label)
        self.parameterSet_label = QtGui.QLabel(self.meshType_frame)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setBold(True)
        self.parameterSet_label.setFont(font)
        self.parameterSet_label.setObjectName("parameterSet_label")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.parameterSet_label)
        self.gridLayout_7.addWidget(self.meshType_frame, 0, 0, 1, 1)
        self.meshTypeOptions_frame = QtGui.QFrame(self.scaffoldFrame)
        self.meshTypeOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshTypeOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshTypeOptions_frame.setObjectName("meshTypeOptions_frame")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.meshTypeOptions_frame)
        self.verticalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.gridLayout_7.addWidget(self.meshTypeOptions_frame, 2, 0, 1, 1)
        self.modifyOptions_frame = QtGui.QFrame(self.scaffoldFrame)
        self.modifyOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.modifyOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.modifyOptions_frame.setObjectName("modifyOptions_frame")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.modifyOptions_frame)
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.timeSeries_groupBox = QtGui.QGroupBox(self.modifyOptions_frame)
        self.timeSeries_groupBox.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.timeSeries_groupBox.setFont(font)
        self.timeSeries_groupBox.setObjectName("timeSeries_groupBox")
        self.gridLayout_5 = QtGui.QGridLayout(self.timeSeries_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.timePoint_label = QtGui.QLabel(self.timeSeries_groupBox)
        self.timePoint_label.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timePoint_label.sizePolicy().hasHeightForWidth())
        self.timePoint_label.setSizePolicy(sizePolicy)
        self.timePoint_label.setObjectName("timePoint_label")
        self.gridLayout_5.addWidget(self.timePoint_label, 0, 0, 1, 1)
        self.timePoint_spinBox = QtGui.QSpinBox(self.timeSeries_groupBox)
        self.timePoint_spinBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timePoint_spinBox.sizePolicy().hasHeightForWidth())
        self.timePoint_spinBox.setSizePolicy(sizePolicy)
        self.timePoint_spinBox.setMaximum(1000000000)
        self.timePoint_spinBox.setObjectName("timePoint_spinBox")
        self.gridLayout_5.addWidget(self.timePoint_spinBox, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 1, 1, 1)
        self.verticalLayout_17.addWidget(self.timeSeries_groupBox)
        self.gridLayout_7.addWidget(self.modifyOptions_frame, 4, 0, 1, 1)
        self.transformation_groupBox = QtGui.QGroupBox(self.scaffoldFrame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.transformation_groupBox.setFont(font)
        self.transformation_groupBox.setObjectName("transformation_groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.transformation_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rateOfChange_label = QtGui.QLabel(self.transformation_groupBox)
        self.rateOfChange_label.setObjectName("rateOfChange_label")
        self.gridLayout_2.addWidget(self.rateOfChange_label, 6, 0, 1, 1)
        self.rateOfChange_horizontalSlider = QtGui.QSlider(self.transformation_groupBox)
        self.rateOfChange_horizontalSlider.setMinimum(1)
        self.rateOfChange_horizontalSlider.setMaximum(20)
        self.rateOfChange_horizontalSlider.setProperty("value", 10)
        self.rateOfChange_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateOfChange_horizontalSlider.setObjectName("rateOfChange_horizontalSlider")
        self.gridLayout_2.addWidget(self.rateOfChange_horizontalSlider, 6, 2, 1, 1)
        self.rotateAxis_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.rotateAxis_label.setFont(font)
        self.rotateAxis_label.setObjectName("rotateAxis_label")
        self.gridLayout_2.addWidget(self.rotateAxis_label, 0, 0, 1, 1)
        self.position_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.position_label.setFont(font)
        self.position_label.setObjectName("position_label")
        self.gridLayout_2.addWidget(self.position_label, 3, 0, 1, 1)
        self.positionY_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionY_label.setFont(font)
        self.positionY_label.setObjectName("positionY_label")
        self.gridLayout_2.addWidget(self.positionY_label, 4, 2, 1, 1)
        self.positionZ_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionZ_label.setFont(font)
        self.positionZ_label.setObjectName("positionZ_label")
        self.gridLayout_2.addWidget(self.positionZ_label, 4, 4, 1, 1)
        self.positionX_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionX_label.setFont(font)
        self.positionX_label.setObjectName("positionX_label")
        self.gridLayout_2.addWidget(self.positionX_label, 4, 0, 1, 1)
        self.positionY_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionY_doubleSpinBox.setFont(font)
        self.positionY_doubleSpinBox.setMinimum(-1000000000.0)
        self.positionY_doubleSpinBox.setMaximum(1000000000.0)
        self.positionY_doubleSpinBox.setObjectName("positionY_doubleSpinBox")
        self.gridLayout_2.addWidget(self.positionY_doubleSpinBox, 5, 2, 1, 1)
        self.pitch_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.pitch_doubleSpinBox.setFont(font)
        self.pitch_doubleSpinBox.setMinimum(-360.0)
        self.pitch_doubleSpinBox.setMaximum(360.0)
        self.pitch_doubleSpinBox.setObjectName("pitch_doubleSpinBox")
        self.gridLayout_2.addWidget(self.pitch_doubleSpinBox, 2, 2, 1, 1)
        self.roll_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.roll_label.setFont(font)
        self.roll_label.setObjectName("roll_label")
        self.gridLayout_2.addWidget(self.roll_label, 1, 4, 1, 1)
        self.positionZ_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionZ_doubleSpinBox.setFont(font)
        self.positionZ_doubleSpinBox.setMinimum(-1000000000.0)
        self.positionZ_doubleSpinBox.setMaximum(1000000000.0)
        self.positionZ_doubleSpinBox.setObjectName("positionZ_doubleSpinBox")
        self.gridLayout_2.addWidget(self.positionZ_doubleSpinBox, 5, 4, 1, 1)
        self.roll_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.roll_doubleSpinBox.setFont(font)
        self.roll_doubleSpinBox.setMinimum(-360.0)
        self.roll_doubleSpinBox.setMaximum(360.0)
        self.roll_doubleSpinBox.setObjectName("roll_doubleSpinBox")
        self.gridLayout_2.addWidget(self.roll_doubleSpinBox, 2, 4, 1, 1)
        self.yaw_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.yaw_label.setFont(font)
        self.yaw_label.setObjectName("yaw_label")
        self.gridLayout_2.addWidget(self.yaw_label, 1, 0, 1, 1)
        self.pitch_label = QtGui.QLabel(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.pitch_label.setFont(font)
        self.pitch_label.setObjectName("pitch_label")
        self.gridLayout_2.addWidget(self.pitch_label, 1, 2, 1, 1)
        self.yaw_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.yaw_doubleSpinBox.setFont(font)
        self.yaw_doubleSpinBox.setMinimum(-360.0)
        self.yaw_doubleSpinBox.setMaximum(360.0)
        self.yaw_doubleSpinBox.setObjectName("yaw_doubleSpinBox")
        self.gridLayout_2.addWidget(self.yaw_doubleSpinBox, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 5, 5, 1, 1)
        self.positionX_doubleSpinBox = QtGui.QDoubleSpinBox(self.transformation_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.positionX_doubleSpinBox.setFont(font)
        self.positionX_doubleSpinBox.setMinimum(-1000000000.0)
        self.positionX_doubleSpinBox.setMaximum(1000000000.0)
        self.positionX_doubleSpinBox.setObjectName("positionX_doubleSpinBox")
        self.gridLayout_2.addWidget(self.positionX_doubleSpinBox, 5, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 5, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 5, 1, 1, 1)
        self.gridLayout_7.addWidget(self.transformation_groupBox, 5, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.scaffoldFrame)
        spacerItem7 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem7)
        self.fitting_groupBox = QtGui.QGroupBox(self.parameterFitPage)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.fitting_groupBox.setFont(font)
        self.fitting_groupBox.setObjectName("fitting_groupBox")
        self.gridLayout_6 = QtGui.QGridLayout(self.fitting_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.NelderMead_radioButton = QtGui.QRadioButton(self.fitting_groupBox)
        self.NelderMead_radioButton.setObjectName("NelderMead_radioButton")
        self.gridLayout_6.addWidget(self.NelderMead_radioButton, 0, 2, 1, 1)
        self.optimisationMethod_label = QtGui.QLabel(self.fitting_groupBox)
        self.optimisationMethod_label.setObjectName("optimisationMethod_label")
        self.gridLayout_6.addWidget(self.optimisationMethod_label, 0, 0, 1, 1)
        self.SLSQ_radioButton = QtGui.QRadioButton(self.fitting_groupBox)
        self.SLSQ_radioButton.setObjectName("SLSQ_radioButton")
        self.gridLayout_6.addWidget(self.SLSQ_radioButton, 1, 1, 1, 1)
        self.fit_pushButton = QtGui.QPushButton(self.fitting_groupBox)
        self.fit_pushButton.setEnabled(False)
        self.fit_pushButton.setObjectName("fit_pushButton")
        self.gridLayout_6.addWidget(self.fit_pushButton, 10, 2, 1, 1)
        self.ConjugateGradient_radioButton = QtGui.QRadioButton(self.fitting_groupBox)
        self.ConjugateGradient_radioButton.setObjectName("ConjugateGradient_radioButton")
        self.gridLayout_6.addWidget(self.ConjugateGradient_radioButton, 1, 2, 1, 1)
        self.LMBFGS_radioButton = QtGui.QRadioButton(self.fitting_groupBox)
        self.LMBFGS_radioButton.setObjectName("LMBFGS_radioButton")
        self.gridLayout_6.addWidget(self.LMBFGS_radioButton, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem9, 9, 2, 1, 1)
        self.fitting_progressBar = QtGui.QProgressBar(self.fitting_groupBox)
        self.fitting_progressBar.setEnabled(False)
        self.fitting_progressBar.setProperty("value", 0)
        self.fitting_progressBar.setTextVisible(False)
        self.fitting_progressBar.setObjectName("fitting_progressBar")
        self.gridLayout_6.addWidget(self.fitting_progressBar, 11, 2, 1, 1)
        self.label = QtGui.QLabel(self.fitting_groupBox)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 11, 1, 1, 1)
        self.fitOption_frame = QtGui.QFrame(self.fitting_groupBox)
        self.fitOption_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fitOption_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.fitOption_frame.setObjectName("fitOption_frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.fitOption_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fitOptions_label = QtGui.QLabel(self.fitOption_frame)
        self.fitOptions_label.setObjectName("fitOptions_label")
        self.gridLayout_3.addWidget(self.fitOptions_label, 0, 0, 1, 1)
        self.fitCurrentTime_radioButton = QtGui.QRadioButton(self.fitOption_frame)
        self.fitCurrentTime_radioButton.setObjectName("fitCurrentTime_radioButton")
        self.gridLayout_3.addWidget(self.fitCurrentTime_radioButton, 0, 1, 1, 1)
        self.example_label = QtGui.QLabel(self.fitOption_frame)
        self.example_label.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.example_label.setFont(font)
        self.example_label.setObjectName("example_label")
        self.gridLayout_3.addWidget(self.example_label, 4, 1, 1, 1)
        self.fitSpecificTime_radioButton = QtGui.QRadioButton(self.fitOption_frame)
        self.fitSpecificTime_radioButton.setObjectName("fitSpecificTime_radioButton")
        self.gridLayout_3.addWidget(self.fitSpecificTime_radioButton, 3, 1, 1, 1)
        self.fitSpecificTimelineEdit = QtGui.QLineEdit(self.fitOption_frame)
        self.fitSpecificTimelineEdit.setEnabled(False)
        self.fitSpecificTimelineEdit.setObjectName("fitSpecificTimelineEdit")
        self.gridLayout_3.addWidget(self.fitSpecificTimelineEdit, 5, 1, 1, 1)
        self.fitAllTime_radioButton = QtGui.QRadioButton(self.fitOption_frame)
        self.fitAllTime_radioButton.setObjectName("fitAllTime_radioButton")
        self.gridLayout_3.addWidget(self.fitAllTime_radioButton, 7, 1, 1, 1)
        self.currentTimePoint_label = QtGui.QLabel(self.fitOption_frame)
        self.currentTimePoint_label.setEnabled(False)
        self.currentTimePoint_label.setText("")
        self.currentTimePoint_label.setObjectName("currentTimePoint_label")
        self.gridLayout_3.addWidget(self.currentTimePoint_label, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.fitOption_frame, 3, 0, 7, 2)
        self.verticalLayout_5.addWidget(self.fitting_groupBox)
        spacerItem10 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem10)
        self.loadSaveWidgets = QtGui.QWidget(self.parameterFitPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadSaveWidgets.sizePolicy().hasHeightForWidth())
        self.loadSaveWidgets.setSizePolicy(sizePolicy)
        self.loadSaveWidgets.setObjectName("loadSaveWidgets")
        self.gridLayout = QtGui.QGridLayout(self.loadSaveWidgets)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.saveSettingsButton = QtGui.QPushButton(self.loadSaveWidgets)
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.gridLayout.addWidget(self.saveSettingsButton, 0, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 0, 1, 1)
        self.loadSettingsButton = QtGui.QPushButton(self.loadSaveWidgets)
        self.loadSettingsButton.setEnabled(True)
        self.loadSettingsButton.setObjectName("loadSettingsButton")
        self.gridLayout.addWidget(self.loadSettingsButton, 0, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.loadSaveWidgets)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem12)
        self.resetButton_widget = QtGui.QWidget(self.parameterFitPage)
        self.resetButton_widget.setObjectName("resetButton_widget")
        self.gridLayout_4 = QtGui.QGridLayout(self.resetButton_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 0, 0, 1, 1)
        self.alignResetButton = QtGui.QPushButton(self.resetButton_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignResetButton.sizePolicy().hasHeightForWidth())
        self.alignResetButton.setSizePolicy(sizePolicy)
        self.alignResetButton.setObjectName("alignResetButton")
        self.gridLayout_4.addWidget(self.alignResetButton, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.resetButton_widget)
        self.optimisationNotes_frame = QtGui.QFrame(self.parameterFitPage)
        self.optimisationNotes_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.optimisationNotes_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.optimisationNotes_frame.setObjectName("optimisationNotes_frame")
        self.formLayout = QtGui.QFormLayout(self.optimisationNotes_frame)
        self.formLayout.setObjectName("formLayout")
        self.optimisationMethodTexts_plainTextEdit = QtGui.QPlainTextEdit(self.optimisationNotes_frame)
        self.optimisationMethodTexts_plainTextEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.optimisationMethodTexts_plainTextEdit.setFont(font)
        self.optimisationMethodTexts_plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.optimisationMethodTexts_plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.optimisationMethodTexts_plainTextEdit.setReadOnly(True)
        self.optimisationMethodTexts_plainTextEdit.setObjectName("optimisationMethodTexts_plainTextEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.optimisationMethodTexts_plainTextEdit)
        self.verticalLayout_5.addWidget(self.optimisationNotes_frame)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.toolBox.addItem(self.parameterFitPage, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewAllButton = QtGui.QPushButton(self.frame)
        self.viewAllButton.setObjectName("viewAllButton")
        self.horizontalLayout_2.addWidget(self.viewAllButton)
        self.doneButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout_2.addWidget(self.doneButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.sceneviewerWidget = NodeEditorSceneviewerWidget(ScaffoldParameterFitter, shareableWidget)
        self.sceneviewerWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy)
        self.sceneviewerWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.sceneviewerWidget.setObjectName("sceneviewerWidget")
        self.horizontalLayout.addWidget(self.sceneviewerWidget)

        self.retranslateUi(ScaffoldParameterFitter)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(ScaffoldParameterFitter)

    def retranslateUi(self, ScaffoldParameterFitter):
        ScaffoldParameterFitter.setWindowTitle(QtGui.QApplication.translate("ScaffoldParameterFitter", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("ScaffoldParameterFitter", "Scaffol Parameter Fitter", None, QtGui.QApplication.UnicodeUTF8))
        self.meshType_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Scaffold type:", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterSet_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Scaffold species:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeSeries_groupBox.setTitle(QtGui.QApplication.translate("ScaffoldParameterFitter", "Time Sequence (active only if time-series data is available)", None, QtGui.QApplication.UnicodeUTF8))
        self.timePoint_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Toggle time for data cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.transformation_groupBox.setTitle(QtGui.QApplication.translate("ScaffoldParameterFitter", "Edit Transformation:", None, QtGui.QApplication.UnicodeUTF8))
        self.rateOfChange_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Rate of change:", None, QtGui.QApplication.UnicodeUTF8))
        self.rotateAxis_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Rotation (Euler angles):", None, QtGui.QApplication.UnicodeUTF8))
        self.position_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Postions:", None, QtGui.QApplication.UnicodeUTF8))
        self.positionY_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.positionZ_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.positionX_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.roll_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Roll", None, QtGui.QApplication.UnicodeUTF8))
        self.yaw_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Yaw", None, QtGui.QApplication.UnicodeUTF8))
        self.pitch_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.fitting_groupBox.setTitle(QtGui.QApplication.translate("ScaffoldParameterFitter", "Estimate New Scaffold Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.NelderMead_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Nelder-Mead", None, QtGui.QApplication.UnicodeUTF8))
        self.optimisationMethod_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Optimisation method*:", None, QtGui.QApplication.UnicodeUTF8))
        self.SLSQ_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "S-LSQ", None, QtGui.QApplication.UnicodeUTF8))
        self.fit_pushButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.ConjugateGradient_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Conjugate Gradient", None, QtGui.QApplication.UnicodeUTF8))
        self.LMBFGS_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "LM-BFGS", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Fitting Progress:", None, QtGui.QApplication.UnicodeUTF8))
        self.fitOptions_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.fitCurrentTime_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Fit current time-point", None, QtGui.QApplication.UnicodeUTF8))
        self.example_label.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "e.g: 2 or 1..5 or 1,2,3", None, QtGui.QApplication.UnicodeUTF8))
        self.fitSpecificTime_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Fit specific time-point(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.fitAllTime_radioButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Fit all time-points", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSettingsButton.setToolTip(QtGui.QApplication.translate("ScaffoldParameterFitter", "Offset the model to the centre of the data points. May need to click View All afterwards.", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSettingsButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSettingsButton.setToolTip(QtGui.QApplication.translate("ScaffoldParameterFitter", "Load pre-saved alignment settings", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSettingsButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Load Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.alignResetButton.setToolTip(QtGui.QApplication.translate("ScaffoldParameterFitter", "Reset the alignment settings", None, QtGui.QApplication.UnicodeUTF8))
        self.alignResetButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.optimisationMethodTexts_plainTextEdit.setPlainText(QtGui.QApplication.translate("ScaffoldParameterFitter", "* Optimisation methods: (Default is LM-BFGS)\n"
"\n"
"> LM-BFGS:\n"
"\n"
"\n"
"> Nelder-Mead:\n"
"\n"
"\n"
"> Conjugate Gradient:\n"
"\n"
"\n"
"> S-LSQ:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.parameterFitPage), QtGui.QApplication.translate("ScaffoldParameterFitter", "Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAllButton.setToolTip(QtGui.QApplication.translate("ScaffoldParameterFitter", "Adjust the view to see the whole model", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAllButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setToolTip(QtGui.QApplication.translate("ScaffoldParameterFitter", "Finish this step", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("ScaffoldParameterFitter", "Done", None, QtGui.QApplication.UnicodeUTF8))

from .nodeeditorsceneviewer import NodeEditorSceneviewerWidget