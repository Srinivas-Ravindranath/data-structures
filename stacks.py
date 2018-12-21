class Stacks:
    stck = []
    global length
    length = -1

    def __init__(self, value):
        if value == "pop":
            self.pop()
        elif value == "push":
            self.push()

    def push(self):
        # self.length = -1
        value = int(input("Enter the value to be pushed: "))
        self.stck.append(value)
        global length
        length = length + 1
        self.display()

    def pop(self):

        global length
        if length == -1:
            print("stack underflow")

        else:
            print("{} popped \n".format(self.stck[length]))
            del self.stck[length]
            length = length - 1

        self.display()

    def display(self):

        print("Stack \n")
        print(" -----")
        for i in range(len(self.stck) - 1, -1, -1):
            # print(i)
            print("| {} |".format(self.stck[i]))
        print(" -----")


if __name__ == "__main__":
    ch = ''
    while ch != 'exit':
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        ch = input("Enter pop to pop from stack \nEnter push to push to stack \nEnter exit to exit\n")
        call = Stacks(ch)
        print(
            "--------------------------------------------------------------------------------------------------------------------")
