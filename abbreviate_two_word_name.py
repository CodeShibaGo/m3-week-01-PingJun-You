''''''
'''
## 詳細說明

實現一個函數，該函數接受兩個單詞的名字，並返回它們的縮寫，縮寫應該是兩個單詞的首字母大寫並用句點分隔。
'''

def abbrev_name(name):
  words = name.split()
  first_letters = [word[0].upper() for word in words]  # 逐筆取出[0]，並upper()，最後存為list
  abbreviation = '.'.join(first_letters)  # 整合list內的元素為str，並以"."為分隔
  return abbreviation


# print(abbrev_name("Sam Harris"))
# print(abbrev_name("patrick feeney"))
