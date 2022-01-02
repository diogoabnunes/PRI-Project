q: race_text:"incident Verstappen"~10 race_text:"crash Verstappen"~10 race_text:"accident Verstappen"~10 race_text:"collision Verstappen"~10
q.op: OR
fq: date:[NOW-1YEAR/YEAR TO NOW]
fl: raceId, year, name, qualifying_text, race_text, score