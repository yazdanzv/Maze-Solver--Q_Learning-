from Dic_Map_Builder import Dic_Builder
from Episode_Generator import Episode_Generator
from Q_Table import Q_Table
from GUI import GUI

MAP = [['A', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'F', 'W', 'B', 'W', 'W', 'W', 'W'],
       ['F', 'W', 'W', 'W', 'W', 'B', 'F', 'W', 'W', 'W'],
       ['B', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'W', 'W'], ['W', 'F', 'B', 'W', 'B', 'F', 'B', 'B', 'B', 'W'],
       ['W', 'W', 'B', 'W', 'B', 'W', 'W', 'W', 'W', 'W'],
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'F', 'W', 'W', 'W', 'W', 'B', 'B', 'B', 'B'],
       ['W', 'B', 'B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'F', 'T']]

a = Dic_Builder(MAP)
# print(a.dic_map)
b = Episode_Generator(100, a.dic_map, 10)
c = b.random_picker()
print(c)
print(b.block_checker(c))
print(b.get_possible_actions('00'))
print(b.episode_generator())
d = b.series_generator()
# print(d)
# print(len(d))
# print()
# print()
e = Q_Table(a.dic_map, 100, 10)
print(e.get_max_next_state('10'))
print('answer')
print()
# e.state_calculator({'10': 'D'})
# episode = b.episode_generator()
# print('Episode')
# print(episode)
# e.episode_calculator(episode)
series = e.series_generator()
e.series_calculator(series)
e.policy_builder()
print(e.policy_table)
# e.seen_positions = []
# f = e.get_reward('10')
# s = e.get_max_next_state('10')
print(e.q_table)
g = GUI(e.policy_table)
