symptom(john, fever).
symptom(john, headache).
symptom(jane, cough).
symptom(jane, fatigue).
symptom(mary, sore_throat).
symptom(mary, fever).

condition(fever, flu).
condition(headache, migraine).
condition(cough, cold).
condition(fatigue, flu).
condition(sore_throat, cold).

diagnose_patient(Patient, Condition) :-
    symptom(Patient, Symptom),
    condition(Symptom, Condition).

diagnose_interactive :-
    write('Enter patient name: '),
    read(Patient),
    write('Enter symptom: '),
    read(Symptom),
    condition(Symptom, Condition),
    write('Diagnosis for '), write(Patient), write(': '), write(Condition),
    nl.

