class Yatzy:

    @staticmethod
    def chance(*dice):
        total = 0
        for number in dice:
            total += number
        return total

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = 4
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVES = 5
        return dice.count(FIVES) * FIVES

    @staticmethod
    def sixes(*dice):
        SIXES = 6
        return dice.count(SIXES) * SIXES

    @staticmethod
    def one_pair(*dice):
        ONE_PAIR = 2
        lista = []
        for die in dice:
            if dice.count(die) == ONE_PAIR:
                lista.append(die)

        if lista == []:
            return 0
        else:
            lista.sort()
            return lista[-1] * ONE_PAIR

    @staticmethod
    def two_pair(*dice):
        TWO_PAIR = 2
        lista = []
        for die in dice:
            if dice.count(die) >= TWO_PAIR:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue

        if lista == [] or len(lista) == 1:
            return 0
        else:
            return (lista[0] * TWO_PAIR) + (lista[-1] * TWO_PAIR)

    @staticmethod
    def three_of_a_kind(*dice):
        THREE_KIND = 3
        lista = []
        for die in dice:
            if dice.count(die) >= THREE_KIND:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue

        if lista == []:
            return 0
        else:
            return lista[-1] * THREE_KIND

    @staticmethod
    def four_of_a_kind(*dice):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
 

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
