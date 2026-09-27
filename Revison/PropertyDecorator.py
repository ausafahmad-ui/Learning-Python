class Samsung:
    def __init__(self,MobilePrice):
        self._MobilePrice=MobilePrice

    @property
    def MobilePrice(self):
        return self._MobilePrice
    @MobilePrice.setter
    def MobilePrice(self,value):
        if value<0:
            print("price cant be negative")
        else:
            self.MobilePrice=value
s=Samsung(1000)
s.MobilePrice=-9
print(s.MobilePrice)              