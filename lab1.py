import logging

logging.basicConfig(level=logging.INFO)


def fibonachi(number):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < number - 2:
        fibsum = fib1 + fib2
        fib1 = fib2
        fib2 = fibsum
        i += 1
    logging.info(fib2)
    return


def main():
    while True:
        try:
            number = int(input("Input number: "))
            break
        except ValueError:
            logging.error("Invalid type! Please try again.")
    fibonachi(number)
    return


if __name__ == "__main__":
    main()
