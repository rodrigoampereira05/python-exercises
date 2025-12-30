countries = ["Portugal", "Spain", "Germany", "Ireland","France"]

print(countries)
print(countries[0])
print(countries[-1])

add_country = input("Add a country: ")
countries.append(add_country)
print(countries)

remove_country = input("Remove 'France': ")
countries.remove(remove_country)
print(countries)

print(len(countries))
