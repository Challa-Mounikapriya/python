{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number4\n",
      "1\n",
      "2\n",
      "6\n",
      "24\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter a number\"))\n",
    "factorial=1\n",
    "for i in range(1,n+1):\n",
    "    factorial*=i\n",
    "    print(factorial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number4\n",
      "1\n",
      "2\n",
      "6\n",
      "24\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter a number\"))\n",
    "factorial=1\n",
    "i=1\n",
    "while i<=n:\n",
    "    factorial*=i\n",
    "    i+=1\n",
    "    print(factorial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}