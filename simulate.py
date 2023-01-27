import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.RUN()
simulation.Get_Fitness()