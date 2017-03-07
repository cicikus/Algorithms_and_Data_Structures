fun print_list(x: int list) = app (fn i => print(Int.toString i ^ " ")) x;

print_list([1, 2, 3]);
print("\n");