import numpy as np
from PIL import Image

class Ant:
    def __init__(self):
        self.size = 1024
        self.position = [512, 512]
        self.direction = 0   # 'up': 0, 'right': 1, 'down': 2, 'left': 3
        self.desk = np.zeros([self.size,self.size])
        self.track = np.zeros([self.size,self.size])

    def is_direction_correct(self):
        if self.direction == -1:
            self.direction = 3
        elif self.direction == 4:
            self.direction = 0

    def make_move(self):
        match self.direction:
            case 0:
                self.position[0] -= 1
            case 1:
                self.position[1] += 1
            case 2:
                self.position[0] += 1
            case 3:
                self.position[1] -= 1


    def if_white_cell(self):
        self.direction +=1
        self.is_direction_correct()
        self.desk[self.position[0]][self.position[1]] = 1
        self.track[self.position[0]][self.position[1]] = 1
        self.make_move()

    def if_black_cell(self):
        self.direction -= 1
        self.is_direction_correct()
        self.desk[self.position[0]][self.position[1]] = 0
        self.track[self.position[0]][self.position[1]] = 1
        self.make_move()

    def game(self):
        while self.position[0] not in [0, self.size-1] and self.position[1] not in [0, self.size-1]:
            if self.desk[self.position[0]][self.position[1]] == 0:
                self.if_white_cell()
            else:
                self.if_black_cell()

    def get_black_cells_sum(self):
        return self.desk.sum()

    def get_track(self):
        return self.track

    def get_desk(self):
        return self.desk

    def save_track(self):
        image = Image.fromarray(((np.ones([self.size,self.size]) - self.get_track()) * 255).astype(np.uint8), mode='L')

        image.save('output.bmp')

a = Ant()
a.game()
print(a.get_black_cells_sum())
a.save_track()
