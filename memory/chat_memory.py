class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, q, a):
        self.history.append((q, a))

    def get(self):
        return self.history[-5:]
