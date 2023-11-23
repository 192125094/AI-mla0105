condition_diabetes(john).
condition_hypertension(mary).
condition_obesity(emma).

diet_recommendation(X, 'Diabetes') :-
    condition_diabetes(X),
    write(X), write(' should follow a diet rich in fiber and low in sugar.'),
    nl.

diet_recommendation(X, 'Hypertension') :-
    condition_hypertension(X),
    write(X), write(' should follow a low-sodium diet and reduce caffeine intake.'),
    nl.

diet_recommendation(X, 'Obesity') :-
    condition_obesity(X),
    write(X), write(' should focus on a balanced diet with portion control and regular exercise.'),
    nl.

