'''====================================================
AI/ML EXAM IMPORTANT NUMERICAL & MCQ QUESTIONS
====================================================

----------------------------------------------------
1. SVM HYPERPLANE QUESTION
----------------------------------------------------

Question:
Given hyperplane:
6x1 + 12x2 + 6 = 0
Find the class of point (3,2).

Solution:

Substitute point:

S = 6(3) + 12(2) + 6

  = 18 + 24 + 6

  = 48

Case:

S > 0  → Positive Class (+1)
S < 0  → Negative Class (-1)
S = 0  → On Hyperplane

Answer:

48 > 0

Therefore point belongs to Positive Class.

----------------------------------------------------
2. SVM DISTANCE QUESTION
----------------------------------------------------

Question:
Find distance of point (3,2) from:

6x1 + 12x2 + 6 = 0

Formula:

Distance =
|Ax + By + C|
-----------------
√(A² + B²)

Solution:

Numerator:

|6(3)+12(2)+6|

= |48|

= 48

Denominator:

√(6² + 12²)

= √(36+144)

= √180

= 13.416

Distance:

48 / 13.416

= 3.58

Answer:

Distance = 3.58

----------------------------------------------------
3. RL EXPLOITATION QUESTION
----------------------------------------------------

Q-values:

Up      = 4.5
Down    = 2.6
Left    = 3.2
Right   = Unreachable

Question:
Which action is selected during Exploitation?

Rule:

Exploitation chooses Highest Q-value.

Highest:

max(4.5,2.6,3.2)

= 4.5

Answer:

UP

----------------------------------------------------
4. RL EXPLORATION QUESTION
----------------------------------------------------

Question:
Which action may be selected during Exploration?

Answer:

Any valid action.

Reason:

Exploration means trying new actions.

Agent may choose:

Up
Down
Left

even if they are not best.

----------------------------------------------------
5. WHY EXPLORATION IS IMPORTANT?
----------------------------------------------------

Answer:

Exploration helps:

1. Discover new actions
2. Discover better paths
3. Avoid local optimum
4. Improve long-term reward

Without exploration, agent may never find the best solution.

----------------------------------------------------
6. WHY EXPLOITATION IS IMPORTANT?
----------------------------------------------------

Answer:

Exploitation:

1. Uses existing knowledge
2. Gives highest immediate reward
3. Faster decisions
4. Uses best known action

----------------------------------------------------
7. DECISION TREE ENTROPY QUESTION
----------------------------------------------------

Dataset:

Yes = 9
No = 5

Formula:

Entropy =
-p(Yes)log₂p(Yes)
-p(No)log₂p(No)

Calculation:

p(Yes)=9/14=0.64

p(No)=5/14=0.36

Entropy

= -(0.64log₂0.64)
  -(0.36log₂0.36)

= 0.94

Answer:

Entropy = 0.94

----------------------------------------------------
8. DECISION TREE ROOT NODE QUESTION
----------------------------------------------------

Information Gain values:

Outlook  = 0.246
Temp     = 0.029
Humidity = 0.151
Windy    = 0.048

Rule:

Choose attribute with Highest Information Gain.

Highest:

0.246

Answer:

Outlook becomes Root Node.

----------------------------------------------------
9. HOW TO CONSTRUCT DECISION TREE
----------------------------------------------------

Step 1:
Calculate Entropy

Step 2:
Calculate Information Gain of all attributes

Step 3:
Select attribute with Highest Information Gain

Step 4:
Make it Root Node

Step 5:
Split dataset

Step 6:
For each branch calculate Entropy again

Step 7:
Repeat until Entropy = 0

Flow:

Dataset
 ↓
Entropy
 ↓
Information Gain
 ↓
Best Attribute
 ↓
Split
 ↓
Repeat
 ↓
Decision Tree

----------------------------------------------------
10. K-MEANS NUMERICAL QUESTION
----------------------------------------------------

Points:

A(1,1)
B(1,0)
C(0,2)
D(2,4)
E(3,5)

Centroids:

C1=A
C2=D

Question:

Which cluster does E belong to?

Distance(E,C1)

= √[(3-1)²+(5-1)²]

= √20

= 4.47

Distance(E,C2)

= √[(3-2)²+(5-4)²]

= √2

= 1.41

Answer:

1.41 < 4.47

E belongs to Cluster 2

----------------------------------------------------
11. K-MEANS ALGORITHM STEPS
----------------------------------------------------

1. Choose K

2. Select Random Centroids

3. Compute Distance

4. Assign nearest cluster

5. Compute New Mean

6. Update Centroids

7. Repeat

8. Stop when assignments do not change

----------------------------------------------------
12. ELBOW METHOD QUESTION
----------------------------------------------------

K     WCSS

1     100
2      60
3      30
4      15
5      13
6      12

Question:

Find Optimal K.

Observation:

Sharp decrease till K=4

After that improvement is small.

Answer:

K = 4

----------------------------------------------------
13. GMM QUESTION
----------------------------------------------------

Cluster A = 0.7

Cluster B = 0.3

Question:

Which cluster is assigned?

Rule:

Choose Highest Probability

Answer:

Cluster A

----------------------------------------------------
14. K-MEANS vs GMM
----------------------------------------------------

K-MEANS

Hard Clustering
Distance Based
Uses Centroid
Fast
Uses Euclidean Distance

GMM

Soft Clustering
Probability Based
Uses Gaussian Distribution
Uses EM Algorithm
Handles Overlapping Clusters

----------------------------------------------------
15. RL BUILDING BLOCKS
----------------------------------------------------

Agent:
Learner

Environment:
World

State:
Current Position

Action:
Move

Reward:
Feedback

Goal:
Target

Episode:
Complete Journey

----------------------------------------------------
16. RL EXPLORATION vs EXPLOITATION
----------------------------------------------------

EXPLOITATION

Uses known best action

Higher immediate reward

May miss better solutions

Example:
Go to favorite restaurant

EXPORATION

Try new actions

May discover better solution

Lower reward initially

Example:
Try new restaurant

----------------------------------------------------
17. Q-LEARNING IMPORTANT FACTS
----------------------------------------------------

Policy (π)
= Strategy

Value Function V(s)
= How good is a state?

Q Function Q(s,a)
= How good is an action in a state?

Alpha (α)
= Learning Rate

Gamma (γ)
= Discount Factor

Q-table
= Stores State-Action values

Higher Q-value
= Better Action

----------------------------------------------------
18. MOST IMPORTANT MCQ FACTS
----------------------------------------------------

1. SVM:
   wTx+b > 0 → Positive Class

2. SVM:
   wTx+b < 0 → Negative Class

3. SVM:
   wTx+b = 0 → Hyperplane

4. K-Means uses Euclidean Distance

5. K-Means is Hard Clustering

6. GMM is Soft Clustering

7. GMM uses EM Algorithm

8. Entropy = Measure of Impurity

9. Highest Information Gain → Root Node

10. Elbow Method uses WCSS

11. Silhouette Score Range:
    -1 to +1

12. RL learns using Rewards

13. Exploration = Try New

14. Exploitation = Use Best Known

15. Q-Learning = Model-Free RL

16. DQN = Model-Free RL

17. SARSA = Model-Free RL

18. Value Iteration = Model-Based RL

19. Policy Iteration = Model-Based RL

20. Goal of RL =
    Maximize Cumulative Reward

====================================================
30 SECOND EXAM REVISION
====================================================

SVM:
wTx+b>0 → Positive
wTx+b<0 → Negative
wTx+b=0 → Hyperplane

Decision Tree:
Entropy → Information Gain → Root Node

K-Means:
Distance Based
Hard Clustering

GMM:
Probability Based
Soft Clustering

RL:
Exploration → Try New
Exploitation → Best Known

Q-Learning:
Higher Q-value = Better Action

Elbow:
Choose K at Elbow Point

Silhouette:
+1 Best
0 Overlap
-1 Wrong Assignment

====================================================
'''