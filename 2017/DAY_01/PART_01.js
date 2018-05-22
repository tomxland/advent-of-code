var fs = require('fs');

function getCapcha(input) {
  var sum = 0;

  for (var i = 0; i < input.length; i++) {
    var first = input.charAt(i);
    var second;

    if (i == input.length - 1) {
      second = input.charAt(0);
    } else {
      second = input.charAt(i + 1)
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