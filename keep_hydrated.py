''''''
'''
（保持水分充足！）

## 詳細說明

你需要寫一個函數，該函數接受一個表示時間的浮點數，並返回保持水分充足所需的水量，以毫升（ml）為單位。
你可以假設一小時需要喝1杯水，即200毫升。
'''

def litres(time):
    # 使用整數除法，向下取整數
    #  1cup/hr = 200cc/hr
    
    return int(time // 2)

