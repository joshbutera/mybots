import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1
x, y, z = 0, 0, height/2

sensorNeurons = {
   0: 'Torso',
   1: 'BackLeg',
   2: 'FrontLeg'
}

motorNeurons = {
   3: 'Torso_BackLeg',
   4: 'Torso_FrontLeg'
}

def Create_World():
   pyrosim.Start_SDF("world.sdf")
   pyrosim.Send_Cube(name="Box", pos=[-2,2,z] , size=[length,width,height])
   pyrosim.End()

def Generate_Body():
   pyrosim.Start_URDF("body.urdf")

   pyrosim.Send_Cube(name='Torso', pos=[0,0,1.5] , size=[1,1,1])
   pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
   pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])

   pyrosim.Send_Joint( name = 'Torso_BackLeg' , parent= 'Torso' , child = 'BackLeg' , type = 'revolute', position = [-0.5,0,1])
   pyrosim.Send_Cube(name='BackLeg', pos=[-0.5,0,-0.5] , size=[1,1,1])

   pyrosim.End()

def Generate_Brain():
   pyrosim.Start_NeuralNetwork("brain.nndf")

   pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
   pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
   pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
   pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
   pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

   # for neuron in sensorNeurons:
   #    for motor in motorNeurons:
   #       pyrosim.Send_Synapse( sourceNeuronName = neuron , targetNeuronName = motor , weight = 1.0 )


   pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )

   pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )
   pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )

   pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()