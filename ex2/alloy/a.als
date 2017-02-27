sig State {
	succesor: State
}

sig InitialState extends State{}

fact {some InitialState}

pred show () {}
run show for 5
