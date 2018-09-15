"""
author: xingbuxing
date: 2018年01月11日
功能：本程序主要介绍python的常用内置数据结果，如list、dict等。希望以后大家只要看这个程序，就能回想起相关的基础知识。
"""


# =====list介绍
# 使用[]中括号就可以新建一个数组。
# list_var = []  # 这是一个空list
# print(list_var, type(list_var))

# list是具有顺序的一组对象，其中的元素不需要是同类型
# list_var = [1, '2', 3, 4.0, 5, 6, 'seven', [8], '九']  # list举例，其中包含了整数、小数、字符串、数组
# print(list_var)


# =====list常见操作：索引，选取list中的某个元素
# list_var = [1, '2', 3, 4.0, 5, 6, 'seven', [8], '九']  # list举例

# print(list_var[0])  # 输出排在第1个位置的元素。位置的计数是从0开始的。
# print(list_var[3])  # 输出排在第4个位置的元素。
# print(list_var[8])  # 输出排在第9个位置的元素。也就是最后一个元素。
# print(list_var[-1])  # 输出最后一个元素的另外一种方式。
# print(list_var[-2])  # 输出最后第二个位置的元素。
# print(list_var[9])  # 超出长度会报错 IndexError: list index out of range
# print(list_var[-10])  # 超出长度会报错 IndexError: list index out of range
# list_var[3] = 100  # 可以根据索引，直接修改list中对应位置的元素
# print(list_var)


# =====list常见操作：切片，选取list中的一连串元素
# list_var = [1, '2', 3, 4.0, 5, 6, 'seven', [8], '九']  # list举例
# print(list_var[3:8])  # list[a:b]，从第a个位置开始，一直到第b个位置之前的那些元素
# print(list_var[:4])  # list[:b]，从头开始，一直到第b个位置之前的那些元素
# print(list_var[3:])  # list[a:]，从第a个位置开始，一直到最后一个元素
# print(list_var[1:7:3])  # list[a:b:c]，每c个元素，选取其中的第一个


# =====list常见操作：两个list相加
# list_var1 = [1, '2', 3, 4.0, 5]
# list_var2 = [6, 'seven', [8], '九']
# print(list_var1 + list_var2)  # 两个list相加


# =====list常见操作：判断一个元素是否在list当中
# list_var = [1, '2', 3, 4.0, 5]
# print(1 in list_var)  # 判断1元素，是否在list_var中出现
# print(100 in list_var)  # 判断100元素，是否在list_var中出现


# =====list常见操作：len，max，min
# list_var = [1, 2, 3, 4, 5]
# print(len(list_var))  # list中元素的个数，或者说是list的长度
# print(len([]))  # 空list的长度是？
# print(max(list_var))  # 这个list中最大的元素，
# print(min(list_var))  # 最小的元素


# =====list常见操作：删除其中的一个元素
# list_var = [1, 2, 3, 4, 5]
# del list_var[0]  # 删除位置0的那个元素
# print(list_var)


# =====list常见操作：如何查找一个元素的在list中的位置
# list_var = [3, 5, 1, 2, 4]  # 如何才能知道1这个元素，在list中的位置是什么？
# 不知道的话，直接搜索


# =====list常见操作：append,在后方增加一个元素
# list_var = [1, '2', 3, 4.0, 5]
# list_var.append(6)
# print(list_var)
# list_var.append(['seven', [8], '九'])
# print(list_var)


# =====list常见操作：两个list合并
# list_var = [1, '2', 3, 4.0, 5]
# list_var.extend([6, 'seven', [8], '九'])
# print(list_var)


# =====list常见操作：逆序、排序、
# list_var = [3, 5, 1, 2, 4]
# list_var.reverse()
# print(list_var)
# list_var = [3, 5, 1, 2, 4]
# list_var.sort()
# print(list_var)
# list_var = [3, 5, 1, 2, 4]
# print(sorted(list_var))
# print(list_var)


