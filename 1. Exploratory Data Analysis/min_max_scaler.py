"""
MinMaxScaling :

MinmaxScaling is an often-used method
in data science to perform equivalent
patterns or correlations. The feature
can be scattered in a variational range.
Now if we fit the model into that,
that might give some features more
important than others. So min-max
scaling sets the value in 0 to 1
range and thus retrieving the appropriate
information.

Operation :

data[i] = ( data[i] -  minimum value of the series ) / ( maximum value of the series "data" -  minimum value of the series "data" )

"""


# Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Loading data into dataframe
iris_data_path = 'D:/temp/Iris.csv'
data = pd.read_csv( iris_data_path )

# Min-Max_Scaling :

"""
In this function, we are performing
the operation into the valid
integer/float value features.In this function, we are performing
the operation into the valid
integer/float value features.
"""

def min_max_scaling(dataframe,features):
    for feature in features:
        min_value = min( dataframe[ feature ] )
        max_value = max( dataframe[ feature ] )

        dataframe[ feature ] = ( dataframe[ feature ] - min_value ) / ( max_value - min_value )

    return dataframe

# Setting the label which neds to be scaled

features = data.columns[1 : -1]   # ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

print('Before MinMaxScaling...........')
for feature in features:
    min_value = min( data[feature] )
    max_value = max( data[feature] )
    print("feature {} ---> Min Value : {} | Max Value : {}".format(feature , min_value , max_value))


# Perfrming scaling over the selected features of the data
data = min_max_scaling( data , features )

# Checking if the operation gone right
for feature in features:
    min_value = min( data[feature] )
    max_value = max( data[feature] )
    assert min_value ==0.0 and max_value==1.0

print('Success')

