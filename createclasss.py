class rectangle :
    length = 0
    width = 0
    def setLongWide(self,length,width):
        self.length = length
        self.width = width
    def circumference(self):
        return 2*(self.length+self.width)
    def wholeArea(self):
        return self.length*self.width
    def __str__(self):
        return str(print("RECTANGLE\n""Long = ",self.length," cm", "\nWide = ",self.width," cm"))
    
R1 = rectangle()
long = int(input("Fill the long : "))
wide = int(input("Fill the wide : "))
R1.setLongWide(long,wide)
keliling = R1.circumference()
luas = R1.wholeArea()
keterangan = R1.__str__()

print("Hasil Operasionalnya :\n""keliling :",keliling, "\nLuas : ",luas )

