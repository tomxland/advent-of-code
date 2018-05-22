var filename = process.argv[2];

var json = require(filename);

function getSum(obj) {
	sum = 0
	if (Array.isArray(obj)) {
		for (var i = 0; i < obj.length; i++) {
			if (typeof obj[i] == 'number') {
				sum += obj[i]
			}
			else if (typeof obj[i] == 'object') {
				sum += getSum(obj[i])
			}
		}
	} else if (typeof obj == 'object') {
		for (prop in obj){
			if (obj[prop] === "red") {
				return 0
			}
			else if (typeof obj[prop] == 'number') {
				sum += obj[prop]
			}
			else if (typeof obj[prop] == 'object') {
				sum += getSum(obj[prop])
			}
		}
	} else if (typeof obj == 'number') {
		return obj
	}

	return sum
}

console.log(getSum(json));