
'''
The decimal system uses the digits 0-9, the binary system uses the digits 0 and 1, and the hexadecimal system uses the digits 0-9 and the letters A-F.  The ternary system is a base-3 numeral system that uses the digits 0, 1, and 2.

Given a number *n*, write a function that generates all *n*-digit ternary numbers.
 

EXAMPLE(S)
Numbers starting with zero shouldn't normally be included but the ternary representing the zero value is a valid 1-digit ternary. No other strings should start with a "0"!

generateNDigitTernaries(1) == ["0","1","2"]
generateNDigitTernaries(2) == ["10","11","12","20","21","22"]

generateNDigitTernaries(3) == ["100", "101", "102", "110", "111", "112" ...]

generateNDigitTernaries(4) == ["100", "101", "102", "110", "111", "112" ...]

 

FUNCTION SIGNATURE
function generateNDigitTernaries(n) {
def generateNDigitTernaries(n: int) -> list[str]:


'''


function generateNDigitTernaries(n) {
    const track = []
    const res = []

    function helper() {
        if (track.length == n) {
            res.push(track.join(""))
            return
        }

        for (let i=0
             i < 3
             i++){
            if (!track & & i === 0) {
                continue
            }
            track.push(i)
            helper()
            track.pop()
        }
    }

    helper()
    return res
}

console.log(generateNDigitTernaries(2))
console.log(generateNDigitTernaries(3))
console.log(generateNDigitTernaries(4))
