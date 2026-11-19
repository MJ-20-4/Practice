affirmations = [
    "abundance",
    "love",
    "light",
    "joy",
    "peace",
    "happiness",
    "freedom",
    "success",
    "health",
    "wealth",
    "prosperity",
]

# print() syntax
print("you are abundance", "you are love", "you are light")

# f-string syntax
print(f"you are {affirmations[0]}")

# str.format() syntax
print("you are {}".format(affirmations[1]))

# join() syntax
print(", ".join(f"you are {word}" for word in affirmations))

# loop syntax
for word in affirmations:
    print("you are", word)

