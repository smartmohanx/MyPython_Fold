'''
19.Wap on Overloading to Implement Addition operations with
different Parameters ex : add(int,int), add(float,int),
add(float,int,str);
'''
class Addition:
    def add(self,no1,no2,no3 = None):
            self.no1 = (no1)
            self.no2 = (no2)
            self.no3 = (no3)
            if self.no3 is not None:
                self.sum = (self.no1) + (self.no2) + float(self.no3)
                print(self.sum)
            else:
                self.sum = (self.no1) + (self.no2) 
                print(self.sum)     

print("WELCOME TO SMART-XTECH!")
print("Addition:")

obj = Addition()
obj.add(1,1)
obj.add(1,1,1)

