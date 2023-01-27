import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
   def __init__(self):
      self.motors = {}
      self.nn = NEURAL_NETWORK("brain.nndf")

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
   
   def Act(self):
      for neuronName in self.nn.Get_Neuron_Names():
         if self.nn.Is_Motor_Neuron(neuronName):
            jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('ASCII')
            desiredAngle = self.nn.Get_Value_Of(neuronName)
            self.motors[jointName].Set_Value(desiredAngle)

      # for jointName in self.motors:
      #    self.motors[jointName].Set_Value(t)
   def Get_Fitness(self, robotId):
      stateOfLinkZero = p.getLinkState(robotId,0)
      positionOfLinkZero = stateOfLinkZero[0]
      xCoordinateOfLinkZero = positionOfLinkZero[0]
      f = open("fitness.txt", "w")
      f.write(str(xCoordinateOfLinkZero))
      f.close()

   def Think(self):
      self.nn.Update()
      # self.nn.Print()
   