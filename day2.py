import os, re

with open ("2.txt", "r") as puzzle:
  data = puzzle.read().splitlines()

ids = 0
power_sum = 0

red_limit = 12
green_limit = 13
blue_limit = 14

for line in data:
  is_valid = True
  min_amt = [0, 0, 0]
  
  # Structure of input
  # Game X: X [blue/red/green], ...;
  # Split string by : to get game ID
  # Split latter string to get shown cubes
  info = line.replace(" ", "")
  id_info, game_sets = info.split(":")
  
  # Game1, 3blue,4red;1red,2green,6blue;2green
  print(f"Game Info {id_info} / Sets Info {game_sets}\n===")
  
  sets = game_sets.split(";")
  for set_info in sets:
    shown = set_info.split(",")
    for value in shown:
      amount = int(re.sub('[A-Za-z]', "", value))
      color = re.sub('[0-9]', "", value)
      print(f"Color: {color}, Amount: {amount}")
      if color == "red":
        if amount > min_amt[0]: min_amt[0] = amount
        if amount > red_limit: 
          is_valid = False
          print(f"{amount} is larger than limit {red_limit}")
      elif color == "green":
        if amount > min_amt[1]: min_amt[1] = amount
        if amount > green_limit: 
          is_valid = False
          print(f"{amount} is larger than limit {green_limit}")
      elif color == "blue":
        if amount > min_amt[2]: min_amt[2] = amount
        if amount > blue_limit: 
          is_valid = False
          print(f"{amount} is larger than limit {blue_limit}")
  
  if is_valid:
    ids += int(id_info[4:])
  
  power_sum += min_amt[0] * min_amt[1] * min_amt[2]

print(f"Part 1: {ids}\nPart 2: {power_sum}")