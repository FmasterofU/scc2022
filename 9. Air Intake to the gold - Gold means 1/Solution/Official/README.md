## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-20%)

Title: Air Intake to the gold. Gold means 1.
Prerequisites: SCS_Red Bull_SteganographyChallenge.jpg
Type: Steganography

**Steganography: The root "steganos" comes from the Greek "hidden" and "graph" for "to write". Literally, this means "hidden writing".** As the main purpose is to hide a secret inside something that is not a secret, let's see how it works. It has been used for centuries, but these days, hackers and IT people have digitized this word. As steganography is the tale of Man and Machine, we decided to offer you a picture that shows also a similar tale. Watch as Max Verstappen, the RB7, and Alpine Ski Racer Aksel Lund Svindal meet up for a showdown in Kitzbühel as they take on the famous Streif. See the tale here: https://www.youtube.com/watch?v=gkwoK0EfKdc

If the pinnacle of motorsport met the pinnacle of winter sports, how do you compare between Formula 1 at the Red Bull Ring in Austria and the World Cup downhill on the Streif? Speed, g-forces, track record, or height differences - there are plenty of similarities... The picture describes the essence of competition and the beauty of Austria, the home of Red Bull. Would you be creative enough to discover the flag hidden in this shot?

2. First idea while doing steganography (-20%)

Similar to Formula 1 - a picture contains also something else behind the vehicle. It can be beautiful with colors but there is something else. The file format means something, as the engine behind a vehicle. Read the picture as you would read a car characteristics - not only observing with eyes but also with some tools. We can try to open the picture with many tools including:

    -   exiftool
    -   strings (Unix command)
    -   binwalk
    -   ...
You can naturally look at some steganography tools that can help you to observe the behind the scene of a .png/.jpeg file. We can recommend the article [of 0xRick](https://0xrick.github.io/lists/stego) for further learning around stenography.

3. Trying something simple (-20%)

You should get inspired by the title of the challenge itself. As it says: `Air Intake to the gold. Gold means 1.`, we should maybe think about it.

We can obviously understand that as with every sport, you need to breathe and take air to win, in Formula 1, the engine needs also some air Air – or rather oxygen. This is an essential part of the combustion process and having enough airflow at maximum possible pressure will maximize the amount of torque produced. Delivering this optimum therefore depends on the constituent parts of the system.

Firstly, the shape of the airbox governs how much air can be taken into the engine unit. If the inlet is too small, the engine will be ‘starved’ of air and therefore produce less power. If it is too large, however, the engine will not be more efficient on a linear scale – more air does not mean more power; exactly the correct amount must be introduced. This relates back to trying to try to keep the total pressure as high as possible. To achieve this we need to keep as much dynamic pressure created from the car speed as possible. This is of course a compromise with the adverse effect on the aerodynamics of having a giant airbox, which would create turbulence for the rear wing so we look to the airbox to keep as high a percentage of dynamic pressure as we can.

Watch close to the Air Intake of Formula 1 in the picture, you should be able to the rectangle with blue and yellow pixels, what do those mean? This is certainly a message.

4. Planning the attack (-20%)

The first idea in mind is reading the blue or the yellow as a word. Could it mean something? Does it help? Maybe a word in other languages? Japanese? Cyrillic word? Indian word? Looking for something is often the best way to find it.

```
“Wir mussen wissen. Wir werden wissen. (We must know. We will know.) [Inscribed on his tomb in Gottingen.]”
― David Hilbert
```

5. Complete solution (-100%)

Another idea would be to think about the computer's language. What about bits 1-0-1-1-..? As we understand each color is associated with a bit, we have to extract the bit one by one (or we should create a script that will extract the color for us).

Remind the title? "Gold means 1". The color of Gold is close to the Yellow color - in the rectangle, you can see the yellow color - it must be associated with the bit value 1. Therefore, the blue color is associated with the bit value 0. By extracting one by one, we get the following bits group:

```0010010001111011010100100100001001011111010100110100001101010011010111110101001101010100010001010100011101111101```
You can now use a tool to convert binary to ASCII (with a command line in the terminal or with a tool) to retrieve the flag.

Of course, this is far from being a real case as it would be really simple. Consider this challenge more as a puzzle to solve than a real-world case.

# Lessons learned:

    -   Reading ASCII characters is pretty natural but computers only understand bits
    -   A hidden message could be anywhere, in the file itself or elsewhere