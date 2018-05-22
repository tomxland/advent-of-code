var fs = require('fs');

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

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(getCapcha(data))
});