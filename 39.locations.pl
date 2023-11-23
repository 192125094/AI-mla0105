location(chicago, illinois).
location(new_york, new_york).
location(los_angeles, california).

stays(john, chicago).
stays(amy, new_york).
stays(michael, los_angeles).


list_persons_state_city :-
    stays(Person, City),
    location(City, State),
    write('Person: '), write(Person),
    write(', City: '), write(City),
    write(', State: '), write(State), nl,
    fail.
find_state(Person) :-
    stays(Person, City),
    location(City, State),
    write(Person), write(' is staying in '), write(State), nl.

