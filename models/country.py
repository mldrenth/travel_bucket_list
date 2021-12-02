class Country:
    def __init__(self, name, visited, id = None):
        self.name = name
        self.visited = visited
        self.id = id
    
    def change_visited_status(self, status):
        self.visited = status
