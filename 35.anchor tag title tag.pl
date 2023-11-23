post(1, 'First Post', 'This is the content of the first post.').
post(2, 'Second Post', 'This is the content of the second post.').
post(3, 'Third Post', 'This is the content of the third post.').

anchor_tag(PostID, AnchorTag) :-
    post(PostID, Title, _),
    atomic_list_concat(['<a href="#post', PostID, '">', Title, '</a>'], AnchorTag).

title_tag(PostID, TitleTag) :-
    post(PostID, Title, _),
    atomic_list_concat(['<h2>', Title, '</h2>'], TitleTag).

example_blog :-
    anchor_tag(1, AnchorTag1),
    anchor_tag(2, AnchorTag2),
    anchor_tag(3, AnchorTag3),
    title_tag(1, TitleTag1),
    title_tag(2, TitleTag2),
    title_tag(3, TitleTag3),
    format('Blog:\n~w\n~w\n\n~w\n~w\n\n~w\n~w\n', [AnchorTag1, TitleTag1, AnchorTag2, TitleTag2, AnchorTag3, TitleTag3]).
