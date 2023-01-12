import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
backLegTargetAngles = numpy.load('data/backLegtargetAngles.npy')
frontLegTargetAngles = numpy.load('data/frontLegtargetAngles.npy')

matplotlib.pyplot.plot(backLegTargetAngles, label='Back Leg', linewidth=3)
matplotlib.pyplot.plot(frontLegTargetAngles, label='Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
