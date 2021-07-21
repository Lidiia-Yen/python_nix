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
    print('result=', t.result(), 'earned_points=', t.score(), 'goals_excluding_missing=', t.dif())
    t1 = TeamResultChild(3, 2, 1, 0, 0)
    print('result=', t1.result(), 'earned_points=', t1.score(), 'goals_excluding_missing=', t1.dif(), 'general_games=', t1.games())

