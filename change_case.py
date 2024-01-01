''''''
'''
(改變大小寫)

## 詳細說明

這個題目要求你寫一個函式，能夠接受一個字串作為輸入，然後返回一個新的字串，其中所有的字母都被轉換成大寫或小寫，
具體的轉換方式由函式的參數決定。如果參數是 "upper"，則轉換成大寫，如果參數是 "lower"，則轉換成小寫。
'''


def change_case(input_str, case):
    if case=="upper":
        return input_str.upper()
    elif case=="lower":
        return input_str.lower()

# print(change_case("Hello World", "upper"))
