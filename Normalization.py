#将椭圆归一化为圆
from sklearn import preprocessing
import numpy as np
x=np.array([[1.,2.,0.],[2.,0.,1.]])
x_normalized=preprocessing.normalize(x,norm='l2')
print(x_normalized)

#另外一种方法
normalizer=preprocessing.Normalizer().fit(x)
print(normalizer.transform(x))