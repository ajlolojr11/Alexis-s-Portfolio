--Demonstrate WHERE keyword

SELECT "title", "author" FROM "longlist" WHERE "year" = 2023;

SELECT "title", "author", "year" FROM "longlist" WHERE "year" = 2023;

SELECT "title", "author", "year" FROM "longlist" WHERE "year" = 2022;

SELECT "title", "author", "year" FROM "longlist" WHERE "year" = 2021;

--Using operator != and <>

SELECT "title", "format" FROM "longlist" WHERE "format" != 'hardcover';

SELECT "title", "format" FROM "longlist" WHERE "format" <> 'hardcover';

--Using NOT keyword

SELECT "title", "format" FROM "longlist" WHERE NOT "format" = 'hardcover';

--Using AND, OR keywords and () operator

SELECT "title", "author", "year", "format" FROM "longlist"
WHERE ("year" = 2022 OR "year" = 2023)
AND "format" != 'hardcover';

--Using BETWEEN ... AND ...
SELECT "title", "year" FROM "longlist"
WHERE "year" BETWEEN 2019 AND 2022;

--Using >, <, >=, <=
SELECT "title", "year" FROM "longlist"
WHERE "year" >= 2019 AND "year" <= "2022";

SELECT "title", "rating" FROM "longlist"
WHERE "rating" > 4.0;

SELECT "title", "rating", "votes" FROM "longlist"
WHERE "rating" > 4.0 AND "votes" > 10000;

SELECT "title", "pages" FROM "longlist"
WHERE "pages" < 300;
