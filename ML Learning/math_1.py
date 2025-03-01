def gradient(X):
    for i in range(1, 21):
        step = 0.1
        grad = 2 * X
        X = X - step * grad

    print(X)


if __name__ == "__main__":
    initial_X = 10
    gradient(initial_X)