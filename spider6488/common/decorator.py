import asyncio
import datetime
import functools
import time


def run_time(func):
    """
    单次爬取运行时间统计
    :param func:
    :return:
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        res = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        count_run_time = (end_time - start_time).total_seconds()
        print("###################   " + str(count_run_time) + "   ###################")
        return res
    return inner


DEFAULT_FMT = '[{elapsed:0.7f}ms] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            elapsed *= 1000
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


async def demo():
    for i in range(100):
        print()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(demo()))
    loop.run_until_complete(demo())
