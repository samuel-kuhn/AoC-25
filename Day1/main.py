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

def calc_next_position(dial: int, rot: Rotation):
    if rot.direction == 'L':
        return (dial - rot.count) % 100
    else:
        return (dial + rot.count) % 100


with open("input.txt", "r") as f:
  rotations = f.readlines()


def method1():
  zero_count = 0
  dial = 50
  for r_string in rotations:
    rotation = parse(r_string)
    dial = calc_next_position(dial, rotation)
    if dial == 0:
      zero_count += 1
  return zero_count

def method_CLICK():
  zero_count = 0
  dial = 50

  for r_string in rotations:
    rotation = parse(r_string)

    if rotation.direction == 'L':
      for tic in range(rotation.count):
        dial -= 1
        dial = dial % 100
        if dial == 0:
          zero_count += 1
    else:
      for tic in range(rotation.count):
        dial += 1
        dial = dial % 100
        if dial == 0:
          zero_count += 1

  return zero_count

if __name__ == "__main__":
  print("Method 1 result: " + str(method1()))
  print("Method CLICK result: " + str(method_CLICK()))


