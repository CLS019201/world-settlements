# Text Mining - Vizualising World Settlements - Jason Fan and Tom Wang
[github.io page](http://jasonfan74.github.io/world-settlements)
##Acknowledgements:

* First, we would like to thank Prof. Maxim Romanov for his patience, time and enthusiasm.
* We would also like to thank Mike Bostock for his commitment to providing opensource code for Visualizations with D3

### Usage:

#### Option 1: Run Using Python simple server:
With python installed, simply run `python -m SimpleHTTPServer 8080` and open up `localhost:8080` on a web browser

#### Option 2: Run with Node.js server:
* Install Node.js
* Install Express package with NPM, using `npm install express`
* open up `localhost:8080` on a web browser

### Information about the project:

The goal of this project is to produce meaningful visualizations of the urbanization/settlement of the globe through extracting information from Wikipedia.

We took advantage of Wikipedia's markup of pages and extracted 800 thousand entries (infboxes) containing locational information from the database of 15 million entries. Due to the scope of the project and the time on hand, we focused on the largest class of infoboxes namely those for "settlements". We collected 300 thousand infoboxes for settlements.

Out of the 300 thousand infoboxes, 18 thousand had information concerning the establishment dates. We plotted each of these settlements and created interactive visualizations that show when and where settlements were established

### About the vizualizations:

The vizualization can be put into 2 categories, binned, and not binned. Binned vizualizations collect points into hexagonal bins on the map and display the median age of settlements within the hexagonal area. The unbinned maps display each of the 18,000 points on the maps.

For both maps, older settlements are mapped in dark colors, new settlements are displayed in light blue.

