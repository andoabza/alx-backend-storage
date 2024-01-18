-- select all bands with if stlye is glam ROck and calculate lifespan until 2022

SELECT
    band_name,
    band_style,
    (2022 - band_year_formed) AS lifespan FROM metal_bands
WHERE
    band_style = 'Glam Rock'
ORDER BY
lifespan DESC;



