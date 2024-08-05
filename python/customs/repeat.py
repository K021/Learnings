import asyncio
import logging

from asyncio import ensure_future
from typing import Callable, Container


def repeat_every(
    *,
    seconds: float = 1,
    wait_first: bool = False,
    logger: logging.Logger = None,
    raise_exceptions: bool = False,
    max_repetitions: int = None,
):
    """
    This function returns a decorator that schedules a function to execute periodically 
    after every `seconds` seconds.

    Parameters
    ----------
    seconds : float
        The number of seconds to wait before executing the function again.
    wait_first : bool, optional
        Whether to wait `seconds` seconds before executing the function for the first 
        time, by default False.
    logger : logging.Logger, optional
        The logger to use for logging exceptions, by default None.
    raise_exceptions : bool, optional
        Whether to raise exceptions instead of logging them, by default False.
    max_repetitions : int, optional
        The maximum number of times to repeat the function. If None, the function will 
        repeat indefinitely, by default None.
    """
    def decorator(func):
        is_coroutine = asyncio.iscoroutinefunction(func)
        
        async def repeat(*args, **kwargs):
            repetitions = 0

            if wait_first:
                await asyncio.sleep(seconds)

            while max_repetitions is None or repetitions < max_repetitions:
                try:
                    if is_coroutine:
                        await func(*args, **kwargs)
                    else:
                        func(*args, **kwargs)
                    
                except Exception as e:
                    if logger is not None:
                        logger.exception(e)
                    if raise_exceptions:
                        raise e

                repetitions += 1

                await asyncio.sleep(seconds)
        
        return repeat

    return decorator


async def arepeat(
    func: Callable,
    *,
    seconds: float,
    wait_first: bool = False,
    logger: logging.Logger = None,
    raise_exceptions: bool = False,
    max_repetitions: int = None,
    args: Container = (),
    kwargs: dict = {},
):
    """
    This function returns a decorator that schedules a function to execute periodically 
    after every `seconds` seconds.

    Parameters
    ----------
    seconds : float
        The number of seconds to wait before executing the function again.
    wait_first : bool, optional
        Whether to wait `seconds` seconds before executing the function for the first 
        time, by default False.
    logger : logging.Logger, optional
        The logger to use for logging exceptions, by default None.
    raise_exceptions : bool, optional
        Whether to raise exceptions instead of logging them, by default False.
    max_repetitions : int, optional
        The maximum number of times to repeat the function. If None, the function will 
        repeat indefinitely, by default None.
    """
    is_coroutine = asyncio.iscoroutinefunction(func)

    repetitions = 0

    if wait_first:
        await asyncio.sleep(seconds)
    
    while max_repetitions is None or repetitions < max_repetitions:
        try:
            if is_coroutine:
                await func(*args, **kwargs)
            else:
                await asyncio.to_thread(func, *args, **kwargs)

        except Exception as e:
            if logger is not None:
                logger.exception(e)
            if raise_exceptions:
                raise e
        
        repetitions += 1
        
        await asyncio.sleep(seconds)
    