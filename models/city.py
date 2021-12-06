class City:
    def __init__(self, name, country, want_to_visit, visited = False, id = None):
        self.name = name
        self.country = country
        self.want_to_visit = want_to_visit
        self.visited = visited
        self.id = id
    
    def toggle_visited_status(self):
        self.visited = not self.visited
    
    def toggle_want_to_visit_status(self):
        self.want_to_visit = not self.want_to_visit