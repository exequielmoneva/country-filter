# Country filter API

A simple API for filtering countries from a dataset over an specific satisfaction index value.


# Requirements
 - Docker
 - Python 3.8

# Installation
Inside the root folder of the project, run the following command

```sh
> docker-compose build
```

Then start the project with the following command

```sh
> docker-compose up
```

Now, you should be able to test the endpoints.

# Available API endponits:

## Get API health
this endpoint allows you to check whether the API is running or not. If the API is running, you should receive a simple confirmation message.

```
http://localhost:5000/
```
Example response:
```
API is running
```

## GET filtered countries

```
http://localhost:5000/country/satisfaction_index
```
Example response with satisfaction_index 100000:
```json
{
  "countries": [
    {
      "Country": "Belgium",
      "Flags": "",
      "Indicator": "Household net financial wealth",
      "Inequality": "Total",
      "Measure": "Value",
      "PowerCode": "Units",
      "Reference Period": "",
      "Unit": "US Dollar",
      "Value": 104084
    },
    {
      "Country": "Switzerland",
      "Flags": "",
      "Indicator": "Household net financial wealth",
      "Inequality": "Total",
      "Measure": "Value",
      "PowerCode": "Units",
      "Reference Period": "",
      "Unit": "US Dollar",
      "Value": 128415
    },
    {
      "Country": "United States",
      "Flags": "",
      "Indicator": "Household net financial wealth",
      "Inequality": "Total",
      "Measure": "Value",
      "PowerCode": "Units",
      "Reference Period": "",
      "Unit": "US Dollar",
      "Value": 176076
    }
  ]
}
```

## Swagger endpoint
This endpoint allows anyone to visualize and interact with the API's resources.

```
http://localhost:5000/api/docs
```

### ToDos

 - Write integration tests
 - Apply cache for the GET endpoint
