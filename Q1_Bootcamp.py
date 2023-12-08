shopping_items = input("Enter the items you want: ")
	
# Separate the items entered by shopper
items = shopping_items.split()
	
# Create a list to store item
item_list = []
	
# Loop through each item in the list
for item in items:
    # Convert it into an integer
	item_to_int = int(item)
	# Add the converted item to the list
	item_list.append(item_to_int)
	
# Initialize a variable to store the shopping code
	shopping_code = 0
	
# Using math to combine number
for number in item_list:
	shopping_code = shopping_code * 10 + number
print(f"Your shopping code is: {shopping_code}")
