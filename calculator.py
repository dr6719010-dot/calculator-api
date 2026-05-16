from fastapi import HTTPException


def validate_numbers(nums):
    if nums is None:
        raise HTTPException(status_code=400, detail="numbers are required")

    if len(nums) == 0:
        raise HTTPException(status_code=400, detail="numbers list cannot be empty")

    return nums


def calculate_sum(nums):
    nums = validate_numbers(nums)
    return sum(nums)


def calculate_product(nums):
    nums = validate_numbers(nums)

    result = 1
    for n in nums:
        result *= n

    return result


def calculate_difference(nums):
    nums = validate_numbers(nums)

    result = nums[0]
    for n in nums[1:]:
        result -= n

    return result


def calculate_division(nums):
    nums = validate_numbers(nums)

    if len(nums) < 2:
        raise HTTPException(
            status_code=400,
            detail="division requires at least 2 numbers"
        )

    if 0 in nums[1:]:
        raise HTTPException(
            status_code=400,
            detail="division by zero is not allowed"
        )

    result = nums[0]
    for n in nums[1:]:
        result /= n

    return result