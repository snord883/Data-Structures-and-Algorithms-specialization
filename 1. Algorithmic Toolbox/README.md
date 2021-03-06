# **Algorithmic Toolbox**
- **T(n)** denotes the number of *lines of code* executed

## **Fibonacci Numbers**
[Visualization](https://www.cs.usfca.edu/~galles/visualization/DPFib.html)

### **Naive approach:** 
![alt_text](./images/fib_nums.JPG 'image')
![alt_text](./images/fib_nums2.JPG 'image')
![alt_text](./images/fib_nums3.JPG 'image')


- Reasoning for it being so inefficient
    - Calculations are being duplicated unnecessarily throughout the recursion process
    
![alt_text](./images/fib_nums4.JPG 'image')


### **Efficient Algorithm**
![alt_text](./images/fib_nums5.JPG 'image')

<br>
<hr>
<br>

## **Greatest Common Divisor**

### **Naive approach**
![alt_text](./images/gcd.JPG 'image')

### **Efficient Algorithm**
![alt_text](./images/gcd2.JPG 'image')
![alt_text](./images/gcd3.JPG 'image')
![alt_text](./images/gcd4.JPG 'image')
![alt_text](./images/gcd5.JPG 'image')
![alt_text](./images/gcd6.JPG 'image')

<br>
<hr>
<br>

## **Computing Runtimes**
- Flaws in the "counting lines" approach is that not every line is equivalent in execution time.
- Different factors for runtime:
    - Speed of the computer, the system architecture, the compiler being used, memory hierarchy

<br>
<hr>
<br>

## **Asymptotic Notation**
[Helpful link](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation)
- How does runtime **scale** with **input size**

![alt_text](./images/asymptotic.JPG 'image')
![alt_text](./images/asymptotic2.JPG 'image')

<br>
<hr>
<br>

## **Big-O Notation**
![alt_text](./images/o_rules.JPG 'image')
![alt_text](./images/others.JPG 'image')
![alt_text](./images/others2.JPG 'image')

<br>
<hr>
<hr>
<br>

# **Greedy Algorithms**
- A *greedy choice* is called **safe move** if there is an optimal solution consistent with this first move. 

![alt_text](./images/greedy5.JPG 'image')
![alt_text](./images/greedy6.JPG 'image')

## **Largest Number**
![alt_text](./images/greedy.JPG 'image')

## **Car Fueling**
![alt_text](./images/greedy2.JPG 'image')

## **Car Fueling - Implementation and Analysis**
![alt_text](./images/greedy3.JPG 'image')
![alt_text](./images/greedy4.JPG 'image')

## **Celebration Party Problem**
Orginal Problem:

![alt_text](./images/party.JPG 'image')

Naive Approach:
- O(2^n)

![alt_text](./images/party2.JPG 'image')

Efficient Algorithm:
- O(n) (O(nlogn) if sorting is need to be completed first)

![alt_text](./images/party3.JPG 'image')

<br>
<hr>
<hr>
<br>

#  **Divide & Conquer**
- Break down the problem:

![alt_text](./images/divide_conquer.JPG 'image')
![alt_text](./images/divide_conquer4.JPG 'image')
![alt_text](./images/divide_conquer5.JPG 'image')

- Must be of the **same type**

![alt_text](./images/divide_conquer2.JPG 'image')

- Also not overlapping:

![alt_text](./images/divide_conquer3.JPG 'image')

<br>
<hr>
<br>

## **Binary Search**
[Helpful link](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)

- Recursive Version:

![alt_text](./images/binary_search.JPG 'image')

- Iterative Version:

![alt_text](./images/binary_search3.JPG 'image')

- Runtime of binary search

![alt_text](./images/binary_search2.JPG 'image')

<br>
<hr>
<br>

## **Polynomial Multiplication**
![alt_text](./images/polynomial.JPG 'image')

- Naive Approach:

![alt_text](./images/polynomial2.JPG 'image')


- Divide & Conquer Algorithm (Naive D&C):

![alt_text](./images/polynomial3.JPG 'image')
![alt_text](./images/polynomial4.JPG 'image')
![alt_text](./images/polynomial5.JPG 'image')


- Divide & Conquer Algorithm (Fast D&C):

![alt_text](./images/polynomial6.JPG 'image')
![alt_text](./images/polynomial7.JPG 'image')
![alt_text](./images/polynomial8.JPG 'image')

<br>
<hr>
<br>

## **Master Theorem**
![alt_text](./images/master.JPG 'image')
![alt_text](./images/master2.JPG 'image')
![alt_text](./images/master3.JPG 'image')

![alt_text](./images/master4.JPG 'image')

<br>
<hr>
<br>

## **Sorting**
[Visualization](https://www.toptal.com/developers/sorting-algorithms)
[Helpful Link](https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/sorting)

## **Selection Sort**
![alt_text](./images/selection.JPG 'image')
![alt_text](./images/selection2.JPG 'image')

## **Merge Sort**
![alt_text](./images/merge.JPG 'image')
![alt_text](./images/merge2.JPG 'image')
![alt_text](./images/merge3.JPG 'image')

## **Count Sort**
![alt_text](./images/count.JPG 'image')
![alt_text](./images/count2.JPG 'image')
![alt_text](./images/count3.JPG 'image')

## **Quick Sort**
[Helpful link](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort)
- Worse Case (Unbalanced partitions): O(n**2)
- Best Case (Balanced partitions): O(nlogn)

![alt_text](./images/quick.JPG 'image')
![alt_text](./images/quick2.JPG 'image')
![alt_text](./images/quick3.JPG 'image')
![alt_text](./images/quick4.JPG 'image')

## **Quick3 Sort**
![alt_text](./images/quick_3.JPG 'image')


<br>
<hr>
<hr>
<br>

# **Dynamic Programming**
[Helpful Link](https://www.cs.usfca.edu/~galles/visualization/DPChange.html)
[Additional Slides](https://www.dropbox.com/s/qxzh146jd72188d/dynprog.pdf?dl=0)
[Advanced Reading](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/06-sparsedynprog.pdf)

![alt_text](./images/dp.JPG 'image')
![alt_text](./images/dp2.JPG 'image')
![alt_text](./images/dp3.JPG 'image')
![alt_text](./images/dp4.JPG 'image')
![alt_text](./images/dp5.JPG 'image')

<br>
<br>

## **Alignment Game**
![alt_text](./images/alignment_game.JPG 'image')
![alt_text](./images/alignment_game2.JPG 'image')
![alt_text](./images/alignment_game3.JPG 'image')
![alt_text](./images/alignment_game4.JPG 'image')
![alt_text](./images/alignment_game5.JPG 'image')

<br>

## **Edit Distance**
[Edit Distance Calc](http://www.let.rug.nl/kleiweg/lev/)

![alt_text](./images/edit_distance.JPG 'image')
![alt_text](./images/edit_distance2.JPG 'image')
![alt_text](./images/edit_distance3.JPG 'image')

## **Edit Distance Example**
![alt_text](./images/edit_distance4.JPG 'image')
![alt_text](./images/edit_distance5.JPG 'image')
![alt_text](./images/edit_distance6.JPG 'image')

## **Optimal Alignment**
![alt_text](./images/optimal_edit_distance.JPG 'image')


<br>
<hr>
<hr>
<br>


# **Dynamic Programming 2**
- New Knapsack problem:
    - Cannot take fractional items; either include item or not

![alt_text](./images/knap1.JPG 'image')
![alt_text](./images/knap2.JPG 'image')

## **Knapsack with Repetitions**
![alt_text](./images/knap3.JPG 'image')
![alt_text](./images/knap4.JPG 'image')

## **Knapsack without Repetitions**
![alt_text](./images/knap5.JPG 'image')
![alt_text](./images/knap6.JPG 'image')

## **Memoization**
![alt_text](./images/knap7.JPG 'image')

## **Placing Parentheses**
![alt_text](./images/parentheses.JPG 'image')
![alt_text](./images/parentheses2.JPG 'image')
![alt_text](./images/parentheses3.JPG 'image')
![alt_text](./images/parentheses4.JPG 'image')
![alt_text](./images/parentheses5.JPG 'image')