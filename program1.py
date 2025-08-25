import random

class SimpleReflexAgent:
    def __init__(self, grid, start_pos=(0, 0)):
        self.grid = grid
        self.pos = start_pos
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT", "CLEAN"]

    def percept(self):
        
        x, y = self.pos
        return self.grid[x][y]

    def rule(self, percept):
        
        if percept == "D":  
            return "CLEAN"
        else: 
            return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self, action):
        
        x, y = self.pos
        new_x, new_y = x, y

        if action == "UP": new_x -= 1
        elif action == "DOWN": new_x += 1
        elif action == "LEFT": new_y -= 1
        elif action == "RIGHT": new_y += 1

        
        if (0 <= new_x < len(self.grid) and 
            0 <= new_y < len(self.grid[0]) and 
            self.grid[new_x][new_y] != "O"):   
            self.pos = (new_x, new_y)

    def clean(self):
        x, y = self.pos
        if self.grid[x][y] == "D":
            self.grid[x][y] = "E"  
            print(f"Cleaned at {self.pos}")

    def step(self):
        
        percept = self.percept()
        action = self.rule(percept)

        if action == "CLEAN":
            self.clean()
        else:
            self.move(action)
            print(f"Moved {action} to {self.pos}")

grid = [
    ["E", "D", "O", "E"],
    ["E", "E", "D", "E"],
    ["O", "E", "E", "D"],
    ["E", "O", "E", "E"]
]

agent = SimpleReflexAgent(grid)

for _ in range(10):
    agent.step()
