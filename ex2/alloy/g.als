sig State {
	succesor:  set State
}

sig InitialState extends State{}

fact {some InitialState}

fun succesors (s: State): set State {
    s.succesor
}

fact factName{
//s is a reachable state from inital state i, and there exists a state k, s.t. k is also reachable from i and is reachable from itself and k!=s
some s:State | (some i:InitialState | (s in i.^succesor  and some k:State| k in i.^succesor and k in k.^succesor and k!= s))
}

pred show () {}
run show for 5


