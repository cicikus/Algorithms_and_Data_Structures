fun isMember(lst, element) = if lst = [] then false
	else if element = hd(lst) then true
	else isMember(tl(lst), element);

print(Bool.toString(isMember([1, 2, 3], 3)) ^ "\n");
print(Bool.toString(isMember([1, 2, 3], 0)) ^ "\n");
print(Bool.toString(isMember([], 3)) ^ "\n");