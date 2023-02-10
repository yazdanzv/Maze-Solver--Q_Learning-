class Dic_Builder:
    def __init__(self, game_map: list):  # Checked
        self.game_map = game_map
        self.names = {'W': 'Way', 'B': 'Block', 'F': 'Flag', 'T': 'target', 'A': 'Agent'}
        self.dic_map = {}
        self.create()

    def create(self):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                self.dic_map[f'{i}{j}'] = self.names[self.game_map[i][j]]
