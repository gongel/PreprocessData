#特征二值化是对数值特征进行阈值化处理得到布尔值的过程
#超过阈值的为1，否则为0
from sklearn import  preprocessing
import numpy as np
x=np.array([[-5,1,2],[6,5,-2]])
binarizer1=preprocessing.Binarizer(threshold=0.0).fit(x)
print(binarizer1.transform(x))
print(preprocessing.Binarizer(threshold=5).fit_transform(x))
