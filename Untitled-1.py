class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)
        self.position = 0
 
    def __getitem__(self, item):
        return self.buffer[item]
 
    def write(self, text):
        for ch in text:
            if self.position < len(self.buffer):
                self.buffer[self.position] = ch
                self.position += 1

b = Buffer()
b.write("hello")
print(b[0]) # h
print(b[1]) # e
print(b[2]) # l
print(b[3]) # l
print(b[4]) # o