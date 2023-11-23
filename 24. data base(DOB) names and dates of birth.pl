
dob(john, '1990-05-15').
dob(jane, '1985-02-20').
dob(bob, '1995-11-10').
dob(alice, '1980-07-03').
dob(susan, '1992-09-28').


get_dob(Person, DOB) :- dob(Person, DOB).


youngest_person(Person) :-
    dob(Person, DOB),
    \+ (dob(_, OtherDOB), OtherDOB @< DOB).


is_older(Person1, Person2) :-
    dob(Person1, DOB1),
    dob(Person2, DOB2),
    DOB1 @> DOB2.
