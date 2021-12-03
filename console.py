import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as citty_repository

country_repository.delete_all()

country_greece = Country("Greece", "Europe", True, True)
country_repository.save(country_greece)

pdb.set_trace()