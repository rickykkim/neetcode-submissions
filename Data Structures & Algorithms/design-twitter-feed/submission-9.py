class Twitter:

    def __init__(self):
        self.count = 1
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)      # user follows -> [...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet = [(-t[0], t[1]) for t in self.tweet[userId]]
        for user in self.following[userId]:
            for t in self.tweet[user]:
                tweet.append((-t[0], t[1]))
        
        heapq.heapify(tweet)
        res = []
        count_t = 10
        while count_t > 0 and len(tweet) > 0:
            _, tid = heapq.heappop(tweet)
            res.append(tid)
            count_t -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)