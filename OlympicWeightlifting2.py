{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import matplotlib\n",
    "import matplotlib.pylab as plt\n",
    "import scipy as sp\n",
    "%matplotlib inline\n",
    "import math\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "r = requests.get(\"http://www.iwf.net/results/ranking-list/?ranking_year=2015&ranking_agegroup=Senior&ranking_gender=M&ranking_category=all&ranking_lifter=all&x=18&y=10\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "r.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(r.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "rows = soup.find_all(\"tr\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#this list will collect the body weight of the lifters\n",
    "bw = []\n",
    "for row in rows:\n",
    "    cells = row.find_all('td')\n",
    "\n",
    "    \n",
    "\n",
    "    for i, cell in enumerate(cells):\n",
    "        if i == 4:\n",
    "            bw.append(cell.text.strip())\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "len(bw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#this list will collect the total lifted by the lifters.\n",
    "total = []\n",
    "for row in rows:\n",
    "    cells = row.find_all('td')\n",
    "\n",
    "    \n",
    "\n",
    "    for i, cell in enumerate(cells):\n",
    "        if i == 7:\n",
    "            total.append(cell.text.strip())\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "len(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#A and b are the constants given to calculate the Sinclair coefficient and Sinclair total\n",
    "A = 0.794358141\n",
    "b = 174.393\n",
    "#this lis will collect the Sinclair total of the lifters.\n",
    "sinclair = []\n",
    "\n",
    "for i in range(len(total)):\n",
    "    if float(bw[i]) > b:\n",
    "        ts = float(total[i])\n",
    "        sinclair.append(ts)\n",
    "    \n",
    "    else:\n",
    "        s = math.log(float(bw[i])/b, 10)\n",
    "        ts = float(total[i])*(10**(A*(s**2)))\n",
    "        sinclair.append(ts)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "len(sinclair)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#56kg weight class\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([40, 56, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many lifters are in the 56kg weight class\n",
    "a1 = 0\n",
    "b1 = 0\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 56:\n",
    "        a1 = a1+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 56 and sinclair[i] >= 400:\n",
    "        b1 = b1+1        \n",
    "        \n",
    "c1 = 100*(b1/a1) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b1,a1,c1)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#62kg weight class\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([56.01, 62, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many lifters in the 62\n",
    "a2 = 0\n",
    "b2 = 0\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 62 and float(bw[i]) > 56:\n",
    "        a2 = a2+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 62 and float(bw[i]) > 56 and sinclair[i] >= 400:\n",
    "        b2 = b2+1        \n",
    "        \n",
    "c2 = 100*(b2/a2) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b2,a2,c2)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#69\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([62.01, 69, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 69\n",
    "a3 = 0\n",
    "b3 = 0\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 69 and float(bw[i]) > 62:\n",
    "        a3 = a3+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 69 and float(bw[i]) > 62 and sinclair[i] >= 400:\n",
    "        b3 = b3+1        \n",
    "        \n",
    "c3 = 100*(b3/a3) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b3,a3,c3)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#77\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([69.01, 77, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 77\n",
    "a4 = 0\n",
    "b4 = 0\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 77 and float(bw[i]) > 69:\n",
    "        a4 = a4+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 77 and float(bw[i]) > 69 and sinclair[i] >= 400:\n",
    "        b4 = b4+1        \n",
    "        \n",
    "c4 = 100*(b4/a4) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b4,a4,c4)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#85\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([77.01, 85, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 85\n",
    "a5 = 0\n",
    "b5 = 0\n",
    "\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 85 and float(bw[i]) > 77:\n",
    "        a5 = a5+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 85 and float(bw[i]) > 77 and sinclair[i] >= 400:\n",
    "        b5 = b5+1        \n",
    "        \n",
    "c5 = 100*(b5/a5) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b5,a5,c5)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#94\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([85.01, 94, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 94\n",
    "a6 = 0\n",
    "b6 = 0\n",
    "\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 94 and float(bw[i]) > 85:\n",
    "        a6 = a6+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 94 and float(bw[i]) > 85 and sinclair[i] >= 400:\n",
    "        b6 = b6+1        \n",
    "        \n",
    "c6 = 100*(b6/a6) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b6,a6,c6)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#105\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([94.01, 105, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 105\n",
    "a7 = 0\n",
    "b7 =0\n",
    "\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 105 and float(bw[i]) > 94:\n",
    "        a7 = a7+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) <= 105 and float(bw[i]) > 94 and sinclair[i] >= 400:\n",
    "        b7 = b7+1        \n",
    "        \n",
    "c7 = 100*(b7/a7) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b7,a7,c7)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#105 plus\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([105, 191, 100, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#how many in 105 plus\n",
    "a8 = 0\n",
    "b8 = 0\n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) > 105:\n",
    "        a8 = a8+1\n",
    "        \n",
    "for i in range(len(bw)):\n",
    "    if float(bw[i]) > 105 and sinclair[i] >= 400:\n",
    "        b8 = b8+1        \n",
    "        \n",
    "c8 = 100*(b8/a8) \n",
    "#b  number of people with a sinclair above 400, c percentage.\n",
    "print(b8,a8,c8) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#plot of total based on body weight\n",
    "plt.plot(bw, total, 'ro')\n",
    "plt.axis([35, 192, 0, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#plot of sinclair total based on body weight\n",
    "plt.plot(bw, sinclair, 'ro')\n",
    "plt.axis([35, 192, 0, 500])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
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
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
