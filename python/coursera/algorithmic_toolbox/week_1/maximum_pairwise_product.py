# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    index_1 = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index_1]:
            index_1 = i

    index_2 = 0
    for i in range(1, len(numbers)):
        if numbers[i] != A[index_1] and numbers[i] > numbers[index_2]:
            index_2 = i

    return numbers[index_1] * numbers[index_2]

if __name__ == '__main__':
    # n = int(input())
    # input_numbers = list(map(int, input().split()))
    # assert len(input_numbers) == n
    # print(max_pairwise_product(input_numbers))
    n = 10**5
    A = [0] * n
    print(max_pairwise_product_naive(A))

