def calculate_volume_of_sphere(radius):
    pi = 3.1416
    volume=(4/3)*pi*radius**3
    return volume

radius_1 = 30
volume_1 = calculate_volume_of_sphere(radius_1)
print("The volume of sphere with radius "+str(radius_1)+" is: "+str(volume_1))

radius_2 = 40
volume_2 = calculate_volume_of_sphere(radius_2)
print("The volume of sphere with radius "+str(radius_2)+" is: "+str(volume_2))
