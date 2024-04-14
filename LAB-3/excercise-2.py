#I. You have collected information about cities in your province. You decide to store each city’sname, population, and mayor in a file. Write a python program to accept the data for a number of cities from the keyboard and store the data in a file in the order in which they’re entered.
num_cities = int(input("Enter the number of cities: "))

    # Open a file in write mode to store the city data
with open("city_data.txt", "w") as file:
        # Iterate through each city to get its data
        for i in range(num_cities):
            print(f"\nEnter data for City {i+1}:")
            city_name = input("Enter city name: ")
            population = input("Enter population: ")
            mayor = input("Enter mayor's name: ")

            # Write the city data to the file
            file.write(f"{city_name},{population},{mayor}\n")

print("City data has been saved to city_data.txt")

#Write a python program to create a data file student.txt and append the message “Now we are AI students"

# Open the file in append mode
with open("student.txt", "a") as file:
    # Append the message to the file
    file.write("Now we are AI students\n")

print("Message appended to student.txt")

