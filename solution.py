import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

class SOLUTION:
   def __init__(self, myID):
      self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
      self.weights = self.weights * 2 - 1
      self.myID = myID
   
   def Create_World(self):
      pyrosim.Start_SDF("world.sdf")
      pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
      pyrosim.End()

   def Create_Body(self):
      pyrosim.Start_URDF("body.urdf")

      pyrosim.Send_Cube(name='Torso', pos=[0,0,1] , size=[2,0.8,0.6])

      pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-0.8,0.1,1], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.4,0] , size=[0.2,0.3,0.2])
      pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0.2,0.6,0], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,0] , size=[0.5,0.2,0.2])
      pyrosim.Send_Joint( name = "LowerFrontLeg_FrontLegFoot" , parent= "LowerFrontLeg" , child = "FrontLegFoot" , type = "revolute", position = [0.2,0,-0.5], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="FrontLegFoot", pos=[0,0,0] , size=[0.2,0.2,0.75])
      
      pyrosim.Send_Joint( name = 'Torso_BackLeg' , parent= 'Torso' , child = 'BackLeg' , type = 'revolute', position = [-0.8,-0.1,1], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='BackLeg', pos=[0,-0.4,0] , size=[0.2,0.3,0.2])
      pyrosim.Send_Joint( name = 'BackLeg_LowerBackLeg' , parent= 'BackLeg' , child = 'LowerBackLeg' , type = 'revolute', position = [0.2,-0.6,0], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='LowerBackLeg', pos=[0,0,0] , size=[0.5,0.2,0.2])
      pyrosim.Send_Joint( name = 'LowerBackLeg_BackLegFoot' , parent= 'LowerBackLeg' , child = 'BackLegFoot' , type = 'revolute', position = [0.2,0,-0.5], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='BackLegFoot', pos=[0,0,0] , size=[0.2,0.2,0.75])
      
      pyrosim.Send_Joint( name = 'Torso_LeftLeg' , parent= 'Torso' , child = 'LeftLeg' , type = 'revolute', position = [0.8,0.1,1], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='LeftLeg', pos=[0,0.4,0] , size=[0.2,0.3,0.2])
      pyrosim.Send_Joint( name = 'LeftLeg_LowerLeftLeg' , parent= 'LeftLeg' , child = 'LowerLeftLeg' , type = 'revolute', position = [0.2,0.6,0], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='LowerLeftLeg', pos=[0,0,0] , size=[0.5,0.2,0.2])
      pyrosim.Send_Joint( name = 'LowerLeftLeg_LeftLegFoot' , parent= 'LowerLeftLeg' , child = 'LeftLegFoot' , type = 'revolute', position = [0.2,0,-0.5], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='LeftLegFoot', pos=[0,0,0] , size=[0.2,0.2,0.75])
      
      pyrosim.Send_Joint( name = 'Torso_RightLeg' , parent= 'Torso' , child = 'RightLeg' , type = 'revolute', position = [0.8,-0.1,1], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='RightLeg', pos=[0,-0.4,0] , size=[0.2,0.3,0.2])
      pyrosim.Send_Joint( name = 'RightLeg_LowerRightLeg' , parent= 'RightLeg' , child = 'LowerRightLeg' , type = 'revolute', position = [0.2,-0.6,0], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='LowerRightLeg', pos=[0,0,0] , size=[0.5,0.2,0.2])
      pyrosim.Send_Joint( name = 'LowerRightLeg_RightLegFoot' , parent= 'LowerRightLeg' , child = 'RightLegFoot' , type = 'revolute', position = [0.2,0,-0.5], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name='RightLegFoot', pos=[0,0,0] , size=[0.2,0.2,0.75])

      pyrosim.End()

   def Create_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
      pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
      pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
      pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LowerBackLeg")
      pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LowerFrontLeg")
      pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerLeftLeg")
      pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerRightLeg")
      pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "FrontLegFoot")
      pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "BackLegFoot")
      pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "LeftLegFoot")
      pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "RightLegFoot")

      pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackLeg")
      pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_FrontLeg")
      pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_LeftLeg")
      pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Torso_RightLeg")
      pyrosim.Send_Motor_Neuron( name = 17 , jointName = "BackLeg_LowerBackLeg")
      pyrosim.Send_Motor_Neuron( name = 18 , jointName = "FrontLeg_LowerFrontLeg")
      pyrosim.Send_Motor_Neuron( name = 19 , jointName = "LeftLeg_LowerLeftLeg")
      pyrosim.Send_Motor_Neuron( name = 20 , jointName = "RightLeg_LowerRightLeg")
      pyrosim.Send_Motor_Neuron( name = 21 , jointName = "LowerFrontLeg_FrontLegFoot")
      pyrosim.Send_Motor_Neuron( name = 22 , jointName = "LowerBackLeg_BackLegFoot")
      pyrosim.Send_Motor_Neuron( name = 23 , jointName = "LowerLeftLeg_LeftLegFoot")
      pyrosim.Send_Motor_Neuron( name = 24 , jointName = "LowerRightLeg_RightLegFoot")

      for currentRow in range(self.weights.shape[0]):
         for currentCol in range(self.weights.shape[1]):
            pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentCol+c.numSensorNeurons , weight = self.weights[currentRow][currentCol] )

      pyrosim.End()

   def Create_Object(self):
      pyrosim.Start_URDF("object.urdf")
      pyrosim.Send_Cube(name="Box", pos=[-2,0,0.5] , size=[1,1,1])
      pyrosim.End()

   def Start_Simulation(self, directOrGUI):
      self.Create_World()
      self.Create_Body()
      self.Create_Brain()
      self.Create_Object()
      os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

   def Wait_For_Simulation_To_End(self):
      while not os.path.exists("fitness" + str(self.myID) + ".txt"):
         time.sleep(0.01)
      f = open("fitness" + str(self.myID) + ".txt", "r")
      self.fitness = float(f.read())
      os.system("rm fitness" + str(self.myID) + ".txt")

   def Mutate(self):
      randomRow = random.randint(0,c.numSensorNeurons - 1)
      randomCol = random.randint(0,c.numMotorNeurons - 1)
      self.weights[randomRow][randomCol] = random.random() * 2 - 1

   def Set_ID(self, id):
      self.myID = id
