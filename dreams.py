HOUSE_PRICE = 1000000


def get_tests():
    def get_test(test):
        return test.strip().split(" ")

    def _generate():
        file = open("dreams.txt", "r")
        tests = file.readlines()[1:]
        file.close()

        for test in tests:
            yield list(map(lambda x: float(x), get_test(test)))

    return list(_generate())


output = open("output.txt", "a")

for test, variables in enumerate(get_tests()):

    m, c, t, n, i, k = variables

    # savings
    r = 0

    # current month
    month = 1

    while r < HOUSE_PRICE:

        r += m - c

        # tax months
        if month % n == 0:
            r -= t * (n * m)

        # unexpected expense month
        if month % k == 0:
            r -= i

        month += 1

    output.write(f"Case #{test + 1}: {month - 1}\n")

output.close()
