from typing import Any


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self) -> None:
        self.__capacity = 8
        self.__length = 0
        self.__hash_table = [None] * self.__capacity
        self.__load_factor = 2/3

    def __len__(self) -> int:
        return self.__length

    def __setitem__(self, key: Any, value: Any) -> None:
        node = Node(key, value)
        index = node.hash % self.__capacity
        if self.__hash_table[index] is None:
            self.__hash_table[index] = node
            self.__length += 1
        else:
            if self.__hash_table[index].key != key:
                index = Dictionary.find_bucket(self.__hash_table, index, self.__capacity)
                self.__hash_table[index] = node
                self.__length += 1
            else:
                self.__hash_table[index] = node

        if self.__length >= self.__load_factor * self.__capacity:
            self.__resize()

    @staticmethod
    def find_bucket(hash_table: list, index: int, capacity: int) -> int:
        i = 1
        while True:
            next_index = (index + i) % capacity
            if hash_table[next_index] is None:
                return next_index
            i += 1

    def __resize(self) -> None:
        new_capacity = self.__capacity * 2

        new_hash_table = [None] * new_capacity
        for node in self.__hash_table:
            if node is not None:
                new_index = node.hash % new_capacity
                if new_hash_table[new_index] is not None:
                    new_index = Dictionary.find_bucket(new_hash_table, new_index, new_capacity)
                new_hash_table[new_index] = node

        self.__hash_table = new_hash_table
        self.__capacity = new_capacity

    def __getitem__(self, key) -> None:
        _hash = hash(key)
        index = _hash % self.__capacity
        if self.__hash_table[index] is None:
            raise KeyError(f"Key {key} not found!")
        if self.__hash_table[index].key != key:
            raise KeyError(f"Key {key} not found!")

        return self.__hash_table[index].value

    def clear(self) -> None:
        self.__hash_table = [None] * self.__capacity
        self.__length = 0

    def __delitem__(self, key) -> None:
        _hash = hash(key)
        index = _hash % self.__capacity
        if self.__hash_table[index] is None:
            raise KeyError(f"Key {key} not found!")
        if self.__hash_table[index].key != key:
            raise KeyError(f"Key {key} not found!")

        del self.__hash_table[index]
        self.__length -= 1


custom_dict = Dictionary()
custom_dict[8] = "8"
custom_dict[16] = "16"
custom_dict[32] = "32"
custom_dict["one"] = 1
custom_dict["one"] = 11
custom_dict["f"] = 60
custom_dict["g"] = 70
# value = custom_dict["a"]
# value2 = custom_dict["b"]
