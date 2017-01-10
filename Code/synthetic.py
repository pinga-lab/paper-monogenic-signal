"""
    A Python script to calculate the non-scale and Poisson scale-space
    Monogenic Signal attributes using monogenic.py
    The program is under the conditions terms in the file LICENSE.txt

    Authors: Marlon C. Hidalgo-Gato and Valeria C.F. Barbosa, 2016.

"""

import numpy as np

import matplotlib.pyplot as plt

from monogenic import nss_monogenic_signal, pss_monogenic_signal


def plot_edges(size):
    # First Break - Hingeline
    plt.plot([-50, -25], [-15, -15], color='k', linewidth=size,
             linestyle='--')
    plt.plot([-25, -10], [-5, -5], color='k', linewidth=size,
             linestyle='--')
    plt.plot([-25, -25], [-30, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([-10, -10], [-25, 25], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([-10, 10], [0, 0], color='k', linewidth=size,
             linestyle='--')
    plt.plot([10, 10], [-20, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([10, 30], [-3, -3], color='k', linewidth=size,
             linestyle='--')
    plt.plot([30, 30], [-20, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([30, 50], [-5, -5], color='k', linewidth=size,
             linestyle='--')

    # Continental Oceanic Boundary - COB
    plt.plot([-50, -25], [0, 0], color='w', linewidth=size,
             linestyle='--')
    plt.plot([-25, -10], [3, 3], color='w', linewidth=size,
             linestyle='--')
    plt.plot([-10, 10], [12, 12], color='w', linewidth=size,
             linestyle='--')
    plt.plot([10, 30], [15, 15], color='w', linewidth=size,
             linestyle='--')
    plt.plot([30, 50], [10, 10], color='w', linewidth=size,
             linestyle='--')

    # Intrusion
    plt.plot([0, 10], [30, 30], color='r', linewidth=size,
             linestyle='--')
    plt.plot([0, 0], [30, 40], color='r', linewidth=size,
             linestyle='--')
    plt.plot([0, 10], [40, 40], color='r', linewidth=size,
             linestyle='--')
    plt.plot([10, 10], [30, 40], color='r', linewidth=size,
             linestyle='--')

    # Dike
    plt.plot([-50, -0.95], [-35, -10], color='0.35', linewidth=2.5,
             linestyle='--')


def plot_monogenic(attributes, titles):
    # Plotting the attributes of the Monogenic Signal
    plt.figure(figsize=(20, 5))
    for i, par in enumerate(attributes):
        plt.subplot(1, 3, i + 1)
        plt.title(title[i])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.contourf(yp/1000., xp/1000., par, 50, cmap=plt.cm.RdBu_r)
        cb = plt.colorbar(pad=0.05)
        if i:
            cb.set_label("Radians", labelpad=5, rotation=90)
        else:
            cb.set_label("nT", labelpad=5, rotation=90)
        plt.xlabel('Easting Coordinate (km)')
        plt.ylabel('Northing Coordinate (km)')
        plot_edges(2)
        plt.show()

# Open File "data.dat" and import data
data = np.loadtxt("data.dat")
xp = data[:, 0]
yp = data[:, 1]
zp = data[:, 2]
tf = data[:, 3]

grd_shape = (200, 200)

xp = np.reshape(xp, grd_shape)
yp = np.reshape(yp, grd_shape)
zp = np.reshape(zp, grd_shape)
tf = np.reshape(tf, grd_shape)

# Calculating the Non-scale-space Monogenic Signal Attributes
nss_filters = nss_monogenic_signal(xp, yp, tf, pad_pt=10,
                                   pad_mode="linear_ramp")

# Calculating the Poisson scale-space Monogenic Signal Attributes
pss_filters = pss_monogenic_signal(xp, yp, tf, hc=500, hf=450,
                                   pad_pt=10, pad_mode='mean', )

# Plotting the total-field anomaly
plt.figure(figsize=(10, 10))
plt.title('Total Field Anomaly')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, tf, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
plt.show()

# Plotting the monogenic signal attributes
title = ["a) Non-scale Amplitude", "b) Non-scale Phase",
         "c) Non-scale Orientation"]

plot_monogenic(nss_filters, title)

title = ["a) Poisson Scale-Space Amplitude", "b) Poisson Scale-Space Phase",
         "c) Poisson Scale-Space Orientation"]

plot_monogenic(pss_filters, title)
