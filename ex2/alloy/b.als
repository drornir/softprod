sig State {
	succesor:  set State
}

sig InitialState extends State{}

fact {some InitialState}

fun succesors (s: State): set State {
    s.succesor
}

fact f{
some s: State | #(succesors[s])>1
}

pred show () {}
run show for 5
