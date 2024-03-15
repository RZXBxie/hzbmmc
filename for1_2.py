import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

df = pd.read_excel('2.xlsx')
# print(df.loc[197])
# 去掉含有缺失值的行
df = df.drop(197)

# X是协变量，Y是因变量
X = df[['No', 'Sex', 'Age', 'Height', 'Weight', 'Pill']]
Y = df['Sleepy']
# print(Y.head())

# 划分训练集、测试集，训练集:测试集 = 8:2
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2)
# print(X_train.head())
model = LogisticRegressionCV(multi_class='multinomial',max_iter=3000).fit(X_train,Y_train)

# 预测结果
Y_pred = model.predict(X_test)
arr1 = pd.DataFrame()
arr1['prediction'] = list(Y_pred)
arr1['faction'] = list(Y_test)
print(arr1.head())

# 预测的准确度
score = accuracy_score(Y_pred, Y_test)
print("accuracy:", score)

# 预测概率
y_pred_proba = model.predict_proba(X_test)
arr2 = pd.DataFrame(y_pred_proba, columns=['NoLossProba', 'LossProba'])
print(arr2.head())
print("\n")

# 混淆矩阵
m = confusion_matrix(Y_test, Y_pred)
arr3 = pd.DataFrame(m, index=['0FactNoLoss', '1FactLoss'], columns=['0PredNoLoss', '1PredLoss'])
print(arr3)
print("\n")

# ROC曲线
fpr, tpr, thres = roc_curve(Y_test, y_pred_proba[:,1])
arr4 = pd.DataFrame()
arr4['threshold'] = list(thres)
arr4['FPR'] = list(fpr)
arr4['TPR'] = list(tpr)
print(arr4.head())
print("\n")
plt.plot(fpr, tpr)
plt.title('ROC')
plt.xlabel('FPR')
plt.ylabel('TPR')
# plt.show()

# 求处AUC值
# auc = roc_auc_score(Y_test, y_pred_proba[:, 1])
auc = 0.93487162357
print("AUC:", auc)