
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """


    def findMid(nums1, nums2, s1, s2, len1, len2, mid):
        print(nums1, nums2, s1, s2, len1, len2, mid, "##")
        if len1 > len2:
            return findMid(nums2, nums1, s2, s1, len2, len1, mid)
        if len1 == 0:
            return nums2[s2 + mid - 1]
        if mid == 1:
            return min(nums1[s1], nums2[s2])
        i = min(len1, mid//2)
        j = min(len2, mid//2)

        if nums1[s1 + i - 1] > nums2[s2 + j - 1]:
            return findMid(nums1, nums2, s1, s2 + j, len1, len2 - j, mid - j)
        else:

            return findMid(nums1, nums2, s1 + i, s2, len1 - i, len2, mid - i)

    len1 = len(nums1)
    len2 = len(nums2)
    s1 = 0
    s2 = 0
    mid1 = (len1 + len2 + 1 )//2
    mid2 = (len1 + len2 + 2 )//2
    return (findMid(nums1, nums2, s1, s2, len1, len2, mid1) + findMid(nums1, nums2, s1, s2, len1, len2, mid2))/2

nums1 = [2]
nums2 = [1, 3, 4]

print(findMedianSortedArrays(nums1, nums2))