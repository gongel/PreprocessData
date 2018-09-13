#自定义转换器
from sklearn import preprocessing
import numpy as np
transformer=preprocessing.FunctionTransformer(np.log1p) #np.log1p: log(1 + x) 以e为底数
x=np.array([[0,1],[2,3]])
print(transformer.transform(x))#两者等效
print(transformer.fit_transform(x))#两者等效


#**********************************************
np.log10(10)#1
np.log2(2)#1
np.log(np.e)#1