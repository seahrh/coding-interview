![default_workflow](https://github.com/seahrh/coding-interview/actions/workflows/default.yml/badge.svg?branch=master)

Coding interview questions and solutions in Python 3
=====================================================

Accepted / Tested solutions in Python 3.12

Great question. Let’s dissect **branch and bound**, **backtracking**, and **recursion**—three classic approaches that are often confused, but have distinct philosophies.

---

## At a Glance

| Technique         | Definition                                                                                           | Used For                        | Key Feature              | Typical Implementation   |
|-------------------|------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------|-------------------------|
| Backtracking      | Systematically searches for a solution by trying choices and undoing ("backtracking") when needed.   | Constraint satisfaction, puzzles | Explores all possibilities| Often recursion, maybe iteration |
| Branch and Bound  | Optimizes search by “bounding” away parts of the search space that can’t lead to a better solution.  | Optimization problems            | Pruning/Bounding         | Often recursion, maybe iteration |
| Recursion         | A way of calling a function from itself to solve subproblems.                                        | Many algorithm types             | Function calls itself    | Foundation for both above |

---

## More Precise Definitions & Comparisons

### 1. **Recursion**
- **WHAT:**
  A programming technique; a function calls itself to break down a problem.
- **WHERE USED:**
  Everywhere: sorting, trees, graph traversals, and yes, backtracking and branch & bound.
- **HOW:**
  Handles repeated or nested work elegantly.

### 2. **Backtracking**
- **WHAT:**
  An **algorithm**; systematically explores possible options, *backtracking* (undoing) when a dead-end is hit.
- **WHERE USED:**
  Puzzle solving (Sudoku, N-Queens), path-finding, combinatorial search (generating permutations/combinations).
- **HOW:**
  Usually via recursion—each call tries options, and “backs out” upon failure. But can be iterative.

- **Key Point:**
  Backtracking explores every possible solution, but only goes forward if current choices don't violate constraints.

### 3. **Branch and Bound**
- **WHAT:**
  A **strategy** for combinatorial optimization, like finding maxima/minima (travelling salesman, knapsack).
- **WHERE USED:**
  Problems where you want “the best” solution, not *any* solution.
- **HOW:**
  Branches like backtracking, but also calculates bounds to *prune* search—if a partial solution can’t possibly improve the current best, ignore (prune) it.

- **Key Point:**
  Pruning saves time by *never* visiting bad options. Often combined with heuristics or estimates.

---

## Simple Example: N-Queens

- **Backtracking:**
  Try to place queens, back out when one can’t be placed legally.
- **Branch and Bound:**
  Same as above, but if you *know* (with math or logic) that a partial placement *can’t* lead to a solution, skip every subtree below.

---

## Real-world Significance

- **Backtracking**: Good for exhaustive search under constraints.
- **Branch and Bound**: Good for speeding up optimization—sometimes skips 99% of search tree.
- **Recursion**: Essential tool for both, but *not* a strategy itself—just helps implement them.

---

## In Summary

- **Recursion** = programming pattern.
- **Backtracking** = strategy to explore options and “undo.”
- **Branch and Bound** = advanced strategy that “prunes” bad options for efficiency.

END
