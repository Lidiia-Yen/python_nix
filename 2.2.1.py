class TeamResult:
    def __init__(self, one, two, three, four, five):
        self.win = one
        self.draw = two
        self.loss = three
        self.scored = four
        self.missed = five

    def result(self):
        return self.scored, self.missed

    def score(self):
        return (self.win * 3) + (self.draw * 1)

    def dif(self):
        return self.scored - self.missed


class TeamResultChild(TeamResult):
    def games(self):
        return self.win + self.draw + self.loss


if __name__ == '__main__':
    t = TeamResult(2, 1, 0, 4, 2)
    print(t.result(), t.score(), t.dif())
    t1 = TeamResultChild(3, 2, 1, 0, 0)
    print(t1.result(), t1.score(), t1.dif(), t1.games())

