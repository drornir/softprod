sig State {
	succesor:  set State
}

sig InitialState extends State{}

fact {some InitialState}

fun succesors (s: State): set State {
    s.succesor
}

fact factName{
some s:State | (#s.succesor =0 and some i:InitialState | s in i.^succesor)
}

pred show () {}
run show for 5
