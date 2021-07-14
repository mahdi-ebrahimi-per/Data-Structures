# in priority queue, we insert number and delete maximum number in the queue
# در صف اولويتي، ما عدد اضافه ميکنيم، ووقت جذف، بزرگ ترين عدد يا آيتم رو از صف حذف ميکنيم

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

        #retuen all of item in queue / تمام آيتم هاي صف را بر ميگرداند
	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty / چک کردن خالي بود صف
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue / اضافه کردن آيتم به صف
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority / حذف آیتم از صف
	def delete(self): 
		try:
			# find biggest item / پیدا کردن بزرگ ترین آیتم
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

# Test 
myQueue = PriorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
print(myQueue)		

# delete and return all of items that deleted / حذف تمام آیتم ها و برگرداندن تمام آنهایی که حذف شده اند
while not myQueue.isEmpty():
	print(myQueue.delete())




# edited fire from Geeks for Geeks
