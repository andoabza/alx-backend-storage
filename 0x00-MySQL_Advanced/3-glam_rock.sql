-- select all bands with if stlye is glam ROck and calculate lifespan until 2022
-- glam rock

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;