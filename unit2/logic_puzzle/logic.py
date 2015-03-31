"""
UNIT 2: uiLogic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

import itertools

def solve_puzzle():
    days = monday, tuesday, wednesday, thursday, friday = [0, 1, 2, 3, 4]
    orderings = list(itertools.permutations(days))
    return next((Hamming, Knuth, Minsky, Simon, Wilkes)
        for(Hamming, Knuth, Minsky, Simon, Wilkes ) in orderings
        if Knuth - Simon == 1 #6
        for(programmer, designer, manager, writer, jobless ) in orderings
        if not programmer is Wilkes #2
        if not Minsky is writer #4
        if not manager is Knuth #5a
        if not thursday is designer #7
        if Knuth - manager == 1 #10
        for(laptop, droid, iphone, tablet, nothing) in orderings
        if wednesday is laptop #1
        if (programmer is Wilkes and droid is Hamming) or (programmer is Hamming and droid is Wilkes) #3
        if not friday is tablet #8
        if not tablet is manager #5b
        if not designer is droid #9
        if (laptop is monday and Wilkes is writer) or (laptop is writer and Wilkes is monday) #11
        if iphone is tuesday or tablet is tuesday #12
    )
    solution.sort()
    return solution
    
def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    people = ["Hamming", "Knuth", "Minsky", "Simon", "Wilkes"]
    solution = solve_puzzle()
    answer = [ (solution[index], human) for index, human in enumerate(people)]
    answer.sort()
    print [k[1] for k in answer]

logic_puzzle()