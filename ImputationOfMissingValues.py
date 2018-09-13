#丢失值（ 0, blanks, NaNs or other placeholders）的填充（ either using the mean, the median or the most frequent value of the row or column in which the missing values are located）
#注意：如果缺失值为NaN，需要提前把数据中的缺失值用np.nan替换
from sklearn import preprocessing
import numpy as np
imp=preprocessing.Imputer(missing_values='NaN',strategy='mean',axis=0)
imp.fit([[2,1,3],[3,np.nan,6],[2,0,1]])
print(imp.transform([[1,np.NaN,1]])) #[[ 1.   0.5  1. ]]
