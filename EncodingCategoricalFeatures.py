#OneHotEncoder详见 https://www.cnblogs.com/zhoukui/p/9159909.html
from sklearn import preprocessing
import numpy as np
enc=preprocessing.OneHotEncoder(sparse=False)
x=np.array([[0,0,0],[1,1,2],[0,2,1],[5,5,5]])
enc.fit(x)
print(enc.transform([[1,1,2]]))