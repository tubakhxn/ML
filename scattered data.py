import numpy as np
train_df = ...  
data=train_df.values
data[:5]
def check_purity(data):
    label_coloumn= data[:,-1]
    unique_classes= np.unique(label_coloumn)
    if len(unique_classes)==1:
        return False
    else:
        return True
check_purity(train_df.patel_width>0.8)
