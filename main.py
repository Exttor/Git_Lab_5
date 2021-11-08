def medians(nums1, nums2):
    nums_all = nums1 + nums2
    nums_all.sort()
    print(nums_all)
    if len(nums_all)%2 == 0:
        return float((nums_all[:((int(len(nums_all)/2)) + 1)][-1] + nums_all[:((int(len(nums_all)/2)))][-1])/2)
    else:
        return float(nums_all[:((int(len(nums_all)/2)) + 1)][-1])
