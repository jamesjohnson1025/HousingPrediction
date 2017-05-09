"""
    Predict's the housing prices

"""
import matplotlib.pyplot as plt
from helpers.data import fetch_housing_data
from helpers.data import load_housing_data
from helpers.data import split_train_test

#fetch_housing_data();

housing = load_housing_data()

# Head part of data
print housing.head()

# info part of the data
print housing.info()

#value counts
print housing['ocean_proximity'].value_counts()

#describe method shows a summary of numerical attributes
print housing.describe()

housing.hist(bins=150,figsize=(20,15))

#plt.show()

train_data,test_data = split_train_test(housing,0.2)
print 'Training data length is %s' % len(train_data)
print 'Testing data length is %s' % len(test_data)

