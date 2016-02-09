# This function adds an item to the budget list
def add_item():
	items_dict = {}
	items_dict["name"] = raw_input("Name Your Budget Item:").strip()
	needs_integer = True
	while needs_integer == True:
		try:
			items_dict["amount"] = int(raw_input("How much is it?:").strip())
			needs_integer = False
		except:
			print "Please enter a number"
	items_dict["monthly"] = raw_input("Is this a monthly expense?").strip()
	items_dict["weekly"] = raw_input("Is this a weekly expense?").strip()
	return items_dict

def showitems(items_in_budget):
	for index, items_dict in enumerate(items_in_budget):
		print str(index + 1) + " Name: " + items_dict["name"] + "; Amount: " + str(items_dict["amount"]) + "; Monthly: " + items_dict["monthly"]

def remove_item(item_to_remove):
	showitems(item_to_remove)
	global all_items_array
	needs_integer = True
	while needs_integer == True:
		try:
			response_integer = int(raw_input("Which item would you like to remove? \nIf you would not like to remove an item, type '0'"))
			needs_integer = False
		except: 
			print "Please enter a number"
		if response_integer == 0:
			break
		else:
			del all_items_array[(response_integer-1)]

def save_funct(item_to_save):
	with open("Budget.csv", "w") as budget_file:
		budget_file.write("Name, Amount, Monthly Expense\n")
		for budget_item in item_to_save: 
			budget_file.write(str(budget_item["name"]) + "," + str(budget_item["amount"]) + "," + str(budget_item["monthly"]) + "\n")
	  
def read_spreadsheet(array):
	with open(raw_input("What is the name of the file you'd like to open?").strip() + ".csv", "r") as external_budget_file:
		external_user_input = external_budget_file.readlines() 
		print external_user_input
		new_nested_array_header = external_user_input
		new_nested_array = new_nested_array_header[1:]
		for each_element in new_nested_array:
			array_2 = each_element.split(",")
			print array_2
			new_hash = {'name':array_2[0], 'amount':array_2[1], 'monthly':array_2[2].strip('\n')}
			array.append(new_hash)
		print array
		
options = ("Your Budget Options: \nA) Add item\nS) Show item\nR) Remove item\nSave) Save Spreadsheet\nRead) Import Spreadsheet Data\nQ) Quit Program\n\n")
userchoice = raw_input(options).strip().upper()        
all_items_array = []
while userchoice != "Q":
	if userchoice == "A":
		items_dict_var = add_item()
		all_items_array.append(items_dict_var)
	elif userchoice == "S":
		showitems(all_items_array)
	elif userchoice == "R":
		remove_item(all_items_array)
	elif userchoice == "SAVE":
		save_funct(all_items_array)
	elif userchoice == "READ":
		read_spreadsheet(all_items_array)
	else:
		print "That is not a valid option!"
	userchoice = raw_input(options).strip().upper()        
