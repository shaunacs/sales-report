"""Generate sales report showing total melons each salesperson sold."""

# Creates an empty list that will contain salespeople
salespeople = []
# Creates an empty list containing melons sold
melons_sold = []

# Opens the sales report file
f = open('sales-report.txt')
# Iterates through each line in the sales file
for line in f:
    # Strips each line of any white space at the end
    line = line.rstrip()
    # Separates each component of the line and puts them into a list
    entries = line.split('|')

    # Assigns the first component of the list to salesperson
    salesperson = entries[0]
    # Changes the string containing melons sold into an integer and assigns it to melons
    melons = int(entries[2])

    # Checks to see if the salesperson is in the salespeople list
    if salesperson in salespeople:
        # If they are already in the list, this finds what index they are at
        position = salespeople.index(salesperson)

        # Updates the melons sold by the salesperson in the list
        melons_sold[position] += melons
    else:
        # If not already in the list, this adds the salesperson to the end of the list
        salespeople.append(salesperson)
        # This also appends the number of melons this person sold
        melons_sold.append(melons)

# Ideas for improvement:
# Create a dictionary to store the values of salesperson and melons sold
# This way, each salesperson can be attached to the number of melons they sold


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
