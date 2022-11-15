# BGS Open API - Features

How to use

## Overview

## Getting Started

## Technical Specification

### Technical Details

Requests are structured using keyword-value pair (KVP) parameter encoding, and HTTP GET. All requests must be encoded correctly according to standard percent-encoding procedures for a URI.

#### Authentication

No authentification is required to use the API.

#### Encryption

All calls must be made using a secure hypertext encryption (HTTPS).

All calls made to any of our APIs must support TLS v1.2 in line with current cyber security recommendations.

#### Response Codes

| Code | Official description          | Explanation in context of the API                                       |
| ---- | ----------------------------- | ----------------------------------------------------------------------- |
| 200  | OK                            | Request had been successful.                                            |
| 400  | The request was not supported | E.g. missing query parameter, malformed syntax.                         |
| 401  | Unauthorized                  | The client has not provided authentication or incorrect authentication. |
| 404  | Not Found                     | The server has not found anything matching the Request-URI.             |
| 406  | Not Supported                 | A request header value was not supported.                               |
| 504  | Service Unavailable           | Temporary outage due to overloading or maintenance.                     |

#### Endpoints

| Resource                               | Path                                                        | Description                                                                                                                                |
| -------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Landing Page                           | /                                                           | General information about the service and provides links to all available endpoints.                                                       |
| Conformance Declaration                | /conformance                                                | This endpoint list of all conformance classes specified in a OGC API – Features standard that the API conforms to.                        |
| API definition                         | /api                                                        | The API definition provides metadata about the API itself and its implementation.                                                          |
| Feature collections                    | /collections                                                | Lists all the available Feature collections through the API e.g., bld-fts-buildingline.                                                    |
| Feature collection                     | /collections/{collectionId}                                 | Provides information about a specific Feature collection including spatial & temporal extents, available coordinate reference systems etc. |
| /collections/{collectionId}/schema     | Provides the schema for the feature collection.             |                                                                                                                                            |
| /collections/{collectionId}/queryables | Lists the attributes that can be used to filter your query. |                                                                                                                                            |
| Features                               | /collections/{collectionId}/items                           | List of the features provided by the feature collection (limited to 100 per transaction).                                                  |
| Feature                                | /collections/{collectionId}/items/{featureId}               | This endpoint returns the latest version of a single feature within the specific feature collection.                                       |

#### Coordinate Reference System

All data supplied by the BGS Open API – Features will default to WGS84 longitude/latitude (CRS84) unless otherwise specified using the *crs* parameter.

Other options (if supported by the feature collection) include British National Grid (BNG) EPSG:27700, World Geodetic System (WGS84: EPSG: 4326), Web Mercator (EPSG: 3857).

| Parameter | Value                                                                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| crs       | The coordinate reference system of the response geometries. It must be a coordinate reference system supported by the collection. Default is WGS84 longitude/latitude |

#### Queryables

With the OS NGD API – Features, you can filter by attributes to create customised data selections; however, the OGC API – Features standard does not assume that all the attributes of a feature collection are available to construct a filtered query.

For each feature collection, a set of attributes have been defined to build a filtered query; as a result, only attributes identified in the /queryables endpoint for each feature collection are supported when applying attribute filtering.

#### Filtering

Any of the parameters listed in the tables below are optional parameters to refine the features returned.

##### Spatial

| Parameter | Value                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bbox      | The bbox parameter specifies a valid bounding box. Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four numbers:* Lower left corner, coordinate axis 1 (e.g., min x axis)* Lower left corner, coordinate axis 2 (e.g., min y axis)* Upper right corner, coordinate axis 1 (e.g., max x axis)* Upper right corner, coordinate axis 2 (e.g., max y axis) | [Simple bbox](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html?_gl=1*1tgmq65*_ga*OTM1NzUxNjM4LjE2Njg1MDQxOTk.*_ga_59ZBN7DVBG*MTY2ODUwNDE5OS4xLjEuMTY2ODUwNzM3Mi42MC4wLjA.#filter=bbox) |
| bbox-crs  | The coordinate reference system of the bbox parameter.                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                            |

##### Temporal

| Parameter | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| datetime  | The datetime parameter specifies a valid date-time with UTC time zone (Z) or an open or closed interval. Only features that have a temporal geometry (versionavailablefromdate or versionavailabletodate) that intersects the value in the datetime parameter are selected.Date and time expressions adhere to[RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.6):* A date-time: 2021-12-12T13:20:50Z* A closed interval: 2021-12-12T13:20:50Z/2021-12-18T12:31:12Z* Open-start intervals: ../2021-12-18T12:31:12Z or /2021-12-18T12:31:12Z* Open-end intervals: 2021-12-12T13:20:50Z/.. or 2021-12-12T13:20:50Z/ | [Datetime filter](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=bbox,datetime) |

##### Attribute

| Parameter   | Value                                                                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter      | A filter expression in CQL format which is applied when retrieving features to determine which features are included in a result set.                                                                     |
| filter-crs  | Specify which of the supported CRSs to use to encode geometric values in a filter expression. It must be a coordinate reference system supported by the collection. Default is WGS84 longitude / latitude |
| filter-lang | Specify the language used for the filter expression. The default language is cql-text                                                                                                                     |
| limit       | Limits the maximum number of features to be returned in a single response (default and max is 100 per request)                                                                                            |
| offset      | Skips past the specified number of features in the collection (default and min is 0 per request).                                                                                                         |

### Use of CQL Operators

The BGS Open API – Features supports a generic filter grammar called Common Query Language (CQL) for specifying enhanced filter criteria to return a subset of features. CQL was created as a text encoding based on the capabilities defined in the OGC Filter Encoding standard, which is more straightforward and more readable.

The following table documents the supported operators.

| Operator Type | Supported Operators                                                                                                                        | Examples                                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Logical       | and, or, not [<>]                                                                                                                          |                                                                                                                                                                                                                                                                                                            |
| Spatial       | intersects                                                                                                                                 | [CQL spatial filter: intersects – point](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=cql-spatial-intersects-point)[CQL spatial filter: intersects – polygon](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=cql-spatial-intersects-polygon) |
| Comparison    | equal to [ = ], less than [ < ], less than or equal to [ <= ], greater than [ > ], greater than or equal to [ >=], null, like, in, between | [CQL comparison filter: equal to](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=bbox,cql-comparison-equal-to)                                                                                                                                                                |
| Array         | aequals, acontains, contained by, aoverlaps                                                                                                | [CQL array filter: aequals](https://labs.os.uk/public/osngd/os-ngd-api-features/examples/items.html#filter=bbox,cql-array-aequals)                                                                                                                                                                            |

## Examples

### Simple Queries

Limited to BBOX, Property Display/Filters & Sort.

Example: To get [all Hydrocarbon Wells where water depth = 50 m and include attributes wellid, wellname, completion_date, water_depth_m, tvd_m, td_m](https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells/items?f=json&lang=en-US&limit=10&properties=wellid,wellname,completion_date,water_depth_m,tvd_m,td_m&water_depth_m=50)

### CQL Queries

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

### Juypter Notebooks

In the `notebook` folder we have a few example Jupyter Notebooks showing how you can interact with our data.

Follow the instructions below to install and run the demonstration Jupyter Notebook on your own
machine.  Alternatively, you can [view the code and results](notebooks\ogcapi-features-cql-owslib-earthquakes.ipynb) in your browser.  Click [here](https://nbviewer.org/github/BritishGeologicalSurvey/BGS-OGCAPI-Documentation/blob/main/notebooks/ogcapi-features-cql-owslib-earthquakes.ipynb) for mobile-friendly version rendered by _Jupyter nbviewer_.
