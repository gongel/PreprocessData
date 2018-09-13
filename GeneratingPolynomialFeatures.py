#生成多项式特征（nonlinear features of the input data）
import numpy as np
from sklearn import preprocessing
x=np.arange(6).reshape(3,2)
poly=preprocessing.PolynomialFeatures(2)
print(poly.fit_transform(x)) #The features of X have been transformed from (X_1, X_2) to (1, X_1, X_2, X_1^2, X_1X_2, X_2^2).

x2=np.arange(6).reshape(3,2)
poly2=preprocessing.PolynomialFeatures(degree=2,interaction_only=True)
print(poly2.fit_transform(x2))#只有交互性的乘积会出现，这里是x1*x2，not x1**2，x2**2


