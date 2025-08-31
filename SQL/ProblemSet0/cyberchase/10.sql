/*In the episodes table, you’ll find the following columns:

-id, which uniquely identifies each row (episode) in the table
-season, which is the season number in which the episode aired
-episode_in_season, which is the episode’s number within its given season
-title, which is the episode’s title
-topic, which identifies the ideas the episode aimed to teach
-air_date, which is the date (expressed as YYYY-MM-DD) on which the episode “aired” (i.e., was published)
production_code, which is the unique ID used by PBS to refer to each episode internally*/

--write a SQL query to list the ids, titles, and production codes of all episodes. Order the results by production code, from earliest to latest.

SELECT "id", "title", "production_code" FROM "episodes"
ORDER BY "production_code" ASC;
