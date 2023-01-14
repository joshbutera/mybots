import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class MOTOR:
   def __init__(self, jointName, robotId):
      self.jointName = jointName
      self.robotId = robotId
      self.Prepare_To_Act()

   def Prepare_To_Act(self):
      self.amplitude = np.pi/4
      self.frequency = 10
      if self.jointName == b'Torso_BackLeg':
         self.frequency = 5
      self.offset = 0

      self.motorValues = (np.sin(self.frequency * np.linspace(0, 2*np.pi, c.length) + self.offset)) * self.amplitude

   def Set_Value(self, t):
      pyrosim.Set_Motor_For_Joint(
         bodyIndex = self.robotId,
         jointName = self.jointName,
         controlMode = p.POSITION_CONTROL,
         targetPosition = self.motorValues[t],
         maxForce = 25)