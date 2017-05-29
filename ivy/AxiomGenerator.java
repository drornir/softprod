package com.soft;

import java.util.ArrayList;
import java.util.List;

public class AxiomGenerator {

    public static void main(String[] args) {

//        axioms();
	// write your code here

        conjectures();




    }

    private static void conjectures() {

        List<String> vars = new ArrayList<>();
        vars.add("inLinel0");
        for (int i = 0; i < 8; i++) {
            vars.add("inLinee" + i);
        }

        for (int i = 0; i < 6; i++) {
            vars.add("inLined" + i);
        }

        vars.add("inLinefinishedLine");
        vars.add("inLinedReturn");

        System.out.println("#automatically generated conjectures");
        for (int i = 0; i < vars .size(); i++)
            for (int j = i + 1; j < vars .size(); j++)
                //System.out.println("axiom "+ vars.get(i) + "~=" + vars.get(j));
                System.out.println("conjecture " + vars.get(i)+"(T1) & " + vars.get(j) +"(T2) -> T1 ~= T2");
    }

    private static void axioms() {
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
