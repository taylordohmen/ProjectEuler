let prime = function(n) {
	if (n < 2) {return false;}
	if (n === 2) {return true;}
	if (n % 2 === 0) {return false;}
	for (let i = 3; i < Math.sqrt(n) + 1; i += 2) {
		if (n % i === 0) {return false;}
	}
	return true;
}

let max = 0;
let A = undefined;
let B = undefined;
for (let a = -999; a < 1000; a++) {
	for (let b = -1000; b <= 1000; b++) {
		let f = n => n*n + a*n + b;
		let n = 0;
		while (prime(f(n))) { n++; }
		if (n > max) { max = n; A = a; B = b; }
	}
}
console.log(A*B);