from scipy.stats import spearmanr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 读取Excel表格
df = pd.read_excel('第四问满意度实际评分数据.xlsx',usecols="Q,W,Y,AB,CU,EU,EV,EW,EX,EY,EZ,FA,FB,FC,ES,ET")

X = pd.get_dummies(df, columns=['有无追加镇静','呛咳','有无追加镇痛','体动','术中其他','是否出现了恶心呕吐的情况是','是否出现了头晕头昏头痛是', '有没出现嗜睡乏力的情况呢有','有没出现腹胀腹痛的情况呢有','还有没其他不舒服的情况呢有'], drop_first=True)
X = X.fillna(X.mean())
X=X.drop(columns='满意度实际评分',axis = 1)
X['满意度实际评分'] = df['满意度实际评分']
print(X)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['font.family'] = 'sans-serif'  # 设置全局字体
print(X)
# 计算每个特征与目标变量之间的Spearman相关系数和p-value
corrs = []
p_values = []
# 创建一个2行3列的子图，并设置子图大小为(10, 6)
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
i = 0
j = 0

for col in X.columns:
    if col != '满意度实际评分':

        corr, p_value = spearmanr(X[col], X['满意度实际评分'])
        corrs.append(corr)
        #print(corr)
        p_values.append(p_value)
        #print(p_value)
        if(col == '麻醉医生满意度' or col == '是否出现了头晕头昏头痛是_是'or col == '是否出现了恶心呕吐的情况是_是' or col =='有无追加镇痛_有'):
            # 绘制箱线图
            print(col)
            print(X['满意度实际评分'])

            a = pd.DataFrame({col: X[col], '满意度实际评分': X['满意度实际评分']})
            axes[i,j].boxplot(data = a, x = col)
            axes[i,j].set_title(col+'Box plot')
            if(j == 1):
                i = 1
                j = -1
            j+=1
            
# 调整子图之间的间距和周围的边距
fig.tight_layout(pad=2, w_pad=1, h_pad=1)   
plt.show()

# 将结果存储在一个DataFrame中
results = pd.DataFrame({'Feature': X.columns[:-1], 'Correlation': corrs, 'P-value': p_values})
'''
# 打印结果
print(results)

# 创建可视化表格
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')
ax.axis('tight')
table = ax.table(cellText=results.values, colLabels=results.columns, loc='center')

# 保存图像文件
plt.savefig('results.png')
'''
x_values = ['镇静药总剂量','呛咳','恶心呕吐','头晕头昏头痛','镇痛药总剂量','开始给药时间','最后给药时间','IPI达到4分时间','睁眼时间','进镜时间','出镜时间','出PACU']
y1 = [-0.249,0.17,-0.231,-0.091,-0.221,-0.283,-0.276,-0.295,-0.291,-0.315,0.287,0.277]
y2 = [0.000,0.001,0.000,0.082,0.000,0.00,0.000,0.00,0.000,0.000,0.00,0.00]
'''
# 绘制散点图
plt.scatter(x_values, y1)

# 绘制折线图
plt.plot(x_values, y2, color='red')

# 添加标题和标签
plt.title('R corr and p_values')
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(fontsize=8, rotation=90)
plt.yticks(fontsize=12)
# 显示图像
plt.show()
'''
# 绘制折线图
plt.plot(x_values, y1, color='red', linestyle='-', label='corr', marker='o')
plt.plot(x_values, y2, color='blue', linestyle='--', label='p_value',marker='s')

# 添加标签和标题
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('各影响用户满意程度的因素的corr值和p_values值')
plt.xticks(fontsize=8, rotation=30)
plt.yticks(fontsize=12)
# 添加图例
plt.legend()

# 显示图表
plt.show()
