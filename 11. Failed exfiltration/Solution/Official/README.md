## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-16%)

You were called in to investigate the traces left behind attackers who successfully hacked your employer's system and supposedly managed to exfiltrate information. During your investigation you received a document captured in network traffic. Your task is to investigate this artifact and find out if any information was exfiltrated.

2. Looking under the hood (-16%)

Notice that although the document seems empty, there are white space characters in it.

3. Digging deeper (-16%)

Analyze the types of whitespaces. Show them in Word. If the document is in PDF or other format, attempt to load it into Word (or another text processor) to actually be able to investigate its elements character-by-character.

4. Trying something simple (-16%)

Notice that the couple of leading whitespaces are actually CRLF. It might mean that the attackers wanted to hind something below these whitespaces.

5. Going even deeper (-16%)

Analyze the whitespace sequence near the bottom of the page. Notice that there seems to be an array of different whitespaces. Attempt to find what can be the meaning of the first character sequence.

6. Complete solution (-100%)

Notice that the character sequence near the bottom of the document is a sequence of whitespaces. Identify this sequence as Morse code. Identify the whitespace which acts as a separator. Split the sequence around the separators and use an online tool to decode the text character by character.

# Lessons learned:

    -   Humans do not see white spaces. If you can't see it, it does not necessarily mean it is not there. Look harder.
    -   Morse code is simple and can be represented with whitespaces as well.