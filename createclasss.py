class rectangle :
    length = 0
    width = 0
    def __init__ (length,width):
        length = length
        width = width
    def circumference(length,width):
        return 2*(length+width)
    def wholeArea(length, width):
        return length*width
    def __str__(length,width):
        return str(print("RECTANGLE\n""Long = ",length, "\nWide = ",width))
    
R1= rectangle
long= R1.length
wide= R1.width
long = input("Fill the long :")
wide = input("Fill the wide :")

R1.__init__(long,wide)
keliling = R1.circumference(long,wide)
luas = R1.wholeArea(long,wide)
keterangan = R1.__str__(long,wide)
print("keliling :",keliling, "\nLuas : ",luas )

