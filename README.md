bus-catcher
===========

Fetches information from Florianópolis bus lines and displays in a stem-and-leaf plot.

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

05:27D 05:45D 06:13D 06:27D 06:45D 06:52
07:00 07:13D 07:20 07:32D 07:45D 08:00D
08:30 09:02D 09:33D 10:03 10:33D 11:05D
11:20D 11:25D 11:32D 11:47D 12:00 12:13D
12:27D 12:40 12:48D 13:05 13:23 13:42
14:02D 14:23 14:43 15:03D 15:23D 15:43
16:03D 16:20 16:30D 16:40 16:55 17:10D
17:20D 17:30 17:40 17:50D 18:00 18:10
18:20D 18:30D 18:40D 18:50 19:00D 19:10
19:20 19:30 19:40D 19:52D 20:02D 20:12
20:22 20:33 20:56 21:10D 21:25 21:42
21:58 22:15D 22:30 22:40D 22:50 23:00D
23:20 23:33D 00:12 01:00

Taken from: http://www.consorciofenix.com.br/horarios/ingleses,264

How it becomes in stem-and-leaf:

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

Future
======

This was just a coding exercise, but can expand to a exporter of bus lines data to different
formats, to store in database and to show it on the web or make an API available.

Feel free to fork and I'll be glad to accept pull requests.
