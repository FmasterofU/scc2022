## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-20%)

Your objective is to find the BTC balance of a scrambled bitcoin address at the time a BTC transfer was made at 8:21pm on February 20th, 2022. This value can only be found using a debugger or other tool for reverse engineering.

2. Let's try something quite simple (-20%)

Using your debugger of choice (e.g. GDB) start debugging the given binary file.

Add a breakpoint as defined below:

```gdb
(gdb) b *0x0000555555555573
(gdb) c
```
3. Let's see what we have (-20%)

At this moment, we have the value of the BTC balance in stack memory. Let's first check the CPU registers. We display the values of the CPU registers and focus on the RBP register value. It contains the memory address we need to read. The content of the `RBP` address is not usable, meaning the variable for comparison is somewhere at lower memory addreses, for example `RBP -8`, `-16`, etc.

```gdb
(gdb) info registers
rbp            0x7fffffffdf70
(gdb) x/s 0x7fffffffdf70
0x7fffffffdf70:    "\300UUUUU"
```
4. Dig deeper (-20%)

We change the address to lower memory addresses DWORD’s space and read the content, where we will find the BTC balance amount.

```gdb
(gdb) x/s 0x7fffffffdf60
0x7fffffffdf60:    ""
(gdb) x/s 0x7fffffffdf50
0x7fffffffdf50:    "76.31342913"
```
5. Complete solution (-100%)

You can complete the challenge as follows.

1. Debug the binary using GDB or a similar tool
2. Insert a breakpoint and execute step-by-step
3. Investigate the CPU registers
4. Focus on the `RBP` register value which contains a memory address
5. Notice that the value at memory location `RBP` is not what we need
6. Investigate the memory address below the address the `RBP` register value points to (`-8`, `-16`, etc)
# Lessons learned:

    -   There is valuable data in binary that is only revealed during dynamic analytics in reverse engineering.
    -   Assembler instructions are key for reverse engineering, especially cmp, generally used in conditional execution.
    -   CPU registers contain key information during debugging sessions.