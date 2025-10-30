class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.feed = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.timer, tweetId))      
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.following[userId].add(userId)
        for following in self.following[userId]:
            for time, post in self.feed[following]:
                heapq.heappush(feed, (time, post))
                if len(feed) > 10:
                    heapq.heappop(feed)
        res = []
        while feed:
            _, id = feed[0]
            res.append(id)
            heapq.heappop(feed)
        return res[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)