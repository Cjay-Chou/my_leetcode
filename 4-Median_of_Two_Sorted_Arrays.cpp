/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

*/

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
{
	//get two array's length
	int len1 = nums1.size();
	int len2 = nums2.size();
	int len = len1 + len2;
	//Sort two arrays
	int *nums = new int[len];
	int i = 0, j = 0;
	for (int k = 0; k < len; ++k) {
		if (j == len2 || (i < len1 && nums1[i] < nums2[j])) {
			nums[k] = nums1[i++];
		}
		else {
			nums[k] = nums2[j++];
		}
	}
	//Median based on odd or even length
	if (len % 2 != 0)
		return nums[len / 2];
	else
		return (nums[len / 2 - 1] + nums[len / 2]) / 2.0;

}