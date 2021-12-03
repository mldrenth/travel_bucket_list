class City:
    def __init__(self, name, country, want_to_visit, visited = False, id = None):
        self.name = name
        self.country = country
        self.want_to_visit = want_to_visit
        self.visited = visited
        self.id = id
    
    def change_visited_status(self,status):
        self.visited = status

    def change_want_to_visit_status(self, status):
        self.want_to_visit = status