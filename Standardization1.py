#标准化1：减去均值，然后除以当前的标准差
from sklearn import preprocessing
import numpy as np
x=np.array([[1.,2.,0.],[2.,0.,1.]])
#axis为哪个轴，哪个轴就看作是整体，然后和别的整体进行标准化（默认axis=0）
x_scaled1=preprocessing.scale(x,axis=0)#将每个样本的所有特征看成整体，和其他样本的每个特征标准化（样本对应的特征 标准化）
x_scaled2=preprocessing.scale(x,axis=1)#每个样本自己内部所有特征一起标准化
#标准化后，标准差为1，均值为0
print(x_scaled1.std(axis=0))#[ 1.  1.  1.]
print(x_scaled1.mean(axis=0))#[ 0.  0.  0.]

#保存训练集中的均值和方差，然后用于转换测试集数据(axis=0)
scaler=preprocessing.StandardScaler().fit(x)
print(scaler.mean_)#x的axis=0的均值
print(scaler.scale_)#x的axis=0的标准差
print(scaler.var_)#x的axis=0的方差
x_test=np.array([[6.,6.,6.]])
print(scaler.transform(x_test))