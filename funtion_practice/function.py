from util.logger import get_logger
logger = get_logger()


def func_name():
    logger.info('Welcome to function')
    return 'Yes'


logger.info(func_name())
func_name()


def sum_two(a, b):
    logger.info('The number given for sum are a:%s and b:%s', a, b)
    result = a + b
    logger.info(result)
    return a + b


logger.info(sum_two(1, 1))
sum_two(1, 5)
fun = sum_two(10, 10)
print(fun)


# Example of default argument

def sum_three(a, b, c=1):
    logger.info('value of c:%s', c)
    result = a + b + c
    logger.info(result)
    return result


sum_three(c = 5, b = 10, a = 4)

sum_two(1, b=3)
sum_three(1, c=30, b=20)
#sum_two(1, a=1)
#sum_three(1, 2, b=20)


def handle_error(div_func):
    def modified_div_two_num(a,b):
        if b:
            return a/b

    return modified_div_two_num


@handle_error
def div_two_num(a, b):
    logger.info("a:%s, b:%s",a, b)
    return a/b


logger.info(div_two_num(4,2))
logger.info(div_two_num(4,0))
