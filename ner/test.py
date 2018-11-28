# -*- coding:utf-8 -*-

# f = open("newtab.txt", 'r', encoding="utf-8", errors='ignore')
#
# full_txt = f.read()
#
# for i in range(15):
#     ntxt = full_txt.replace("\n\n","\n")
#     full_txt = ntxt.replace("\n\n","\n")
# f.close()
#
# f = open("format_tab.txt",'w',encoding="utf-8",errors='ignore')
# f.write(full_txt)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import pandas as pd
from sklearn.decomposition import PCA


plt.figure()
# X, y = make_blobs(n_samples=1000, n_features=2, centers=[
#     [-1, -1], [0, 0], [1, 1], [2, 2]], cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)  # 生成测试数据
# for index, k in enumerate((2, 3, 4, 5)):
#     plt.subplot(2, 2, index + 1)
#     y_pred = KMeans(n_clusters=k, random_state=9).fit_predict(X)  # 预测值
#     score = metrics.calinski_harabaz_score(X, y_pred)
#     plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=10, edgecolor='k')
#     plt.text(.99, .01, ('k=%d, score: %.2f' % (k, score)),  # 文本注释，标注关键信息
#              transform=plt.gca().transAxes, size=10, horizontalalignment='right')
# f = open("format_tab.txt","r",encoding='utf-8',errors='ignore')
df = pd.read_table('format_tab.txt')
dataMat = np.array(df.iloc[:,2:5])
#调用sklearn中的PCA，其中主成分有3列
pca_sk = PCA(n_components=3)
#利用PCA进行降维，数据存在newMat中
newMat = pca_sk.fit_transform(dataMat)
#利用KMeans进行聚类，分为3类
kmeans = KMeans(n_clusters=3,random_state=0).fit(dataMat)
#labels为分类的标签
labels = kmeans.labels_
#把标签加入到矩阵中用DataFrame生成新的df，index为类别的编号，这里是0,1,2
dataDf = pd.DataFrame(dataMat,index=labels,columns=['x1','x2','x3'])
#数据保存在csv文件中
dataDf.to_csv('pca_cluster.csv')
print(pca_sk.explained_variance_ratio_)
plt.show()
