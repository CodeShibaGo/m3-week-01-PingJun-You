''''''
'''
## 詳細說明

這個題目要求你寫一個函式，該函式接受一個包含字母的字串，然後返回一個新的字串，其中只包含原始字串中的大寫字母。請保持原始字母的相對順序。

'''

def find_capitals(word):
    capitals = [char for char in word if char.isupper()]
    return ''.join(capitals)


# ans = find_capitals("The Quick Brown Fox")
# print(ans)
#
# ans = find_capitals("Hello World")
# print(ans)
#
# ans = find_capitals("Python is Fun")
# print(ans)



