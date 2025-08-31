--Demonstrates LIKE keyword (%, _)

--Can have any string before or after the word 'love'
SELECT "title" FROM "longlist"
WHERE "title" LIKE '%love%';

--Can only have string after the word 'The' (i.e. begins with 'The')
SELECT "title" FROM "longlist"
WHERE "title" LIKE 'The %';

--Search for multiple words withing the same string that aren't necessarily next to another but in the same order
SELECT "title" FROM "longlist"
WHERE "title" LIKE 'The%love%';

-- _ matches any single character
SELECT "title" FROM "longlist"
WHERE "title" LIKE 'P_re';

--Show case insensitive vs case sensitive filtering
SELECT "title" FROM "longlist"
WHERE "title" LIKE 'pyre';
--vs
SELECT "title" FROM "longlist"
WHERE "title" = 'pyre';
