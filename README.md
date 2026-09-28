# Lab 03 - Basic Python: Strings, Lists, and Dictionaries

In this lab, we'll practise the tools from this week's lectures: pulling apart and
building up **strings** and collecting values in **lists** (the three core parts),
with a stretch that builds a **dictionary**. You'll write four small functions and
check them against a set of automated tests.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 03 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 03 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** Your own account
   - **Repository name:** `lab03-csci1030u`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.  For the TA to see your work, you will need to add them as a collaborator.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab03-your-username
cd lab03-your-username
```

## Instructions

You will edit **`lab03.py`**. The four function definitions are already written for
you - **do not rename them or change their arguments**, because the tests call them by
name. Replace each `pass` with your code, and use **`return`** to send the answer back
(not `print`).

### Part 1 - `pig_latin(word)`

Write the body of `pig_latin`, which takes a single lowercase `word` and returns its
Pig Latin form:

- if the word starts with a **vowel** (`a`, `e`, `i`, `o`, `u`), add `"way"` to the end;
- otherwise, move the **first letter to the end** and add `"ay"`.

Hint: string slicing helps - `word[0]` is the first letter and `word[1:]` is the rest.

```python
pig_latin("banana")   # returns "ananabay"
pig_latin("python")   # returns "ythonpay"
pig_latin("apple")    # returns "appleway"
```

### Part 2 - `word_lengths(sentence)`

Write the body of `word_lengths`, which takes a `sentence` and returns a **list**
containing the length of each word. Words are separated by spaces.

Hint: `sentence.split()` breaks the sentence into a list of words. Start with an empty
list and `.append()` each word's length as you loop.

```python
word_lengths("the quick brown fox")   # returns [3, 5, 5, 3]
word_lengths("hello")                 # returns [5]
word_lengths("")                      # returns []
```

### Part 3 - `reverse_words(sentence)`

Write the body of `reverse_words`, which returns `sentence` with the **order of its
words reversed** (the letters within each word stay the same).

Hint: `sentence.split()` gives you a list of words, and you can reverse a list with a
slice (`words[::-1]`). Then join the words back together with spaces.

```python
reverse_words("the quick brown fox")   # returns "fox brown quick the"
reverse_words("hello")                 # returns "hello"
reverse_words("a b c")                 # returns "c b a"
```

### Part 4 - `letter_counts(text)`  *(stretch - optional)*

Write the body of `letter_counts`, which returns a **dictionary** mapping each letter
to how many times it appears in `text`. Ignore case (treat `A` and `a` as the same
letter) and ignore anything that isn't a letter (spaces, punctuation, digits).

Hint: loop through `text.lower()`; `ch.isalpha()` tells you whether a character is a
letter. Build the dictionary as you go - the first time you see a letter, start its
count at 1; after that, add 1.

```python
letter_counts("hello")         # returns {'h': 1, 'e': 1, 'l': 2, 'o': 1}
letter_counts("Mississippi")   # returns {'m': 1, 'i': 4, 's': 4, 'p': 2}
letter_counts("a a a")         # returns {'a': 3}
```

This part is optional - the three parts above are the core of the lab. Do it if you
have time.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

Read the output closely - a failing test tells you which function is wrong and shows
what it expected versus what your code returned. Fix, save, and run `pytest` again.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 03 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 03 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab03-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