# =====dict介绍
# 使用{}大括号就可以新建一个dict。
# dict_var = {}  # 这是一个空dict
# print(dict_var, type(dict_var))

# 具有一系列成对的对象。一个叫做key，一个叫做value。其中的元素(包括key和value)不需要是同类型
# dict_var = {'btc': '比特币',
#             'eth': '比特币',
#             'XRP': '比特币'}  # 其中'btc'、'eth'、'XRP'就是key，'比特币'、'以太坊'、'瑞波币'就是相对应的value。
# print(dict_var)

# 字典是无顺序，key不可重复
# print(dict_var[0])  # 因为没有顺序，所以dict_var[0]并不能取出第0个位置的元素，此处会报错。


# =====dict常见操作：根据key的值，取相应的value的值
# print(dict_var['bch'])  # 获取'sh600000'这个key对应的value
# print(dict_var.get('bch'))  # 效果同上


# =====dict常见操作：增加、修改一对key：value
# dict_var['bch'] = '比特现金'
# print(dict_var)
# dict_var['bch'] = '比特币现金'
# print(dict_var['bch'])


# =====dict常见操作：判断一个key是不是在dict里面
# print('bch' in dict_var)


# =====dict常见操作：输出一个dict中所有的key和value

# print(dict_var.keys())  # 输出所有的key
# print(dict_var.values())  # 输出所有的value


# =====字符串转义
# print('what is wrong')  # 如何输入what's wrong
# print('what\'s wrong\t')  # 使用\对特殊字符进行转义。转义也可以用于表达不可见字符，例如tab符号：\t。
# print('\\')  # 如果要表达\本身，也需要转义，写为\\。
# print(r'what\'s wrong')  # 在字符串的开始加r（Raw String），使得字符串中不发生转义。


# =====字符串常见操作：字符串相加，相乘
# symbol1 = 'btcusd'
# symbol2 = 'ethusd'
# print(symbol1 + ', ' + symbol2)  # 字符串可以直接相加
# print(symbol1 * 3)  # 字符串可以乘以整数
# print('*' * 30)


# =====字符串常见操作：startswith、endswith
# symbol = 'btcusd'
# print(symbol.startswith('btc'))  # 判断字符串是否是以'btc'开头
# print(symbol.startswith('b'))
# print(symbol.startswith('usd'))
# print(symbol.endswith('usd'))


# =====字符串常见操作：判断
# symbol = 'btcusd'
# print('btc' in symbol)  # 判断字符串中是否包含'btc'
# print('eth' in symbol)


# =====字符串常见操作：替换
# symbol = 'btcusd'
# print(symbol.replace('btc', 'eth'))  # 将字符串中的'btc'替换成'eth'
# print('ethusd, xrpusd'.replace('usd', 'btc'))  # 会替换所有的sh


# =====字符串常见操作：split
# symbol = 'btcusd, ethusd, xrpusd'
# print(symbol.split(', '))
# print(symbol.split(', ')[0])
# print(symbol.split('usd'))
# 逆操作
# symbol_list = ['btcusd', 'ethusd', 'xrpusd']
# print(', '.join(symbol_list))


# =====字符串常见操作：strip
# symbol = '  btcusd  '
# print(symbol)
# print(symbol.strip())  # 去除两边的空格


# =====字符串的选取：把字符串当做list
# symbol = 'btcusd'
# print(symbol[0])
# print(symbol[:3])
# print(symbol[3:])
# print(len(symbol))















# =====list常见操作：range函数
# range函数用于快速创建[0，1，2，3，4，5，6……]这样的list
# list_var = range(5)
# print(range(5))  # range(a)，对于[0，1，2，3……]这个数组，取前a个元素
# print(range(1, 5))  # range(a, b)，对于[0，1，2，3……]这个数组，取从第a个位置的元素开始，到第b个位置元素之前的那个元素
# print(range(1, 10, 3))  # range(a, b, c), 每c个元素，选取其中的一个

