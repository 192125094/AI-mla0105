father(john, lisa).
father(tom, mary).
father(mike, emma).

mother(mary, lisa).
mother(mary, mike).
mother(emma, olivia).

sister(X, Y) :-
    mother(M, X),
    mother(M, Y),
    X \= Y.

grandfather(X, Y) :-
    father(X, Z),
    father(Z, Y).

grandmother(X, Y) :-
    mother(X, Z),
    mother(Z, Y).
