''''''
'''
## 詳細說明

你需要寫一個函數，用於分類新的社交網絡成員。每位成員都有兩個屬性：年齡（整數）和貢獻度分數（浮點數）。為了分類成員，你的函數需要滿足以下條件：

1. 如果成員的年齡大於等於 55，且貢獻度分數大於 7，則分類為 "Senior"。
2. 如果成員的年齡小於 55，且貢獻度分數大於 7，則分類為 "Senior"。
3. 其他情況，分類為 "Open"。

你需要返回一個列表，列表中包含每位成員的分類。
'''



def categorize_new_member(data):
    categories=[]

    for member in data:
        age, score = member

        if(age>=55 and score>7) or (age<55 and score>7):
            categories.append('Senior')
        else:
            categories.append('Open')

    return categories

data = [(45, 12.5), (55, 9.0), (65, 8.0), (21, 11.5)]
category_member_list = categorize_new_member(data)
print(f"category_member_list:{category_member_list}")


data = [(58, 8.5), (80, 6.0), (40, 7.0)]
category_member_list = categorize_new_member(data)
print(f"category_member_list:{category_member_list}")

