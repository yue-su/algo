
'''
❓ PROMPT
Implement a stack that returns the most frequent element when the pop() method is called instead of the last element added. In the event of a tie, pop the last element added into the stack.

Example(s)
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

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
class FreqStack:
    def push(val: int) -> None:
        pass

    def pop() -> Optional[int]:
        pass
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class FreqStack:
    def __init__(self) -> None:
        self.max_freq = 0
        self.num_freq = {}
        self.freq_num = {}

    def push(self, val: int) -> None:
        new_freq = self.num_freq.get(val, 0) + 1
        self.num_freq[val] = new_freq

        if new_freq in self.freq_num:
            self.freq_num[new_freq].append(val)
        else:
            self.freq_num[new_freq] = [val]
            self.max_freq = new_freq

    def pop(self):
        if self.max_freq == 0:
            return None
        res = self.freq_num[self.max_freq].pop()
        if len(self.freq_num[self.max_freq]) == 0:
            self.freq_num.pop(self.max_freq)
            self.max_freq -= 1
        self.num_freq[res] -= 1
        return res


freqStack = FreqStack()
freqStack.pop()
freqStack.push(1)
freqStack.push(2)
freqStack.push(1)
freqStack.push(3)
freqStack.push(1)
freqStack.push(1)
print(freqStack.pop())  # 1
freqStack.push(2)
freqStack.push(3)
print(freqStack.pop())  # 1
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3
print(freqStack.pop())  # 3

print(freqStack.num_freq)
print(freqStack.freq_num)
