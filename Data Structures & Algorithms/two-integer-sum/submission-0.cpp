class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       int n = nums.size();
       unordered_map<int, int> previous_numbers;
       for (int i = 0; i < n; i++){
            int diff = target - nums[i];
            if (previous_numbers.find(diff) != previous_numbers.end()){
                return {previous_numbers[diff],i};
            }
            previous_numbers.insert({nums[i],i});
       }
       return {};
    }
};
