class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
       List<List<Integer>> li = new ArrayList<>();
       Arrays.sort(nums);
       int n = nums.length;
       Set<ArrayList<Integer>> set = new HashSet<>();
       for(int i = 0;i<n;i++){
        for(int j = i+1;j<n;j++){
            int left = i+1;
            int right = j-1;
            long sum = nums[i]+nums[j];
            while(left<right){
                if(sum+nums[right]+nums[left]>target){
                    right--;
                }else if(sum+nums[right]+nums[left]<target)
                    left++;
                else{
                    if(!set.contains(new ArrayList<>(Arrays.asList(nums[i],nums[left],nums[right],nums[j]))))
                    li.add(new ArrayList<>(Arrays.asList(nums[i],nums[left],nums[right],nums[j])));
                    set.add(new ArrayList<>(Arrays.asList(nums[i],nums[left],nums[right],nums[j])));
                    left++;
                    right--;
                }
            }
        }
       }
       return li;
    }
}