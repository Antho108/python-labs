# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
from math import pi

r = 3.14
height = 5

base_area = pi * r ** 2
volume = base_area * height
volume = round(volume, 2)

# surface A = 2πr² + 2πrh
surface_area = 2 * pi * r**2 + 2 * pi * r * height
surface_area = round(surface_area, 2)

print("Base area:", round(base_area, 2))
print("Volume:", volume)
print("Surface area:", surface_area)