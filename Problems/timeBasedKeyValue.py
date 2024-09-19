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

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds or not self.ds[key]:
            return ""
        else:
            left = 0
            right = len(self.ds[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.ds[key][mid][0] == timestamp:
                    return self.ds[key][mid][1]
                elif self.ds[key][mid][0] > timestamp:
                    right = mid - 1
                elif self.ds[key][mid][0] < timestamp:
                    left = mid + 1
                    if left < len(self.ds[key]) and self.ds[key][left][0] > timestamp:
                        return self.ds[key][mid][1]
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)