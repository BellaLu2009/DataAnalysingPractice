import os
import pandas as pd
from numba.cuda.printimpl import print_item

# print(len(os.listdir("BJ")))

numbers = []
BJ=os.listdir("BJ")
BJ.remove('bj873693.csv')
BJ.remove('bj920002.csv')





    # print(len(df))
    # print(df.columns.tolist())
    # print(result_df)
    # print(f"第一天的收盘价是: {first_price}")
    # print(f"最后一天的收盘价是: {last_price}")
    # print(zhangfu)
    # print(f"单日波动额度为: {result['涨跌额度']:.2f} 元")




    # break22
# print(max(numbers))
#     开盘价，涨跌幅，振幅, 量比

# print("单日波动最大的股票是:")
# print(max_stock_result)

# 'bj873693.csv'


# a=[]
# # a=["bj...csv"]
# bj = [1,2,3,4,5,6,7,3] # 被减数
# a = [2,3] # 减数
# # c = bj - a
# c = [] # 结果
# for x in bj:
#     if x not in a:
#         c.append(x)
# # c is bj - a de jieguo
# 
# 
# 
# print(c)

def find_max(a):
    max_stock_result = None
    max_fluctuation = 0
    c=[]
    BJ目录下所有的文件名 = os.listdir("BJ")
    # print(BJ)
    # c=BJ-a
    for b in BJ目录下所有的文件名:
        if b not in a:
            c.append(b)


    # print()
    for x in c:
        # print(x)
        # file_path is *****
        file_path = os.path.join("BJ", x)
        df = pd.read_csv(file_path, encoding="gbk")
        result_df = df[['交易日期', '股票代码', '开盘价', '涨跌幅', '振幅', '量比', '收盘价']]
        first_price = df['收盘价'].iloc[-1]
        last_price = df['收盘价'].iloc[0]
        zhangfu = last_price - first_price
        numbers.append(zhangfu)
        df['涨跌额度'] = (df['收盘价'] - df['开盘价']).abs()
        max_row_index = df['涨跌额度'].idxmax()
        result = df.loc[max_row_index]
        result = result[['股票代码', '交易日期', '涨跌额度']]

        if result['涨跌额度'] > max_fluctuation:
            max_fluctuation = result['涨跌额度']
            max_stock_result = result
    # (type(max_stock_result))
    # (max_stock_result)
    stock=max_stock_result['股票代码']
    # i am:bj873693
    # i can: f'AAA{变量}AAAA'
    # i want:["bj...csv"]
    # stock + '.csv' =  f'{stock}.csv'
    a.append(f'{stock}.csv')
    # print(a)
    return a
a = []
print(a)
a = find_max(a)
print(a)
a = find_max(a)
print(a)
a = find_max(a)
print(a)
a = find_max(a)
print(a)
a = find_max(a)
print(a)
a = find_max(a)
print(a)






