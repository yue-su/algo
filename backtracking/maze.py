def printSubSeq(string):
  x = 0

  def helper(string, seq=""):
    nonlocal x

    if not string:
      x += 1
      if x == 5: print(seq)
      return
    
    helper(string[1:], seq + string[0])  # Include curr char
    helper(string[1:], seq)  # Exclude curr char

  helper(string)

print(printSubSeq("JOHN"))