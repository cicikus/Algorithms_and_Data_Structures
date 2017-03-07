datatype intlist = Nil | Cons of (int * intlist)

fun reverse(list: intlist): intlist = 
	case list of Nil => Nil
		| Cons(hd, tl) => append(reverse(tl), Cons(hd, Nil))