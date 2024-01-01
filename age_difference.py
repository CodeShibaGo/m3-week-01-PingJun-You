''''''
'''
(找到家庭成員之間的最大和最小年齡差)

給定一個家庭成員的年齡清單，你需要找出家庭成員中最年輕和最年長的成員之間的年齡差。你將會得到一個包含多個正整數的清單，
其中每個整數代表一個家庭成員的年齡。你需要寫一個函數來計算並返回最年長成員和最年輕成員的年齡差。
'''


def age_difference(ages):

    max_age = max(ages)
    min_age = min(ages)
    return max_age-min_age

# print(age_difference([18, 25, 50, 35, 40]))
# print(age_difference([30, 20, 25, 40, 45, 50]))
# print(age_difference([10, 5, 8, 20, 15, 25]))



