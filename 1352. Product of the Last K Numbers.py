#简化的点在于：①：如果乘的数里有0直接就是0
#②：可以构建一个累乘数组，这样就可以直接只访问一个或几个值而不用一个个重新乘起来
class ProductOfNumbers:
    def __init__(self):
        self.product_accumulate = []
        self.product=1
        

    def add(self, num: int) -> None:
        if num != 0 :
            self.product *= num
            self.product_accumulate.append(self.product)
        else:
            self.product = 1
            self.product_accumulate=[]
    def getProduct(self, k: int) -> int:
        if k > len(self.product_accumulate): #被0清过了，例如30254返回后4个乘积，但此时product_accumulate只有3个数
            return 0 
        elif k == len(self.product_accumulate):
            return self.product_accumulate[-1]
        else: #k < len(self.product_accumulate) 例如30254返回后两个乘积
            return int(self.product_accumulate[-1] / self.product_accumulate[-1-k])





        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
