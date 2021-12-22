
class Solution:
    def nextGreaterElement0(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            cur_greater = -1
            start_index = nums2.index(nums1[i])
            for j in range(start_index, len(nums2)):
                if nums2[j] > nums1[i]:
                    cur_greater = nums2[j]
                    break
            res.append(cur_greater)
        return res

    def nextGreaterElement(self, nums1, nums2):
        res = []
        for num in nums1:
            tmp = []
            max = -1
            is_found = False
            while len(nums2) and not is_found:
                top = nums2.pop()
                if top > num:
                    max = top
                elif top == num:
                    is_found = True
                tmp.append(top)
            res.append(max)
            while len(tmp) != 0:
                nums2.append(tmp.pop())
        return res