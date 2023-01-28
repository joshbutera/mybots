from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import constants as c

class SIMULATION:
   def __init__(self, directOrGUI, solutionID):
      self.world = WORLD()
      self.robot = ROBOT(solutionID)
      self.directOrGUI = directOrGUI

      if directOrGUI == "DIRECT":
         self.physicsClient = p.connect(p.DIRECT)
      else:
         self.physicsClient = p.connect(p.GUI)

      p.setAdditionalSearchPath(pybullet_data.getDataPath())
      p.setGravity(0,0,-9.8)

      self.planeId = p.loadURDF("plane.urdf")
      self.robotId = p.loadURDF("body.urdf")
      p.loadSDF("world.sdf")

      pyrosim.Prepare_To_Simulate(self.robotId)
      self.robot.Prepare_To_Sense()
      self.robot.Prepare_To_Act(self.robotId)
   
   def RUN(self):
      # np.save('data/backLegTargetAngles.npy', backLegSensorValues)
      # np.save('data/frontLegTargetAngles.npy', backLegSensorValues)

      for i in range(c.length):
         p.stepSimulation()
         self.robot.Sense(i)
         self.robot.Think()
         self.robot.Act()

         if self.directOrGUI == "GUI":
            time.sleep(1/240)
         
      # np.save('data/backLegSensorValues.npy', backLegSensorValues)
      # np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

   def Get_Fitness(self):
      self.robot.Get_Fitness(self.robotId)
   
   def __del__(self):
      p.disconnect()