import csv

# Prompt user to enter the datapoints one by one and validate input
datapoints = []
for metric in ['number of users', 'number of artists', 'number of collectors', '24-hour volume', '7-day volume', 'all-time volume', 'total sales', 'average sale amount', 'average network gratuity']:
    while True:
        value = input(f"Enter the {metric}: ")
        try:
            datapoints.append(float(value))
            break
        except ValueError:
            print(f"Error: Invalid input. {metric.capitalize()} must be a number.")

# Write the datapoints to a CSV file
with open('datapoints.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Datapoint', 'Value'])
    writer.writerow(['Number of Users', datapoints[0]])
    writer.writerow(['Number of Artists', datapoints[1]])
    writer.writerow(['Number of Collectors', datapoints[2]])
    writer.writerow(['24-Hour Volume', datapoints[3]])
    writer.writerow(['7-Day Volume', datapoints[4]])
    writer.writerow(['All-Time Volume', datapoints[5]])
    writer.writerow(['Total Sales', datapoints[6]])
    writer.writerow(['Average Sale Amount', datapoints[7]])
    writer.writerow(['Average Network Gratuity', datapoints[8]])

print("Datapoints have been exported to datapoints.csv")
