print(f'loading run.py:__name__={__name__}')

import module1

#That means when we run a file python change the name of that module to main
import timing
code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100)
print(result)

#If we name a file __main__.py we can call directory and even zipfiles