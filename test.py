from multiProcessing.multiProcessing import MultiProcessing
import time

mp_obj = MultiProcessing()

def example_function(arg):
    print(f"Processing {arg}")
    time.sleep(1)
    return f"Processed {arg}"


if __name__ == '__main__':
    mp_obj.run_multiprocess(func=example_function, args=['Hello, World!', ''])