class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8

    def __len__(self) -> int:
        return self.length

    def __set_item__(self, key, value) -> None:
        index = hash(key)


