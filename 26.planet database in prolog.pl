% Facts about planets
planet(mercury, 0.39, 0.055).
planet(venus, 0.72, 0.815).
planet(earth, 1.0, 1.0).
planet(mars, 1.52, 0.107).
planet(jupiter, 5.20, 318.0).
planet(saturn, 9.58, 95.0).

% Rule to calculate the distance between two planets
distance_between(Planet1, Planet2, Distance) :-
    planet(Planet1, Dist1, _),
    planet(Planet2, Dist2, _),
    Distance is abs(Dist1 - Dist2).

% Rule to find planets closer to the Sun than Earth
closer_to_sun_than_earth(Planet) :-
    planet(Planet, Dist, _),
    Dist < 1.0.  % Earth's distance is 1.0 (normalized)


