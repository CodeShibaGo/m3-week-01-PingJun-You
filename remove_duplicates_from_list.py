''''''
'''
(從列表中移除重複項)


## 詳細說明

這個題目要求你寫一個函式，該函式接受一個列表作為輸入，然後返回一個新列表，其中移除了原列表中的重複項。新列表應該保留原始順序。
'''

def distinct(seq):
    new_list=[]

    for value in seq:
        if value not in new_list:
            new_list.append(value)

    return new_list


# print(distinct([1, 2, 2, 3, 4, 4, 5]))