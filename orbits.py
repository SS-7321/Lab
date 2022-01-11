# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:45:33 2021

@author: Shan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rotate(point, angle):
    ox, oy = 0 , 0
    px, py = point
    angle = angle *(np.pi/180)
    qx = ox + np.cos(angle) * (px - ox) - np.sin(angle) * (py - oy)
    qy = oy + np.sin(angle) * (px - ox) + np.cos(angle) * (py - oy)
    return qx, qy

FOURPI = 2*1.881*np.pi

fig, ax = plt.subplots()
ax = plt.axis([-230,280,-250,250])
fig.gca().set_aspect("equal")
t = np.arange(0.0, FOURPI, 0.001)
angle = 0
def coeff(r,e):
    a = r/(1-e)
    c = a*e
    b = a*np.sqrt(1-(e**2))
    d = 0
    return a,b,c,d

ra,rb,rc,rd = coeff(206.655215,0.093)
ba,bb,bc,bd = coeff(147.098291,0.017)
goldZoneUp, goldZoneLo = 0.95*149.598, 1.47*149.598
avgGZR = np.mean([goldZoneLo,goldZoneUp])

plt.plot(avgGZR*np.cos(t/1.881),avgGZR*np.sin(t/1.881), 'c', lw = 40)
# plt.plot(goldZoneUp*np.cos(t/2),goldZoneUp*np.sin(t/2), 'm')
# plt.plot(goldZoneLo*np.cos(t/2),goldZoneLo*np.sin(t/2), 'm')
plt.plot(rotate([ra*np.cos(t/1.881),rb*np.sin(t/1.881)],angle)[0]+rc, rotate([ra*np.cos(t/1.881),rb*np.sin(t/1.881)],angle)[1]+rd, 'k--') # mars orbit
plt.plot(rotate([ba*np.cos(t/1.881),bb*np.sin(t/1*881)],angle)[0]+bc, rotate([ba*np.cos(t/1.881),bb*np.sin(t/1.881)],angle)[1]+bd, 'k--') #earth orbit
plt.plot(0,0,'yo', markersize=20)

redDot, = plt.plot([ra*np.cos(0)+rc], [rb*np.sin(0)+rd], 'ro', markersize=5, label = "Mars")
blueDot, = plt.plot([ba*np.cos(0)+bc], [bb*np.sin(0)+bd], 'bo', markersize=5, label = "Earth")

def animate(i):
    redDot.set_data(rotate([ra*np.cos(i/1.881),rb*np.sin(i/1.881)],angle)[0]+rc, rotate([ra*np.cos(i/1.881),rb*np.sin(i/1.881)],angle)[1]+rd)
    blueDot.set_data(rotate([ba*np.cos(i),bb*np.sin(i)],angle)[0]+bc, rotate([ba*np.cos(i),bb*np.sin(i)],angle)[1]+bd)
    return blueDot, redDot,
plt.legend(loc=1)
orbitsAnim = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, FOURPI, 0.1), interval=10, blit=True, repeat=True)

#Savewriters: only uncomment ONE of the three sets of code

#1: using FFMpeg
# FFMpegWriter = animation.writers['ffmpeg']()
# writer = animation.FFMpegWriter(fps=10)
# orbitsAnim.save('orbitsEM.mp4', writer = FFMpegWriter, dpi=(200))

#2: using Pil
writergif = animation.PillowWriter(fps=60) 
orbitsAnim.save('orbitEM.gif', writer=writergif, dpi=(200))

#3: using base
#myAnimation.save('orbitEM.mp4', fps=120)#, extra_args=['-vcodec', 'libx264'])