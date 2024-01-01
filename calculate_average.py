''''''
'''
## 詳細說明

這個題目要求你寫一個函式，該函式接受一個整數列表作為輸入，然後計算這個列表中所有數字的平均值，並返回平均值。
'''

def calculate_average(nums):
    total_sum = sum(nums)  #計算總和
    average = total_sum / len(nums)  # 計算平均值
    return average


# calculate_average([10, 20, 30, 40, 50])

