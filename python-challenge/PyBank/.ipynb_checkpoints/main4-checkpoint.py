{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-48ede006f68a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     12\u001b[0m     \u001b[0mcsvreader\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mcsv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcsvfile\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdelimiter\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m','\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mheader\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcsvreader\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcsvreader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m     \u001b[0mmonth_count\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "#path to the csvfile\n",
    "csvpath = os.path.join('Resources', 'budget_data.csv')\n",
    "\n",
    "#lists to add csv data \n",
    "month_count=[]\n",
    "profit=[]\n",
    "change_profit=[]\n",
    "\n",
    "with open(csvpath, 'r') as csvfile:\n",
    "    csvreader= csv.reader(csvfile, delimiter=',')\n",
    "    header=next(csvreader)\n",
    "for row in csvreader:\n",
    "    month_count.append(row[0])\n",
    "\n",
    "#print(f\"csv Header:{header}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<tokenize>\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    for i in range(len(profit)-1):\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for row in csvreader:\n",
    "        month_count.append(row[0])\n",
    "        profit.append(int(row[1]))\n",
    "    for i in range(len(profit)-1):\n",
    "        change_profit.append(profit[i+1]-profit[i])"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
