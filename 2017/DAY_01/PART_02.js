function getCapcha(input) {
  var sum = 0;

  for (var i = 0; i < input.length; i++) {
    var first = input.charAt(i);
    var second;

    var middle = input.length / 2;

    if (i < middle) {
      second = input.charAt(i + middle);
    } else {
      second = input.charAt(i - middle);
    }

    if (first == second) {
      sum += parseInt(first);
    }
  }

  return sum; 
}