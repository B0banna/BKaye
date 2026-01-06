print("Welcome to Mad Libs!")
adj = input("Enter an Adjective: ").lower()
noun = input("Enter a noun: ").lower()
place = input("Enter a place: ").capitalize()
verb = input("Enter a verb: ").lower()

text = f"One day, a {adj} cat decided to jump over a giant {noun}. Everyone in the town of {place} started to {verb} in excitement!"
print(text)