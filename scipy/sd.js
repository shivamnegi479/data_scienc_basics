
	// Taking input as an array A having some elements.
	var A = [ 1, 2, 3, 4, 5 ];
	
	// Mapping with map function.
	b = A.map(x => [x * 3]);
	console.log(b);
	
	// Mapping and flatting with flatMap() function.
	c = A.flatMap(x => [x * 3]);
	console.log(c);
	
	// Mapping and flatting with flatMap() function.
	d = A.flatMap(x => [[ x * 3 ]]);
	console.log(d);

