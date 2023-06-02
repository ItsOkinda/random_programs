# circular queue is a queue similar to linear queue but the last item is connected to the first item
# it also follows the fifo order 
#also known as a ring buffer
# implemented in traffic lights since each ligt is given a specific ammount of time to be on and goes on and on
# has 2 pointers rear and rear(last element)

class CircularQueue():
    def __init__(self,value):
        self.value=value
        self.queue = [None for i in range(value)]
       #value defines size of the queue
        self.front = self.rear = -1

    def enqueue(self,data):
        #check if queue is full
        if (self.front==  (self.rear+1) %self.value):
            print(" Queue is full .......")
        
        #check if queue is empty
        elif(self.front== -1):

            self.front = self.rear =0
            self.queue[self.rear]=data

        else:
            self.rear = self.rear+1 %self.value
            self.queue[self.rear]=data

    def dequeue(self,data):
        if (self.front== -1):
            print("error queue is empty")
        elif self.front == self.rear:
            item = self.queue[self.front]
            elf.front=self.rear+1
            return item
        else :
            item = self.queue[self.front]
            self.front = self.front+1 % self.value
            return item

    def display(self):
        if self.front==- 1:
            print("queue i empty")
        
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end="")
            
            print()


que = CircularQueue(5)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(55)
que.display() 