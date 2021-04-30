# You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

# You may jump forward from index i to index j (with i < j) in the following way:

# During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
# During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
# It may be the case that for some index i, there are no legal jumps.
# A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

# Return the number of good starting indices.


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        # ODD JUMPS: sort indices of arr by values in arr and create a stack that contains every other index
        sorted_indexes = sorted(range(len(arr)), key = lambda i: arr[i])
        oddnext = self.makeStack(sorted_indexes)

        # EVEN JUMPS: sort indices of arr by values in arr in reverse order and create a stack that contains every other index
        sorted_indexes.sort(key = lambda i: arr[i], reverse = True)
        evennext = self.makeStack(sorted_indexes)

        # initialize odd and even lists that will contain
        # the information of if the end can be reached
		# from the respective index
        odd = [False] * len(arr)
        even = [False] * len(arr)

        # the last index is always counted
        odd[len(arr)-1] = even[len(arr)-1] = True

        # iterate through arr backwards, starting at next to last element
        for i in range(len(arr)-2, -1, -1):

            # if an odd jump is available from current index,
            # check if an even jump landed on the index of the available
            # odd jump and set current index in odd to True if it did
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]

            # if an even jump is available from current index,
            # check if an odd jump landed on the index of the available
            # even jump and set current index in even to True if it did
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum(odd)
    
    # makes monotonic stack
    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        # delete stack as a memory optimization
        del stack
        return result