# ----------------- this is also called exponential algorithm
'''
🔹 What is Tower of Hanoi?

Tower of Hanoi is a classic problem in recursion (very important for exams like GATE).

It consists of:

3 rods (pegs) → A, B, C
N disks of different sizes
Disks are stacked on one rod in increasing size (largest at bottom)
🎯 Goal

Move all disks from Source rod (A) → Destination rod (C)
using Auxiliary rod (B)
'''

#⚠️ Rules (VERY IMPORTANT)
'''
Only one disk can be moved at a time
Only the top disk can be moved
Bigger disk cannot be placed on smaller disk
'''

# ----------------------- algorithm
# input : n(number of disk)
# output: the movement to be made
# if n=1 move the single disk A to C and stop  -------------> base commands
# Move the top n-1 disks form A to B, using C as a auxiliary ------------> recursion
# move the remaining disk from A to C------------------> actual value
# move the n-1 disk from B to C, using A as auxiliry--------> recursion

# ----------------- example
'''
📌 Example (N = 3)

Initial:
A: [3,2,1]   B: []   C: []

Steps:

Move disk 1 → C
Move disk 2 → B
Move disk 1 → B
Move disk 3 → C
Move disk 1 → A
Move disk 2 → C
Move disk 1 → C

Final:

A: []   B: []   C: [3,2,1]
'''


# ------------------ psudo code
'''
TOH(n, source, aux, dest):
    if n == 1:
        print "Move disk 1 from source to dest"
        return

    TOH(n-1, source, dest, aux)
    print "Move disk n from source to dest"
    TOH(n-1, aux, source, dest)
'''

# ------------ code 
def toh(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    
    # Step 1: Move n-1 disks from source → auxiliary
    toh(n - 1, source, destination, auxiliary)
    
    # Step 2: Move nth disk from source → destination
    print(f"Move disk {n} from {source} → {destination}")
    
    # Step 3: Move n-1 disks from auxiliary → destination
    toh(n - 1, auxiliary, source, destination)


# Driver code
n = 3
toh(n, 'A', 'B', 'C')


'''
📌 Output for n = 3

Move disk 1 from A → C
Move disk 2 from A → B
Move disk 1 from C → B
Move disk 3 from A → C
Move disk 1 from B → A
Move disk 2 from B → C
Move disk 1 from A → C
'''

'''
toh(3)
 ├── toh(2)
 │    ├── toh(1)
 │    ├── move disk 2
 │    └── toh(1)
 ├── move disk 3
 └── toh(2)
'''