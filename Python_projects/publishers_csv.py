import os
import numpy as np

data = os.listdir('C:/Users/Mikke/OneDrive/Desktop/Projekter/new-adnami-publishers/adnami-publishers/src/publishers')

np.savetxt("publishers.csv", data, delimiter=", ", fmt="% s")



