import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class MOTOR:
   def __init__(self, jointName, robotId):
      self.jointName = jointName
      self.robotId = robotId

   def Set_Value(self, desiredAngle):
      pyrosim.Set_Motor_For_Joint(
         bodyIndex = self.robotId,
         jointName = self.jointName,
         controlMode = p.POSITION_CONTROL,
         targetPosition = desiredAngle,
         maxForce = 25)