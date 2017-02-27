sig State {
	succesor:  set State
}

sig InitialState extends State{}

fact {some InitialState}

fun succesors (s: State): set State {
    s.succesor
}

fact factName{
all  s: State | (some r:InitialState |s in r .^succesor)
}

pred show () {}
run show for 5
