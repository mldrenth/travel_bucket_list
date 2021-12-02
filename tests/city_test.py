import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country("Greece", True)
        self.city_1 = City("Thessaloniki", self.country, True ,1)
        self.city_2 = City("Patras", self.country,)
    
    def  test_city_has_name(self):
        self.assertEqual("Thessaloniki", self.city_1.name)
    
    def test_city_has_country(self):
        self.assertEqual(self.country, self.city_1.country)
    
    def test_city_has_visited_status(self):
        self.assertEqual(False, self.city_2.visited)
    
    def test_city_can_set_id(self):
        self.assertEqual(1, self.city_1.id)
    
    def test_city_mark_as__visited(self):
        self.city_2.change_visited_status(True)
        self.assertEqual(True, self.city_2.visited)
    
    def test_city_mark_as_not_visited(self):
        self.city_1.change_visited_status(False)
        self.assertEqual(False, self.city_1.visited)
