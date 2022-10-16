# import the module
import python_weather
import asyncio
import os


async def getweather(city):
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(format=python_weather.METRIC) as client:

        # fetch a weather forecast from a city
        weather = await client.get(city)

        # returns the current day's forecast temperature (int)
        # print(weather.current.temperature)

        return weather.current.temperature

