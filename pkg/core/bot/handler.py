class Handler:
    def __init__(self, func, owner: str = "main", type="loop"):
        self.func = func
        self.owner = str(owner)
        self.type = type

    def run(self, event):
        if self.type == "loop":
            self.func()
            return
        self.func(event)
