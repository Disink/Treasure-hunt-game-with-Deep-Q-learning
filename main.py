from game import Game
from Q_learning import QLearningTable as QLT
import os
import time

EPISODE = 500
INTERVAL = 0.01


def loop():
    for episode in range(EPISODE):
        while True:
            action = QL.choose_action(str(game.player_pos))
            observation = str(game.player_pos)
            game.move(action)
            observation_ = str(game.player_pos)
            game.show()

            event, reward = game.get_reward()

            QL.learn(observation, action, reward, observation_, event)

            print("Episode: {}".format(episode))

            time.sleep(INTERVAL)

            if event == "done":
                game.reset()
                break


if __name__ == "__main__":
    game = Game()
    game.buid_default_map()
    QL = QLT(actions=game.action_space)
    loop()
