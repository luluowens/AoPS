class Jar :

    def __init__(self, jar_size) :
        self.size = jar_size
        self.amount = 0

    def __str__(self) :
        answer = "a "
        answer += str(self.size) + "-liter jar with "
        answer += str(self.amount) + " liters of water"
        return answer

    def fill_jar(self) :
        self.amount = self.size

    def empty_jar(self) :
        self.amount = 0

    def pour(self, other_jar) :
        other_leftover = other_jar.size - other_jar.amount
        if self.amount <= other_leftover :
            other_jar.amount += self.amount
            self.amount = 0
        else :
            other_jar.amount = other_jar.size
            self.amount -= other_leftover

