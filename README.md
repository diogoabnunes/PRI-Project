# PRI

# Bibliography

- https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020
- https://www.kaggle.com/codingminds/formula-1-race-fan-ratings


# Identification and briefly description of the datasets selected

- **drivers.csv**: driverId, driverRef, number, code (3 letters), forename, surname, date of birth, nationality and Wiki URL
- **constructors.csv**: constructorId, constructorRef, name, nationality, Wiki URL
- **circuits.csv**: circuitId, circuitRef, name, location, country, and Wiki URL
- **seasons.csv**: year and Wiki URL
- **races.csv**: raceId, year, round, circuitId, name, date, time, Wiki URL
- **pit_stops.csv**: raceId, driverId, stop, lap, time, duration, milliseconds
- **qualifying.csv**: id, raceId, driverId, constructorId, number, position, q1,q2,q3
- **status.csv**: statusId, status ("Finished", "Disqualified", etc)
- **results.csv**: resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId
- **lap_times.csv**: raceId, driverId, lap, position, time, milliseconds

## Discard?
- **driver_standings.csv**: driverStandingsId, raceId, driverId, points, position, positionText, wins
- **constructor_standings.csv**: constructorStandingsId, raceId, constructorId, points, position, positionText, wins
- **constructor_results.csv**: constructorResultsId, raceId, constructorId, points, status


# First draft of the data processing pipeline
![First Draft of the pipeline](images/pipeline.drawio.png)

## Data Collection
### Scrapy
- circuits, constructors, drivers, races, seasons

## Data Preparation
### Data Cleaning
- constructor_standings.csv: positionText tem a position ou E ou até mesmo -, e ainda não sei qual a diferença ao certo
- results.csv: position removed; positionText to position; time removed; milliseconds to time;

- Remove position column from constructor_standings.csv, results.csv, driver_standings.csv. We already have positionText column that gives more information (position, R(etired), D(isqualified))

- Remove duration column on pit_stops.csv (still have miliseconds column)

- Remove time column on lap_times.csv and results.csv (we still have miliseconds column)
