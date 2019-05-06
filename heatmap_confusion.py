"""
Created on Sat Sep 22 12:19:09 2018

@author: abhi
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

###########################################

nn_pav=[[     10  ,  1 ,   0  ,  0, 4540,   91  ,  0 ,   0 ,   0],
 [     211, 2455 ,   0 , 274, 1204 ,8911  ,  0   , 0  ,  0],
 [      1  ,  0  ,  0 ,   0, 1466  ,  3  ,  0  ,  0 ,   0],
 [       0 , 239,    0 ,1693  , 92 , 121,    0 ,   0   , 0],
 [       0  ,  0    ,0  ,  0 , 942 ,   0  ,  0 ,   0  ,  0],
 [       0 ,  24  ,  0 ,   8 ,1056, 2433 ,   0  ,  0  ,  0],
 [       0  ,  0  ,  0  ,  0 , 923  ,  8 ,   0 ,   0  ,  0],
 [       0  ,  0  ,  0 ,   0, 2559 ,  19 ,   0  ,  0 ,   0],
 [       0   , 1    ,0  ,  0 ,   0  ,  0  ,  0    ,0 , 662]]

df = pd.DataFrame(nn_pav)

df.columns = ['Water',	
	'Trees',	
	'Asphalt',	
	'Self-Blocking Bricks',	
	'Bitumen',	
	'Tiles',	
	'Shadows',	
	'Meadows',	
	'Bare Soil']

df.index = ['Water',	
	'Trees',	
	'Asphalt',	
	'Self-Blocking Bricks',	
	'Bitumen',	
	'Tiles',	
	'Shadows',	
	'Meadows',	
	'Bare Soil']

ax = sns.heatmap(df,cmap="Spectral" )
ax.set_yticklabels(ax.get_yticklabels(), rotation =0)
ax.set_xticklabels(ax.get_yticklabels(), rotation =60)
plt.title('CNN on Pavia University Data')
plt.show()


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

matrix_pines = [[10 , 0 , 0 , 0 , 0 , 0 , 0  , 0  , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
	[0 , 227 ,  9 ,  0  , 1 ,  0 ,  0  , 0 ,  0 , 10 , 38 ,  1  , 0 ,  0 ,  0  , 0 ],
	[0 ,  8 , 134 , 5 ,  0  , 0  , 0 ,  0 , 0 , 0 , 13 ,  6 ,  0  , 0 ,  0 ,  0 ],
	[0 ,  5 ,  7 , 31 ,  2 ,  2 ,  0 ,  0 ,  0 ,  0 ,  1 ,  0 ,  0  , 0 ,  0 , 0 ],
	[0 ,  0 ,  0 ,  2 , 94 ,  0 ,  0 , 0  , 0 ,  0 ,  0 ,  0 ,  0 ,  1 ,  0 ,  0 ],
	[0 ,  0 ,  0 ,  0 , 3 , 141 ,  0 ,  0 ,  0 ,  1 ,  0 ,  0 ,  0 ,  0 ,  1  , 0 ],
	[0 ,  0 ,  0 , 0 , 0  , 0 ,  5 ,  1 ,  0 ,  0 ,  0  , 0 ,  0 ,  0 ,  0 ,  0 ],
	[1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 95 , 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  	0 ],
	[0 ,  0 ,  0 ,  0 ,  0 , 0 ,  0 ,  0 ,  4 ,  0  , 0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
	[0 , 14  , 1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 138 , 41 ,  1 ,  0  , 0 ,  0  , 0 ],
	[0 , 28 , 27 , 1 ,  2 ,  2 ,  1 , 0 ,  0 , 25 , 394 , 11 ,  0 , 0 ,  0 ,  0 ],
	[0 ,  1  , 6 , 1 ,  2 ,  0 ,  0 , 0 , 0 ,  0 ,  8 , 101 , 0 ,  0 ,  0 ,  0 ],
	[0 ,  0 ,  0 , 0 ,  0  , 0 ,  0 , 0 ,  1  , 0 ,  0 , 0 , 40 , 0 ,  0 ,  0 ],
	[0 ,  0 ,  0 , 0 , 1 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 236 , 12 , 0 ],
	[0 , 0 ,  0 , 0 , 3 ,  4 ,  0 ,  0 ,  2 ,  0 ,  1 ,  0 ,  1 , 11 , 56 , 0 ],
	[0 , 0 ,  0 , 0 , 0 , 0 ,  0 ,  0  , 0  , 0 ,  1 ,  0 , 0 ,  0 ,  0 , 18 ]]

knn_pines = [[  5 ,  0  , 0 ,  0  , 0 ,  0  , 0 ,  4  , 0 ,  0  , 1 ,  0 ,  0  , 0  , 0  , 0],
   [0 , 207 ,  8 ,  1  , 0 ,  0  , 0  , 0 ,  0 , 10 , 51 ,  9 ,  0  , 0 ,  0 ,  0],
   [0 , 18 , 97 ,  2 ,  0  , 0  , 0 ,  0 ,  0 ,  5 , 33 , 11  , 0 ,  0 ,  0 ,  0],
   [0 , 20 ,  3 , 16  , 0 ,  0 ,  0  , 0 ,  0  , 0 ,  8  , 1  , 0  , 0 ,  0  , 0],
   [0  , 1 ,  0 ,  1 , 85  , 4  , 1 ,  0 ,  0  , 1 ,  1 ,  1 ,  0 , 2 ,  0 ,  0],
   [0 ,  0 ,  0 ,  0 ,  0 , 143  , 0  , 0 ,  0  , 0 ,  0 ,  0 ,  0 ,  1  , 2  , 0],
   [1 ,  0  , 0  , 0  , 0 ,  0  , 5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0  , 0  , 0  , 0],
   [0  , 0  , 0 ,  0  , 0  , 0 ,  0 , 96 ,  0 ,  0 ,  0  , 0  , 0  , 0  , 0 ,  0],
   [0  , 0  , 0  , 0  , 0 ,  1 ,  0  , 0 ,  2 ,  0 ,  0 ,  0  , 1 ,  0 ,  0 ,  0],
   [0  , 8 ,  6  , 0  , 2  , 0 ,  1 ,  0  , 0 , 149 , 26  , 3  , 0 ,  0 ,  0 ,  0],
   [0 , 33 , 23  , 4 ,  0  , 1 ,  2  , 1  , 0 , 31 , 393 ,  3  , 0  , 0 ,  0 ,  0],
   [0 , 20 ,  7  , 0  , 0 ,  0 ,  0 ,  0  , 0  , 8 , 19 , 65  , 0 ,  0  , 0  , 0],
   [0 ,  0 ,  0  , 0  , 0  , 2 ,  0  , 0  , 0  , 0  , 1  , 0 , 38 ,  0 ,  0  , 0],
   [0 ,  0  , 0 ,  0  , 5 ,  0  , 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  2 , 241 , 5 , 0],
  [ 0 ,  0 ,  0 ,  0  , 6 , 19 ,  0  , 0 ,  1  , 2 ,  0  , 0 ,  5 , 17 , 28  , 0],
   [0 ,  0  , 0  , 0  , 0 ,  0  , 0  , 0 ,  0  , 0  , 1 ,  0  , 0 ,  0 ,  0 , 18]]

forest_pines =  [[ 0 ,  0  , 0  , 0  , 0 ,  9  , 0  , 0  , 0 ,  0 ,  1  , 0 ,  0  , 0  , 0  , 0],
   [0 , 102 ,  0  , 0  , 0 ,  4  , 0  , 0 ,  0 ,  0 , 180 ,  0 ,  0  , 0  , 0  , 0],
  [ 0 , 19 ,  0 ,  0  , 0 ,  0 ,  0  , 0  , 0 ,  0 , 147 ,  0 ,  0 ,  0 ,  0  , 0],
   [0 , 20 ,  0  , 0  , 0  , 6  , 0 ,  0 ,  0  , 0 , 22 ,  0  , 0  , 0 ,  0  , 0],
   [0 ,  1  , 0  , 0 ,  0 , 29  , 0 ,  0  , 0  , 0 ,  2 ,  0  , 0  , 65 ,  0  , 0],
   [0 ,  0 ,  0 ,  0  , 0 , 145 ,  0 ,  0 ,  0  , 0  , 1  , 0  , 0  , 0 ,  0  , 0],
   [0 ,  0  , 0  , 0  , 0 ,  6  , 0 ,  0  , 0 ,  0  , 0 ,  0  , 0  , 0 ,  0 ,  0],
   [0 ,  1  , 0  , 0  , 0 , 94 ,  0 ,  0  , 0  , 0  , 1  , 0 ,  0  , 0  , 0  , 0],
   [0  , 0 ,  0  , 0  , 0  , 4  , 0  , 0 ,  0  , 0 ,  0  , 0  , 0  , 0  , 0  , 0],
   [0 ,  0 ,  0 ,  0 ,  0 ,  7 , 0  , 0 ,  0 ,  0 , 188  , 0 ,  0 ,  0  , 0  , 0],
  [ 0 , 12  , 0 ,  0 ,  0 ,  8 ,  0 ,  0  , 0 ,  0 , 471  , 0 ,  0  , 0 ,  0 ,  0],
  [0  , 18 ,  0  , 0  , 0 ,  5 ,  0  , 0  , 0  , 0 , 96 ,  0 ,  0 ,  0  , 0  , 0],
  [0  , 0 ,  0  , 0  , 0 , 41 ,  0 ,  0 ,  0 ,  0  , 0 ,  0 ,  0  , 0 ,  0 ,  0],
   [0 ,  0  , 0  , 0  , 0 ,  8  , 0  , 0  , 0 ,  0 ,  0 ,  0 ,  0 , 245 ,  0 ,  0],
   [0  , 0 ,  0 ,  0 ,  0 , 54 ,  0  , 0  , 0  , 0  , 0 ,  0  , 0 , 24 ,  0 ,  0],
   [0  , 1 ,  0 ,  0  , 0  , 7  , 0 ,  0 ,  0 ,  0 , 11 ,  0  , 0  , 0  , 0 ,  0]]

nn_pines =[[   0 ,  0  , 0  , 0 ,  0 , 33 ,  0  , 0 ,  0  , 0 ,  0  , 0 ,  0 ,  0 ,  0  , 0],
 [   0 , 84 ,  4  , 0  , 0, 273,   0 ,  0  , 0 ,253  , 1  , 0 ,385  , 0 ,  0 ,  0],
 [   0  , 0 , 27 ,  0 ,  0, 174 ,  0 ,  0 ,  0 , 21 ,  0 ,  0, 359 ,  0  , 0,   0],
 [    0 ,  1 ,  2 ,  0 ,  0 , 94 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 69 ,  0 ,  0  , 0],
 [   0  , 0  , 0  , 0 ,  0 , 60 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 , 53 ,226 ,  0 ,  0],
 [    0 ,  0 ,  0  , 0  , 0 ,159 ,  0 ,  0  , 0  , 0  , 0 ,  0, 329  ,23  , 0   ,0],
 [   0  , 0 ,  0   ,0  , 0 , 13,   0  , 0  , 0   ,0 ,  0 ,  0 ,  7 ,  0 ,  0 ,  0],
 [   0 ,  0 ,  0  , 0  , 0 ,262  , 0  , 0  , 0   ,0  , 0  , 0,  73,   0  , 0   ,0],
 [   0 ,  0 ,  0  , 0  , 0 ,  1  , 0 ,  0 ,  0 ,  0  , 0  , 0 , 13 ,  0  , 0 ,  0],
 [   0  , 0  , 0  , 0  , 0 , 54  , 0  , 0 ,  0 ,152 ,  0  , 0 ,475 ,  0  , 0 ,  0],
 [    0 , 12 ,  7  , 0 ,  0 ,460 ,  0  , 0 ,  0 ,453   ,1 ,  0, 786 ,  0 ,  0  , 0],
 [   0 ,  0,   8 ,  0  , 0 ,122 ,  0  , 0  , 0 , 48 ,  1  , 0 ,237 ,  0 ,  0  , 0],
 [   0   ,0 ,  0 ,  0  , 0  , 0   ,0  , 0,   0 ,  0 ,  0  , 0, 144 , 0  , 0  , 0],
 [   0 ,  0 ,  0 ,  0  , 0  , 6  , 0  , 0 ,  0  , 0   ,0  , 0, 191 ,689 ,  0,  0],
 [   0  , 0  , 0 ,  0 ,  0 , 23  , 0  , 0  , 0 ,  0 ,  0  , 0 ,193,  55 ,  0 ,  0],
 [    0  , 1 ,  2  , 0   ,0   ,4  , 0 ,  0  , 0 ,  4 ,  0  , 0 , 55 ,  0 ,  0 ,  0]]

df = pd.DataFrame(nn_pines)

df.columns = ['Alfalfa',	
'Corn-notill',
'Corn-mintill',
'Corn'	,
'Grass-pasture',	
'Grass-trees'	,
'Grass-pasture-mowed',	
'Hay-windrowed'	,
'Oats'	,
'Soybean-notill'	,
'Soybean-mintill',	
'Soybean-clean',	
'Wheat'	,
'Woods'	,
'Buildings-Grass-Trees-Drives',	
'Stone-Steel-Towers']

df.index = ['Alfalfa',	
'Corn-notill',
'Corn-mintill',
'Corn'	,
'Grass-pasture',	
'Grass-trees'	,
'Grass-pasture-mowed',	
'Hay-windrowed'	,
'Oats'	,
'Soybean-notill'	,
'Soybean-mintill',	
'Soybean-clean',	
'Wheat'	,
'Woods'	,
'Buildings-Grass-Trees-Drives',	
'Stone-Steel-Towers']


#ax = sns.heatmap(df,cmap="YlGnBu" , annot=True, fmt="d")
ax = sns.heatmap(df ,cmap="Spectral")
ax.set_yticklabels(ax.get_yticklabels(), rotation =0)
ax.set_xticklabels(ax.get_yticklabels(), rotation =90)
plt.title('CNN on Indian Pines Data')
plt.show()

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

svm_salinas = [[402  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0  ,  0   , 0 , 0   , 0], 
    [0  , 747  ,  0 ,   0  ,  0  ,  0  ,  0 , 0  ,  0 , 0 ,   0  ,  0 ,   0  ,  0 , 0  ,  0],
    [0  ,  0 , 395  ,  0  ,  0 ,   0  ,  0 ,   0  ,  0  ,  0   , 0  ,  0  ,  0   , 0 , 0  ,  0],
    [0  ,  0 ,   0 , 280 , 0  ,  0 , 0  ,  0  ,  0 ,   0 ,   0  ,  0 ,   0 ,   0,
     0 ,   0],
    [0  ,  0   , 0   , 1 , 534  ,  0  ,  0  ,  0  ,  0   , 0  ,  0  ,  0  ,  0   , 0 , 0  ,  0],
    [0  ,  0  ,  0  ,  0   , 0 , 792 , 0 , 0 ,   0  ,  0 ,   0 ,   0 ,   0 ,   0,
     0 ,   0],
    [0 ,   0  ,  0  ,  0  ,  0  ,  0 , 717  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 0 ,   0],
    [0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 , 2255 , 0 ,   0 ,   0 ,   0 ,   0   , 0 , 0 ,   0],
    [0  ,  0  ,  0  ,  0 ,   0 ,   0  ,  0  ,  0 , 1240 ,   0 ,   0 ,   0  ,  0   , 0 , 0 ,   0],
   [ 0  ,  0  ,  0 ,   0 ,   0   , 0   , 0 ,   0  ,  0 , 655  ,  0  ,  0  ,  0   , 1 , 0 ,   0],
    [0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  0 ,   0  ,  0  ,  0 , 213 ,   1  ,  0   , 0 , 0  ,  0],
   [ 0  ,  0   , 0  ,  0  ,  0 ,   0  ,  0  ,  0   , 0   , 0  ,  0 , 386 ,   0   , 0 , 0  ,  0],
   [ 0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0  ,  0 , 184 ,   0 , 0  ,  0],
   [ 0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  1  ,  0  ,  0  ,  0 , 213 , 0   , 0],
   [ 0   , 0  ,  0 ,   0 ,   0  ,  0  ,  0  ,  0  ,  0 ,   0   , 0  ,  0  ,  0   , 0 , 1454  ,  0],
   [ 0  ,  0  ,  0 ,   0  ,  0  ,  0  ,  0 ,   0 ,   0 ,   0  ,  0  ,  0 ,   0   , 0 , 0 , 362]]
    
rf_salinas=[[    0 ,  19  ,  0  ,  0  ,  0  ,  0  ,  0 , 383 ,   0  ,  0 ,   0  ,  0  ,  0   , 0 , 0 ,   0],
    [0 , 263 ,   0  ,  0   , 0 ,   0 ,   0 , 483  ,  0  ,  0  ,  0   , 0  ,  0   , 0 , 0  ,  0],
   [ 0  ,  0  ,  0  ,  0 , 0  ,  0  ,  0 , 396  ,  0 ,   0  ,  0  ,  0  ,  0 ,   0 , 0  ,  0],
   [ 0  ,  0  ,  0 ,   0  ,  0 ,   0 ,   0  , 162 ,   0  ,  0 ,   0 ,   0 ,   0   , 0 , 117 ,    0],
   [ 0 ,   0  ,  0  ,  0  ,  0  ,  2  ,  0 , 392  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 142  ,  0],
   [ 0  ,  0  ,  0  ,  0  ,  0 , 772  ,  0  , 19  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 2  ,  0 ],
   [ 0  ,  0  ,  0  ,  0  ,  0   , 0 , 336 , 143  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 236  ,  0],
   [ 0 ,   0  ,  0 ,   0   , 0  ,  0  ,  0 , 2222  ,  0 ,   0  ,  0 ,   0 ,  0  ,  0 , 
    34 ,   0],
    [0  ,  0   , 0  ,  0  ,  0  ,  0   , 0  ,  0 , 1240 ,   0 ,   0  ,  0  ,  0 ,   0 , 0  ,  0],
    [0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 171 , 485   , 0 ,   0  ,  0 ,   0   , 0 , 0  ,  0],
   [ 0   , 0  ,  0  ,  0  ,  0 ,   0  ,  0 , 182 ,  32 ,   0  ,  0 ,   0  ,  0   , 0 , 0  ,  0],
   [ 0  ,  0 ,   0  ,  0  ,  0   , 0 ,   0 , 369 ,  17 ,   0 ,   0  ,  0 ,   0   , 0 , 0  ,  0],
   [ 0 ,   0  ,  0  ,  0  ,  0   , 0 ,   0 ,  85  , 96  ,  3  ,  0 ,   0  ,  0   , 0 , 0 ,   0],
   [ 0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 , 176 ,  38  ,  0 ,   0   , 0   , 0   , 0 , 0 ,   0],
   [ 0  ,  0  ,  0  ,  0   , 0  ,  0  ,  0 ,  34 ,  0  ,  0 ,   0  ,  0  ,  0   , 0 ,  1420 ,   0],
   [ 0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  , 1 , 317 , 0  ,  0 ,   0  ,  0 ,   0 , 40  ,  4]]
   
knn_salinas =  [[402 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0   , 0 , 0  ,  0],
    [0 , 745 ,   0  ,  0  ,  0  ,  0 ,   0 ,   1 ,   0  ,  0 ,   0  ,  0  ,  0  ,  0 , 0  ,  0],
    [0  ,  0 , 396 ,   0 ,   0  ,  0 ,   0 ,   0  ,  0  ,  0  ,  0  ,  0 ,   0   , 0 , 0  ,  0],
    [0 ,   0   , 0 , 272 ,   2  ,  0  ,  0  ,  1  ,  0  ,  0   , 0  ,  0  ,  0   , 0 , 4  ,  0],
    [0  ,  0  ,  0  ,  7 , 528  ,  1  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0 ,   0   , 0 , 0  ,  0],
    [0  ,  0   , 0 ,   0  ,  0 , 791 ,   1 ,   0 ,   0 ,   0  ,  0  ,  0  ,  0   , 0 , 0  ,  0],
    [0  ,  0  ,  0  ,  0  ,  0  ,  0 , 716 ,   0  ,  0 ,   0  ,  0  ,  0  ,  0   , 0 , 0 ,   0],
    [0 ,   0  ,  0  ,  2  ,  0  ,  0 ,   0 , 2250 , 0 ,   0 ,   0 ,   0 ,   0 , 0 , 3  ,  0],
    [0  ,  0  ,  0  ,  0 ,   0  ,  0 ,   0  ,  0 , 1241  ,  0  ,  0  ,  0  ,  0   , 0 , 0  ,  0],
    [0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  0 ,   0 , 0 , 654 ,   0 ,   0 ,   0  ,  2 , 0  ,  0],
    [0  ,  0 ,   0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 , 211 ,   3 ,   0   , 0 , 0  ,  0],
    [0  ,  0   , 0  ,  0 ,   0  ,  0  ,  0 ,   0 ,   0  ,  0  ,  2 , 381  ,  4   , 0 , 0  ,   0],
    [0  , 0  ,  0 ,   0 ,   0  ,  0  ,  0  ,  0  ,  0 ,   0 ,   0  ,  1 , 179   , 3 , 0  ,  0],
    [0  ,  0 ,   0 ,   0 ,   0  ,  0  ,  0 ,   0 ,   0  ,  2 ,   0 ,   0  ,  5 , 207 , 0  ,  0],
    [0  ,  0 ,   0 ,   0  ,  0  ,  0  ,  0   , 0 ,   0 ,   0  ,  0  ,  0  ,  0   , 0 , 1454  ,  0],
    [0  ,  0  ,  0  ,  0  ,  0  ,  0  ,  0 ,   0  ,  0  ,  0  ,  0   , 0 ,   0    , 0 , 0 , 362]] 
    

nn_sal=[[    1154  ,  0  ,  0  ,  0  ,  0 ,   0 , 195 ,   0  ,  0  ,  0  ,  0  ,  0 ,   0
    , 0   , 0  , 58],
 [ 1  , 54  ,  0 ,   0 ,   0   , 0, 1256 ,   3   , 0 ,   0 ,   0  ,  0  ,  0,
     0   , 6, 1289],
 [  0   , 0  ,  0,  190 ,   0   , 0   , 0   , 0  ,  0  ,  0 ,   0 ,1193  ,  1,
     0   , 0 ,   0],
 [       0  ,  0   , 0 , 976 ,   0  ,  0   , 0  ,  0   , 0 ,   0  ,  0  ,  0 ,   0,
     0 ,   0  ,  0],
 [       0  ,  0 ,   0, 1794  ,  0  ,  0  ,  0  ,  0  ,  0   , 0  ,  0 ,  79  ,  2,
     0  ,  0  ,  0],
 [       0  ,  0 ,   0 ,   1  ,  0   , 0   , 0 ,2433  ,  0 , 259 ,   0  , 31 ,  41,
     0   , 7  ,  0],
 [       0  ,  0 ,   0   , 0  ,  0  ,  0 ,1622  ,  5  ,  0  ,  0 ,   0 ,   0  ,  0,
     0   , 0  ,879],
 [       0  ,  0 ,   0 , 364 ,   0  ,  0  ,  0 ,2870,    0  ,  5 ,   0  ,119,   21,
     0 ,4435 ,  76],
 [       0 ,   0   , 0  ,  0  ,  0  ,  0   , 0   , 0   , 0  ,  0  ,  0, 4343  ,  0
    , 0  ,  0,    0],
 [      0  ,  0   , 0 , 203  ,  0  ,  0   , 0 , 199  ,  0  , 36  ,  0 ,1799 ,  21,
     0  , 36,    1],
 [      0 ,   0 ,   0 ,   3  ,  0  ,  0   , 0  ,  0  ,  0   , 0  ,  0 , 745  ,  0,
     0   , 0 ,   0],
 [       0  ,  0    ,0   , 0 ,   0  ,  0   , 0   , 0  ,  0  ,  0  ,  0 ,1349,    0,
     0  ,  0   , 0],
 [       0   , 0  ,  0  ,  0  ,  0  ,  0 ,   0 ,   1  ,  0  ,  0  ,  0  ,380  ,261,
     0  ,  0  ,  0],
 [      0  ,  0  ,  0 ,  10  ,  0   , 0   , 0 , 470  ,  0  ,  0  ,  0  , 39 , 125,
   105   , 0   , 0],
 [      0  ,  0 ,   0 , 307  ,  0  ,  0 ,   0  ,760  ,  0  ,  1 ,   0 ,  24   , 3,
     0, 3950 ,  43],
 [     0   , 0   , 0 ,   7  ,  0 ,   0,    2  , 10 ,   0,    0   , 0   , 6  ,  0,
     0  , 11, 1229]]
 
 
mou_aviris=[[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
        [  0,   6,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,  12,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   4,   0,  17,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,  78,  17,   0,   8,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   1, 101,   0,   3,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0, 158,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   7,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0, 114,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0, 111,   0,   0,   0,
          0,   1,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  68,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   3,   0,   0,   0,
          0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,  37,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,  34,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   5,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   6,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   4]]
       
hu_aviris=[
       [   6,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [     0,  12,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [     0,   0,  21,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [   0,   0,   0,  87,  15,   0,   1,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [     0,   0,   0,   5, 100,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [     0,   0,   0,   0,   0, 158,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [     0,   0,   0,   0,   0,   0,   7,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [   0,   0,   0,   0,   0,   0,   0, 114,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [    0,   0,   0,   0,   0,   0,   0,   0, 111,   0,   0,   0,
          0,   1,   0,   0,   0,   0,   0],
       [   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,
          0,   0,   0,   0,   0,   0,   0],
       [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  68,   0,
          0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11,
          0,   0,   0,   0,   0,   0,   0],
       [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          3,   0,   0,   0,   0,   0,   0],
       [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,  37,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,  34,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   5,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   6,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   4,   0],
       [ 0,   0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   8]]
df = pd.DataFrame(hu_aviris)

df.columns =  [   "Grass",
                        "Baresoil",
                        "Plough Field",
                        "Rail",
                        "Maize",
                        "Building",
                        "Trees",
                        "Bricks",
                        "Water",
                        "Pigeon Pea",
                        "Building Conc",
                        "Wheat",
                        "Mustard",
                        "Road",
                        "Lin Seeds",
                        "Brinjal",
                        "Tobacco",
                        "Amla",
                        "Caster",
                        ]
df.index =  [  "Grass",
                        "Baresoil",
                        "Plough Field",
                        "Rail",
                        "Maize",
                        "Building",
                        "Trees",
                        "Bricks",
                        "Water",
                        "Pigeon Pea",
                        "Building Conc",
                        "Wheat",
                        "Mustard",
                        "Road",
                        "Lin Seeds",
                        "Brinjal",
                        "Tobacco",
                        "Amla",
                        "Caster",
                        ]

#ax = sns.heatmap(df,cmap="YlGnBu" , annot=True, fmt="d")
ax = sns.heatmap(df ,cmap="Spectral")
ax.set_yticklabels(ax.get_yticklabels(), rotation =0)
ax.set_xticklabels(ax.get_yticklabels(), rotation =90)
plt.title('1D CNN on AVIRIS')
plt.show()





# extra class labels just in case the labels above get deleted by the user.

pines = ['Alfalfa',	
'Corn-notill',
'Corn-mintill',
'Corn'	,
'Grass-pasture',	
'Grass-trees'	,
'Grass-pasture-mowed',	
'Hay-windrowed'	,
'Oats'	,
'Soybean-notill'	,
'Soybean-mintill',	
'Soybean-clean',	
'Wheat'	,
'Woods'	,
'Buildings-Grass-Trees-Drives',	
'Stone-Steel-Towers']

salinas = ['Brocoli_green_weeds_1',	
	'Brocoli_green_weeds_2'	,
	'Fallow	',
	'Fallow_rough_plow'	,
'Fallow_smooth'	,
	'Stubble',	
'Celery',	
	'Grapes_untrained',	
	'Soil_vinyard_develop',	
	'Corn_senesced_green_weeds',	
	'Lettuce_romaine_4wk',	
	'Lettuce_romaine_5wk',	
	'Lettuce_romaine_6wk',	
	'Lettuce_romaine_7wk',
	'Vinyard_untrained'	,
	'Vinyard_vertical_trellis']

pavia = ['Water',	
	'Trees',	
	'Asphalt',	
	'Self-Blocking Bricks',	
	'Bitumen',	
	'Tiles',	
	'Shadows',	
	'Meadows',	
	'Bare Soil']