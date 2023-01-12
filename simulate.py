import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import math
import random

length = 1000
pi = np.pi
backLegAmplitude, backLegFrequency, backLegPhaseOffset = pi/4, 10, 0
frontLegAmplitude, frontLegFrequency, frontLegPhaseOffset = pi/4, 10, pi/4

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(length)
frontLegSensorValues = np.zeros(length)

backLegTargetAngles = (np.sin(backLegFrequency * np.linspace(0, 2*np.pi, length) + backLegPhaseOffset)) * backLegAmplitude
frontLegTargetAngles = (np.sin(frontLegFrequency * np.linspace(0, 2*np.pi, length) + frontLegPhaseOffset)) * frontLegAmplitude

np.save('data/backLegTargetAngles.npy', backLegSensorValues)
np.save('data/frontLegTargetAngles.npy', backLegSensorValues)

for i in range(length):
   p.stepSimulation()
   backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

   pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = b'Torso_BackLeg',
      controlMode = p.POSITION_CONTROL,
      targetPosition = backLegTargetAngles[i],
      maxForce = 25)
   
   pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = b'Torso_FrontLeg',
      controlMode = p.POSITION_CONTROL,
      targetPosition = frontLegTargetAngles[i],
      maxForce = 25)

   time.sleep(1/60)
   
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

p.disconnect()