#223407020209 沈成林
import numpy as np

'''
总预算：N元 购买物品个数：m个
重要度：Int 1-5（5等最重要）
物品价格Int
使每件物品的价格与重要度的乘积总和最大

Example:
	1000为总预算，只能购买5件商品
	 400x5+300x5+200x2=39001
'''

#贪婪算法（不可行）
'''

def ListDescSort(list_to_be_sorted):
	return sorted(list_to_be_sorted, key=lambda d: d['scaled_value'], reverse=True)

N, m = map(int,input().split())

item_info_list = []

for i in range(1, m+1):
	v, p = map(int,input().split())
	scaled_value = v*p;
	item_info_list.append({'item_price': v, 'item_priority': p, 'scaled_value': scaled_value})

desc_list = ListDescSort(item_info_list)

total_money = 0
total_scaled_value = 0

print(desc_list)

for item in desc_list:

	total_money = total_money + item['item_price']

	if total_money <= N:
		total_scaled_value = total_scaled_value + item['scaled_value']

print(total_scaled_value)
'''

#背包算法

'''
创建一系列子背包

[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]

暂时设为空，等待填入数据
'''
#mn

#总预算：N元 购买物品个数：m个
N, m= map(int, input().split())

#重新命名N. m以便阅读
rows_num = m + 1
columns_num = N + 1

item_info_list = [[0,0]]
for i in range(m):
	money, value = map(int,input().split())
	item_info_list.append([money,value])

print(item_info_list)	

backpack = [[0 for i in range(N+1)] for j in range(m+1)]
print(np.array(backpack))

'''
按item单价从小到大从第一行开始填入scaled_value（总价值）最大的数据，
每行只能从所在行及当前行以前的item中选取并依次填入子背包
每行最后一列所在元素即为最大价值元素

[[   0    0    0 ...    0    0    0]
 [   0    0    0 ... 1600 1600 1600]
 [   0    0    0 ... 2000 2000 2000]
 [   0    0    0 ... 3500 3500 3500]
 [   0    0    0 ... 3500 3500 3500]
 [   0    0    0 ... 3900 3900 3900]]
 
列表最后一行最后一列所在元素即为最大价值
'''

for row in range(1, rows_num):
	for column in range(1, columns_num):
		#若item单价大于等于该背包最大容量，则填入价值最大者，否则填入同列上一行的数据（因为上一行所在的价值是未解锁该行item时价值最大的item，所以认为此数据也为价值最大的数据）
		if column < item_info_list[row][0]:
			backpack[row][column] = backpack[row-1][column]
		else:
			backpack[row][column] = max(backpack[row-1][column], item_info_list[row][1]*item_info_list[row][0]+backpack[row-1][column-item_info_list[row][0]])
print(np.array(backpack))
print(backpack[-1][-1])
