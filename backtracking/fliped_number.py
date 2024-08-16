def underlineMistakenNumbers(upperBound: int = 650) -> list[int]:
    numbers = [0, 1, 6, 8, 9]
    track = []
    res = []

    def flip(track):
        nums = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        number = 0
        flipped = 0
        for i in range(len(track)):
            flipped += nums[track[i]] * 10 ** i

        for i in range(len(track)-1, -1, -1):
            number += track[i] * 10 ** (len(track) - 1 - i)

        return [number, flipped]

    def helper():
        if len(track) > 3:
            return

        number, flipped = flip(track)

        if len(str(flipped)) == len(track) and flipped <= upperBound and number <= upperBound and flipped != number:
            res.append(number)

        for i in range(5):
            if not track and numbers[i] == 0:
                continue
            track.append(numbers[i])
            helper()
            track.pop()

    helper()

    return res


rest = underlineMistakenNumbers(650)
print(sorted(rest))
print([6, 9, 16, 18, 19, 61, 66, 68, 81, 86, 89,
      91, 98, 99, 109, 119, 161, 191, 601, 611])
