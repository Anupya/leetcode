"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
"""
from typing import List 

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.feed = {}
        self.all_tweets = [] # all tweets created by anyone ever, sorted from most to least recent

    def _addUserToAllObjects(self, userId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        if userId not in self.followers:
            self.followers[userId] = []
        if userId not in self.feed:
            self.feed[userId] = []

    def _updateFeed(self, userId: int, tweetId: int) -> None:
        if userId in self.feed:
            self.feed[userId] = [tweetId] + self.feed[userId]
        else:
            self.feed[userId] = [tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._addUserToAllObjects(userId)

        # store it in user's tweets and all tweets
        self.tweets[userId].append(tweetId)
        self.all_tweets = [tweetId] + self.all_tweets
        
        # update feed for all followers
        for followerId in self.followers[userId]:
            self._updateFeed(followerId, tweetId)
        
        # update feed for tweet poster
        self._updateFeed(userId, tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        return self.feed[userId][:10] if userId in self.feed else []

    def follow(self, followerId: int, followeeId: int) -> None:
        self._addUserToAllObjects(followerId)
        self._addUserToAllObjects(followeeId)

        # add to list of followers
        if followeeId in self.followers:
            if followerId in self.followers[followeeId]: # duplicate follow, do nothing
                return
            self.followers[followeeId].append(followerId)
        else:
            self.followers[followeeId] = [followerId]
        
        # followee has not tweeted anything
        if followeeId not in self.tweets:
            return

        # add all tweets of followee to follower's feed
        new_feed = []
        for tweetId in self.all_tweets:
            if tweetId in self.tweets[followeeId]: # if tweeted by new followee, add it
                new_feed.append(tweetId)
            elif tweetId in self.feed[followerId]: # if already in the feed, add it
                new_feed.append(tweetId)
        self.feed[followerId] = new_feed

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._addUserToAllObjects(followerId)
        self._addUserToAllObjects(followeeId)

        if followeeId in self.followers and followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
            if not self.tweets[followeeId]: # if the unfollowed person never tweeted anything
                return 

            # get current feed of followerId and remove all the followee tweets
            new_feed = []
            for tweetId in self.feed[followerId]:
                if tweetId not in self.tweets[followeeId]:
                    new_feed.append(tweetId)
            self.feed[followerId] = new_feed

            

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)