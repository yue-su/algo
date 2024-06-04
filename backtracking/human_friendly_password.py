'''
❓ PROMPT
Given a list of words *L* and a maximum password length *maxLength*, generate all valid human-friendly passwords using *L* that are at most *maxLength* long with the following rules. This was inspired by https://xkcd.com/936/

We can generate a human-friendly password by concatenating several words from a list of words (e.g. *correct horse battery staple*). Define a human-friendly password to be a string made up of words such that:

1. The password is comprised of only words from the list
2. Each word is separated by a space between them
3. Each word is used at most once
4. The password is can be at most *maxLength* long when including spaces.

Example(s)
These are valid human-friendly passwords generated from the list:
[apple, bat, cheese, dog]
- apple bat cheese dog
- apple cheese bat
- dog apple
- cheese bat dog

However, there's a maxLength value that can be passed in that limits the possible combinations:
generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 10) ==
[
  "apple",
  "dog",
  "zebra",
  "apple dog",
  "dog apple",
  "dog zebra",
  "zebra dog"
]
"zebra apple" and "apple zebra" are skipped because they're 11 chars.
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function generateAllHumanFriendlyPasswords(words, maxLength) {
def generateAllHumanFriendlyPasswords(words: list[str], maxLength: int) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def generateAllHumanFriendlyPasswords(words: list[str], maxLength: int) -> list[str]:
    track = []
    res = []
    used = [False] * len(words)

    def helper():
        password = " ".join(track)
        if 0 < len(password) <= maxLength:
            res.append(password)

        for i in range(len(words)):
            if used[i]:
                continue
            
            used[i] = True
            track.append(words[i])
            helper()
            track.pop()
            used[i] = False

    helper()

    return res

print(generateAllHumanFriendlyPasswords([], 0) == [])
print(generateAllHumanFriendlyPasswords([], 5) == [])
print(generateAllHumanFriendlyPasswords(["horse"], 0) == [])
print(generateAllHumanFriendlyPasswords(["horse"], 4) == [])
print(generateAllHumanFriendlyPasswords(["horse"], 5) == ["horse"])
print(generateAllHumanFriendlyPasswords(["horse"], 10) == ["horse"])

print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 0) == [])
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 1) == [])
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 3) == ["dog"])
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 5) == ["apple","dog","zebra"])
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 8) == ["apple","dog","zebra"])
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 9) == 
  ["apple","apple dog","dog","dog apple","dog zebra","zebra","zebra dog"])
print(generateAllHumanFriendlyPasswords(
  ["apple", "dog", "zebra"], 10) == 
  ["apple","apple dog","dog","dog apple","dog zebra","zebra","zebra dog"])
print(generateAllHumanFriendlyPasswords(
  ["apple", "dog", "zebra"], 11) == 
  ["apple","apple dog","apple zebra","dog","dog apple","dog zebra","zebra","zebra apple","zebra dog"])
print(generateAllHumanFriendlyPasswords(
  ["apple", "dog", "zebra"], 20) == 
  ["apple","apple dog","apple dog zebra","apple zebra","apple zebra dog","dog","dog apple","dog apple zebra","dog zebra","dog zebra apple","zebra","zebra apple","zebra apple dog","zebra dog","zebra dog apple"])
