import asyncio

import python_weather


async def get_weather_now(location):
    """Returns the current weather state of a specific location
    Ret: Temp(C), Description, Feels_like"""
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(location)
        state = weather.current
        return state.temperature, state.description, state.feels_like


async def get_weather_today(location):
    """Returns the state of the weather today in the location
    Ret: Max_temp, Min_temp, [(time, Chance of Rain, Description)]"""
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        temps = []
        descriptions = []

        weather = await client.get(location)
        forecast = iter(weather.forecasts)
        for forecast in weather.forecasts:
            for hour in forecast.hourly:
                temps.append(hour.temperature)
                descriptions.append((hour.time, hour.chances_of_rain, hour.description))

            return max(temps), min(temps), descriptions


print(asyncio.run(get_weather_today(location="latakia")))
