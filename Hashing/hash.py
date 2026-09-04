#Brute force
def cou():
    count=0
    arr=[1,3,4,1,3,5]
    n=int(input("The element: "))
    for i in arr:
        if i==n:
            count=count+1
    print("The element have in array: ", count)
cou()    





# Frequency Counting using Hashing

arr = [2, 4, 5, 2, 5]  # Original array

# Create a hash array of size 8.
# Every element initially has frequency 0.
# Valid indexes are 0 to 7.
hashlist = [0] * 8

# Pre-store the frequency of each number
for i in arr:
    # The value 'i' is used as the index of hashlist.
    # Increase the frequency by 1.
    hashlist[i] += 1

# Print the complete hash array
print(hashlist)
# Output: [0, 0, 2, 0, 1, 2, 0, 0]


# Fetch / Query the frequency

t = int(input("Enter time: "))

# Run the query loop 't' times
for j in range(t):

    # Take the number whose frequency we want to find
    e = int(input("Enter element: "))

    # Use 'e' as the index and get its frequency
    print(hashlist[e])
    
    
    
    
    
# Character Frequency Counting using Hashing

s = input("Enter a string: ")

# Create a hash table for 26 lowercase English letters
hash_table = [0] * 26

# Pre-store the frequency of each character
for ch in s:

    # Convert character into an index
    # a → 0, b → 1, c → 2, ..., z → 25
    index = ord(ch) - ord('a')

    # Increase the frequency
    hash_table[index] += 1


# Take the character whose frequency we want to find
ch = input("Enter character: ")

# Convert the character into its hash index
index = ord(ch) - ord('a')

# Print its frequency
print("Frequency:", hash_table[index])







# Frequency Counting using Dictionary (Hashing)

arr = [1, 2, 3, 1, 3, 2]

# Create an empty dictionary.
# It will store:
# number → frequency
freq = {}

# Go through each number in the array
for num in arr:

    # Check whether the number already exists in the dictionary
    if num in freq:

        # If it exists, increase its frequency by 1
        freq[num] += 1

    else:

        # If it does not exist, add it to the dictionary
        # with an initial frequency of 1
        freq[num] = 1


# Print the final frequency dictionary
print(freq)

# Output:
# {1: 2, 2: 2, 3: 2}