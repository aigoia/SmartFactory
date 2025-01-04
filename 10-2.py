class Health:
    def __init__(self, name, hp):
        self._name = name
        self.__hp = 50
        self.hp = 100 if hp > 100 else 0 if hp < 0 else hp 

    def exercise(self, times=1):
        self.__hp = self.__hp + times if self.__hp + times < 100 else 100
        self.hp = self.hp + times if self.hp + times < 100 else 100
        print(f"{self._name} private hp {self.__hp}")
        print(f"{self._name} public hp {self.hp}")

    def drink_alcohol(self, times=1):
        self.__hp = self._hp - times if self.__hp + times < 1 else 1
        self.hp = self.hp - times if self.hp + times < 100 else 100
        print(f"{self._name} private hp {self.__hp}")
        print(f"{self._name} public hp {self.hp}")
        
test = Health("jone", 50)
test.exercise(4)
test.__hp = 0
test.hp = 0
test.exercise(4)
