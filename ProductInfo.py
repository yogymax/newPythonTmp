

'''

 id -- 1 - 100
 Name - Caps--  -- name digit
 price -- <1000 = 1000

'''


class Product:

    def __init__(self,id):
        self.set_product(id)
        self.set_product(id)

    def get_productId(self):
        return self._productId

    def set_productId(self,id):
        if id > 0:
            self._productId = id
        else:
            self._productId = 0

    def __str__(self):
        return 'ProductId : {}'.format(self._productId)

    productId = property(get_productId,set_productId)
    productName = property(get_productId, set_productId)

p1 = Product(-10) # -- setter
p1.set_product(-100) #--- property
print(p1)