"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns ""."""

"""
Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.
"""


class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ds:
            self.ds[key].append([timestamp, value])
        else:
            self.ds[key] = [[timestamp, value]]

        
    def display(self):
        print(self.ds)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds or not self.ds[key]:
            return ""
        elif len(self.ds[key]) == 1 and self.ds[key][0][0] <= timestamp:
            return self.ds[key][0][1]
        else:
            left = 0
            right = len(self.ds[key]) - 1
            prev_mid = None
            while left <= right:
                mid = (left + right) // 2
                if self.ds[key][mid][0] == timestamp:
                    return self.ds[key][mid][1]
                elif self.ds[key][mid][0] > timestamp:
                    right = mid - 1
                elif self.ds[key][mid][0] < timestamp:
                    prev_mid = mid
                    left = mid + 1
            if prev_mid is None:
                return ""
            else:
                return self.ds[key][prev_mid][1]
        

    
test = TimeMap()
test.set("foo", "bar", 1)
print(test.get("foo", 1))
print(test.get("foo", 3))
test.set("foo", "bar2", 4)
print(test.get("foo", 4))
print(test.get("foo", 5))
test.display()




# O(log n) time complexity
class TimeMap2:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ds:
            self.ds[key].append([timestamp, value])
        else:
            self.ds[key] = [[timestamp, value]]

        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.ds.get(key, [])
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    

test = TimeMap2()
test.set("foo", "bar", 1)
print(test.get("foo", 1))
print(test.get("foo", 3))
test.set("foo", "bar2", 4)
print(test.get("foo", 4))
print(test.get("foo", 5))
test.display()
