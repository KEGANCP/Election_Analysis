

county=("Arapaho","Denver","Jefferson")
voters=422829,463353,432438
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


