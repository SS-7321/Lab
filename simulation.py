import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import pylab as pl

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

def FaradayFunction(Freq,Amp,Ns,Np):
    Vp = Amp/np.sqrt(2)
    Vs = (Vp*Ns)/Ns
    return 

def update():
    Freq = float(tbox_Freq.text())
    Amp = float(tbox_Amp.text())
    Np = float(tbox_Np.text())
    Ns = float(tbox_Ns.text())
    y = np.sin(2*np.pi*Freq*x)*Amp
    line.set_data(x, y)
    fig.canvas.draw_idle()


fig, ax = pl.subplots()
x = np.linspace(0, 10, 200)
line, = ax.plot(x, 0*x)
#ax.set_xlim([])


#Frequency input
root = fig.canvas.manager.window
panel_Freq = QtWidgets.QWidget()
hbox_Freq = QtWidgets.QHBoxLayout(panel_Freq)
tbox_Freq = QtWidgets.QLineEdit(parent = panel_Freq)
tbox_Freq.textChanged.connect(update)
hbox_Freq.addWidget(tbox_Freq)
panel_Freq.setLayout(hbox_Freq)

dock_Freq = QtWidgets.QDockWidget("Frequency", root)
root.addDockWidget(Qt.BottomDockWidgetArea, dock_Freq)
dock_Freq.setWidget(panel_Freq)


#Amplitude input
panel_Amp = QtWidgets.QWidget()
hbox_Amp = QtWidgets.QHBoxLayout(panel_Amp)
tbox_Amp = QtWidgets.QLineEdit(parent = panel_Amp)
tbox_Amp.textChanged.connect(update)
hbox_Amp.addWidget(tbox_Amp)
panel_Amp.setLayout(hbox_Amp)

dock_Amp = QtWidgets.QDockWidget("Amplitude", root)
root.addDockWidget(Qt.BottomDockWidgetArea, dock_Amp)
dock_Amp.setWidget(panel_Amp)


#N_Primary coil input
panel_Np = QtWidgets.QWidget()
hbox_Np = QtWidgets.QHBoxLayout(panel_Np)
tbox_Np = QtWidgets.QLineEdit(parent = panel_Np)
tbox_Np.textChanged.connect(update)
hbox_Np.addWidget(tbox_Np)
panel_Np.setLayout(hbox_Np)

dock_Np = QtWidgets.QDockWidget("Np", root)
root.addDockWidget(Qt.BottomDockWidgetArea, dock_Np)
dock_Np.setWidget(panel_Np)


#N_Secondary coil input
panel_Ns = QtWidgets.QWidget()
hbox_Ns = QtWidgets.QHBoxLayout(panel_Ns)
tbox_Ns = QtWidgets.QLineEdit(parent = panel_Ns)
tbox_Ns.textChanged.connect(update)
hbox_Ns.addWidget(tbox_Ns)
panel_Ns.setLayout(hbox_Ns)

dock_Ns = QtWidgets.QDockWidget("Ns", root)
root.addDockWidget(Qt.BottomDockWidgetArea, dock_Ns)
dock_Ns.setWidget(panel_Ns)


pl.show()