class queue:
    queues = []
    global front
    front = 0
    global rear
    rear = 0

    def __init__(self, value):
        if value == "queue":
            self.enqueue()
        elif value == "dequeue":
            self.dequeue()

    def enqueue(self):

        value = int(input("Enter the value to be queued:\n"))
        global rear
        self.queues.append(value)
        rear += 1
        print(rear)
        print(self.queues)
        self.display()

    def dequeue(self):

        global front
        global rear

        if rear == 0 and front == 0:
            print("Queue is empty")

        else:
            deleted = self.queues[front]
            del self.queues[front]
            rear = rear - 1
            print("dequeued {}".format(deleted))
            self.display()

    def display(self):

        print("Queue \n")

        for i in range(0, len(self.queues)):
            # print(i)
            print("| {} |".format(self.queues[i]), end='')
            # print("\n")
        print("\n")


if __name__ == "__main__":
    ch = ''
    while ch != 'exit':
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        # print("\n")
        ch = input("Enter queue to queue into queue \nEnter dequeue to dequeue from queue \nEnter exit to exit\n")
        call = queue(ch)
        # print("\n")
        print(
            "--------------------------------------------------------------------------------------------------------------------")
