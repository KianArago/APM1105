{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0f338f2a",
   "metadata": {},
   "source": [
    "# Start the Python interpreter and use it as a calculator."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92377d1e",
   "metadata": {},
   "source": [
    "# Exercises 1-2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90ecf752",
   "metadata": {},
   "source": [
    "#### 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5d5ada4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.00 kilometers is equal to 6.21 miles!\n"
     ]
    }
   ],
   "source": [
    "kilometers = 10\n",
    "\n",
    "mile_per_km = 0.621371\n",
    "\n",
    "miles = kilometers * mile_per_km\n",
    "\n",
    "print('%0.2f kilometers is equal to %0.2f miles!' %(kilometers,miles))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f39d56fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the distance value in kilometers: 10\n",
      "10.00 kilometers is equal to 6.21 miles\n"
     ]
    }
   ],
   "source": [
    "# Taking kilometers input from the user\n",
    "kilometers = float(input(\"Enter the distance value in kilometers: \"))\n",
    "\n",
    "# conversion factor\n",
    "mile_per_km = 0.621371\n",
    "\n",
    "# calculate miles\n",
    "miles = kilometers * mile_per_km\n",
    "print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e769479c",
   "metadata": {},
   "source": [
    "#### 3. If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "62419b4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exercises 1-2. Item 3\n",
      "\n",
      "Pace in minutes per mile: 7.003500000000001\n",
      "Average speed in mph: 8.567144998929106\n"
     ]
    }
   ],
   "source": [
    "from __future__ import print_function, division\n",
    "\n",
    "print(\"Exercises 1-2. Item 3\\n\")\n",
    "\n",
    "mins = 43.5\n",
    "hours = mins / 60\n",
    "\n",
    "km_per_mile = 1.61\n",
    "distance_in_km = 10 \n",
    "miles = distance_in_km / km_per_mile \n",
    "\n",
    "pace = mins / miles\n",
    "mph = miles / hours\n",
    "\n",
    "print('Pace in minutes per mile:', pace)\n",
    "print('Average speed in mph:', mph)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}