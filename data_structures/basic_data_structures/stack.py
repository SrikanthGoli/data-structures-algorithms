
# Stack Data Structure
class stack(object):

    def __init__(self):

        self.stack = []
        self.size = -1

    def len(self):

        return len(self.stack)

    def push(self, data):

        self.stack.append(data)
        self.size += 1

    def pop(self):

        self.stack.remove(self.stack[self.size])
        self.size -= 1

    def display(self):

        print(self.stack)


test = stack()
test.push(10)
test.push(20)
test.push(30)
test.push(40)
test.push(50)
test.push(60)
test.pop()

print(test.display())