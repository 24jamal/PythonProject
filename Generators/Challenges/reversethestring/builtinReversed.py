def builtinReversed(s):

    str = reversed(s)
    for ch in str:
        yield(ch)

for i in builtinReversed("jamal"):
    print(i)

def reverse_string(s):
    rev_iter = reversed(s)   # get reversed iterator
    while True:
        try:
            ch = next(rev_iter)  # get next element manually
            yield ch
        except StopIteration:
            break  # exit when iterator is exhausted


for i in reverse_string("justin"):
    print(i)
