import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as citty_repository

country_repository.delete_all()

country_greece = Country("Greece", "Europe", True, True)
country_repository.save(country_greece)
country_japan = Country("Japan", "Asia", True)
country_repository.save(country_japan)

results = country_repository.select_all()
for country in results:
    print(country.__dict__)

selected_country = country_repository.select(country_greece.id)
print(selected_country)

pdb.set_trace()