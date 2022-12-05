import logging
import time

YELLOW = "\x1b[33;20m"
GREEN = "\033[92m"
RESET = "\x1b[0m"

logging.basicConfig(
    level=logging.INFO,
    format=YELLOW + '\n\n%(levelname)s: ' + RESET +'%(asctime)s - %(message)s'
)


def timelogger(year: int, day: int, part: int=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()

                if part == None:
                    logging.info(
                        f"AoC {year}, Day {day}: {func.__name__}() took {end - start:.3f} seconds"
                    )
                else:
                    logging.info(
                        f"AoC {year}, Day {day} | Part {part}: {func.__name__}() took {end - start:.3f} seconds"
                    )
            except Exception as e:
                logging.error(e)
            else:
                return result
        return wrapper
    return decorator