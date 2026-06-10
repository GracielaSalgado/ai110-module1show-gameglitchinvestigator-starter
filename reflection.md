# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started? 

When I tried to guess the number the number was below 0 when it was supposed to be 1-100. Or the opposite where the number was bigger than 100. The "New Game" button didn't work either, when you press it, it does not restart the game. Instead it changes teh number of attempts and does not allow you to submit your answer.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |

| Clicks the "Restart Game" Button | Restarts the game | Gives more attempts but doesn't restart | no error stated but it does say a new game has started |

| When guessing the number, the hint will either tell you higher or lower than the secret number |The hint gives an accurate lower or higher answer | gives inaccurate hints of whether the number being guessed is lower or higher|No error shown, the hint just not changes|

|If the input is valid between 1-100| When entering a number it should be a valid number between 1-100 | You can enter numbers higher than 100 or lower than 1 even going into the negatives | No error shown |

## 2. How did you use AI as a teammate?

Copliot to help understand the format of the bug answers. A few of the suggestions were true when I went back to play the game. Such as the attemps and the hint suggestions. While were correct it was a bit wordy and added things it was not suppose to. 

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

I asked my AI tool to generate a pytest and to specifically target the bug to see if it was really fixed. I used a pytest to test whether the high and low range bug was fixed. It showed that it was fixed but that the code was still buggy. AI did help me design and understand the test by explaining the steps along the way. 

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

I learned that every time you interact with a button or a box or checking a box it runs the entire script from top to bottom. A rerun is how the app remembers things across those reruns. Without it it would wipe everything.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

To try and problem solve the bug myself or to pin point where exactly the bug is. I also want to start creating tests to make sure that my code fixed it. This project definitly helped changed the way I use AI and use AI generated code. 

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
