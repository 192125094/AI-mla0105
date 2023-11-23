is_mammal(dog).
is_mammal(cat).
is_mammal(horse).

is_bird(sparrow).
is_bird(eagle).
is_bird(penguin).

is_mammal_animal(X) :-
    is_mammal(X),
    write(X), write(' is a mammal.').

is_bird_animal(X) :-
    is_bird(X),
    write(X), write(' is a bird.').

is_animal(X) :-
    is_mammal_animal(X);
    is_bird_animal(X).

