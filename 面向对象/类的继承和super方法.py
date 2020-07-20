# 调用类的__mro__查看该类的继承顺序 method resolution order
# super函数的语法为：super(type, instance) OR super(type, subtype)
# super通常用来调用父类中的方法，其查找顺序为继承顺序MRO

class Creature:
    def speak(self):
        print('生物')

class Aquatic(Creature):
    def speak(self):
        super().speak()
        print('水栖生物')
    
class Terrestrial(Creature):
    def speak(self):
        super().speak()
        print('陆栖生物')
    
class Frog(Terrestrial, Aquatic):
    def speak(self):
        super(Frog, self).speak()
        print('青蛙')
    
print(Frog.__mro__)
hama = Frog()
hama.speak()