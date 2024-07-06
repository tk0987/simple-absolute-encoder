import magpylib as mg
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import matplotlib
matplotlib.use('TkAgg')


x_sensor=0.01# in m, for test
y_sensor=0.0 # in m for testing

fields=[]
angles=[]

sensor = mg.Sensor(position=(x_sensor,y_sensor,0.00125))

for angle in range(360):
    cube_magnet = mg.magnet.Cuboid(magnetization=(1e6, 0, 0), dimension=(0.005, 0.005, 0.005),orientation=R.from_euler("xyz",(0,0,angle/180*np.pi))) # x axis magnetization, all dims in [mm]

    B=sensor.getB(cube_magnet)
    fields.append(B)
    angles.append(angle)

fields=np.asanyarray(fields)
print(np.shape(fields))
angles=np.asanyarray(angles)
plt.plot(angles,fields[:,0])
plt.show()
