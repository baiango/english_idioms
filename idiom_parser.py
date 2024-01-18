def parse_idioms(file_path):
	idioms = []

	with open(file_path, 'r') as file:
		for line in file:
			# Strip whitespace and the outer quotes
			line = line.strip().strip('"')

			# Split the line at '>>' to get idiom and definition
			parts = line.split('>>')

			# Check if the line is correctly formatted
			if len(parts) == 2:
				# Remove the curly braces and strip extra whitespace
				idiom = parts[0].strip().strip('{}').strip()
				definition = parts[1].strip().strip('{}').strip()

				# Add the parsed idiom and definition to the list
				idioms.append((idiom, definition))

	return idioms

# Replace with the actual file path
file_path = 'output_idioms.csv'
idioms_list = parse_idioms(file_path)
print(idioms_list)
