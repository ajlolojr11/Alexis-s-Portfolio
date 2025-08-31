/*In the episodes table, you’ll find the following columns:

-id, which uniquely identifies each row (episode) in the table
-season, which is the season number in which the episode aired
-episode_in_season, which is the episode’s number within its given season
-title, which is the episode’s title
-topic, which identifies the ideas the episode aimed to teach
-air_date, which is the date (expressed as YYYY-MM-DD) on which the episode “aired” (i.e., was published)
production_code, which is the unique ID used by PBS to refer to each episode internally*/

--write a query that counts the number of episodes released in Cyberchase’s first 6 years, from 2002 to 2007, inclusive.

SELECT COUNT("title") FROM "episodes"
WHERE "air_date" BETWEEN '2002-01-01' AND '2007-12-31';
