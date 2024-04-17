# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:10:14 2023

@author: yuzt
"""

import matplotlib.pyplot as plt
squares=[1,4,9,23]
plt.plot(squares, linewidth=2)
plt.axis([0,10,0,100])
plt.tick_params(axis='both',labelsize=12,color='red',labelcolor='green')
plt.show()