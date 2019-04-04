# 利用C4.5算法生成决策时，贷款申请样本数据表如下：
# ID 年龄 有工作 有自己的房子 信贷情况 类别
# 1  青年  否        否       一般     否
# 2  青年  否        否        好      否
# 3  青年  是        否        好      是
# 4  青年  是        是        一般    是
# 5  青年  否        否        一般    否
# 6  中年  否        否        一般    否
# 7  中年  否        否        好      否
# 8  中年  是        是        好      是
# 9  中年  否        是       非常好   是
# 10 老年  否        是       非常好   是
# 11 老年  否        是       非常好   是
# 12 老年  否        是       非常好   是
# 13 老年  是        否         好     是
# 14 老年  是        否       非常好   是
# 15 老年  否        否        一般    否

import numpy as np
# load table
loand_table=np.array([['青年','否','否','一般','否'],
                      ['青年','否','否','好','否'],
                      ['青年','是','否','好','是'],
                      ['青年','是','是','一般','是'],
                      ['青年','否','否','一般','否'],
                      ['中年','否','否','一般','否'],
                      ['中年','否','否','好','否'],
                      ['中年','是','是','好','是'],
                      ['中年','否','是','非常好','是'],
                      ['老年','否','是','非常好','是'],
                      ['老年','否','是','非常好','是'],
                      ['老年','否','是','非常好','是'],
                      ['老年','是','否','好','是'],
                      ['老年','是','否','非常好','是'],
                      ['老年','否','否','一般','否']])
# calculate the information increase rate of part table
def calculate_part_entry():
    row, col = loand_table.shape
    types = []
    for t in loand_table[:, [-1]]:
        types.append(t[0])
    print(types)
    type_diction = {}

    for type in types:
        if type not in type_diction.keys():
            type_diction[type] = 1
        else:
            type_diction[type] = type_diction[type] + 1

    the_whole_table__information_increase_rate = 0
    for key, value in type_diction.items():
        print(key)
        inc = -(value / row) * np.log2(value / row)
        the_whole_table__information_increase_rate = the_whole_table__information_increase_rate + inc

    print('the start information entropy is:' + the_whole_table__information_increase_rate)







