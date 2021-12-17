import copy
import random


class Hat:
    def __init__(self, **kwarg):
        contents = []
        for key in kwarg.keys():
            for n in range(kwarg[key]):
                contents.append(key)
        self.contents = contents

    def draw(self, number):
        contents = self.contents
        if number >= len(contents):
            return contents

        s = []

        for n in range(number):
            len_contents = len(contents)
            index = random.randrange(len_contents)
            ball = contents[index]
            s.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        # update contents
        self.contents = contents
        return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_num = 0
    for n in range(num_experiments):
        example = copy.copy(hat)
        s = example.draw(num_balls_drawn)
        correct = True
        for key in expected_balls.keys():
            if s.count(key) < expected_balls[key]:
                correct = False
                break
        if correct:
            count_num += 1

    return count_num / num_experiments