class MissingNumber:

    def __init__(self):
        print("Finding a missing number")

    def missing_number(self, nums: list) -> int:
        """
        Task 2: This method returns a missing number from the array
        :param self: it is necessary for creating a new class instance
        :param nums: input list of numbers
        """
        nums.sort()
        print(f"Sorted input list: {nums}")
        for i in nums:
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1
