class Solution {
public:

// 0 = RED, 1 = WHITE, 2 = BLUE 

    void sortColors(vector<int>& nums) {
        vector<int> count(3); 

        for(int& num : nums){  // go through each number in the nums array
            count[num]++; // update the index each time by 1 when seen in nums
        }

        int index = 0;
        for (int i = 0; i < 3; i++){ // go through all 3 indexs in our count array
            for(int j = 0; j < count[i]; j++){ // repeat for each number of 0's 1's and 2's
                nums[index++] = i; // place number and then increase index as well, so we place correct number of 0's,1's,2's
            }
        }
    }
};