"""Time logger to be used as a decorator for my
Advent of Code solutions.
"""
import logging
import time

YELLOW = "\x1b[33;20m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\x1b[0m"

logging.basicConfig(
    level=logging.INFO,
    format=YELLOW + '\n\n%(levelname)s: ' + RESET + '%(asctime)s - %(message)s'
)


def timelogger(year: int = 0, day: int = 0, part: int | None = None):
    """Decorator to time the execution of a function.

    Parameters:
    -----------
        year: int
            The year of the AoC puzzle.
        day: int
            The day of the AoC puzzle.
        part: int or None
            The part of the AoC puzzle (optional). If set to None,
            part will not be printed.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()

                time_taken = end - start
                if time_taken < 0.5:
                    time_taken = GREEN + f"{time_taken*1000:.2f} " + RESET + "ms"
                elif time_taken < 1:
                    time_taken = YELLOW + f"{time_taken*1000:.2f} " + RESET + "ms"
                else:
                    time_taken = RED + f"{time_taken:.2f} " + RESET + "s"

                if part is None:
                    logging.info(
                        f"AoC {year}, Day {day}:               {func.__name__}() took {time_taken}"
                    )
                else:
                    logging.info(
                        f"AoC {year}, Day {day} | Part {part}: {func.__name__}() took {time_taken}"
                    )
            except Exception as e:
                logging.error(e)
            else:
                return result
        return wrapper
    return decorator

