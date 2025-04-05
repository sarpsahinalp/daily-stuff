function subsetXORSum(nums: number[]): number {
    return xorSum(nums, 0, 0)
};

function xorSum(nums: number[], index: number, currentXor: number) {
    if (index == nums.length) return currentXor;

    let withElement = xorSum(nums, index + 1, currentXor ^ nums[index]);

    let withoutElement = xorSum(nums, index + 1, currentXor);

    return withElement + withoutElement;
}