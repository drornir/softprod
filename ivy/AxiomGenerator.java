package com.soft;

import java.util.ArrayList;
import java.util.List;

public class AxiomGenerator {

    public static void main(String[] args) {
	// write your code here


        List<String> vars = new ArrayList<>();
        vars.add("l0");
        for (int i = 0; i < 8; i++) {
            vars.add("e" + i);
        }

        for (int i = 0; i < 6; i++) {
            vars.add("d" + i);
        }

        vars.add("finishedLine");
        vars.add("dReturn");

        System.out.println("#automatically generated axioms");
        for (int i = 0; i < vars .size(); i++)
            for (int j = i + 1; j < vars .size(); j++)
                System.out.println("axiom "+ vars.get(i) + "~=" + vars.get(j));
    }
}
