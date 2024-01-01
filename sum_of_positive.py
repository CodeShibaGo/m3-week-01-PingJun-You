''''''

'''
(正數之和)

## 詳細說明

這個題目要求你寫一個函式，該函式接受一個整數陣列作為輸入，然後返回陣列中所有正數的總和。
'''

def positive_sum(arr):
    total = 0
    for num in arr:
        # 如果是正數，就加入總和
        if num > 0:
            total += num
    return total

