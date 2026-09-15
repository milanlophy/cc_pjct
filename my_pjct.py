# Sample data

areas = [
    "Kozhikode Beach",
    "Kallayi",
    "Feroke",
    "Kunnamangalam",
    "Thamarassery"
]

flood_risk = [8, 9, 7, 4, 3]
landslide_risk = [1, 2, 1, 5, 9]
coastal_risk = [10, 8, 7, 1, 0]
rainfall = [180, 200, 170, 190, 250]

# storing the information for one area as a tuple
print("\n Information of one area (Kozhikode Beach)\n")
area1 = ("Kozhikode Beach", 8, 1, 10, 180)

print(area1)
print("Area:", area1[0])
print("Flood Risk:", area1[1])
print("Landslide Risk:", area1[2])
print("Coastal Risk:", area1[3])
print("Rainfall:", area1[4])


# Checking if its highly prone to disasters
print("\n Report of different areas\n")
for i in range(len(areas)):
    total_risk = flood_risk[i] + landslide_risk[i] + coastal_risk[i]

    if total_risk >= 18:
        status = "Economically Sensitive Area"
    elif total_risk >= 10:
        status = "Moderately Sensitive Area"
    else:
        status = "Less Sensitive Area"

    print(areas[i], ":", status)
