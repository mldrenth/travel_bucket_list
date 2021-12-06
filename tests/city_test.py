import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country("Greece", "Europe", True, True)
        self.city_1 = City("Thessaloniki", self.country, True, True ,1)
        self.city_2 = City("Patras", self.country, True)
        self.city_3 = City("Athens",self.country, False)
    
    def  test_city_has_name(self):
        self.assertEqual("Thessaloniki", self.city_1.name)
    
    def test_city_has_country(self):
        self.assertEqual(self.country, self.city_1.country)
    
    def test_city_has_want_to_visit_status(self):
        self.assertEqual(True, self.city_2.want_to_visit)
    
    def test_city_has_visited_status(self):
        self.assertEqual(False, self.city_2.visited)
    
    def test_city_can_set_id(self):
        self.assertEqual(1, self.city_1.id)
    
    def test_city_mark_as__visited(self):
        self.city_2.toggle_visited_status()
        self.assertEqual(True, self.city_2.visited)
      
    def test_city__mark_as_want_to_visit(self):
        self.city_3.toggle_want_to_visit_status()
        self.assertEqual(True, self.city_3.want_to_visit)
    
