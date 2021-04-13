parent('Habib' , 'Rana').
parent('Habib' , 'Panna').
parent('Habib' , 'Shova').
parent('Habib' , 'Ratna').
parent('Habib' , 'Shovon').
parent('Panna' , 'Zahin').
parent('Panna' , 'Labiba').
parent('Rana' , 'Mashrur').
parent('Rana' , 'Mayisha').
female('Shova'). female('Ratna'). female('Labiba'). female('Mayisha').
sister(X, Y) :- parent(Z, X), parent(Z, Y), not(X=Y), female(X).
brother(X,Y):-parent(Z,X),parent(Z,Y), not(X=Y), not( female(X)).
uncle(P,M):-parent(R,M),parent(Z,R),parent(Z,P), not(R=P),not(female(P)).
aunt(L,M):-parent(R,M),parent(Z,L),parent(Z,R), not(L=R) ,female(L).

/* Procedure to find the SISTER of X*/
findS :- write(' Name: '), read(X), write('Sister: '), sister(S,X), write(S), tab(5), fail.
findS.

/* Procedure to find the Brother of X*/
findB:-write('Name: '),read(X),write('Brother: '),brother(B,X),write(B),tab(5),fail.
findB.
/*Procedure to find the Uncle of P*/
findU:-write('Name: '),read(P),write('Uncle '),uncle(U,P),write(U),tab(5),fail.
findU.

/*Procedure to find the Aunt of  L*/
findA:-write('Name: '),read(L),write('Aunt '),aunt(A,L),write(A),tab(5),fail.
findA.
