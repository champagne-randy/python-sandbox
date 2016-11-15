"""
	Lists:

	A datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)

	Python lists are very flexible and can hold completely heterogeneous, arbitrary data, and they can be appended to very efficiently, in amortized constant time. If you need to shrink and grow your array time-efficiently and without hassle, they are the way to go. But they use a lot more space than C arrays.
"""


print "\nLists:\n"
print "Declaring and initializing"
zoo_animals = ["pangolin", "cassowary", "sloth", "mina"];
print zoo_animals

print "Empty list"
empty_list = []
print empty_list

print "\nAccess by Index"
if len(zoo_animals) > 3:
	print "   The first animal at the zoo is the " + zoo_animals[0]
	print "   The second animal at the zoo is the " + zoo_animals[1]
	print "   The third animal at the zoo is the " + zoo_animals[2]
	print "   The fourth animal at the zoo is the " + zoo_animals[3]

print "\nUpdate list"
zoo_animals[1] = "Mitch"
print "The new second animal is " + zoo_animals[1]















"""
	List Length:
	
	A list doesn't have to have a fixed length. You can add items to the end of a list any time you like!
"""

print "\n\nList Length:"
letters = ['a', 'b', 'c']
print letters
print "list length is: " + str(len(letters))
print " "


# append list new cell
print "appending isht"
letters.append('d')
print letters
print "new length after appending new cell: " + str(len(letters))
print letters
















"""
	List Slicing:

	Sometimes, you only want to access a portion of a list.

	>>> letters = ['a', 'b', 'c', 'd', 'e']
	>>> slice = letters[1:3]
	>>> print slice
	>>> print letters
	
	In the above example, we first create a list called letters.
	
	Then, we take a subsection and store it in the slice list. We start at the index before the colon and continue up to but not including the index after the colon.
	
	Next, we print out ['b', 'c']. Remember that we start counting indices from 0 and that we stopped before index 3.
	
	Finally, we print out ['a', 'b', 'c', 'd', 'e'], just to show that we did not modify the original letters list.

"""

print "\n\nList Slicing:"
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
print suitcase

print "\nThe first and second items (index zero and one)"
first  = suitcase[0:2]
print first

print "\nThird and fourth items (index two and three)"
middle =  suitcase[2:4]
print middle

print "\nThe last two items (index four and five)"
last   = suitcase[4:6]
print last











"""
	Slicing Lists and Strings:

	You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.

	>>> my_list[:2]
	>>> # Grabs the first two items
	
	>>> my_list[3:]
	>>> # Grabs the fourth through last items

	If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included.

"""


print "\n\nSlicing Lists and Strings:\n"

print "a string:"
animals = "catdogfrog"
print "'" + animals + "'"

print "\nThe first three characters of animals"
cat  = animals[:3]
print cat

print "\nThe fourth through sixth characters"
dog  = animals[3:6]
print dog

print "\nFrom the seventh character to the end"
frog = animals[6:]
print frog
















"""
	Searching and inserting:

	Sometimes you need to search for an item in a list.
	
	>>> animals = ["ant", "bat", "cat"]
	>>> print animals.index("bat")

	First, we create a list called animals with three strings.
	Then, we print the first index that contains the string "bat", which will print 1.
	

	We can also insert items into a list.
	
	>>> # We insert "dog" at index 1, which moves everything down by 1.
	>>> animals.insert(1, "dog")
	>>> # We print out ["ant", "dog", "bat", "cat"]
	>>> print animals
	
	
"""

print "\n\nSearching and inserting:"

print "\nanimals"
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print animals

print "\nUse index() to find 'duck'"
duck_index = animals.index("duck") 
print "duck_index is: " + str(duck_index)

print "\nUse insert(index, object) to add 'cobra' at before 'duck'"
animals.insert(duck_index, "cobra")
print animals















"""
	Remove a Few Things
	Sometimes you need to remove something from a list.

	beatles = ["john","paul","george","ringo","stuart"]
	beatles.remove("stuart")
	print beatles
	>> ["john","paul","george","ringo"]
	We create a list called beatles with 5 strings.
	Then, we remove the first item from beatles that matches the string "stuart". Note that .remove(item) does not return anything.
	Finally, we print out that list just to see that "stuart" was actually removed.

"""


print "\n\nRemove things from a list:"

print "\nyou can also use the remove('item') to remove an item from a list"
print "given a list named backpack"
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
print backpack

print "\nbackpack.remove('dagger')"
backpack.remove('dagger')
print backpack
















"""
	For loops and lists:

	If you want to do something with every item in the list, you can use a for loop. If you've learned about for loops in JavaScript, pay close attention! They're different in Python.
	
	>>> for variable in list_name:
	>>>     # Do stuff!

	A variable name follows the for keyword; it will be assigned the value of each list item in turn.
	
	Then in list_name designates list_name as the list the loop will work on. The line ends with a colon (:) and the indented code that follows it will be executed once per item in the list.
"""

print "\n\nFor loops and lists:"

