# BGS OGCAPI Documentation

To make our data more FAIR, BGS have made a selection of our Open Data available as an API using the OGCAPI-Features standard at https://ogcapi.bgs.ac.uk/. This is targeted at academics, developers, data scientists & geospatial specialists who would like to work with our data programmatically using R/Python etc or would like a live connection to frequently updated datasets in their desktop GIS platform.  

We would really appreciate your [feedback or suggestions](https://github.com/BritishGeologicalSurvey/BGS-OGCAPI-Documentation/issues) including what other data would benefit from this delivery mechanism.

The API is compatible with both ESRI ArcPro & QGIS allowing you a “live” link to the data – useful for those with frequent updates
- ArcPro - https://pro.arcgis.com/en/pro-app/2.8/help/data/services/add-ogc-api-services.htm
- QGIS - https://docs.qgis.org/3.22/en/docs/training_manual/online_resources/wfs.html

Swagger API documentation is available - https://ogcapi.bgs.ac.uk/openapi?f=html 

Data collections include:
- Earthquakes – Recent (https://ogcapi.bgs.ac.uk/collections/recentearthquakes) and Historical (https://ogcapi.bgs.ac.uk/collections/historicalearthquakes) 
- Landslide Database Index - https://ogcapi.bgs.ac.uk/collections/landslideindex 
- Borehole Records (SOBI) - https://ogcapi.bgs.ac.uk/collections/onshoreboreholeindex 
- Offshore Hydrocarbon Wells - https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells 

# Queries

Current queries are limited to BBOX, Property Display/Filters & Sort.

Example: To get all Hydrocarbon Wells where water depth = 50 m and include attributes wellid, wellname, completion_date, water_depth_m, tvd_m, td_m =  https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells/items?f=json&lang=en-US&limit=10&properties=wellid,wellname,completion_date,water_depth_m,tvd_m,td_m&water_depth_m=50 

More detailed querying will be possible shortly such as, get features between two points / along a polyline, or get all landslides in a polygon with first known year between 1664 and 1899. 

# Examples

In the `notebook` folder we have a few example Jupyter Notebooks showing how you can interact with our data. 

Follow the instructions below to install and run the demonstration Jupyter Notebook on your own
machine.  Alternatively, you can [view the code and results](notebooks\ogcapi-features-cql-owslib-earthquakes.ipynb) in your browser.  Click [here](https://nbviewer.org/github/BritishGeologicalSurvey/BGS-OGCAPI-Documentation/blob/main/notebooks/ogcapi-features-cql-owslib-earthquakes.ipynb) for mobile-friendly version rendered by _Jupyter nbviewer_.

## Prerequisites

+ Python 3
+ A Python 3 package manager e.g. pip3, conda

## Installing dependencies

The following packages should be installed via `pip3` or `conda`:

```
pip3 install -r requirements.txt
```

### For developers

To test that the notebook runs to completion, extra packages are required:

```bash
pip3 install -r requirements-dev.txt
```

Run the test with:

```bash
pytest --nbval-lax notebooks\ogcapi-features-cql-owslib-earthquakes.ipynb
```


## Starting the notebook

The demo runs in a Jupyter notebook.  Start the notebook with:

```
jupyter notebook
```

A browser window will open at [http://localhost:8888](http://localhost:8888)
with a list of available notebooks.
