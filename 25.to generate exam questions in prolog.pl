student(john, cs101).
student(alice, math202).
student(bob, phy301).

teacher(prof_smith, cs101).
teacher(prof_jones, math202).
teacher(prof_doe, phy301).

subject(cs101, 'Computer Science').
subject(math202, 'Mathematics').
subject(phy301, 'Physics').

generate_question(Question) :-
    student(Student, Subject),
    teacher(Teacher, Subject),
    subject(Subject, SubjectName),
    format(atom(Question), 'Who is the teacher of ~w in the subject ~w?', [Student, SubjectName, Teacher]).






