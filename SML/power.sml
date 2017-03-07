exception Undefined;

fun undefined () = raise Undefined;

fun power(0: int, 0: int) = undefined()
	| power(x: int, 0: int): int = 1
	| power(x: int, n: int) = x * power(x, n-1);


print(Int.toString(power(1, 3)) ^ "\n");
print(Int.toString(power(3, 1)) ^ "\n");
print(Int.toString(power(5, 2)) ^ "\n");
print(Int.toString(power(2, 5)) ^ "\n");
print(Int.toString(power(1, 0)) ^ "\n");
print(Int.toString(power(0, 1)) ^ "\n");
print(Int.toString(power(0, 0)) ^ "\n");