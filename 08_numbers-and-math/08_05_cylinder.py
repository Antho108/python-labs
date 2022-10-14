# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
from cmath import pi


r = 3.1
height = 5 
bair = (pi) * r * r 
volume = bair * 5
# surface A = 2 x π x r² + 2 x π x r x h 
surface = (2 * (pi) * 3.1*3*1) + (2 * (pi) * 3.1 * 5)   
bair = round(bair, 2)
volume = round(volume, 2)
surface = round(surface, 2)
print(bair, volume, surface)



   