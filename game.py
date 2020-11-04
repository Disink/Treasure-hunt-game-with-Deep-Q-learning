import numpy as np
import random
import os

GAME_SIZE = 8
START_POS = [1,1]
END_POS = [GAME_SIZE - 1, GAME_SIZE - 1]


def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


class Game():
    def __init__(self):
        self.map_array = np.zeros((GAME_SIZE, GAME_SIZE))
        self.action_space = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.player_pos = []
        self.map_temp = []

    def buid_default_map(self):
        self.player_pos = list(START_POS)
        player_x, player_y = self.player_pos
        for x in range(GAME_SIZE):
            for y in range(GAME_SIZE):
                if y == 0 or y == GAME_SIZE - 1:
                    self.map_array[y][x] = 8
                else:
                    if x == 0:
                        self.map_array[y][0] = 8
                    elif x == GAME_SIZE - 1:
                        self.map_array[y][GAME_SIZE - 1] = 8
                    else:
                        self.map_array[y][x] = random.choice([0,0,0,0,8])

        self.map_array[player_y][player_x] = 1
        self.map_array[GAME_SIZE - 2][GAME_SIZE - 2] = 9
        self.map_temp = np.array(self.map_array)

    def reset(self):
        self.player_pos = list(START_POS)
        self.map_array = np.array(self.map_temp)

    def show(self):
        clear()
        for h in self.map_array:
            for w in h:
                if (w == 1):
                    print("{}".format("◆"), end="")
                elif (w == 8):
                    print("{}".format("■"), end="")
                elif (w == 9):
                    print("{}".format("●"), end="")
                elif (w == 99):
                    print("{}".format("※"), end="")
                else:
                    print("{}".format("□"), end="")
            print("\r")

    def get_reward(self):
        player_x, player_y = self.player_pos
        entity = self.map_array[player_y][player_x]
        if (entity == 9):
            return "done", 1
        elif (entity == 8):
            return "done", -1
        else:
            return "move", 0

    def move(self, action):
        player_x, player_y = self.player_pos

        if (action == "UP"):
            self.player_pos[0] = player_x 
            self.player_pos[1] = player_y -1

            if self.map_array[player_y - 1][player_x] == 0:
                self.map_array[player_y][player_x] = 0
                self.map_array[player_y - 1][player_x] = 1
            else:
                self.map_array[player_y][player_x] = 99

        elif (action == "DOWN"):
            self.player_pos[0] = player_x 
            self.player_pos[1] = player_y + 1

            if self.map_array[player_y + 1][player_x] == 0:
                self.map_array[player_y][player_x] = 0
                self.map_array[player_y + 1][player_x] = 1
            else:
                self.map_array[player_y][player_x] = 99

        elif (action == "LEFT"):
            self.player_pos[0] = player_x - 1
            self.player_pos[1] = player_y 

            if self.map_array[player_y][player_x - 1] == 0:
                self.map_array[player_y][player_x] = 0
                self.map_array[player_y][player_x - 1] = 1
            else:
                self.map_array[player_y][player_x] = 99

        elif (action == "RIGHT"):
            self.player_pos[0] = player_x + 1
            self.player_pos[1] = player_y

            if self.map_array[player_y][player_x + 1] == 0:
                self.map_array[player_y][player_x] = 0
                self.map_array[player_y][player_x + 1] = 1
            else:
                self.map_array[player_y][player_x] = 99
