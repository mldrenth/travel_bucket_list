import unittest
from models.city import City
from models.country import Country
from models.sight import Sight

class TestSight(unittest.TestCase):

    def setUp(self):
        self.country = Country("Greece", "Europe", True, True)
        self.city_1 = City("Thessaloniki", self.country, True, True ,1)
        self.sight = Sight("White Tower", "Landmark", self.city_1, True, True, 1)
        

    def  test_sight_has_name(self):
        self.assertEqual("White Tower", self.sight.name)
    
    def test_sight_has_city(self):
        self.assertEqual(self.city_1, self.sight.city)
    
    def test_sight_has_want_to_visit_status(self):
        self.assertEqual(True, self.sight.want_to_visit)
    
    def test_sight_has_visited_status(self):
        self.assertEqual(True, self.sight.visited)
    
    def test_sight_can_set_id(self):
        self.assertEqual(1, self.sight.id)
    
    def test_sight_mark_as__visited(self):
        self.sight.toggle_visited_status()
        self.assertEqual(False, self.sight.visited)
      
    def test_sight__mark_as_want_to_visit(self):
        self.sight.toggle_want_to_visit_status()
        self.assertEqual(False, self.sight.want_to_visit)