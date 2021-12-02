import unittest

from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country_1 = Country("Greece", True)
        self.country_2 = Country("Japan", False)
        self.country_3 = Country("Australia", True, 3)
    
    def test_country_has_name(self):
        self.assertEqual("Greece", self.country_1.name)
    
    def test_country_has_visited(self):
        self.assertEqual(False, self.country_2.visited)
    
    def test_country_can_set_id(self):
        self.assertEqual(3, self.country_3.id)
    
    def test_country_mark_as__visited(self):
        self.country_2.change_visited_status(True)
        self.assertEqual(True, self.country_2.visited)
    
    def test_country_mark_as__not_visited(self):
        self.country_1.change_visited_status(False)
        self.assertEqual(False, self.country_1.visited)
    
