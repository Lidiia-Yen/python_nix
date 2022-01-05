class TeamResult:
    def __init__(self, won_games, draw_games, loss_games, goals_scored, goals_missed):
        self.won = won_games
        self.draw = draw_games
        self.loss = loss_games
        self.scored = goals_scored
        self.missed = goals_missed

    def result(self):
        if self.scored > self.missed:
            self.won += 1
        elif self.scored < self.missed:
            self.loss += 1
        else:
            self.draw += 1

        return f'\nОбновленные результаты: выигранных игр {self.won}, ничьих {self.draw}, проигранных игр {self.loss}'

    def score(self):
        return f'\nЗаработанные клубом очки {(self.won * 3) + (self.draw * 1)}'

    def dif(self):
        return f'\nРазница забитых и пропущенных голов {self.scored - self.missed}'


class TeamResultChild(TeamResult):
    def games(self):
        TeamResult.result(self)
        return f'\nOбщее количество игр для команды {self.won + self.draw + self.loss}'


if __name__ == '__main__':
    t = TeamResult(2, 1, 0, 4, 2)
    print(f'\nИнстанс класса-родителя', t.result(), t.score(), t.dif())
    t_1 = TeamResultChild(3, 2, 1, 0, 0)
    print(f'\nИнстанс класса-ребенка', t_1.result(), t_1.score(), t_1.dif(), t_1.games())
