from Dic_Map_Builder import Dic_Builder
from Episode_Generator import Episode_Generator
from Q_Table import Q_Table
from GUI import GUI



NUM = 10000
EPISODE_LENGTH = 20
MAP = [['A', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'F', 'W', 'B', 'W', 'W', 'W', 'W'],
       ['F', 'W', 'W', 'W', 'W', 'B', 'F', 'W', 'W', 'W'],
       ['B', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'W', 'W'], ['W', 'F', 'B', 'W', 'B', 'F', 'B', 'B', 'B', 'W'],
       ['W', 'W', 'B', 'W', 'B', 'W', 'W', 'W', 'W', 'W'],
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'F', 'W', 'W', 'W', 'W', 'B', 'B', 'B', 'B'],
       ['W', 'B', 'B', 'B', 'B', 'B', 'W', 'W', 'W', 'W'],
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'F', 'T']]


dic_object = Dic_Builder(MAP)
dic_map = dic_object.dic_map
episode_object = Episode_Generator(NUM, dic_map, EPISODE_LENGTH)
series = episode_object.series_generator()
q_table_object = Q_Table(dic_map, NUM, EPISODE_LENGTH)
q_table_object.series_calculator(series)
q_table_object.policy_builder()
print(q_table_object.policy_table)
print(q_table_object.q_table)
gui_object = GUI(q_table_object.policy_table)

