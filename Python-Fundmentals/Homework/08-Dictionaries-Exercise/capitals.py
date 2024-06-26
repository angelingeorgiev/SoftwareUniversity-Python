country_name = input().split(", ")
capital_cities = input().split(", ")

dictionary = {country_name[index]: capital_cities[index]
              for index in range(len(country_name))}

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
