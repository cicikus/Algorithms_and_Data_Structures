fun gcd(a: int, 0:int): int = a
	| gcd (a: int, b: int) = gcd(b, a mod b);


print(Int.toString(gcd(10, 8)) ^ "\n");
print(Int.toString(gcd(20, 5)) ^ "\n");
print(Int.toString(gcd(0, 8)) ^ "\n");
print(Int.toString(gcd(8, 0)) ^ "\n");
print(Int.toString(gcd(3, 1)) ^ "\n");
print(Int.toString(gcd(1, 3)) ^ "\n");