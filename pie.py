import matplotlib.pyplot as plt

# 数据
labels = ['Wrong with trigger word', 'Wrong without trigger word', 'Too literal', 'Too specific', 'Too general', 'Wrong subelement mapping']
sizes = [63.39, 9.12, 10.43, 4.06, 1.62, 11.38]
colors = ['#FF5050', '#FFFF66', '#99FF66', '#66CCFF', '#FFCC66', '#CC99FF']

# 绘图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')  # 保持圆形
plt.title('Error Type')

# 展示图表
plt.show()