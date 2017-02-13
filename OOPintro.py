#let's define a class
class Aditya():
    def __init__(self,life):
        print("Your class is initiated")
        self.life = life
  
    def addtolife(self):
        self.life += 1
        print(self.life)

    def subtractfrolife(self):
        self.life -= 1
        print(self.life)


s = Aditya(5)
s.addtolife()
s.subtractfrolife()
s.addtolife()
