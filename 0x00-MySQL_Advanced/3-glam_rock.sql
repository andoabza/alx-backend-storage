-- Active: 1705485893796@@127.0.0.1@3306@holberton
-- glam ROck

SELECT band_name, COALESCE(split, 2022) - formed  AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';