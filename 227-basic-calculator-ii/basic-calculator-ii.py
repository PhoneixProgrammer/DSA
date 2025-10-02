import operator

class Solution:
    def calculate(self, s: str) -> int:
        def div_trunc(a, b):
            # Integer division truncated toward zero
            return a // b if a * b >= 0 else -(abs(a) // abs(b))

        # Stacks for numbers and operators
        nums = []
        oper = []

        # Operator functions with precedence handling
        opers = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": div_trunc
        }

        # Current number accumulator (handles multi-digit numbers)
        num = 0
        # Last operator (default + to handle first number)
        last_op = "+"

        # Traverse string left to right
        s = s.replace(" ", "")  # remove spaces for simplicity
        n = len(s)
        i = 0

        while i < n:
            ch = s[i]

            if ch.isdigit():
                # Build multi-digit numbers
                num_start = i
                while i < n and s[i].isdigit():
                    i += 1
                num = int(s[num_start:i])
                i -= 1  # adjust for extra increment at end of number

                # Apply high-precedence immediately (* /)
                if last_op in "*/":
                    prev = nums.pop()
                    num = opers[last_op](prev, num)

                nums.append(num)
            elif ch in "+-*/":
                last_op = ch  # store last operator

            i += 1

        # After traversal, calculate remaining + and - from left to right
        res = nums[0]
        idx = 1
        i = 0
        last_op = "+"
        s = s.replace(" ", "")
        for ch in s:
            if ch.isdigit():
                continue
            if ch in "+-":
                res = opers[ch](res, nums[idx])
                idx += 1

        return res
