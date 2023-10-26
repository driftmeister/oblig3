class leapYear:
    def __init__(self, year) -> None:
        self.year = int(year)

    def isLeapYear(self):
        if(self.year%4 == 0 and self.year>=1700):
            if (self.year%100 == 0):
                if (self.year%400 == 0):
                    return True
                else:
                    return False

            elif (self.year%400 == 0 and self.year%100 != 0):
                return False

            elif (self.year%4000==0):
                return False
            else:
                return True
        elif(self.year%4==0 and self.year<1700):
            return True
        else:
            return False
