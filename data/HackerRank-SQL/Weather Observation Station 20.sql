SELECT ROUND(s.LAT_N,4)
FROM STATION s
WHERE (SELECT ROUND(COUNT(s.ID)/2)-1
FROM STATION) = (SELECT COUNT(s1.ID)
FROM STATION s1
WHERE s1.LAT_N > s.LAT_N);