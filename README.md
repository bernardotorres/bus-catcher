bus-catcher
===========

Fetches information from Florianópolis bus lines and displays in a stem-and-leaf plot.

To run it:

```
$ python setup.py install
$ scrapy crawl fenix
```

I recommend running it inside a virtualenv, since it has very strict setup.py dependencies.

Introduction
============

Inspired by Edward R. Tufte's book, Envisioning Information, which describes timetables
for japan's train lines and from my experience with the same visualization in european city
bus lines, I wanted to make the same exercise in information display for the bus lines in
Florianópolis.

It is a simple change in display, but it can helps finding the next bus faster and grouping
by time it has the advantage of showing the frequency for each hour, thus making it easier
to know when there are more busses available.

How it is today:

| 04:52D | 05:15D | 05:35D | 05:54D | 06:12D | 06:40D |
|--------|--------|--------|--------|--------|--------|
| 07:07D | 07:20  | 07:29  | 07:42D | 07:49  | 08:02D |
| 08:15D | 08:28D | 08:58  | 09:30D | 10:00D | 10:31  | 
| 11:01D | 11:32D | 11:50D | 11:57D | 12:15D | 12:27  |
| 12:42D | 12:55D | 13:10  | 13:15D | 13:34  | 13:55  |
| 14:11  | 14:30D | 14:51  | 15:12  | 15:31D | 15:52D |
| 16:11  | 16:33D | 16:50  | 17:05D | 17:17  | 17:28  | 
| 17:44D | 17:53D | 18:06  | 18:16  | 18:25D | 18:36  |
| 18:46  | 18:55D | 19:02D | 19:12D | 19:24  | 19:30D | 
| 19:40  | 19:50  | 20:00  | 20:10D | 20:23D | 20:31D | 
| 20:41  | 20:52  | 21:03  | 21:38D | 21:52  | 22:11  |
| 22:43D | 23:20  | 00:00D |

Taken from: http://www.consorciofenix.com.br/horarios/ingleses,264

How it becomes in stem-and-leaf:

```
LINHA Ingleses - 264
ORIGEM Dias Úteis - Saída TICAN - Terminal Integração Canasvieiras
SAÍDAS:
05: 27 45
06: 13 27 45 52
07: 00 13 20 32 45
08: 00 30
09: 02 33
10: 03 33
11: 05 20 25 32 47
12: 00 13 27 40 48
13: 05 23 42
14: 02 23 43
15: 03 23 43
16: 03 20 30 40 55
17: 10 20 30 40 50
18: 00 10 20 30 40 50
19: 00 10 20 30 40 52
20: 02 12 22 33 56
21: 10 25 42 58
22: 15 30 40 50
23: 00 20 33
00: 12
01: 00
```

Future
======

This was just a coding exercise, but can expand to a exporter of bus lines data to different
formats, to store in database and to show it on the web or make an API available.

Adding scrappers, it could also fetch bus information for other cities.

Feel free to fork and I'll be glad to accept pull requests.
