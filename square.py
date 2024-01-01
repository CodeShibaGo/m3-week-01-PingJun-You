''''''
'''
## 詳細說明

給定一個正整數，你需要判斷它是否是平方數。如果是平方數，則返回True，否則返回False。平方數是某個整數的平方，例如1、4、9、16等。
'''

def is_square(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

# is_square(1)