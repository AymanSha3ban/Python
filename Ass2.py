# Name :Ayman Shaaban 
# ID : 23120261 
#            Ass No(2) :) 

# 1. Reverse Words in a Sentence
def reverse_words(sentence):
    words = sentence.split(" ")
    return " ".join(words[::-1])

print(reverse_words("Hello world from Python"))  # "Python from world Hello"

# 2. Check if a Word is a Palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# 3. Find the Unique Number in a List
def find_unique_number(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num

print(find_unique_number([4, 1, 2, 1, 2]))  # 4

# 4. Reverse a String (Without Built-in Functions)
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("Python"))  # "nohtyP"

# 5. Find the Maximum Number in a List (Without max())
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([10, 5, 20, 8]))  # 20

# 6. Find the Most Frequent Element in a List (Without Counter)
def most_frequent(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = 0
    max_num = None
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_num = key
    return max_num

print(most_frequent([1, 3, 2, 3, 4, 3, 5]))  # 3
