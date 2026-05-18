from http.client import HTTPException

from exceptions import CalculatorError, EmptyListError, DivisionByZeroError,LogarithmError
import math


def validate_numbers(nums):
    if nums is None:
        raise CalculatorError("numbers are required")
    if len(nums) == 0:
        raise EmptyListError("numbers list cannot be empty")
    return nums


def calculate_sum(nums, base=None):
    nums = validate_numbers(nums)
    return sum(nums)


def calculate_product(nums, base=None):
    nums = validate_numbers(nums )

    result = 1
    for n in nums:
        result *= n

    return result


def calculate_difference(nums, base=None):
    nums = validate_numbers(nums)

    result = nums[0]
    for n in nums[1:]:
        result -= n

    return result


def calculate_division(nums, base=None):
    nums = validate_numbers(nums)
    if len(nums) < 2:
        raise CalculatorError("division requires at least 2 numbers")
    if 0 in nums[1:]:
        raise DivisionByZeroError("division by zero is not allowed")
    result = nums[0]
    for n in nums[1:]:
        result /= n
    return result

def logarithms(nums, base=None):
    nums = validate_numbers(nums)

    for n in nums:
        if n <= 0:
            raise LogarithmError(
                "logarithm is only defined for positive numbers"
            )

    if base is not None:
        if base <= 0:
            raise LogarithmError("base must be positive")

        if base == 1:
            raise LogarithmError("base cannot be 1")

        return [math.log(n, base) for n in nums]

    return [math.log(n) for n in nums]
