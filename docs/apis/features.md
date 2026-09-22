# OGC API – Features

BGS open data collections are available at <https://ogcapi.bgs.ac.uk/> using the [OGC API – Features](https://ogcapi.ogc.org/features/) standard. The OpenAPI definition can be explored in [Swagger UI](https://ogcapi.bgs.ac.uk/openapi?f=html).

## Collections

| Collection | Items |
| --- | --- |
| Earthquakes – recent | [`recentearthquakes`](https://ogcapi.bgs.ac.uk/collections/recentearthquakes) |
| Landslide database index | [`landslideindex`](https://ogcapi.bgs.ac.uk/collections/landslideindex) |
| Borehole records (SOBI) | [`onshoreboreholeindex`](https://ogcapi.bgs.ac.uk/collections/onshoreboreholeindex) |
| Offshore hydrocarbon wells | [`offshore-hydrocarbon-wells`](https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells) |
| World mineral statistics | [`world-mineral-statistics`](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics) |

The live list is always at <https://ogcapi.bgs.ac.uk/collections>.

## Desktop GIS

Both ArcGIS Pro and QGIS can connect to OGC API – Features, giving a live link to the data:

- [ArcGIS Pro: add OGC API services](https://pro.arcgis.com/en/pro-app/latest/help/data/services/add-ogc-api-services.htm)
- QGIS: *Layer › Add Layer › Add WFS / OGC API – Features Layer*, then add `https://ogcapi.bgs.ac.uk/` as a new connection.

## Simple queries

Bounding box, property selection, property equality filters and sorting:

- [Hydrocarbon wells in 50 m of water, selected attributes](https://ogcapi.bgs.ac.uk/collections/offshore-hydrocarbon-wells/items?f=json&limit=10&properties=wellid,wellname,completion_date,water_depth_m,tvd_m,td_m&water_depth_m=50)
- [World mineral statistics, most recent first](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?sortby=-year&f=json&limit=10) · [oldest first](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?sortby=year&f=json&limit=10)
- [World mineral statistics, selected attributes only](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?properties=year,bgs_statistic_type_trans,bgs_commodity_trans,bgs_sub_commodity_trans,country_trans&f=json&limit=10)

## CQL filtering

Collections backed by PostgreSQL support full CQL filter expressions via the `filter` parameter. Browsers will URL-encode for you, so this works pasted straight into the address bar:

```text
https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml BETWEEN 4 AND 4.5 AND depth > 5
```

| Example | Filter |
| --- | --- |
| [Magnitude 4–4.5](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml%20BETWEEN%204%20AND%204.5) | `ml BETWEEN 4 AND 4.5` |
| […and deeper than 5 km](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml%20BETWEEN%204%20AND%204.5%20AND%20depth%20%3E%205) | `ml BETWEEN 4 AND 4.5 AND depth > 5` |
| [Magnitude exactly 4.2](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=ml=%274.2%27) | `ml='4.2'` |
| [Years 1975 or 1990](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=year%20IN%20(%271975%27,%271990%27)) | `year IN ('1975','1990')` |
| [Inside a polygon (west Cornwall)](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?f=json&limit=100&filter=INTERSECTS(shape_wmerc,POLYGON((-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238)))) | `INTERSECTS(shape_wmerc, POLYGON(...))` |
| [Polygon and magnitude 1–2](https://ogcapi.bgs.ac.uk/collections/recentearthquakes/items?limit=100&filter=INTERSECTS(shape_wmerc,POLYGON((-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238)))%20AND%20ml%20BETWEEN%201%20AND%202) | `INTERSECTS(...) AND ml BETWEEN 1 AND 2` |
| [Boreholes in a polygon with AGS logs, 10–50 m long](https://ogcapi.bgs.ac.uk/collections/onshoreboreholeindex/items?f=json&filter=INTERSECTS%28shape,POLYGON%28%28-4.724%2050.238,-5.021%2050.351,-5.394%2050.393,-5.735%2050.238,-5.812%2050.041,-5.416%2049.921,-4.988%2049.886,-4.724%2050.238%29%29%29%20AND%20ags_log_url%20IS%20NOT%20NULL%20AND%20length%20BETWEEN%2010%20AND%2050&limit=10000) | `INTERSECTS(...) AND ags_log_url IS NOT NULL AND length BETWEEN 10 AND 50` |
| [Gold in Guyana before 1975](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?filter=erml_commodity%20LIKE%20%27Gold%27%20AND%20country_iso3_code%20=%20GUY%20AND%20year%20BEFORE%201975-09-19T00:00:00Z&f=json&limit=100) | `erml_commodity LIKE 'Gold' AND country_iso3_code = GUY AND year BEFORE 1975-09-19T00:00:00Z` |
| [Gold in Cyprus after 2002](https://ogcapi.bgs.ac.uk/collections/world-mineral-statistics/items?filter=erml_commodity%20LIKE%20%27Gold%27%20AND%20year%20AFTER%202002-09-19T00:00:00Z%20AND%20country_trans=Cyprus&f=json&limit=100) | `erml_commodity LIKE 'Gold' AND year AFTER 2002-09-19T00:00:00Z AND country_trans=Cyprus` |

!!! note "To confirm before publishing"
    The old README's borehole example said "between 20 and 50 m" but the query uses `BETWEEN 10 AND 50`, and the Cyprus example said "after 2020" while the query uses 2002. The labels above follow the queries. Worth re-testing every example against the live service as part of CI.
