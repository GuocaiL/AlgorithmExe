'''
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。

案例:
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

注意事项:
输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
'''

import itertools
class Solution:
    def readBinaryWatch(self, num: int):
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        list3 = []
        if num != 0:
            for i in itertools.combinations(list1, num):
                hour = 0
                munite = 0
                for j in i:
                    if j <= 3:
                        hour += list2[j]
                    else:
                        munite += list2[j]
                # if munite==60:
                #     munite-=60
                #     hour+=1
                if hour < 12 and munite < 60:
                    if munite == 0:
                        list3.append(str(hour) + ':' + '00')
                    elif munite >= 10:
                        list3.append(str(hour) + ':' + str(munite))
                    else:
                        list3.append(str(hour) + ':0' + str(munite))

        else:
            list3.append("0:00")
        return list3

'''
执行用时 : 60 ms, 在Binary Watch的Python3提交中击败了49.05% 的用户
内存消耗 : 13 MB, 在Binary Watch的Python3提交中击败了87.76% 的用户
'''

