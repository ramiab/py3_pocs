# from asyncio import Queue
import numbers

class EmptyQueueException(Exception):
    pass

class BaseQ():
    def __init__(self):
        self.l = list()

    def enqueue(self, x):
        assert isinstance(x, numbers.Number)
        self.l.append(x)

    def dequeue(self):
        return self.l.pop(0)

    def peek_first(self):
        return self.l[0]

    def peek_last(self):
        return self.l[len(self.l)-1]

    def empty(self):
        return self.l==None or len(self.l)==0

    def clear(self):
        self.l=[]

class MainQ(BaseQ):
    def __init__(self, min_q):
        super().__init__()
        self.min_q = min_q

    def enqueue(self, x):
        super().enqueue(x)
        if self.min_q.empty():
            self.min_q.enqueue(x)
        elif x > self.min_q.peek_last():
            self.min_q.enqueue(x)
        else: # x <= self.min_q.peek_last():
            self.min_q.clear()
            self.min_q.enqueue(x)

    def dequeue(self):
        if self.empty():
            raise EmptyQueueException("Queue is empty")
        x = super().dequeue()
        if x == self.min_q.peek_first():
            self.min_q.dequeue()
        return x

    def get_min(self):
        if self.empty():
            raise EmptyQueueException("Queue is empty, NO minimum")
        return self.min_q.peek_first()

INPUT_NUMS = (("+", 5), ("+", 10), ("+", 3), ("+", 6), ("+", 1), ("+", 2), ("+", 4), ("+", -4), ("+", 100), ("+", -40),
              ("-",None), ("-",None), ("-",None), ("+",-400), ("+",90), ("-",None),
              ("-",None), ("-",None), ("-",None), ("-",None), ("-",None), ("-",None), ("-",None), ("-",None))

if __name__ == '__main__':
    min_q = BaseQ()
    main_q = MainQ(min_q)

    try:
        for operator, i in INPUT_NUMS:
            if operator=="+":
                main_q.enqueue(i)
                print("Added {} ; Min is: {}".format(i,main_q.get_min()))
                print("main_q = {}".format(main_q.l))
                print("min_q = {}".format(main_q.min_q.l))
                print("==========")
            else:
                x = main_q.dequeue()
                print("Removed {} ; Min is: {}".format(x,main_q.get_min()))
                print("main_q = {}".format(main_q.l))
                print("min_q = {}".format(main_q.min_q.l))
                print("==========")
    except Exception as e:
        print("exception: {}".format(e))


