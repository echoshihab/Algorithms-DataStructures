"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
 and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call
to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in 
the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


constraints
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
A user cannot follow himself.

"""


from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.postCount = 0
        self.userTweet = defaultdict(list)  # tracking tweet ids and count of post for a given user
        self.userFollowee = defaultdict(set) # tracking folowee ids of the follower

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweet[userId].append([self.postCount, tweetId])
        self.postCount -= 1 # decrementing to utilize max heap
        

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []
        maxHeap = []

        self.userFollowee[userId].add(userId)
        for followeeId in self.userFollowee[userId]:
            if followeeId in self.userTweet:
                index = len(self.userTweet[followeeId]) - 1
                postCount, tweetId = self.userTweet[followeeId][index]
                maxHeap.append([postCount, tweetId, followeeId, index-1])
        heapq.heapify(maxHeap)

        while maxHeap and len(recentTweets) < 10:
            postCount, tweetId, followeeId, index = heapq.heappop(maxHeap)
            recentTweets.append(tweetId) 
            if index >= 0:
                postCount, tweetId = self.userTweet[followeeId] [index]
                heapq.heappush(maxHeap, [postCount, tweetId, followeeId, index - 1])
        
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowee[followerId]:
            self.userFollowee[followerId].remove(followeeId)