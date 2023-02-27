import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
id = sys.argv[2]

simulation = SIMULATION(directOrGUI, id)
simulation.RUN()
simulation.Get_Fitness()
