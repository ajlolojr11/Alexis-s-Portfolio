--Demonstrates NULL keyword

SELECT "title", "translator" FROM "longlist"
WHERE "translator" IS NULL;

SELECT "title", "translator" FROM "longlist"
WHERE "translator" IS NOT NULL;

