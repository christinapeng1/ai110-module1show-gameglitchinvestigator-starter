# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
Bug #1: The hints were backwards. Expected behavior is to be told to go higher if the secret number is higher than my guess. However, I was told to 'go lower' when the secret number was higher than my guess, and vice versa.

Bug #2: No longer able to submit a guess after winning and then pressing New Game. Expected behavior is to be able to submit a guess and continue a new round, but actual behavior was nothing happened after clicking 'Submit Guess'.

Bug #3: The secret number in easy mode should range from 1 to 20, but it has a range from 1 to 100.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code.

Correct example: One specific glitch I used Claude to investigate was why the hints were backwards. Claude suggested that the bug is in the `check_guess` function. Here was its suggested fix:

```
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "Correct! 🎉"
    elif guess > secret:
        return "Too High", "Go lower!"
    else:
        return "Too Low", "Go higher!"
```
The AI suggestion about the logic being inverted was correct. I verified this by updating the `check_guess` code. Note, I did have to make tweaks to Claude's original suggestion to get it to run. 

Incorrect example: I asked Claude to investigate why I could not submit a guess after winning, and Claude was very confused. It responded by saying a lot of functions in my code raise the NotImplementedError. While that is true, Claude was distracted from investigating my actual bug. I verified this by looking through my code.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed when I playtested it and it worked the way I expected. I also double checked by check_guess function by writing tests in `test_game_logic.py`.

One test I ran was what the expected outcome was when my guess was 75, but the secret was 50. The expected value should be 'Too High', so I made a pytest to validate that it indeed returns 'Too High'. It showed me that my code was handling this case successfully.

AI did not really help me understand the tests, it just told me the answers directly. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?



## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
