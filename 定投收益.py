# -*- coding: utf-8 -*-
# @Time    : 2026/11/6 17:06
# @Author  : cy1026
# @File    : 定投收益.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 20个交易日连续平滑的列表数据（起点和终点均为100，对称下凹无突变）
trading_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 标的A：深V平滑微笑曲线（中间谷底跌到40，平滑过渡）
price_a = [
    100.0, 88.03, 77.4, 68.09, 60.11, 53.46, 48.14, 44.16, 41.5, 40.17,
    40.17, 41.5, 44.16, 48.14, 53.46, 60.11, 68.09, 77.4, 88.03, 100.0
]
def e(price):
    c=0
    for a in price:
        b=10000/a
        c+=b
    #     print(b,123)
    # print(c)
    d=c*100
    return d



# 1000/88.03=第二天股票数量 1000/88.03=第二天股票数量

# 标的B：浅V平滑微笑曲线（中间谷底跌到80，平滑过渡）
price_b = [
    100.0, 96.01, 92.47, 89.36, 86.7, 84.49, 82.71, 81.39, 80.5, 80.06,
    80.06, 80.5, 81.39, 82.71, 84.49, 86.7, 89.36, 92.47, 96.01, 100.0

]

print(e(price_b))
print(e(price_a))
# 2. 构建 DataFrame 并计算定投（每交易日定投 1000 元，共 20,000 元本金）
df = pd.DataFrame({
    '交易日': trading_days,
    '标的A价格': price_a,
    '标的B价格': price_b,
    '定投金额': 1000
})

# 标的A定投计算
df['A_当期份额'] = df['定投金额'] / df['标的A价格']
df['A_累计份额'] = df['A_当期份额'].cumsum()
df['A_累计本金'] = df['定投金额'].cumsum()
df['A_当前市值'] = df['A_累计份额'] * df['标的A价格']

# 标的B定投计算
df['B_当期份额'] = df['定投金额'] / df['标的B价格']
df['B_累计份额'] = df['B_当期份额'].cumsum()
df['B_累计本金'] = df['定投金额'].cumsum()
df['B_当前市值'] = df['B_累计份额'] * df['标的B价格']

df = df.round(2)

# 3. 打印最终结果
total_principal = df['A_累计本金'].iloc[-1]
final_val_a = df['A_当前市值'].iloc[-1]
return_a = (final_val_a - total_principal) / total_principal * 100

final_val_b = df['B_当前市值'].iloc[-1]
return_b = (final_val_b - total_principal) / total_principal * 100

print(f"总本金: ¥{total_principal:,.2f}")
print(f"标的A（深V）期末市值: ¥{final_val_a:,.2f} | 收益率: {return_a:.2f}%")
print(f"标的B（浅V）期末市值: ¥{final_val_b:,.2f} | 收益率: {return_b:.2f}%")

# 4. 绘图
plt.figure(figsize=(9, 4.5))
plt.plot(df['交易日'], df['标的A价格'], marker='o', label='标的A（深V平滑微笑）', color='#1f77b4', linewidth=2)
plt.plot(df['交易日'], df['标的B价格'], marker='s', label='标的B（浅V平滑微笑）', color='#ff7f0e', linewidth=2, linestyle='--')
plt.title('起点与终点相同且全程连续平滑的微笑曲线对比', fontsize=12, fontweight='bold')
plt.xlabel('交易日')
plt.ylabel('价格')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()