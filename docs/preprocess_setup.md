## Parameters for preprocessing data

Open Edit Run/Debug configuration dialog
Select the file preprocess_hydrology under `Script path` 
Under Parameters type either one of the following for each of the river basins and hit the run button
For Stanislaus River
`-b stn -t pre -d historical`
`-b stn -t common -d historical`
`-b stn -t basins -d historical`
`-b stn -t pre -d gcms`
`-b stn -t common -d gcms`
`-b stn -t basins -d gcms`

For Tuolumne River
`-b tuo -t pre -d historical`
`-b tuo -t common -d historical`
`-b tuo -t basins -d historical`
`-b tuo -t pre -d gcms`
`-b tuo -t common -d gcms`
`-b tuo -t basins -d gcms`

For Merced River
`-b mer -t pre -d historical`
`-b mer -t common -d historical`
`-b mer -t basins -d historical`
`-b mer -t pre -d gcms`
`-b mer -t common -d gcms`
`-b mer -t basins -d gcms`


For Upper San Joaquin River
-b usj -t pre -d historical
-b usj -t common -d historical
-b usj -t basins -d historical
-b usj -t pre -d gcms
-b usj -t common -d gcms
-b usj -t basins -d gcms
