import os, re

data = ""
output = 0
output_2 = 0
value_dict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

with open ("1.txt", "r") as puzzle:
  data = puzzle.read().splitlines()

for line in data:
  puz_input = re.sub('[^\d.-]', '', line);
  value = 0
  
  if len(puz_input) == 1:
    value = int(puz_input + puz_input)
  else:
    value = int(puz_input[0] + puz_input[len(puz_input) - 1])
  
  output += int(value)
  
  # Second Star solution
  length = len(line)
  pos = 0
  new_input = ""
  value = 0
  
  for letter in line:
    for key in value_dict:
      if pos + len(key) > length:
        pass
        #print("Out of Bounds")
      else:
        key_length = len(key) + pos
        if key == line[pos:key_length]:
          new_input += str(value_dict[key])
    if letter.isnumeric():
      new_input += str(letter)
    pos += 1
  
  print(f"Converted value of {line} is {new_input}")
  
  #sorted_input = re.sub('[^\d.-]', '', new_input);
  sorted_input = new_input
  print(f"-{sorted_input}")
  
  if len(sorted_input) == 1:
    value = int(sorted_input + sorted_input)
  else:
    value = int(sorted_input[0] + sorted_input[len(sorted_input) - 1])
  
  print(f"--{value}")
  
  output_2 += int(value)
  
  print(f"-total = {output_2}\n===")
  
  #print(f"Part 2\n{new_input}")

print(f"Puzzle solution 1\n{output}\nsolution 2\n{output_2}")