datatype 'a DList = Nil
	| DNode of {elem:'a,
				prev:'a DList,
				next:'a DList};

fun append(lst: 'a DList) = #elem(???);

val empty_dlist = Nil;
val single_dlist = DNode {elem=25, prev=Nil, next=Nil};
print(Int.toString(append(single_dlist)) ^ "\n");