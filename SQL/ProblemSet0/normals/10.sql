/*In normals.db you’ll find a single table of coordinates, normals. In the normals table, you’ll find the following columns:

id, which uniquely identifies each row (coordinate) in the table
latitude, which is the degree of latitude (expressed in decimal format) for the coordinate
longitude, which is the degree of longitude (expressed in decimal format) for the coordinate
0m, which is the normal ocean surface temperature (i.e., the normal temperature at 0 meters of depth), in degrees Celsius, at the coordinate
5m, which is the normal ocean temperature at 5 meters of depth, in degrees Celsius, at the coordinate
10m, which is the normal ocean temperature at 10 meters of depth, in degrees Celsius, at the coordinate
And observations continue until 5500m, or 5500 meters of depth, for some coordinates*/

/*There are 180 whole degrees of latitude. In 10.sql, write a SQL query to determine how many points of
latitude we have at least one data point for. (Why might we not have data points for all latitudes?)*/

SELECT COUNT(DISTINCT "latitude") from "normals";
