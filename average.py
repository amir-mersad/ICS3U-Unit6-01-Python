#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program creates 10 random numbers and calculate the average

import random
import math


def main():
    # This function creates 10 random numbers and calculate the average
    list_numbers = []
    average = 0

    # Process
    for number_of_numbers in range(1, 10 + 1):
        number = random.randint(1, 100)
        list_numbers.append(number)
        print(number)
    for counter in list_numbers:
        average = (counter + average)
    average = average / 10

    # Output
    print(f"\n{average}")


if __name__ == "__main__":
    main()
