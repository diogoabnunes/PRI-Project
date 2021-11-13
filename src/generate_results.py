import pandas as pd

results = pd.read_csv('../F1_Data/results.csv')
drivers = pd.read_csv('../F1_Data/drivers.csv')
races = pd.read_csv('../F1_Data/races.csv')
constructors = pd.read_csv('../F1_Data/constructors.csv')
status = pd.read_csv('../F1_Data/status.csv')

# NAs
# for result in results:
#   print(results[result].value_counts())

# Driver id,name
drivers['driverName'] = drivers['forename'] + ' ' + drivers['surname']
drivers = drivers[['driverId','driverName']]
results = results.merge(drivers, on='driverId') 

# raceId,raceName (year + name)
races['raceName'] = races['year'].apply(str) + ' ' + races['name']
races = races[['raceId','raceName']]
results = results.merge(races, on='raceId') 

# constructorId,name
constructors['constructorName'] = constructors['name']
constructors = constructors[['constructorId','constructorName']]
results = results.merge(constructors, on='constructorId') 

# status merge
results = results.merge(status, on='statusId') 


data = {'resultId' : [], 'raceText': []}

# resultId,raceId,driverId,constructorId,number,grid,position,positionText,positionOrder,
# points,laps,time,milliseconds,fastestLap,rank,fastestLapTime,fastestLapSpeed,statusId
# On {raceName} driver {driverName} driving car No. {number} from {constructorName}. 
# {driverName} started on grid {grid} and after {laps} laps finished on {positionOrder} scoring {points} points.
# Finishing in if{time}.
# The fastest lap by {driverName} was lap No. if{fastestLap} finished in if{fastestLapTime} with an average speed of if{fastestLapSpeed} km/h, ranked number if{rank} fastest lap on the race.
# Drivers status: {status}
for index,result in results.iterrows():
  raceName = result['raceName']
  driverName = result['driverName']
  number = result['number']
  constructorName = result['constructorName']
  grid = result['grid']
  laps = result['laps']
  positionOrder = result['positionOrder']
  points = result['points']
  time = result['time']
  fastestLap = result['fastestLap']
  fastestLapSpeed = result['fastestLapSpeed']
  fastestLapTime = result['fastestLapTime']
  rank = result['rank']
  status = result['status']
  resultId = result['resultId']

  text = f'On the {raceName} driver {driverName}'
  
  if(number != '\\N'):
    text += f' driving car No. {number} from {constructorName}'
  
  text += f' started on grid {grid} and after {laps} laps finished on place number {positionOrder}, \
scoring {points} points.'

  if(time != '\\N'):
    text += " " + f'Finishing the race in {time}.'

  if('\\N' not in {fastestLap,fastestLapSpeed,fastestLapTime,rank}):
    text += f'\nThe fastest lap by {driverName} was lap No. {fastestLap} finished in {fastestLapTime} \
with an average speed of {fastestLapSpeed} km/h. Ranked number {rank} fastest lap on the race.'

  text += f" Driver's status: {status}"

  data['resultId'].append(resultId)
  data['raceText'].append(text)


df = pd.DataFrame(data=data)
df = df.sort_values('resultId')
df.to_csv('../processed_data/gen_result_text.csv',index=False)
