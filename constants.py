import numpy as np

backLegAmplitude, backLegFrequency, backLegPhaseOffset = np.pi/4, 10, 0
frontLegAmplitude, frontLegFrequency, frontLegPhaseOffset = np.pi/4, 10, np.pi/4
length = 1000
numberOfGenerations = 10
populationSize = 1
numSensorNeurons = 12
numMotorNeurons = 11
motorJointRange = 0.6