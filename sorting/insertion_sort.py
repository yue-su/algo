function sort2(arr) {
  let i = 0

  //recursive while
    function compare(j) {
      if (j == 0 || (arr[j] >= arr[j - 1])) {
        return;
      }
      [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];

  return compare(j--);
}

function iterate(i) {
  if (i >= arr.length - 1) {
    return arr;
  }

  let j = i + 1;
  compare(j);

  return iterate(i++);
}

return iterate(0);
}