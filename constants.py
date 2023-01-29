import numpy as np

backLegAmplitude, backLegFrequency, backLegPhaseOffset = np.pi/4, 10, 0
frontLegAmplitude, frontLegFrequency, frontLegPhaseOffset = np.pi/4, 10, np.pi/4
length = 1000
numberOfGenerations = 10
populationSize = 10
numSensorNeurons = 9
numMotorNeurons = 8
motorJointRange = 0.4