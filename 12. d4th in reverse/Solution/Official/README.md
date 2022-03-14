## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-16%)

You were invited by a company to investigate a cyber attack which occurred during the Summer months of 2020. The hackers left behind various artifacts. Among them, you found an interesting binary file which you decided to investigate. You know that it was a novel malware, but you are not sure whether it was designed to target Windows or Linux workstations.

2. Looking under the hood (-16%)

Open the file in a text editor and check its contents. Notice that in the plaintext values you can see a reference to a Python source file with a .py extension.

3. Digging deeper (-16%)

Check out online the tools available to compile Python code. Read about Cython.

4. Trying something simple (-16%)

Notice that Cython code will not run on any workstation, as the binary was created for a specific platform. This is similar as if you'd try to run a Windows EXE on a Linux box without any emulation tools - it would not work.

5. Going even deeper (-16%)

Go back to the challenge text. Notice that the text mentions the Summer months of 2020. Look for a Linux distribution which was used by hackers in that period (Kali 2020.2a).

6. Complete solution (-100%)

Copy the binary into a Kali 2020.2a box and run ith with Python version 3. Observe the output.

# Lessons learned:

    -   Python code can be obfuscated when compiled to binaries.
    -   Python code can be statically compiled by Cython.
    -   Cython code is platform specific. It will not run on a different platform, even though the original, pure Python source code would be cross-platform.