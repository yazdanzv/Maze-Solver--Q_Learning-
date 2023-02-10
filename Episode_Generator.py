import random
import copy
from Dic_Map_Builder import Dic_Builder


class Episode_Generator:
    def __init__(self, num: int, dic_map, episode_max_length):
        self.dic_map = dic_map
        self.num = num
        self.actions = ['U', 'D', 'R', 'L']
        self.episode_max_length = episode_max_length

    def block_checker(self, state):  # Checked
        if self.dic_map[state] != 'Block':
            return False
        else:
            return True

    def random_picker(self):  # Checked
        state = ""
        flag = True
        while flag:
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            state = str(n1) + str(n2)
            flag = self.block_checker(state)
        return state

    def get_possible_actions(self, state: str):  # Checked
        i = int(state[0])
        j = int(state[1])
        i_new = copy.deepcopy(i)
        j_new = copy.deepcopy(j)
        possible_states = {}
        actions = copy.deepcopy(self.actions)
        while len(actions) != 0:
            action = random.choice(actions)
            new_state = copy.deepcopy(state)
            if action == 'U' and i > 0:
                state_up = str(int(state[0])-1)+state[1]
                if not self.block_checker(state_up):
                    i_new -= 1
                    possible_states[state_up] = action
            elif action == 'D' and i < 9:
                state_down = str(int(state[0])+1)+state[1]
                if not self.block_checker(state_down):
                    i_new += 1
                    possible_states[state_down] = action
            elif action == 'L' and j > 0:
                state_left = state[0] + str(int(state[1])-1)
                if not self.block_checker(state_left):
                    j_new -= 1
                    possible_states[state_left] = action
            elif action == 'R' and j < 9:
                state_right = state[0] + str(int(state[1])+1)
                if not self.block_checker(state_right):
                    j_new += 1
                    possible_states[state_right] = action
            actions.remove(action)
        if not bool(possible_states):
            possible_states = None
        return possible_states

    def episode_generator(self):  # Checked
        state = self.random_picker()
        episode = {0: {state: None}}  # A dict of states with key that shows they turns
        for i in range(1, self.episode_max_length):
            possible_next_states: dict = self.get_possible_actions(state)
            if bool(possible_next_states):
                next_state = random.choice(list(possible_next_states.keys()))
                next_action = possible_next_states[next_state]
                episode[i] = {next_state: next_action}
                state = next_state
            else:
                break
        return episode

    def series_generator(self):  # Checked
        episodes = []
        for i in range(self.num):
            episode = self.episode_generator()
            episodes.append(episode)
        return episodes

