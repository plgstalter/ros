from session import Session
from gpx import Gpx
import matplotlib.pyplot as plt
import numpy as np

def show(save=False):
    positions = open('positions.csv', 'r')
    plt.figure();
    for point in positions:
        plt.scatter(point, c='blue');
    if save:
        plt.savefig('positions.png')
    plt.show();
    positions.close()