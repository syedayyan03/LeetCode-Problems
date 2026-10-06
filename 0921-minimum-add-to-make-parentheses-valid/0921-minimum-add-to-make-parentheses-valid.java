class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> st = new Stack<>();

        char arr[] = s.toCharArray();

        for(int i=0; i<arr.length; i++){
            char ch = arr[i];
            if(ch == '('){
                st.push(ch);
            }
            else{
                if(st.isEmpty()){
                    st.push(ch);
                }
                else{
                char peekVal = st.peek();
                if(peekVal == '('){
                    st.pop();
                }
                else{
                    st.push(arr[i]);
                }
                }
            }
        }
        return st.size();
    }
}