# 前段
#     首页页面跳转
# 后段
#     数据库，后台服务，一些接口

'''定义一个函数，接收一个需要排序的列表作为参数。
获取列表的长度并保存下来，用来计算总共需要比较的轮数。
开启一个外层循环，控制整体要进行多少轮比较。
开启一个内层循环，在每一轮中依次检查相邻的两个元素。
判断左边的元素是否比右边的大。
如果左边的大于右边的，就交换这两个元素的位置。
循环全部结束后，返回排好序的列表。'''
def order(list1):
    a=len(list1)
    for i in range(a):
        for j in range(a):
            if list1[i]<list1[j]:
                list1=change(i,j,list1)
    return list1


def change(x,y,ll):

    # ll = [1,2,3,4,5]
    n=ll[x]
    m=ll[y]
    ll[y]=n
    ll[x]=m
    return ll



day=["周一","周二","周三","周四"]
price=[1,2,3,4]
def a(price):
    # b是总股数
    b=100/1+100/2+100/3+100/4
    # c是总价 b*当前价格
    c=b*4

ll = [1,3,4,5,2312,1,3,4,5]
print(order(ll))