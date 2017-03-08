datatype intlist = Nil | Cons of (int * intlist)

(* test to see if the list is empty *)
fun is_empty(xs:intlist):bool = 
	case xs of
	 Nil => true
	 | Cons(_,_) => false

(* Return the number of elements in the list *)
fun length(xs:intlist):int = 
	case xs of Nil => 0
	| Cons(i:int,rest:intlist) => 1 + length(rest)

(* Notice that the case expressions for lists all have the same
 * form -- a case for the empty list (Nil) and a case for a Cons.
 * Also notice that for most functions, the Cons case involves a
 * recursive function call. *)
(* Return the sum of the elements in the list *)
fun sum(xs:intlist):int = 
	case xs of Nil => 0
	| Cons(i:int,rest:intlist) => i + sum(rest)

(* Create a string representation of a list *)
fun toString(xs: intlist):string = 
	case xs of Nil => ""
	| Cons(i:int, Nil) => Int.toString(i)
	| Cons(i:int, Cons(j:int, rest:intlist)) => Int.toString(i) ^ "," ^ toString(Cons(j,rest))
	
(* Return the first element (if any) of the list *)
fun head(is: intlist):int = 
	case is of Nil => raise Fail("empty list!")
	| Cons(i,tl) => i

(* Return the rest of the list after the first element *)
fun tail(is: intlist):intlist = 
	case is of Nil => raise Fail("empty list!")
	| Cons(i,tl) => tl

(* Return the last element of the list (if any) *)
fun last(is: intlist):int = 
	case is of Nil => raise Fail("empty list!")
	| Cons(i,Nil) => i
	| Cons(i,tl) => last(tl)

(* Return the ith element of the list *)
fun ith(is: intlist, i:int):int = 
	case (i,is) of (_,Nil) => raise Fail("empty list!")
	| (1,Cons(i,tl)) => i
	| (n,Cons(i,tl)) =>
	if (n <= 0) then raise Fail("bad index")
	else ith(tl, i - 1)

(* Append two lists:  append([1,2,3],[4,5,6]) = [1,2,3,4,5,6] *)
fun append(list1:intlist, list2:intlist):intlist = 
	case list1 of Nil => list2
	| Cons(i,tl) => Cons(i,append(tl,list2))

(* Reverse a list:  reverse([1,2,3]) = [3,2,1].
 * Notice that we compute this by reversing the tail of the
 * list first (e.g., compute reverse([2,3]) = [3,2]) and then
 * append the singleton list [1] to the end to yield [3,2,1]. *)
fun reverse(list:intlist):intlist = 
	case list of Nil => Nil
	| Cons(hd,tl) => append(reverse(tl), Cons(hd,Nil)) 

fun inc(x:int):int = x + 1;
fun square(x:int):int = x * x;

(* given [i1,i2,...,in] return [i1+1,i2+1,...,in+n] *)
fun addone_to_all(list:intlist):intlist = 
	case list of Nil => Nil
	| Cons(hd,tl) => Cons(inc(hd), addone_to_all(tl))

(* given [i1,i2,...,in] return [i1*i1,i2*i2,...,in*in] *)
fun square_all(list:intlist):intlist = 
	case list of Nil => Nil
	| Cons(hd,tl) => Cons(square(hd), square_all(tl))

(* given a function f and [i1,...,in], return [f(i1),...,f(in)].
 * Notice how we factored out the common parts of addone_to_all
 * and square_all. *)
fun do_function_to_all(f:int->int, list:intlist):intlist = 
	case list of Nil => Nil
	| Cons(hd,tl) => Cons(f(hd), do_function_to_all(f,tl))

(* now we can define addone_to_all in terms of do_function_to_all *)
fun addone_to_all(list:intlist):intlist = 
	do_function_to_all(inc, list);

(* same with square_all *)
fun square_all(list:intlist):intlist = 
	do_function_to_all(square, list);

(* given [i1,i2,...,in] return i1+i2+...+in (also defined above) *)
fun sum(list:intlist):int = 
	case list of Nil => 0
	| Cons(hd,tl) => hd + sum(tl)

(* given [i1,i2,...,in] return i1*i2*...*in *)
fun product(list:intlist):int = 
	case list of Nil => 1
	| Cons(hd,tl) => hd * product(tl)

(* given f, b, and [i1,i2,...,in], return f(i1,f(i2,...,f(in,b))).
 * Again, we factored out the common parts of sum and product. *)
fun collapse(f:(int * int) -> int, b:int, list:intlist):int = 
	case list of Nil => b
	| Cons(hd,tl) => f(hd,collapse(f,b,tl))

(* Now we can define sum and product in terms of collapse *)
fun sum(list:intlist):int = 
	let fun add(i1:int,i2:int):int = i1 + i2
	in 
		collapse(add,0,list)
	end

fun product(list:intlist):int = 
	let fun mul(i1:int,i2:int):int = i1 * i2
	in
		collapse(mul,1,list)
	end

(* Here, we use an anonymous function instead of declaring add and mul.
 * After all, what's the point of giving those functions names if all
 * we're going to do is pass them to collapse? *)
fun sum(list:intlist):int = 
	collapse((fn (i1:int,i2:int) => i1+i2),0,list);

fun product(list:intlist):int = 
	collapse((fn (i1:int,i2:int) => i1*i2),1,list);

(* And here, we just pass the operators directly... *)
fun sum(list:intlist):int = collapse(op +, 0, list);

fun product(list:intlist):int = collapse(op *, 1, list);

