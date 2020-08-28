{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "not prime\n"
     ]
    }
   ],
   "source": [
    "n=int(input())#6\n",
    "fc=0\n",
    "for i in range(1,n+1):#1,7\n",
    "      if n%i==0:#6%1,6%2,6%3,6%6\n",
    "          fc+=1#1,2,3,6\n",
    "if fc==2:\n",
    "      print(\"prime\")\n",
    "else:\n",
    "      print(\"not prime\")#6 is not prime\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "def prime(n):\n",
    "    for i in range(2,abs(int(math.sqrt(n)))+1): \n",
    "        if n%i==0:\n",
    "            break\n",
    "    else:\n",
    "        return(prime)\n",
    "prime()\n",
    "n=int(input())\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "53\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'prime'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def prime(n):\n",
    "    for i in range(2,int(n**0.5)+1):\n",
    "        if n%i==0:\n",
    "            return (\"not prime\")\n",
    "    return (\"prime\")\n",
    "n=int(input())\n",
    "prime(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
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
