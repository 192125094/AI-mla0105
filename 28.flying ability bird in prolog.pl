can_fly(sparrow).
can_fly(eagle).

query_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'),
    nl.
query_can_fly(Bird) :-
    \+ can_fly(Bird),
    write(Bird), write(' cannot fly.'),
    nl.
