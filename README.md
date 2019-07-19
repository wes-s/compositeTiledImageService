# compositeTiledImageService
composites tiled image services into one tile for use with tableau map sources.

Connect heroku app to github repo and deploy

Alter composite_tiled_maps_heroku.tms to include your heroku app name in the two urls on line 3.

Place composite_tiled_maps_heroku.tms (or rename it if you choose) in 'C:\Users\[USER NAME HERE]\Documents\My Tableau Repository\Mapsources\'

Open tableau, create map visulization, and select Map>Background Map>composite_tiled_maps_heroku

To change displayed layers in Tableau Map visualization select Map>Map>Layers and check/uncheck desired layers.
