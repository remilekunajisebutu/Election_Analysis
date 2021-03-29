print("Hello World")


counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for i in range(len(counties)):
    print(counties[i])



counties_tuple = ("Arapahoe1","Denver1","Jefferson1")
for i in range(len(counties_tuple)):
      print(counties_tuple[i])

for county in counties_tuple:
      print(county)

# iterating through a dictionary to get key or values or both

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#another way to get value
for county in counties_dict.values():
    print(county)

# another way to get values
for county in counties_dict:
    print(counties_dict[county])

#another way to get values
for county in counties_dict:
    print(counties_dict.get(county))


for county, voters in counties_dict.items():
    #print(county,voters)
    print("county {} county has voters {} registered voters".format(county, voters))
    print(county + " county has " + str(voters) + " registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)   

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#prints out the key and value within text - useful for assignment
counties_dict = {"Arapahoe1": 422829, "Denver2": 463353, "Jefferson3": 432438}

for county in counties_dict:
    voters = counties_dict[county]
    print("{} county has {:,} registered voters.".format(county, voters))