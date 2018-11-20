# coding: utf-8

# In[31]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


# In[32]:


def duzlem_goster(matris):
    try:
        point1 = np.array([0,0,0])
        normal1 = np.array(matris[0])
        point2 = np.array([0,0,0])
        normal2 = np.array(matris[1])
        point3 = np.array([0,0,0])
        normal3 = np.array(matris[2])
    
        d1 = -np.sum(normal1*point1)
        d2 = -np.sum(normal2*point2)
        d3 = -np.sum(normal3*point3)
    
        # gösterim için meshgrid
        xx, yy = np.meshgrid(range(3),range(3))
        print(d1,d2,d3)
    
        z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
        z2 = (-normal2[0]*xx - normal2[1]*yy - d2)*1./normal2[2]
        z3 = (-normal3[0]*xx - normal3[1]*yy - d3)*1./normal3[2]
        
        print(z1,z2,z3)
    
        plt3d = plt.figure().gca(projection='3d')
        plt3d.plot_surface(xx, yy, z1, color = 'red')
        plt3d.plot_surface(xx, yy, z2, color = 'blue')
        plt3d.plot_surface(xx, yy, z3, color = 'yellow')
        
    except:
        print("hello")
    


# In[33]:


my_matris = np.zeros((3,3))
my_matris[0,0] = 4
my_matris[0,1] = 5
my_matris[0,2] = 6
my_matris[1,0] = 7
my_matris[1,1] = 8
my_matris[1,2] = 9
my_matris[2,0] = 10
my_matris[2,1] = 11
my_matris[2,2] = 12

duzlem_goster(my_matris)

#elemanter islem 1
my_matris[2] = -my_matris[0]*3 + my_matris[2] 

#elemanter işlem 2
my_matris[1] = -my_matris[0]*3 + my_matris[1] 


duzlem_goster(my_matris)