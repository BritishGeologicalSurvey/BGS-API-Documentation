# BGS Open API Documentation

To make our data more FAIR, BGS have made a selection of our Open Data available as an API using the OGCAPI-Features standard at https://ogcapi.bgs.ac.uk/. This is targeted at academics, developers, data scientists & geospatial specialists who would like to work with our data programmatically using R/Python etc or would like a live connection to frequently updated datasets in their desktop GIS platform.

We would really appreciate your [feedback or suggestions](https://github.com/BritishGeologicalSurvey/BGS-OGCAPI-Documentation/issues) including what other data would benefit from this delivery mechanism.

The API is compatible with both ESRI ArcPro & QGIS allowing you a “live” link to the data – useful for those with frequent updates

- [ArcPro](https://pro.arcgis.com/en/pro-app/2.8/help/data/services/add-ogc-api-services.htm)
- [QGIS](https://docs.qgis.org/3.22/en/docs/training_manual/online_resources/wfs.html)

OpenAPI specification is available through Swagger UI at - https://ogcapi.bgs.ac.uk/openapi?f=html

Data collections include:

- [Earthquakes – Recent](https://ogcapi.bgs.ac.uk/collections/recentearthquakes)
- [Landslide Database Index](https://ogcapi.bgs.ac.uk/collections/landslideindex)
- [Borehole Records (SOBI)](https://ogcapi.bgs.ac.uk/collections/onshoreboreholeindex)
- [Offshore Hydrocarbon Wells](https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells)

For further documentations see OS which use the same protocol
- https://labs.os.uk/public/osngd/os-ngd-api-features/
- https://labs.os.uk/public/osngd/os-ngd-api-features/code-playground/#template-leaflet
- https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=bbox,datetime
- https://osngd.gitbook.io/osngd/accessing-os-ngd/access-the-os-ngd-api-features
- https://osdatahub.os.uk/docs/ofa/overview

# Queries

## Simple Queries

Limited to BBOX, Property Display/Filters & Sort.

Example: To get [all Hydrocarbon Wells where water depth = 50 m and include attributes wellid, wellname, completion_date, water_depth_m, tvd_m, td_m](https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells/items?f=json&lang=en-US&limit=10&properties=wellid,wellname,completion_date,water_depth_m,tvd_m,td_m&water_depth_m=50)

## CQL Queries

These allow full complex queries against those collections using a postgres backend.

Some example URL encoded queries:

- [Earthquakes with ml between 4 and 4.5](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml%20BETWEEN%204%20AND%204.5)
- [Earthquakes with ml between 4 and 4.5 and &gt;5km depth](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml%20BETWEEN%204%20AND%204.5%20AND%20depth%20%3E%205)

Users don't have to URL encode the queries - the following will also work if copy & pasted into a browser:
`https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml BETWEEN 4 AND 4.5 AND depth > 5`

- [Earthquakes where ml = 4.2](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml=%274.2%27)
- [Earthquakes with year = 1975 or 1990](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=year%20IN%20(%271975%27,%271990%27))
- [Earthquakes inside a defined polygon](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=INTERSECTS(shape_wmerc,POLYGON((-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238))))
- [Earthquakes inside a defined polygon HTML response](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?filter=INTERSECTS(shape_wmerc,POLYGON((-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238)))&limit=100)
- [All earthquakes in a polygon with a ml (Richter local magnitude) between 1 &amp; 2](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?limit=100&filter=INTERSECTS(shape_wmerc,POLYGON((-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238)))%20AND%20ml%20BETWEEN%201%20AND%202)
- [Boreholes in a polygon area where ags_log_url IS NOT NULL and length is between 20 and 50 m](https://ogcapi.bgs.ac.uk/collections/onshoreboreholeindex/items?f=json&filter=INTERSECTS%28shape,POLYGON%28%28-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238%29%29%29%20AND%20ags_log_url%20IS%20NOT%20NULL%20AND%20length%20BETWEEN%2010%20AND%2050&limit=10000)
- [Mineral statistics for Guyana in 1975 &amp; 1990 with erml_commodity code = Gold](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?filter=erml_commodity%20LIKE%20%27Gold%27%20AND%20yearbook%20IN%20(%271975%27,%271990%27)%20AND%20iso3%20=%20GUY&f=json&limit=100)

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
