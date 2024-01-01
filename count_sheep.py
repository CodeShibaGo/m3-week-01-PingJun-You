''''''
'''
(數羊)
## 詳細說明

給定一個布林值的清單，其中True表示羊在睡覺，False表示羊醒著。你的任務是計算清單中有多少只羊在睡覺（True的數量）。返回睡覺的羊的數量。
'''

def count_sheep(sheep):
    count = 0
    for sleeping in sheep:
        if sleeping:
            count+=1
    return count

