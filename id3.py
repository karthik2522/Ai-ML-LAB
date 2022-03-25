import pandas as pd
import numpy as np


dataset = pd.read_csv('tennis.csv',names=['outlook','temperature','humidity','wind','class'])
attributes = ('outlook','temperature','humidity','wind','playtennis')

def entropy(target_col):
    elements,counts = np.unique(target_col, return_counts=True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

def InfoGain(data,split_attribute_name, target_name="class"):
    total_entropy = entropy(data[target_name])
    val,counts = np.unique(data[split_attribute_name],return_counts=True) 
    weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==val[i]).dropna()[target_name]) for i in range(len(val))])
    Information_Gain = total_entropy - weighted_Entropy
    return Information_Gain

def ID3(data, originaldata, features, target_attribute_name="class",parent_node_class=None):
    if len(np.unique(data[target_attribute_name]))<=1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data)==0:
        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)(1))]
    elif len(features)==0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])]
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature:{}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature]==value).dropna()
            subtree = ID3(sub_data, dataset,features, target_attribute_name, parent_node_class)
            tree[best_feature][value]=subtree
        return(tree)

tree = ID3(dataset,dataset,dataset.columns[:-1])
print(dataset.head())
print(' \nDisplay Tree\n',tree)    

