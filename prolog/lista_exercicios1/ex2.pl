% Programa que recebe uma lista e retorna a soma dos elementos em posições pares

evenSumAux([],_,0).

evenSum(List, Sum) :- evenSumAux(List, 1, Sum).

evenSumAux([_|T], I, Sum) :-
    I mod 2 ==:== 1,
    NewI is I+1,
    evenSum(T, NewI, Sum).

evenSumAux([H|T], I, Sum) :-
    I mod 2 =:= 0,
    NewI is I+1,
    evenSum(T, NewI, SumT),
    Sum is SumT + H.  