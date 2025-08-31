/*In the episodes table, you’ll find the following columns:

-id, which uniquely identifies each row (episode) in the table
-season, which is the season number in which the episode aired
-episode_in_season, which is the episode’s number within its given season
-title, which is the episode’s title
-topic, which identifies the ideas the episode aimed to teach
-air_date, which is the date (expressed as YYYY-MM-DD) on which the episode “aired” (i.e., was published)
production_code, which is the unique ID used by PBS to refer to each episode internally*/

--find the title of the holiday episode that aired on December 31st, 2004.

SELECT "title" FROM "episodes"
WHERE "air_date" = '2004-12-31';

