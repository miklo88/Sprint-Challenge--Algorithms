#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Answer and why: O(n) - The runtime is dependent on size of n.

b) Answer and why: O(n^2) - Giveaway is the two loops that are nested.

c) Answer and why: O(n) - A recursive call on the bunnies. A constant variable, constant output.

## Exercise II

UPER - ANSWER
so if an egg is dropped above floor f in a building it will break
if it is dropped below floor f it will not break. f is our midpoint.

-What I need to do is find the magic floor of F. Which would be our midpoint in our Quicksort Algo. Basically where the first floor of breaking an egg happens and the last when not breaking an egg happens
IF/ELSE

- If the egg doesn't break we need to keep going up floors. So we would +1 increment up every floor until the egg breaks.
- Else the egg does break. We need to go down a floor until it doesn't break. -1 decrement down a floor.

-Based on incrementing up until the egg breaks = decrementing until the egg doesn't break we will find the

O(log n) Runtime can depend on how tall this builiding is.
