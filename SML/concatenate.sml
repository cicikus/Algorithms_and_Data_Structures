fun concat(x, y) = if x = [] then y
	else hd(x)::concat(tl(x), y);


concat([1, 2, 3], [4, 5]);
print(Int.toString(hd(concat([1, 2, 3], [4, 5]))) ^ "\n");
