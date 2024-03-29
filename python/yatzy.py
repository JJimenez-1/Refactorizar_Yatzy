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
        FOUR_KIND = 4
        lista = []
        for die in dice:
            if dice.count(die) >= FOUR_KIND:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue

        if lista == []:
            return 0
        else:
            return lista[-1] * FOUR_KIND

    @staticmethod
    def small_straight(*dice):
        SMALLEST = 1
        lista = []
        for die in dice:
            if dice.count(die) == SMALLEST:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue
            else:
                return 0

        if lista == []:
            return 0
        else:
            return 15

    @staticmethod
    def large_straight(*dice):
        LARGEST = 1
        lista = []
        for die in dice:
            if die == LARGEST:
                return 0
            if dice.count(die) == LARGEST:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue
            else:
                return 0

        if lista == []:
            return 0
        else:
            return 20

    @staticmethod
    def full_house(*dice):
        TWO_KIND = 2
        THREE_KIND = 3
        lista = []
        suma_num_lista = 0
        for die in dice:
            if dice.count(die) == TWO_KIND or dice.count(die) == THREE_KIND:
                if lista.count(die) == 0:
                    lista.append(die)
                else:
                    continue
            else:
                return 0

        if lista == []:
            return 0
        else:
            lista.sort()
            return (lista[0] * dice.count(lista[0])) + (lista[-1] * dice.count(lista[-1]))