print "\nmy_list"
my_list = [1,9,3,8,5,7]
print my_list

print "\nnow printing each cell multiplied by 2"
print """ for number in my_list:
     print number * 2
"""

for number in my_list:
    print number * 2









"""
	Sorting a list:

	If your list is a jumbled mess, you may need to sort() it.
	
	>>> animals = ["cat", "ant", "bat"]
	>>> animals.sort()
	
	>>> for animal in animals:
	>>>     print animal
	
	First, we create a list called animals with three strings. The strings are not in alphabetical order.
	Then, we sort animals into alphabetical order. Note that .sort() modifies the list rather than returning a new list.
	Then, for each item in animals, we print that item out as "ant", "bat", "cat" on their own line each.

"""

print "\n\nSorting a list:"

print "\nstart_list ="
start_list = [5, 3, 1, 2, 4]
print start_list

print "\nsquare_list ="
square_list = []
print square_list

print """\nloop through square_list and store the square of each cell in square_list with\n
 for num in start_list:
     square_list.append( num ** 2)
"""

for num in start_list:
     square_list.append( num ** 2)

print "sort square_list with \nsquare_list.sort()"
square_list.sort()

print "\nsquare_list ="
print square_list










"""

	Dictionaries:

	A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
	
	>>> d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
	
	This is a dictionary called d with three key-value pairs. The key 'key1' points to the value 1, 'key2' to 2, and so on.
	
	Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail address with a username), and more!

"""

print "\n\nDictionaries:"


print "\nAssigning a dictionary with three key-value pairs to residents"
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents

print "\nPrinting residents['Puffin']'s room number"
print residents['Puffin']










"""

	Adding key:value pairs to dictionaries:

	Like Lists, Dictionaries are "mutable". This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:
	
	>>> dict_name[new_key] = new_value
	
	An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.
	
	The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That's right: you can put lists inside dictionaries!)

"""

print "\n\nAdding key:value pairs to dictionaries:"

print "\nEmpty dictionary \nmenu ="
menu = {} 
print menu

print "\nAdding new key-value pair with \nmenu['Chicken Alfredo'] = 14.50"
menu['Chicken Alfredo'] = 14.50
print menu['Chicken Alfredo']

print "\nAdding some dish-price pairs to menu!"
menu['spam'] = 2.50
menu['pasta'] = 5.67
menu['eggs'] = 3.63


print "There are " + str(len(menu)) + " items on the menu."
print menu











"""

	Deleting and updating key:value pairs:

	Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the del command:
	
	>>> del dict_name[key_name]
	
	will remove the key key_name and its associated value from the dictionary.
	
	A new value can be associated with a key by assigning a value to the key, like so:
	
	>>> dict_name[key] = new_value

"""

print "\n\nDeleting and updating key:value pairs:"


print "\n# A dictionary (or list) declaration may break across multiple lines"
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
print zoo_animals


print "\nremoving the 'Unicorn' entry. (Unicorns are incredibly expensive.)\ndel zoo_animals['Unicorn']"
del zoo_animals['Unicorn']
print zoo_animals

print "\nupdating the value for key 'Rockhopper Penguin' \nzoo_animals['Rockhopper Penguin'] = 'Gotham City'"
zoo_animals['Rockhopper Penguin'] = 'Gotham City'
print zoo_animals













"""
	
	Exploring the heterogeneity of dictionaries:

	Let's go over a few last notes about dictionaries
	
	>>> my_dict = {
	>>>     "fish": ["c", "a", "r", "p"],
	>>>     "cash": -4483,
	>>>     "luck": "good"
	>>> }
	>>>
	>>> print my_dict["fish"][0]
	
	In the example above, we created a dictionary that holds many types of values.
	The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.
	Finally, we print the letter 'c'. When we access a value in the dictionary like my_dict["fish"], we have direct access to that value. So we can access the item at index '0' in the list stored by the key "fish"

"""


print "\n\n\nExploring the heterogeneity of dictionaries:"


print "\nDictionaries can be populated with many different kinds of objects i.e. lists, ints, strings..."


print "inventory = "
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
print inventory



print "\n\nAdding a key 'burlap bag' and assigning a list to it"
print "inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']"
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
print inventory


print "\n\nSorting the list found under the key 'pouch'"
print "inventory['pouch'].sort()"
inventory['pouch'].sort() 
print inventory


print "\n\nAdd a key to inventory called 'pocket' and set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'"
print "inventory['pocket'] = ['seashell', 'strange berry', 'lint']"
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print inventory


print "\n\n.sort() the items in the list stored under the 'backpack' key"
inventory['backpack'].sort()
print inventory


print "\n\n.remove('dagger') from the list of items stored under the 'backpack' key"
print "inventory['backpack'].remove('dagger')"
inventory['backpack'].remove('dagger')
print inventory


print "\n\nAdd 50 to the number stored under the 'gold' key"
print "inventory['gold'] += 50"
inventory['gold'] += 50
print inventory


print "\n\nThe end!\n\n\n\n"









