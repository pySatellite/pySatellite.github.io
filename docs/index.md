# LIVING FOR TODAY

![Screenshot](img/satellite-logo.png)

## pySatellite
- Simulate satellite tracking.
- It tells the story of space debris and satellite collisions.
- To Infinity, and Beyond!

## install
```bash
pip install pySatellite
```

## use

```python
from pysatellite import Rocket
from pysatellite import Satellite

Rocket.launch()
Satellite.coordinates()
```


## cli
```bash
$ pySatellite-where-are-you-now 1 {API-KEY}
```
```json
{
  "info": {
    "satname": "CAS500-1",
    "satid": 47932,
    "transactionscount": 0
  },
  "positions": [
    {
      "satlatitude": 77.19527745,
      "satlongitude": 21.20914327,
      "sataltitude": 511.05,
      "azimuth": 345.23,
      "elevation": -24.46,
      "ra": 22.65957619,
      "dec": 26.44078015,
      "timestamp": 1627974910,
      "eclipsed": false
    }
  ]
}
```

[To Infinity, and Beyond!](https://pypi.org/project/pySatellite/){ .md-button }


