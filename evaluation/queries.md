# Queries

## Races

1. Youngest drivers to win races (at their time)
   - q: youngest driver win
   - q.op: AND
   - df: race_text

2. Incidents between drivers in the last year
   - q: "incident Verstappen"~10 "crash Verstappen"~10 "accident Verstappen"~10 "collision Verstappen"~10
   - q.op: OR
   - fq: date:[NOW-2YEAR/YEAR TO NOW]
   - df: race_text

3. Races in the rain that a certain driver won
   - q: race_text:"rain" race_text:"Vettel win"~5
   - q.op: AND
   - df: race_text

## Drivers

4. a
5. b
6. c

## Constructors

7. a
8. b
9. c

## Circuits

10. a
11. b
12. c

## Seasons

13. a
14. b
15. c

## Mix

16. a
17. b
18. c
19. d
20. e

