import pdb
from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

city_repository.delete_all()
country_repository.delete_all()
sight_repository.delete_all()

country_greece = Country("Greece", "Europe", True, True)
country_repository.save(country_greece)
country_japan = Country("Japan", "Asia", True)
country_repository.save(country_japan)
country_china = Country("China", "Asia", True, False, country_japan.id)

city_thessaloniki = City("Thessaloniki", country_greece, True, True)
city_repository.save(city_thessaloniki)
city_tokyo = City("Tokyo", country_japan, True, False)
city_repository.save(city_tokyo)

sight_white_tower = Sight ("White Tower", "Landmark", city_thessaloniki, False, True)
sight_repository.save(sight_white_tower)

results = country_repository.select_all()
for country in results:
    print(country.__dict__)

selected_country = country_repository.select(country_greece.id)
print(selected_country)

results_cities = city_repository.select_all()
for city in results_cities:
    print(city.__dict__)

selected_city = city_repository.select(city_thessaloniki.id)
print (selected_city)

results_sights = sight_repository.select_all()
for sight in results_sights:
    print(sight.__dict__)

selected_sight = sight_repository.select(sight_white_tower.id)
print (selected_sight)

pdb.set_trace()