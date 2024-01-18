-- select all bands with if stlye is glam ROck and calculate lifespan until 2022

SELECT
    band_name,
    (COALESCE(split, 2020) - formed) AS lifespan FROM metal_bands
WHERE
    style LIKE '%Glam Rock%'
ORDER BY
lifespan DESC;



