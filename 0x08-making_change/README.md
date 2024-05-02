# 0x08. Making Change

## Project Description
In the "Change comes from within" project, you'll delve into the realm of dynamic programming and greedy algorithms by tackling the classic coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to not only devise a correct solution but also ensure its efficiency. Below, you'll find key concepts and resources essential for successfully completing this project.

## Concepts Needed
- **Greedy Algorithms:**
  - Understanding the working principles of greedy algorithms and their suitability for the coin change problem.
  - Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
- **Dynamic Programming:**
  - Basic principles of dynamic programming for solving optimization problems.
  - Understanding overlapping subproblems and optimal substructure in the context of the coin change problem.
- **Algorithmic Complexity:**
  - Analyzing time and space complexity of algorithms.
  - Striving for solutions with lower complexity to meet runtime constraints.
- **Problem-Solving Strategies:**
  - Breaking down the problem into smaller, manageable sub-problems.
  - Comparing iterative vs recursive approaches to dynamic programming.
- **Python Programming:**
  - Manipulating lists and utilizing list comprehensions.
  - Implementing functions with efficient looping and conditional statements.

## Resources
- **Python Official Documentation:**
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)
- **GeeksforGeeks Articles:**
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials:**
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jaNZ83Q3QGc) for a visual and step-by-step explanation of the dynamic programming approach.

## Additional Resources
- **Mock Technical Interview**

## Tasks
### 0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

**Prototype:** `def makeChange(coins, total)`
**Return:** Fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
  - The value of a coin will always be an integer greater than 0
  - You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

