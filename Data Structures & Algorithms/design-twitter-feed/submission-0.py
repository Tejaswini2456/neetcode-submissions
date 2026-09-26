import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.following:
            self.following[userId] = set()

        self.following[userId].add(userId)

        heap = []

        for followee in self.following[userId]:

            if followee not in self.tweets:
                continue

            tweets = self.tweets[followee]

            index = len(tweets) - 1

            time, tweetId = tweets[index]

            heapq.heappush(
                heap,
                (-time, tweetId, followee, index - 1)
            )

        result = []

        while heap and len(result) < 10:

            time, tweetId, followee, index = heapq.heappop(heap)

            result.append(tweetId)

            if index >= 0:

                time, tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)
