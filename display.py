import re

s = "05:22D 06:02 06:19D 06:33D 06:46 07:00D 07:13 07:26 07:39 07:52 08:06 08:22D 08:35 09:00 09:20 09:45 10:00 10:20D 10:35 10:55 11:18 11:37 11:48D 12:02 12:18D 12:35 12:50 13:00 13:12 13:31 13:46D 14:05 14:25D 14:45 15:05D 15:25 15:44D 16:02 16:25D 16:38 16:52 17:07D 17:27 17:37 17:52 18:07 18:22 18:37D 18:53 19:08D 19:25D 19:43 20:08 20:30D 21:00D 21:30D 22:00 22:30D 23:00 23:30 00:00"
times = s.split(" ")
byhour = {}
for time in times:
  parser = re.match("([0-9]{2}):([0-9]{2})(D?)", time)
  hour, minute, options = parser.groups(0)
  if not byhour.has_key(int(hour)):
    byhour[int(hour)] = []
  byhour[int(hour)].append(minute)

out = ""
for hour, minutes in byhour.iteritems():
  out += "%02d: " % hour
  for minute in minutes:
    out += "%s " % minute
  out += "\n"

print out
