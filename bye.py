# Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, 
# such as Reykjavik is in Iceland. Give the parameter for the country a
# default value. Call your function for three different cities, at least one
# of which is not in the default country.

# Write a function called city_country() that takes in the name of 
# a city and its country. The function should return a string formatted
# like this: "Santiago, Chile" Call your function with at least three 
# city-country pairs, and print the value that’s returned.

def city_country(city , country):
    return(f"{city} , {country}")

print(city_country("Santiago", "Chille"))




# def describe_city(city , country= "England"):
#     print(f"The city of {city} is in the country {country}.")

# describe_city("Manchester")
# describe_city("London")
# describe_city("Paris","France")

