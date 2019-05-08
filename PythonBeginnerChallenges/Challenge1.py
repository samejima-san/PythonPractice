{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too high!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too high!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 18\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too high!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too low\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too low\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too high!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You're too high!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between 1 and 50 11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You got it!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "i = False\n",
    "randnum = random.randint(1,51)\n",
    "while i == False:\n",
    "    userinput = int(input(\"Guess a number between 1 and 50\"))\n",
    "    if userinput > randnum:\n",
    "        print(\"You're too high!\")\n",
    "    elif userinput < randnum:\n",
    "        print(\"You're too low\")\n",
    "    else:\n",
    "        print(\"You got it!\")\n",
    "        i = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
