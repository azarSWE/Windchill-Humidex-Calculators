# COMP 1026 – Assignment 1

# Azardokht Aryaei

# The purpose of this program is to calculate the windchill or humidex

import math

COLDEST_TEMPERATURE = -50  # minimum air temperature
MODERATELY_COLD_TEMPERATURE = 0  # moderately cold temperature
MODERATELY_WARM_TEMPERATURE = 20  # moderately warm temperature
WARMEST_TEMPERATURE = 50  # maximum air temperature
MIN_WIND_SPEED = 1  # minimum wind speed
MAX_WIND_SPEED = 99  # maximum wind speed

MIN_LOW_WINDCHILL = 0  # minimum low risk windchill
MAX_LOW_WINDCHILL = -9  # maximum low risk windchill
MIN_MODERATE_WINDCHILL = -10  # minimum moderate risk windchill
MAX_MODERATE_WINDCHILL = -27  # maximum moderate risk windchill
MIN_HIGH_WINDCHILL = -28  # minimum high risk windchill
MAX_HIGH_WINDCHILL = -39  # maximum high risk windchill
VERY_HIGH_WINDCHILL = -40  # very high risk windchill

MIN_LOW_HUMIDEX = 20  # minimum low discomfort humidex
MAX_LOW_HUMIDEX = 29  # maximum low discomfort humidex
MIN_MODERATE_HUMIDEX = 30  # minimum moderate discomfort humidex
MAX_MODERATE_HUMIDEX = 39  # maximum moderate discomfort humidex
MIN_HIGH_HUMIDEX = 40  # minimum high discomfort humidex
MAX_HIGH_HUMIDEX = 44  # maximum high discomfort humidex
VERY_HIGH_HUMIDEX = 45  # very high discomfort humidex

# a string variable which prompts the user whether the program must repeat or not
answer = 'y'

# ask user to enter a temperature between -50 and 50
temperature = float(input("Enter a temperature between -50 and 50: "))

while True:
    while COLDEST_TEMPERATURE <= temperature <= WARMEST_TEMPERATURE:

        # calculate windchill
        if COLDEST_TEMPERATURE <= temperature <= MODERATELY_COLD_TEMPERATURE:
            print("Calculating windchill.")

            # prompt user to enter wind speed
            windSpeed = float(input("Enter a wind speed between 1 and 99 km/h: "))
            while windSpeed < MIN_WIND_SPEED or windSpeed > MAX_WIND_SPEED:
                print("That wind speed is invalid.")
                windSpeed = float(input("Enter a wind speed between 1 and 99 km/h: "))

            windChill = round(13.12 + (0.6125 * temperature) - (11.37 * windSpeed ** 0.16) +
                              (0.3965 * temperature * windSpeed ** 0.16))

            print("The windchill is {}.".format(windChill), end=" ")

            # evaluate windchill range
            if MAX_LOW_WINDCHILL <= windChill <= MIN_LOW_WINDCHILL:
                print("Low risk.")
                break
            elif MAX_MODERATE_WINDCHILL <= windChill <= MIN_MODERATE_WINDCHILL:
                print("Moderate risk.")
                break
            elif MAX_HIGH_WINDCHILL <= windChill <= MIN_HIGH_WINDCHILL:
                print("High Risk. Skin can freeze in 10-30 minutes.")
                break
            elif windChill <= VERY_HIGH_WINDCHILL:
                print("Very High Risk. Skin can freeze in under 10 minutes.")
                break

        # calculate humidex
        elif MODERATELY_WARM_TEMPERATURE <= temperature <= WARMEST_TEMPERATURE:
            print("Calculating humidex.")

            # prompt user to enter dew point
            dewPoint = int(input("Enter the dewpoint between -50 and 50: "))
            while dewPoint < COLDEST_TEMPERATURE or dewPoint > temperature:
                print("That dew point is invalid.")
                dewPoint = int(input("Enter the dewpoint between -50 and 50: "))

            fahrenheitTemperature = 6.11 * (math.exp(5417.7530 * (1 / 273.16 - 1 / (273.16 + dewPoint))))
            celciusDegree = 5 / 9 * (fahrenheitTemperature - 10)
            humidex = round(temperature + celciusDegree)

            print("The humidex is {}.".format(humidex), end=" ")

            # evaluate humidex range
            if MIN_LOW_HUMIDEX <= humidex <= MAX_LOW_HUMIDEX:
                print("Little or no discomfort.")
                break
            elif MIN_MODERATE_HUMIDEX <= humidex <= MAX_MODERATE_HUMIDEX:
                print("Some discomfort.")
                break
            elif MIN_HIGH_HUMIDEX <= humidex <= MAX_HIGH_HUMIDEX:
                print("Great discomfort. Avoid exertion.")
                break
            elif humidex >= VERY_HIGH_HUMIDEX:
                print("Dangerous. Heat stroke possible.")
                break

        else:
            print("Windchill and humidex are not a factor at this temperature.")
            break

    # if temperature is out of range, prompt user to enter a new temperature
    else:
        print("That temperature is invalid.")
        temperature = float(input("Enter a temperature between -50 and 50: "))
        continue

    # ask user whether to repeat the program or not
    answer = input("Check another weather condition (Y/N)? ")
    while answer.lower() != "y" and answer.lower() != "n":
        print('That input is invalid.')
        answer = input("Check another weather condition (Y/N)? ")

    if answer.lower() == "y":
        temperature = float(input("Enter a temperature between -50 and 50: "))
        continue
    else:
        break
