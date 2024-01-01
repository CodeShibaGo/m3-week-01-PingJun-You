''''''

'''
(珍妮的秘密訊息)

## 題目說明

珍妮(Jenny)想要寫一個函數，根據給定的名字，回傳一條秘密訊息。如果名字是 "Johnny"，訊息應該是 "Hello, my love!"，其他名字的訊息則應該是 "Hello, {name}!"，其中 `{name}` 會替換為實際的名字。

例如，如果輸入的名字是 "Bob"，則訊息應該是 "Hello, Bob!"。

'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
