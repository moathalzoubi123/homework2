users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty 
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even nnnnnn
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers nnnnn
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy" nnnnnn
# 10. Add another person to the users dictionary 



print(users["Jonathan"]["twitter"]) 

print(users["Erik"]["home_town"])

print(users["Erik"]["lottery_numbers"])

print(users["Avril"]["pets"][0]["species"]) 

users["Erik"]["lottery_numbers"].sort()

print(users["Erik"]["lottery_numbers"][0])

print(min(users["Erik"]["lottery_numbers"]))


# users["Erik"][("lottery_numbers")]

# users.update()

numbers = users["Avril"]["lottery_numbers"]
even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)



users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"]) 


users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"]) 

# q = int({
#   "name" : "fluffy",
#   "species": "dog"
#   }

# users(["Erik"]["pets"]).append(q)

# users.update["Erik"]["pets"]({
#   "name" : "fluffy",
#   "species": "dog"
#   }) 

new_pets= {
  "name" : "fluffy",
  "species": "dog"}
users["Erik"]["pets"].append(new_pets)



users.update({"moath": {
    "twitter": "moath123",
    "lottery_numbers": [129, 145, 33, 3, 9, 245],
    "home_town": "Amman",
    "pets": [
      {
        "name": "shaqra",
        "species": "cat"
      }
    ]
  }}) 

print(users) 

print(users["moath"]) 