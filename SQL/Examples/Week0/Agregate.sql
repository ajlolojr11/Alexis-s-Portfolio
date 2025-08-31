--Demonstratre SQL agregate functions: COUNT, AVG, MIN, MAX, SUM, ROUND

SELECT AVG("rating") FROM "longlist";

SELECT ROUND(AVG("rating"),2) AS "Average Rating"
FROM "longlist";

SELECT MAX("rating") AS "Max Rating"
FROM "longlist";

SELECT MIN("rating") AS "Minimum Rating"
FROM "longlist";

SELECT "title", "votes" FROM "longlist"
ORDER BY "votes" DESC;

SELECT SUM("votes") AS "Sum of votes"
FROM "longlist";

SELECT COUNT(*) FROM "longlist";

SELECT COUNT("translator") FROM "longlist";

SELECT COUNT("Publisher") FROM "longlist";

SELECT COUNT(DISTINCT "publisher") FROM "longlist";
