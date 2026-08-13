import java.util.*;

class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> q = new LinkedList<>();

        for (int val : students) {
            q.add(val);
        }

        int i = 0;
        int count = 0;

        while (!q.isEmpty()) {

            if (q.peek() == sandwiches[i]) {
                q.poll();
                i++;
                count = 0;
            } 
            else {
                int val = q.poll();
                q.add(val);
                count++;
            }

            if (count == q.size()) {
                break;
            }
        }

        return q.size();
    }
}