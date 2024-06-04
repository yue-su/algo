def generateNDigitTernaries(n: int) -> list[str]:
  digits = [str(i) for i in range(n)]
  track = []
  res = []

  print(digits)

  def helper():
    if len(track) == n:
      if track[0] != "0":
        res.append(track.copy())
      return

    for digit in digits:
      track.append(digit)
      helper()
      track.pop()

  helper()

  return res


print(generateNDigitTernaries(3))