class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       
       for (int i = 0; i < strs[0].length(); i++){
        for(const auto &s : strs) {
            if (s.length() == i || s[i] != strs[0][i]){
                return s.substr(0,i);
            }
        }
       }
       return strs[0];
    }
};