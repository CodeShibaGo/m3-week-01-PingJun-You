''''''
'''
## 詳細說明

你需要寫一個函數來計算一個字串中重複出現的字符數量。重複字符指的是在字串中出現超過一次的字符，而且函數不區分大小寫。函數需要返回重複字符的數量。

'''


def count_duplicates(text):
    text = text.lower()  # 函數不區分大小寫，全部轉會為小寫
    char_count = {}  # 使用dict的key, value
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    duplicate_count = 0
    # 把dict的key裡面的value，逐筆取出來判斷。
    for char, count in char_count.items():
        if count > 1:
            duplicate_count += 1

    return duplicate_count



# print(counting_duplicates("abcde"))
# print(counting_duplicates("aabbcde"))
# print(counting_duplicates("aabBcde"))
# print(counting_duplicates("indivisibility"))
# print(counting_duplicates("Indivisibilities"))
# print(counting_duplicates("aA11"))
# print(counting_duplicates("ABBA"))
