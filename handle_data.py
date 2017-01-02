
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[2]:

# get_ipython().magic('matplotlib inline')


# ## Data analysis
# 
# Some files look like they have been made up.
# Look at all the files to see if this may be the case

# In[3]:

def plot_temperature_data(filename):
    
    data = np.loadtxt(fname=filename, delimiter=',')
    
    fig = plt.figure(figsize=(10.0, 3.0))
    
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)
    
    axes1.set_ylabel('mean')
    axes1.plot(np.mean(data, axis=0))
    
    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))
    
    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))
    
    fig.tight_layout()
    plt.show()
    


# In[8]:

def check_data(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        print("Suspicious looking maxima!")
    elif np.sum(data.min(axis=0)) == 0:
        print("Minima add up to zero!")
    else:
        print("Looks OK")


if __name__ == "__main__":

    # In[4]:

    import glob


    # In[5]:

    files = glob.glob('data/temperature-*.csv')
    print(files)


    # In[6]:

    print(files[1])


    # In[9]:

    for file in files:
        print("Working on ", file)
        plot_temperature_data(file)
        check_data(file)


    # In[ ]:



