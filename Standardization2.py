#缩放到指定范围 http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler
#公式：X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
#     X_scaled = X_std * (max - min) + min (这里的max和min是feature_range的上下限)
from sklearn import preprocessing
import numpy as np
x=np.array([[1.,2.,0.],[2.,0.,1.]])
min_max_scaler=preprocessing.MinMaxScaler(copy=True,feature_range=(0,1))
min_max_scaler.fit(x)#	Compute the minimum and maximum to be used for later scaling.
print(min_max_scaler.transform(x))

#8-9可以直接合并为fit_transform(x)  "Fit to data, then transform it."