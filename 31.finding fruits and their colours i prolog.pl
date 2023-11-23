fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grape, purple).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(pear, green).
fruit_color(watermelon, green).

fruit_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

