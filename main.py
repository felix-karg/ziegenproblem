from random import randint

rounds = int(input("Wie viele Runden soll gespielt werden? "))

wins_with_change = 0
wins_without_change = 0

# Runden mit Wechsel
for n in range(rounds):
    win_door = randint(1, 3)
    guess = randint(1, 3)
    goat_door = randint(1, 3)
    while goat_door == guess or goat_door == win_door:
        goat_door = randint(1, 3)

    # Tür wechseln
    for m in range(1, 4):
        if m != goat_door and m != guess:
            new_guess = m
            break

    # Gewinn prüfen
    if new_guess == win_door:
        wins_with_change += 1

# Runden ohne Wechsel
for n in range(rounds):
    win_door = randint(1, 3)
    guess = randint(1, 3)
    goat_door = randint(1, 3)
    while goat_door == guess or goat_door == win_door:
        goat_door = randint(1, 3)

    # Gewinn prüfen
    if new_guess == win_door:
        wins_without_change += 1

probability_with_change = round(wins_with_change / rounds, 2)
probability_without_change = round(wins_without_change / rounds, 2)

print(f"Gewinnwahrscheinlichkeit mit Wechseln: {probability_with_change}%")
print(f"Gewinnwahrscheinlichkeit ohne Wechseln: {probability_without_change}%")
