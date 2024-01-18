-- Active: 1705485893796@@127.0.0.1@3306@holberton
-- glam ROck

SELECT band_name,  ABS(GREATEST(formed, COALESCE(split, 2020)) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;

