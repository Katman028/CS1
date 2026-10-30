levels = [1,2,3,4,5]
coins =[5,8,3,10,7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

print("=====Platform Adventure=====")
for level in levels:
    print("Level:", level)
    print("coins:", coins[level-1])
    print("enemies:", enemies[level-1])
    print("power_ups:", power_ups[level-1])
    print("\n")


print("=====Player Information=====")
player_name = "Hero"
lives = 3
score = 0
total_coins = 0
print("Player Name:", player_name)
print("Lives:", lives)
print("Total coins:", total_coins)
print("\n")



print("=====Level Scores=====")
level_scores = []
for level in levels:
    level_scores.append((coins[level-1]*10) - (enemies[level-1]*5))
    if power_ups[level-1] == "Star":
        level_scores[level-1] += 25
    print(f"Level {level}: {level_scores[level-1]}")
print("\n")

print("=====Adventure Actions=====")
actions = [0, 1, 0, 2, 1]
action_results = []

for i in range(0,5):
    if actions[i] == 0:
        action_results.append("collect coins")
    elif actions[i] == 1:
        action_results.append("Fight enemies")
    elif actions[i] == 2:
        action_results.append("Use Power-up")

for action_result in action_results:
    print(action_result)
print("\n")

print("=====Life history=====")

life_history = []
lives = 3

for i in range(0,5):
    if enemies[i] >= 4 and power_ups[i] != "Star":
        lives -= 1
        life_history.append(lives)
    else:
        life_history.append(lives)
for i in range (0,5):
    print(f"After level {i+1}: {life_history[i]}")
print("\n")


print("=====Coin Collection=====")
bonus_coin_levels = [coin for coin in coins if coin >= 7]
total_coins = 0
for coin in coins:
    total_coins += coin
print(f"Total coins: {total_coins}")
print(f"Level with 7 or more coins: {bonus_coin_levels}")
print("\n")

print("=====Power-Up Inventory=====")
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
print(f"Starting inventory: {inventory}")
print(f"Used Powerups: {used_powerups}")
inventory.pop(0)
inventory.pop(0)
print(f"remaining powerups: {inventory}")
print("\n")

print("=====Level Analysis=====")
total_coins = 0
for coin in coins:
    total_coins += coin
print(f"Total coins: {total_coins}")

most_coins = 0
least_coins = 100
for coin in coins:
    if coin > most_coins:
        most_coins = coin

print(f"Most coins: {most_coins}")
for coin in coins:
    if coin < least_coins:
        least_coins = coin
print(f"Least coins: {least_coins}")

average_coins = total_coins / len(coins)
print(f"Average coins: {average_coins}")

total_enemies = 0
for enemy in enemies:
    total_enemies += enemy
print(f"Total enemies: {total_enemies}")

max_enemies = 0
for enemy in enemies:
    if enemy > max_enemies:
        max_enemies = enemy
print(f"Max enemies: {max_enemies}")
print("\n")

print("=====High Scores=====")
high_scores = [score for score in level_scores if score >= 50]
print(f"High Scores: {high_scores}")
print("\n")

print("=====score history=====")
score_history = []
current_score = 0
for i in range(0,len(level_scores)):
    current_score += level_scores[i]
    score_history.append(current_score)
    print(f"after level {score}: {current_score}")
print(f"first two scores: {score_history[0:2]}")
print(f"last two scores: {score_history[-2:]}")
print("\n")

print("=====final status=====")
if lives == 0:
    print("game over")
elif current_score >= 250:
    print("Adventure champion")
elif current_score >= 150:
    print("great adventure")
else:
    print("keep practicing")
