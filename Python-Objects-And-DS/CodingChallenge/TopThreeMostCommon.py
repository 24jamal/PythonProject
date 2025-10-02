text = "apple banana apple orange banana apple mango mango mango mango"

words = text.split()

freq = {}

for word in words:

    if word in freq:

        freq[word] += 1

    else:
        freq[word] = 1

items = list(freq.items())
print(f"items :{items}")
def get_count(pair):

    return pair[1]

top_common = sorted(items,key=  get_count,reverse=True)

print(top_common)