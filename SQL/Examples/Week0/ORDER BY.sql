--Demonstrates ORDER BY

SELECT "title", "rating" FROM "longlist"
ORDER BY "rating" LIMIT 10;

--Defining Ascending(ASC) or Descending(DESC) in ORDER BY
SELECT "title", "rating", "votes" FROM "longlist"
ORDER BY "rating" DESC, "votes" DESC
LIMIT 10;

SELECT "title" FROM "longlist"
ORDER BY "title";

SELECT "title" FROM "longlist"
ORDER BY "title" DESC;
