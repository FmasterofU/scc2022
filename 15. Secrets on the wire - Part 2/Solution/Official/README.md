## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-16%)

Read the challenge text. Think about how FTP works and which is the default port (21 and 20).

2. Looking under the hood (-16%)

Find the conversations in the PCAP. Follow the stream over port 20 (FTP data transfer). Save the file from the stream.

3. Digging deeper (-16%)

Identify the sent file format. Can you see any data/info in it?

4. Trying something simple (-16%)

Although Vigenere works with capital letters, use the file name as it is written.

5. Going even deeper (-16%)

Use Cyberchef to encrypt and/or decrypt data.

6. Complete solution (-100%)

1. Open the PCAP in the Wireshark.
2. Go to Statistics/Conversations, look for TCP statistics.
3. For the conversation over port 21, click on it, and then click on Follow Stream.
4. Under STOR find the name and type of the file transfered.
5. Go back to conversation over port 20, and click on the follow stream.
6. Click to "Show and save data as" - Raw, and then Save As and save it under its name (point 5).
7. Go to cyberchef and in the input field paste filename (without .zip). Find the Vigenere encrypt box, and move it to the Recipe field. Paste the same filename into the Key field. Read/copy the output.
8. Open the transferred file, click on the compressed file and enter the password - point 8.
9. Read the flag and submit it via the flag submission form/box.
# Lessons learned:

    -   Wireshark - the most capable packet capture analytics tool.
    -   [CyberChef - The Cyber Swiss Army Knife](https://cyberchef.org/) is an excellent online resource for experimenting with cryptographic algorithms and different encoding techniques.