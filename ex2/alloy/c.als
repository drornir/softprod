sig State {
	succesor:  set State
}

sig InitialState extends State{}

fact {some InitialState}

fun succesors (s: State): set State {
    s.succesor
}

fact factName{
some  s: State | (all r:InitialState |s not in r .^succesor)
}

pred show () {}
run show for 5
