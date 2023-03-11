import numpy as np

backLegAmplitude, backLegFrequency, backLegPhaseOffset = np.pi/4, 10, 0
frontLegAmplitude, frontLegFrequency, frontLegPhaseOffset = np.pi/4, 10, np.pi/4
length = 1000
numberOfGenerations = 50
populationSize = 10
numSensorNeurons = 12
numMotorNeurons = 11
motorJointRange = 0.8