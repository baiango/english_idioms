import csv

input_csv_file = "input_idioms.csv"
output_csv_file = "idioms.csv"

# Read data from the input CSV file
data = []
with open(input_csv_file, mode='r') as file:
	reader = csv.reader(file)
	for row in reader:
		data.append(row)

# Create a dictionary to store idioms with their shortest definitions
idioms_dict = {}

for row in data:
	# Skip the row if it's empty or does not contain exactly 2 items (idiom and definition)
	if not row or len(row) != 2:
		continue

	idiom, definition = row

	# Normalize the idiom to lowercase for comparison
	idiom_key = idiom.lower()

	# If the idiom is already in the dictionary, compare definition lengths
	if idiom_key in idioms_dict:
		# Replace if the new definition is shorter
		if len(definition) < len(idioms_dict[idiom_key][1]):
			idioms_dict[idiom_key] = [idiom, definition]
	else:
		# Add the idiom to the dictionary
		idioms_dict[idiom_key] = [idiom, definition]

# Write the filtered data to the output CSV file
with open(output_csv_file, mode='w', newline='') as file:
	writer = csv.writer(file, quoting=csv.QUOTE_ALL)
	for idiom, definition in idioms_dict.values():
		# Format the row as {idiom}>>{definition}
		formatted_row = f"{{{idiom}}}>>{{{definition}}}"
		writer.writerow([formatted_row])
