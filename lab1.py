import logging
logging.basicConfig(level=logging.INFO)


def main():
    fib1 = 1
    fib2 = 1
    while True:
        try:
            n = int(input('input number: '))
            break
        except ValueError:
            logging.info('Invalid type! Please try again.')
    i=0
    while i < n - 2:
        fibsum = fib1 + fib2
        fib1 = fib2
        fib2 = fibsum
        i += 1
    logging.info(fib2)
    return

if __name__ == '__main__':
    main()

