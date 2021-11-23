class YotClub:
    def __init__(self, cool):
        self.cool_inv = 100 - cool

    def get_cool(self):
        return self.cool_inv

    def change_cool(self, cool):
        self.cool_inv = 100 - cool


res = YotClub(900)
print(res.get_cool())
res.change_cool(2345)
print(res.get_cool())
