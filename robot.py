import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
   def __init__(self):
      self.motors = {}

   def Prepare_To_Sense(self):
      self.sensors = {}
      for self.linkName in pyrosim.linkNamesToIndices:
         self.sensors[self.linkName] = SENSOR(self.linkName)
   
   def Sense(self, t):
      for sensor in self.sensors:
         self.sensors[sensor].Get_Value(t)
   
   def Prepare_To_Act(self, robot):
      for self.jointName in pyrosim.jointNamesToIndices:
         self.motors[self.jointName] = MOTOR(self.jointName, robot)
   
   def Act(self, t):
      for jointName in self.motors:
         print(jointName)
         self.motors[jointName].Set_Value(t)
   