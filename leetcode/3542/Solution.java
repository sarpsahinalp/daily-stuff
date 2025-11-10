import java.util.Stack;

class Solution {
    public int minOperations(int[] nums) {
        Stack<Integer> monotonicStack = new Stack<>();
        int out = 0;

        for (Integer num : nums) {
            int last = monotonicStack.isEmpty() ? 0 : monotonicStack.peek();
            while (num < last) {
                monotonicStack.pop();
                out += 1;
                last = monotonicStack.isEmpty() ? 0 : monotonicStack.peek();
            }

            if (num != 0 && last != num) {
                monotonicStack.push(num);
            }
        }

        return out + monotonicStack.size();
    }
}