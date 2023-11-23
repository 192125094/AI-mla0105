gender(john, male).
gender(jane, female).
gender(bob, male).
gender(susan, female).

parent(john, mary).
parent(jane, mary).
parent(bob, ann).
parent(susan, ann).

is_parent(X) :-
    gender(X, male),
    parent(X, _).

is_parent(X) :-
    gender(X, female),
    parent(X, _).

