import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import pylab as pl

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

def FaradayFunction(Freq,Amp,Ns,Np):
    eff = 0.000822 # efficiency of 1 ferrite core as a decimal
    Rp = 18 # resistance of the circuit in the primary coil
    Rs = 27 # resistance of the circuit in the secondary coil
    Vp = Amp*np.sin(2*np.pi*Freq*t)
    Vs = (Vp*Ns)/Np
    Ip = Vp/Rp
    Is = (eff*Vp*Ip)/Vs
    return [Ip, Is]

def update():
    Freq = float(tbox_Freq.text())
    Amp = float(tbox_Amp.text())
    Np = float(tbox_Np.text())
    Ns = float(tbox_Ns.text())
    Ip = FaradayFunction(Freq,Amp,Ns,Np)[0]
    Is = FaradayFunction(Freq,Amp,Ns,Np)[1]
    primary_ax.set_data(t, Ip)
    secondary_ax.set_data(t, Is)
    ax.set_ylim([1.2*Ip.max(),1.2*Ip.min()])
    fig.canvas.draw_idle()


fig, ax = pl.subplots()
t = np.linspace(0, 10, 200)
primary_ax, = ax.plot(t, 0*t, label='Primary coil', color = 'red')
secondary_ax, = ax.plot(t, 0*t, label='Secondary coil', color = 'blue')


root = fig.canvas.manager.window
#Frequency input
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
