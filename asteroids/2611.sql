CREATE DATABASE p51_test;

CREATE TABLE animals (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    escape_attempts INTEGER NOT NULL,
    neutered BOOLEAN NOT NULL,
    weight_kg DECIMAL(5, 2) NOT NULL
);

DELETE FROM animals;

