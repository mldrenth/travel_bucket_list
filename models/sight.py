class Sight:
    def __init__(self, name, category, city, visited, want_to_visit, id = None):
        self.name = name
        self.category = category
        self.city = city
        self.visited = visited
        self.want_to_visit = want_to_visit
        self.id = id
    
    def toggle_visited_status(self):
        self.visited = not self.visited
    
    def toggle_want_to_visit_status(self):
        self.want_to_visit = not self.want_to_visit
    
