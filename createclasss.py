class rectangle :
    length = 0
    width = 0
    def setLW (self,length,width):
        self.length=length
        self.width=width
    def circumference(self):
        return 2*(self.length+self.width)
    def wholeArea(self):
        return self.length*self.width
    def __str__(self):
        return str()
    

R1= rectangle
keliling = R1.setLW(5,4)
print("keliling :",keliling )