## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-25%)

Your goal is to find the amount of BTC transferred at 8:21pm on February 20th, 2022 from a scrambled bitcoin address. The amount can be retrieved using two approaches: one is to search block chain data online, and the second is to debug the binary code and retrieve it from memory during its execution.

Note: Unscramble the given BTC address first.

2. Let's try something quite simple (-25%)

We look for blockchain records for transactions made at 8:21pm on February 20th, 2022. Visit https://www.blockchain.com/explorer and perform the search.

The answer is found at following URL: https://www.blockchain.com/btc/tx/3196f0e198a370db53483ae5b5c337f9ce52c20c81f3db60cb496ed066ef3b85

The amount of BTC transferred at 8:21pm on February 20th, 2022 from BTC address `1E5SyMx6xbLo2W2f8Eih9bnGUf3Ud7rgjW` is `39.53373831`.

3. Find the amount by reversing the binary file (-25%)

Using a debugger of your choice (e.g. GDB), start debugging the given binary file.

Once loaded into the debugger, we put a breakpoint on program entry points (that is, Main function) and then run the binary.

```gdb
(gdb) b *main
(gdb) run
```
Upon running, the binary enters paused mode when it reaches the first breakpoint. We then disassemble the program code to find the line containing the assembler instructions used to compare values `cmp`. The two lines we found are shown below. The first one is for the first input comparison and second is for the second input comparison. Since we answer the first question in this step we will focus on the first line, put a breakpoint on it, and continue running the program that will enter paused mode when the second breakpoint is reached.

```gdb
(gdb) disass main
First Line
0x00005555555554d8 <+308>:    cmpl   $0x0,-0x4(%rbp)
Second Line
0x0000555555555573 <+463>:    cmpl   $0x0,-0x4(%rbp)
(gdb) b *0x00005555555554d8
(gdb) c
```
We display the values of the CPU registers after each step, and we focus on the `RSP` register value. The value contains memory addresses that we need in order to read its content - that is, the value of real BTC amount transferred. The flag is stored in multiple variables and reassembled at the moment of program execution. That is why we cannot find the first flag using static analytics of binary program code to extract strings.

```gdb
(gdb) info registers
rsp            0x7fffffffdef0
(gdb) x/s 0x7fffffffdef0
0x7fffffffdef0:    "39.53373831"
```

4. Complete solution (-100%)

1. Debug the binary using GDB or a similar tool.
2. Insert a breakpoint into the Main function.
3. Execute the binary step-by-step.
4. Investigate the values of the CPU registers at key points of execution, e.g. 'cmp' instruction.
5. Find the BTC amount which is not a static value, but created based on the values of multiple variables.
# Lessons learned:

    -   Bitcoin transactions can be reviewed here https://www.blockchain.com/explorer
    -   Linux binaries are easy to debug with GDB.
    -   Breakpoints allow you to investigate the values of variables during execution.
    -   CPU registers often contain interesting information which can only be glimpsed while executing a binary.