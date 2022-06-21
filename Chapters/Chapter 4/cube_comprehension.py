cubes = [number**3 for number in range(1,11)]
for cube in cubes:
    print(cube)

print("\n\nThe first three items in this list are:")
for cube in cubes[:3]:
    print(cube)

print("\n\nThree items from the middle of this list are:")
for cube in cubes[4:7]:
    print(cube)

print("\n\nThe last three items in this list are:")
for cube in cubes[-3:]:
    print(cube)