DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN,
    want_to_visit BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN,
    want_to_visit BOOLEAN

);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    visited BOOLEAN,
    want_to_visit BOOLEAN
);