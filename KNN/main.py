import numpy as np
import operator
 
 
def knnClassify(inputX, data, labels, k):
 
    # 1.计算测试数据与各训练数据之间的距离。
    dataSize = data.shape[0]
    x = np.tile(inputX, (dataSize, 1)) - data
    xPositive = x ** 2
    xDistances = xPositive.sum(axis=1)
    distances = np.sqrt(xDistances)
 
    # 2.按照距离的大小进行排序。
    sortDisIndex = distances.argsort()
    print(sortDisIndex)
 
    # 3.选择其中距离最小的k个样本点。4.确定K个样本点所在类别的出现频率。
    classCount = {}  # 创建字典：label为键，频数为值
    for i in range(k):
        getLabel = labels[sortDisIndex[i]]
        classCount[getLabel] = classCount.get(getLabel, 0) + 1
 
    # 5.返回K个样本点中出现频率最高的类别作为最终的预测分类。
    sortClass = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortClass[0][0])
 
    return sortClass[0][0]
 
 
if __name__ == '__main__':
    # 测试数据
    inputX = np.array([2, 2.2, 1.9])
    # 训练数据
    data = np.array([[1, 0.9, 1], [0.8, 0.9, 0.7], [1.3, 1, 1.2], [1.2, 0.9, 1],
                     [2, 2.2, 2.1], [2.3, 2.2, 2], [2, 2.2, 1.9], [1.9, 2.2, 2.1],
                     [3.1, 3.1, 3], [2.8, 2.9, 3.1], [2.9, 3, 3.2], [3.1, 3, 3.1]])
    # 训练数据标签
    labels = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
    k = 3
    knnClassify(inputX, data, labels, k)