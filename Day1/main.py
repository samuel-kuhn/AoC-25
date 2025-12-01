import time


class Rotation:
  def __init__(self, direction, count):
    self.direction = direction
    self.count = count

  def get_count(self):
    return self.count

  def get_direction(self):
    return self.direction


def parse(rotation: str):
  direction = rotation[:1]
  count = int(rotation[1:].strip())
  return Rotation(direction, count)


with open("input.txt", "r") as f:
  rotations = f.readlines()


def method1():
  zero_count = 0
  dial = 50
  for r_string in rotations:
    rotation = parse(r_string)
    if rotation.direction == 'L':
      dial += 100
      dial -= rotation.count
    elif rotation.direction == 'R':
      dial += rotation.count
    else:
      raise Exception("Unknown action: " + rotation.direction)

    dial = dial % 100
    if dial == 0:
      zero_count += 1
  return zero_count

def method_CLICK():
  zero_count = 0
  dial = 50
  for r_string in rotations:
    rotation = parse(r_string)
    if rotation.direction == 'L':
      dial -= rotation.count
    elif rotation.direction == 'R':
      dial += rotation.count
    else:
      raise Exception("Unknown action: " + rotation.direction)

    while dial < 0 or dial > 99:
      if dial < 0:
        dial += 100
        zero_count += 1
      if dial > 99:
        dial -= 100
        zero_count += 1
  return zero_count

if __name__ == "__main__":
  print("Method 1 result: " + str(method1()))
  print("Method CLICK result: " + str(method_CLICK()))


