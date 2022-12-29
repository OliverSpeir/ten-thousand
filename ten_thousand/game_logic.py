from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(number):
        return tuple(randint(1, 6) for x in range(0, number))

    @staticmethod
    def calculate_score(roll):
        dice = Counter(roll).most_common()
        score = 0

        if not dice:
            return score

        # 3,4,5,and 6 of a kind
        if (dice[0][1]) >= 3:
            if dice[0][0] != 1:
                score += dice[0][0] * 100 * (dice[0][1] - 2)
                if dice[0][1] == 6:
                    return score
                dice = dice[1:]
            else:
                score += 1000 * (dice[0][1] - 2)
                if dice[0][1] == 6:
                    return score
                dice = dice[1:]

        # 2 3 of a kinds
        if len(dice) == 1:
            if dice[0][1] == 3:
                if dice[0][0] != 1:
                    score += dice[0][0] * 100
                    return score
                else:
                    score += 1000
                    return score

        # straight
        if len(dice) == 6:
            score += 1500
            return score

        # three pair
        if len(dice) == 3:
            if dice[2][1] == 2:
                score += 1500
                return score

        # single 5 or single 1
        else:
            for x in dice:
                if x[0] == 5:
                    score += x[1] * 50
            for x in dice:
                if x[0] == 1:
                    score += x[1] * 100
        print("Total Score", score)
        return score


