# CONE VOLUME CALCULATOR
# First explorations into python

print('Cone volume calculator')
print('-------------------------')


def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


# Get radius
def get_radius():
  radius = input('Radius: ')
  if not is_number(radius):
    print('Invalid input, please provide a number')
    radius = get_radius()
  return radius


radius = get_radius()


# Get height
def get_height():
  height = input('Height: ')
  if not is_number(height):
    print('Invalid input, please provide a number')
    height = get_height()
  return height


height = get_height()

# Calculate the volume
# Formula = (πr^2h)/3

PI = 3.14159265359
radius = float(radius)
height = float(height)
volume = (PI * (radius**2) * height) / 3

print('-------------------------')
print("Volume is ", volume)
