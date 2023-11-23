
% Facts
male(john).
male(bob).
male(bill).

female(marry).
female(sue).

parent(john, bob).
parent(marry, bob).
parent(bob, sue).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

grandfather(X, Y) :- male(X), grandparent(X, Y).
grandmother(X, Y) :- female(X), grandparent(X, Y).

uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).
