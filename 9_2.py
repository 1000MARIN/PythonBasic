# __init__

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damege = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damege))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#tank2 = Unit("탱크2")