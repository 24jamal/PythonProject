# THis is a coding Challenge for collections
# Taken from ChatGPT


#Challenges

#1. Find the most common element in a list

nums = [1, 2, 2, 3, 4, 4, 4, 5,5,5,5]
# Expected Output → 4

freq = {}

for num in nums:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] =1

most_common = None
max_count =0

for num, count in freq.items():

    if count > max_count:
        max_count = count
        most_common = num

print(f"Most common : {most_common}")
print(f"Count : {max_count}")