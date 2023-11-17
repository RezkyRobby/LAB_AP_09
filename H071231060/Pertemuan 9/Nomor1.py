class Human:
    def __init__(self, nama, pos_x=0):
        self.nama = nama
        self.__posisi = pos_x
        self.kecepatan = ""

    def movement(self, arah):
        if arah == "L":
            self.__posisi -= 1
        elif arah == "R":
            self.__posisi += 1

    def setnama(self, nama):
        self.nama = nama

    def getnama(self):
        return self.nama

    def setposition(self, position):
        self.__posisi = position

    def getposition(self):
        return self.__posisi


class Hero(Human):
    def __init__(self, nama, power=15, health=400, armor=15, kecepatan=3, pos_x=0):
        super().__init__(nama, pos_x)
        self._power = power
        self._health = health
        self._armor = armor
        self._kecepatan = kecepatan

    def attack(self, target):
        target.sethealth(target.gethealth() - self._power)

    def setpower(self, power):
        self._power = power

    def getpower(self):
        return self._power

    def sethealth(self, health):
        self._health = health

    def gethealth(self):
        return self._health

    def setarmor(self, armor):
        self._armor = armor

    def getarmor(self):
        return self._armor

    def setkecepatan(self, kecepatan):
        self._kecepatan = kecepatan

    def getkecepatan(self):
        return self._kecepatan


class Warrior(Hero):
    def __init__(self, nama, pos_x=0):
        super().__init__(nama, power=26, armor=30, pos_x=pos_x)

    def special(self, target):
        self.setpower(32)
        self.setarmor(45)
        target.sethealth(target.gethealth() - self._power)


class Assassin(Hero):
    def __init__(self, nama, pos_x=0):
        super().__init__(nama, power=35, kecepatan=4, pos_x=pos_x)

    def special(self, target):
        self.setpower(42)
        self.setkecepatan(7)
        target.sethealth(target.gethealth() - self._power)


class Support(Hero):
    def __init__(self, nama, pos_x=0):
        super().__init__(nama, health=500, armor=8, kecepatan=4, pos_x=pos_x)

    def special(self, target):
        self.setkecepatan(6)
        target.sethealth(target.gethealth() + 150)



# Create hero objects
warrior = Warrior("Roby")
assassin = Assassin("Mufli")
support = Support("jar")

#sebelum
print("health (before)", warrior.gethealth())
assassin.attack(warrior)
#sesudah 
print("health (after)", warrior.gethealth())
print("-"*10)

#seblum 
print("warrior (health)", warrior.gethealth())
print("support (speed)", support.getkecepatan())

support.special(warrior)
print("warrior (health)", warrior.gethealth())
print("support (speed)", support.getkecepatan())