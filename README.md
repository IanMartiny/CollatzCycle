# CollatzCycle

Result from [Eliahou](http://www.sciencedirect.com/science/article/pii/0012365X9390052U) gives that we can put a lower bound on the number of elements in a non-trivial cycle of the Collatz iteration (if one exists). 

Using this method we can get system of equations that all must point to the same number. That system is:

```
    24727*a_1 +       75235*b_1 +        50508*c_1 = |S|
    75235*a_2 +      125743*b_2 +       176251*c_2 = |S|
   125743*a_3 +      301993*b_3 +     16785921*c_3 = |S|
   301994*a_4 +    17087915*b_4 +     85137581*c_4 = |S|
 17087915*a_5 +   102225496*b_5 +     85137581*c_5 = |S|
102225496*a_6 +   187363077*b_6 +     85137581*c_6 = |S|
187363077*a_7 +   272500658*b_7 +    357638239*c_7 = |S|
272500658*a_8 +   630138897*b_8 +   9809721694*c_8 = |S|
630138897*a_9 + 10439860591*b_9 + 102768467013*c_9 = |S|
```

With the constraints: `a_i, b_i, c_i` are all non-negative integers, `b_i > 0`, `a_i*c_i = 0` and if `a_i = c_i = 0` then `b_i = 1`.
