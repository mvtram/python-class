{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a value 8\n",
      "enter a value 4\n",
      "enter a value 2\n",
      "enter a value -1\n",
      "[8, 4, 2]\n",
      "4.666666666666667\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'float' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-8f322c16009d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m/\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmax\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'float' object is not iterable"
     ]
    }
   ],
   "source": [
    "lst=[]\n",
    "a=[]\n",
    "for i in range(0,4,1):\n",
    "    x=int(input(\"enter a value \"))    \n",
    "    if x>0:\n",
    "        lst.append(x)\n",
    "    else:\n",
    "        break\n",
    "print(lst[0:4])\n",
    "for i in lst:\n",
    "    if i%2==0:\n",
    "            a.append(i)\n",
    "    \n",
    "\n",
    "\n",
    "a=sum(a)/len(a)\n",
    "print(a)\n",
    "#a=max(a)\n",
    "#print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime numbers between 1 and 50 are:\n",
      "2\n",
      "3\n",
      "5\n",
      "7\n",
      "11\n",
      "13\n",
      "17\n",
      "19\n",
      "23\n",
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n"
     ]
    }
   ],
   "source": [
    "lower = 1\n",
    "upper = 50\n",
    "print(\"Prime numbers between\",lower,\"and\",upper,\"are:\")\n",
    "\n",
    "for num in range(lower,upper + 1):\n",
    "   # prime numbers are greater than 1\n",
    "   if num > 1:\n",
    "    for i in range(2,num):\n",
    "           if (num % i) == 0:\n",
    "            break\n",
    "    else:\n",
    "           print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter integers5\n",
      "enter integers6\n",
      "enter integers7\n",
      "enter integers8\n",
      "enter integers9\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "lisb=[]\n",
    "for i in range(0,5,1):\n",
    "    x=int(input(\"enter integers\"))\n",
    "    lisb.insert(i,x)\n",
    "print(len(lisb))\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisb[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisb.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 8, 7, 6, 5]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes\n"
     ]
    }
   ],
   "source": [
    "if 5 in lisb:\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"NO\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisb.count(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "del lisb[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[8, 7, 6, 5]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "del lisb[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisb.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6, 7, 8]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "count=0\n",
    "for x in lisb:\n",
    "    if x>5:\n",
    "        count+=1\n",
    "    else:\n",
    "        break\n",
    "print(count)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randint\n",
    "lisc=[]\n",
    "for i in range(20):\n",
    "    lisc.append(randint(1,100))"
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
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[76, 88, 18, 15, 17, 58, 6, 9, 97, 90, 17, 2, 65, 97, 35, 7, 48, 27, 44, 46]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "43.1\n"
     ]
    }
   ],
   "source": [
    "print(sum(lisc)/len(lisc))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisc.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 6, 7, 9, 15, 17, 17, 18, 27, 35, 44, 46, 48, 58, 65, 76, 88, 90, 97, 97]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "97"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisc[0]\n",
    "lisc[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "count=0\n",
    "for i in lisc:\n",
    "    if i%2==0:\n",
    "        count+=1\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[8, 17, 10]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisd=[8,9,10]\n",
    "lisd[1]=17\n",
    "lisd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisd.append(4)\n",
    "lisd.append(5)\n",
    "lisd.append(6)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisd.pop(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[17, 10, 4, 5, 6]"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisd.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisd=lisd*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 5, 6, 10, 17, 4, 5, 6, 10, 17]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "lisd.insert(3,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lisd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "int() argument must be a string, a bytes-like object or a number, not 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-c4ecea79992e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mnumbers\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mnumbers\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\",\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumbers\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: int() argument must be a string, a bytes-like object or a number, not 'list'"
     ]
    }
   ],
   "source": [
    "numbers=[]\n",
    "numbers = int(input().split(\",\"))\n",
    "print(len(numbers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12 12 12 12 11 10 1 3 4 5 11 11 \n"
     ]
    }
   ],
   "source": [
    "numbers=[]\n",
    "s=input()\n",
    "numbers = list(map(int, s.split()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[12, 12, 12, 12, 11, 10, 1, 3, 4, 5, 11, 11]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'replace' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-5f8bd0fcc82b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mnumbers\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m>\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m         \u001b[0mnumbers\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'replace' is not defined"
     ]
    }
   ],
   "source": [
    "\n",
    "for x in numbers:\n",
    "    if x>10:\n",
    "        numbers[replace(x,10)]\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[12, 12, 10, 1, 3, 4, 5, 11]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "first=[\"hello\",\"mahesh\",\"rohan\"]\n",
    "second=[]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ello\n",
      "ahesh\n",
      "ohan\n"
     ]
    }
   ],
   "source": [
    "import string\n",
    "for x in first:\n",
    "    a=x.replace(x[0],\"\")\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1,\n",
       " 4,\n",
       " 9,\n",
       " 16,\n",
       " 25,\n",
       " 36,\n",
       " 49,\n",
       " 64,\n",
       " 81,\n",
       " 100,\n",
       " 121,\n",
       " 144,\n",
       " 169,\n",
       " 196,\n",
       " 225,\n",
       " 256,\n",
       " 289,\n",
       " 324,\n",
       " 361,\n",
       " 400,\n",
       " 441,\n",
       " 484,\n",
       " 529,\n",
       " 576,\n",
       " 625,\n",
       " 676,\n",
       " 729,\n",
       " 784,\n",
       " 841,\n",
       " 900,\n",
       " 961,\n",
       " 1024,\n",
       " 1089,\n",
       " 1156,\n",
       " 1225,\n",
       " 1296,\n",
       " 1369,\n",
       " 1444,\n",
       " 1521,\n",
       " 1600,\n",
       " 1681,\n",
       " 1764,\n",
       " 1849,\n",
       " 1936,\n",
       " 2025,\n",
       " 2116,\n",
       " 2209,\n",
       " 2304,\n",
       " 2401,\n",
       " 2500]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L=[]\n",
    "for x in range(1,51):\n",
    "    L.append(x**2)\n",
    "L    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "122"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ord(\"z\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "alpha=[]\n",
    "c=[]\n",
    "for x in range(0,26,1):\n",
    "    alpha.append(chr(97+x)*3)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aaa',\n",
       " 'bbb',\n",
       " 'ccc',\n",
       " 'ddd',\n",
       " 'eee',\n",
       " 'fff',\n",
       " 'ggg',\n",
       " 'hhh',\n",
       " 'iii',\n",
       " 'jjj',\n",
       " 'kkk',\n",
       " 'lll',\n",
       " 'mmm',\n",
       " 'nnn',\n",
       " 'ooo',\n",
       " 'ppp',\n",
       " 'qqq',\n",
       " 'rrr',\n",
       " 'sss',\n",
       " 'ttt',\n",
       " 'uuu',\n",
       " 'vvv',\n",
       " 'www',\n",
       " 'xxx',\n",
       " 'yyy',\n",
       " 'zzz']"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "alpha"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter size of list4\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "[1, 3, 5, 7]\n",
      "[2, 4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter size of list\"))\n",
    "L=[]\n",
    "M=[]\n",
    "N=[]\n",
    "for x in range(n):\n",
    "    s=int(input())\n",
    "    L.append(s)\n",
    "    #L = list(map(int,s.split()))\n",
    "    p=int(input())\n",
    "    M.append(p)\n",
    "    #M =list(map(int,p.split()))\n",
    "print(L)\n",
    "print(M)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "for x in range(n):\n",
    "    g=L[x]\n",
    "    h=M[x]\n",
    "    N.append(g+h)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 7, 11, 15]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of M\n",
      "4\n",
      "Enter numbers: 1 2 3 4 \n",
      "enter the value of N\n",
      "4 \n",
      "Enter numbers: 2 3 5 6\n",
      "4\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"enter the value of M\")  \n",
    "\n",
    "M=int(input())\n",
    "m=set() \n",
    "\n",
    "#for x in range(M):\n",
    "    #s=input().split()\n",
    "    #m.add(s)\n",
    "m= set(map(int, input('Enter numbers: ').split()))\n",
    "\n",
    "print(\"enter the value of N\") \n",
    "N=int(input())\n",
    "n=set()\n",
    "#for y in range(N):\n",
    "#    p=input().split()\n",
    "#    n.add(p)    \n",
    "n= set(map(int, input('Enter numbers: ').split()))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "E=set()\n",
    "E=m.difference(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "F=set()\n",
    "\n",
    "F=n.difference(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 5, 6]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "E.update(F)\n",
    "sorted(E)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected character after line continuation character (<ipython-input-15-d222863659aa>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-15-d222863659aa>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print(\"E\"\\n)\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected character after line continuation character\n"
     ]
    }
   ],
   "source": [
    "print(\"E\"\\n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "M"
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
