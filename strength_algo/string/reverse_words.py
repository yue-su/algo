""" ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a string, reverse the string word by word.

Note:
• Remove any extra white space(e.g. "b a" -> "a b" // only keep 1 whitespace).
• Remove any leading or trailing white spaces(e.g. " Hi " -> "Hi").

Examples:
• Given a string: "I love programming" // returns: "programming love I"
• Given a string: " " // returns: ""

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

 """


from test_case import Test


def rw(input: str) -> str:
    # Write your code here.
    arr = [item for item in input.split(" ") if item != ""]
    arr.reverse()
    return " ".join(arr)


test = Test()

# Test Cases
test.startProblem("Reverse Words In String")
test.test("world! hello", rw("  hello world!  "), 1)
test.test("", rw(""), 2)
test.test("", rw("   "), 3)
test.test("a", rw("  a"), 4)
test.endProblem()
