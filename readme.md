## Requirements
The package uses matplotlib and pandas for data manipulations and numpy for calculations.
There is an issue with conda repos downgrading numpy for the lastest pandas (0.24). I need histogram2d function from new numpy but `to_numpy()` function from new pandas. Currently, that seems to be impossible.

## Development
uses *pytest* for testing

