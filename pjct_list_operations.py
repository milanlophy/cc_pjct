areas = ["Kozhikode Beach", "Kallayi", "Feroke", "Kunnamangalam"]

flood_risk = [8, 9, 7, 4]
landslide_risk = [1, 2, 1, 5]
coastal_risk = [10, 8, 7, 1]

print("Areas: ",areas)
areas.append("Thamarassery")
print("Appending Thamarassery: ",areas)

print("\nInserting an area (Beypore) at specified position (1): ")
areas.insert(1, "Beypore")
print(areas)

print("\nRemoving an area (Feroke): ")
areas.remove("Feroke")
print(areas)

print("\nRemoving an area using its index (2): ")
removed_area = areas.pop(2)
print("Removed:", removed_area)
print(areas)

print("\nSorting areas alphabetically: ")
areas.sort()
print(areas)

print("\nReversing the list: ")
areas.reverse()
print(areas)

print("\nFinding position of an area: ")
print("Kunnamangalam at position ",areas.index("Kunnamangalam"))

