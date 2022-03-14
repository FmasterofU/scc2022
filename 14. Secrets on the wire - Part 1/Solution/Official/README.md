## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-25%)

Read the challenge text. Think about how FTP works and which is the default FTP port (21).

2. Looking under the hood (-25%)

Download the PCAP file and open it in Wireshark or a similar tool. Find the conversations in the PCAP.

3. Digging deeper (-25%)

Follow the stream. Copy-paste the PASS value as the solution.

4. Complete solution (-100%)

1. Open the PCAP in the Wireshark.
2. Go to Statistics/Conversations, look for TCP statistics
3. For the conversation over port 21, click on it, and then click on Follow Stream
4. Read the PASS and paste it in the submission form/box.
# Lessons learned:

    -   Wireshark is the leading packet capture (PCAP) analytics tool.
    -   If the network traffic was not encrypted, then you can extract even passwords and other valuable information from packet captures.
    -   [CyberChef - The Cyber Swiss Army Knife](https://cyberchef.org/) is an excellent online resource for experimenting with cryptographic algorithms and different encoding techniques.