fun factorial(0: int) : int = 1
	| factorial (n: int) = n * factorial(n-1);

val result = factorial(5: int);
print(Int.toString result ^ "\n");
print(Int.toString (factorial(4: int)) ^ "\n");