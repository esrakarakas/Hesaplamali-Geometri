# coding: utf-8

# In[ ]:


# define a vectorel function( this is <cost,sint,t>) and 
# define its derivative (türevi tanımla)
# comment them
# draw the derivate for a point in that curve
# t=10


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


# In[27]:


# Plot a helix along the x-axis
get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x = np.sin(theta)
y = np.cos(theta)
ax.plot(x,y,z,'b',lw=2)

theta_current = 3 * np.pi/2
x_1 = math.cos(theta_current)
y_1 = math.sin(theta_current)
z_1 = 1

x_2 = math.sin(theta_current)
y_2 = math.cos(theta_current)
z_2 = theta_current

x_3 = x_1+x_2
y_3 = y_1+y_2
z_3 = z_1+z_2


x_s = [x_3, x_2]
y_s = [y_3, y_2]
z_s = [z_3, z_2]

ax.plot(x_s,y_s,z_s)
plt.show()


# In[51]:


# x = acost, y = bsint z = t olarak tanımlanmış eğrinin, t  = 3pi/2'deki teğet doğrusunu çiziniz
# Plot a helix along the x-axis
get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
a = 7
b = 5
# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
z = theta
x = (np.sin(theta))*a
y = (np.cos(theta))*b
ax.plot(x,y,z,'b',lw=2)

theta_current = 3 * np.pi/2
x_1 = math.cos(theta_current)
y_1 = math.sin(theta_current)
z_1 = 1

x_2 = a*math.sin(theta_current)
y_2 = b*math.cos(theta_current)
z_2 = theta_current

x_3 = x_1+x_2
y_3 = y_1+y_2
z_3 = z_1+z_2


x_s = [x_3, x_2]
y_s = [y_3, y_2]
z_s = [z_3, z_2]

ax.plot(x_s,y_s,z_s)
plt.show()


# In[55]:


# x = 6t y = 3t^2 z = t olan eğrinin t = 10 daki teğetini çizdiriniz.
# Plot a helix along the x-axis
get_ipython().run_line_magic('matplotlib', 'notebook')
n = 1000
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = 6*theta
y = 3*(theta**2)
z = theta
ax.plot(x,y,z,'b',lw=2)

theta_current = 10
x_1 = 6 # math.cos(theta_current)
y_1 = 6*theta_current #math.sin(theta_current)
z_1 = 1

x_2 = 0
y_2 = 6
z_2 = 0

x_3 = x_1+x_2
y_3 = y_1+y_2
z_3 = z_1+z_2


x_s = [x_3, x_2]
y_s = [y_3, y_2]
z_s = [z_3, z_2]

ax.plot(x_s,y_s,z_s)
plt.show()