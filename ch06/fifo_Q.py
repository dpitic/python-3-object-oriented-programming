from queue import Queue
from queue import Empty
from queue import Full

# Demonstration of the use of FIFO Queue

lineup = Queue(maxsize=3)
try:
	lineup.get(block=False)
except Empty as e:
	print("Queue is empty")

lineup.put("one")
lineup.put("two")
lineup.put("three")
try:
	lineup.put("four", timeout=1)
except Full as e:
	print("Queue is full")

print("lineup.full() = {}".format(lineup.full()))
print("lineup.get() = {}".format(lineup.get()))
print("lineup.get() = {}".format(lineup.get()))
print("lineup.get() = {}".format(lineup.get()))
print("lineup.empty() = {}".format(lineup.empty()))
