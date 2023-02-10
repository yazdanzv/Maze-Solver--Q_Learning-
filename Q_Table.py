import copy
from Episode_Generator import Episode_Generator

N = 10
M = 10
ALPHA = 1
GAMA = 0.5


class Q_Table(Episode_Generator):
    def __init__(self, dic_map: dict, num: int, episode_max_length):
        super().__init__(num, dic_map, episode_max_length)
        self.dic_map = dic_map
        self.q_table = {}
        self.policy_table = {}
        self.rewards = {'Block': -1000, 'Regular': -1, 'Visited': -2, 'Target': 10, 'Flag': 0.5}
        self.q_table_builder()
        self.seen_positions = []

    def q_table_builder(self):  # Checked
        per_action = [0] * (N * M)
        actions = ['U', 'D', 'L', 'R']
        for i in range(len(actions)):
            temp = copy.deepcopy(per_action)
            self.q_table[actions[i]] = temp

    def get_reward(self, position: str):  # Semi Checked
        count = 0
        if self.dic_map[position] == 'Block':
            count += self.rewards['Block']
        else:
            if position in self.seen_positions:
                count += self.rewards['Visited']
                if self.dic_map[position] == 'Flag':
                    count += self.rewards['Flag']
                elif self.dic_map[position] == 'Target':
                    count += self.rewards['Target']
            else:
                if self.dic_map[position] == 'Flag':
                    count += self.rewards['Flag']
                elif self.dic_map[position] == 'Target':
                    count += self.rewards['Target']
        count += self.rewards['Regular']
        return count

    def get_max_next_state(self, position):  # Semi Checked
        possible_next_states = self.get_possible_actions(position)
        next_positions = list(possible_next_states.keys())
        max = self.get_reward(next_positions[0])
        # print(next_positions[0])
        # print()
        # print(max)
        # print()
        for i in range(1, len(next_positions)):  # Semi Checked
            max_temp = self.get_reward(next_positions[i])
            # print(next_positions[i])
            # print()
            # print(max_temp)
            # print()
            if max < max_temp:
                max = max_temp
        return max

    def state_calculator(self, state: dict):  # Semi Checked
        position = list(state.keys())[0]
        action = state[position]
        position_int = int(position)
        # Q_Learning Formula
        self.q_table[action][position_int] = (1 - ALPHA) * self.q_table[action][position_int] + ALPHA * (
                    self.get_reward(position) + GAMA * self.get_max_next_state(position))
        self.seen_positions.append(position)

    def episode_calculator(self, episode: dict):  # Semi Checked
        state_turns = list(episode.keys())
        self.seen_positions = []
        for i in range(1, len(state_turns)):
            self.state_calculator(episode[i])

    def series_calculator(self, series):  # Semi Checked
        for episode in series:
            self.episode_calculator(episode)

    def policy_builder(self):
        for i in range(M * N):
            max = self.q_table[self.actions[0]][i]
            max_action = self.actions[0]
            for action in self.actions:
                if max < self.q_table[action][i]:
                    max = self.q_table[action][i]
                    max_action = action
            if i <= 9:
                state = f'0{i}'
            else:
                state = str(i)
            if not self.block_checker(state):
                self.policy_table[state] = max_action
            else:
                self.policy_table[state] = 'B'

