# --
# Problem 1: Reverse Sentence

# Understand the problem: Input: takes in a string 'sentence' and Output: prints the sentence with the words in reverse order.
# Split the sentence into words and store in a  list. 
# Reverse the list of words and join them back into a string. Print the reversed sentence.

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)

# --
# Problem 2: Goldilocks Number
# Understand the problem: Input: takes in a list of positive integers 'nums' and Output: returns any number from the list that is neither
# the max of min of the list, and if there is no such number, return -1.


def goldilocks_number(nums):
    # find the max and min of the list
    # sort the list to organize in ascending order (optional)
    sorted_nums = nums.sort()
    # iterate through the list and return the first number that is neither max nor min
    for num in sorted_nums:
        # if the number is not the max or min, return it
        if num != max(sorted_nums)and num != min(sorted_nums):
            return num
    return -1

# --
# Problem 3: Deleete Minimum
# Understand the problem: Input: takes in a list of integers 'hunny_jar_sizes' and Output: returns the number of elements that need to be deleted
# for every new list, find the min of the list and append it to a new list
def delete_minimum_elements(hunny_jar_sizes):
    # new list 
    new_list = []
    # iterate through the original list while there are elements in the list
    while hunny_jar_sizes:
        
        # find min of the list
        min_value = min(hunny_jar_sizes)
        # add the min value to the new list
        new_list.append(min_value)
        # remove the min value from the original list
        hunny_jar_sizes.remove(min_value)

    # print the new list
    print(new_list)

# Test cases: Passed
hunny_jar_sizes = [5, 3, 2, 4, 1]
# delete_minimum_elements(hunny_jar_sizes)

# Output: 
# [1, 2, 3, 4, 5]

hunny_jar_sizes = [5, 2, 1, 8, 2]
# delete_minimum_elements(hunny_jar_sizes)

# Output:
# [1, 2, 2, 5, 8]

# --
# Problem 4: Sum of Digits
# Input: takes in a positive integer 'n' and Output: returns the sum of the digits of the number.
def sum_of_digits(num):
    # convert integer to string to iterate through each digit
    num_str = str(num)
    # initialize sum variable
    sum = 0
    # iterate through each digit in the string
    for digit in num_str:
        # convert the digit back to integer and add to sum
        sum += int(digit)
    print(sum)
# Test cases: Passed
#sum_of_digits(432)  # Output: 9
# sum_of_digits(4)  # Output: 4

# --
# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
# Input: takes in a list of strings 'operations' containing a list of operations 
# bouncy and flouncy increment the value of the var by 1
# trouncy and pouncy decrement the value of the var by 1
# Output: reutnr the final valueo f tigger after performing the operations
def final_value_after_operations(operations):
    # initalize tigger's value = 1
    tigger = 1
    # iterate through the list of operations
    for operation in operations:
        # if the operation is bouncy or flouncy, increment tigger's value by 1
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
        # if the operation is trouncy or pouncy, decrement tigger's value by 1
        elif operation == "trouncy" or operation == "pouncy":
            tigger -= 1
    # return the final value of tigger
    print(tigger)

# Test cases: Passed
operations = ["bouncy", "flouncy", "trouncy"]
operations = ["trouncy", "flouncy", "flouncy"]
#final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)

# --
# Problem 6: Acronym 


# --
# Problem 7: Good Things Come in Threes


# --
# Problem 8: Exclusive Elements 


# --
# Problem 9: Merge Strings Alternately



# --
# Problem 10: Eeyore's House



