class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            # The leftmost number should be the largest
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Append after ensuring that
            q.append(r)

            # Remove outdated index
            if l > q[0]:
                q.popleft()
            
            # Only start adding when the window size is met
            if (r + 1) >= k:
                # Add the leftmost since that's the largest
                output.append(nums[q[0]])
                # Start shifting left when the window size is met
                l += 1
            # Until then (or always), move the right boundary
            r += 1

        return output