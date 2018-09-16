# beta-nearest-building
Getting started with the beta-nearest-building QGIS plugin.

## Things you need before you get started
1. QGIS 3.X installer [found here](https://www.qgis.org/en/site/forusers/download)
2. A beta API Key [register for the beta here](https://developer.psma.com.au/beta-program)
3. Your favourite text editor 
4. The Quick Map Services Plugin for QGIS (insalled through QGIS)
5. [Release 1.0 of the Beta Nearest Buildings Plugin](https://github.com/PSMA/beta-nearest-building/releases)


## Installation Steps
1. Install QGIS onto your machine and open it.
2. Install the Quick Map Services Plugin from Plugins >> Manage and Install Plugins
3. Install the Beta plugin from Plugins >> Manage and Install Plugins >> Install from ZIP
![](https://i.imgur.com/mBI2JfU.png)
4. Once installed you need to enter your beta api key, Open Settings >> User Profiles >> Open Active User Profile Folder
5. Navigate in profile folder to  >> default >> Python >> plugins >> beta-nearest-building-1
6. Edit credentials.py with your fav text editor and replace `your API key here` with the beta API key and save
7. Close and reopen QGIS. 
8. Open a base map from Quick Map Services (example Google Road)
> Change your datum to EPSG:4283
9. Open the Beta Nearest Buildings Plugin and either enter a `Latitude` `Longitude` and `Plot Buildings` or click `select point` and click on the map where you're like to search for buildings.
![](https://i.imgur.com/pqo9lJm.png)
10. The buildings found in the search radius will be plotted as layers in QGIS.
> You can open the Python Console Plugins >> Python Console. for debug infomation.
![](https://i.imgur.com/x0uOdPa.png)


## Please send feedback to beta@psma.com.au
