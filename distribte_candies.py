def distrbute_candies(candies, num_people):
    res = [0] * num_people
    i = 1
    while i < candies:
        idx = (i - 1) % num_people
        res[idx] += i
        candies -= i
        i += 1

    res[(i - 1) % num_people] += candies

    return res


if __name__ == '__main__':
    print(distrbute_candies(10, 3))
