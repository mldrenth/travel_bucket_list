import unittest

from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country_1 = Country("Greece","Europe", True, True)
        self.country_2 = Country("Japan", "Asia", True)
        self.country_3 = Country("Australia","Australia",False, True, 3)
    
    def test_country_has_name(self):
        self.assertEqual("Greece", self.country_1.name)
    
    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country_1.continent)
    
    def test_country_has_visited_status(self):
        self.assertEqual(False, self.country_2.visited)
    
    def test_country_has_want_to_visit_status(self):
        self.assertEqual(True, self.country_2.want_to_visit)
    
    def test_country_can_set_id(self):
        self.assertEqual(3, self.country_3.id)
    
    def test_country_toggle_visited(self):
        self.country_2.toggle_visited_status()
        self.assertEqual(True, self.country_2.visited)
    
    def test_country__unmark_as_want_to_visit(self):
        self.country_2.toggle_want_to_visit_status()
        self.assertEqual(False, self.country_3.want_to_visit)
    
