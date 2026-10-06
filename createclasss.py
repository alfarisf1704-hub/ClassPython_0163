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
    def __str__(self):
        return str()
    

R1= rectangle
R1.__init__(5,4)
keliling = R1.circumference(5,4)
luas = R1.wholeArea(5,4)
print("keliling :",keliling, "\nLuas : ",luas )