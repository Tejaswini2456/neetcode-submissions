class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        indegree = {c:0 for word in words for c in word}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        queue = deque(
            c for c in indegree if indegree[c] == 0
        )
        order = []
        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in adj[char]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != len(indegree):
            return ""
        return "".join(order)