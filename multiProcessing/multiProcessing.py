from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp
from tqdm import tqdm
import logging


class MultiProcessing:
    """
    This class provides various multiprocessing utilities for Python.
    """

    def __init__(self):
        """
        Initializes the library.

        num_processes (int): defaults to the number of available CPUs.
        """

        self.num_processes = mp.cpu_count()

    @property
    def num_processes(self):
        return self.__num_processes

    @num_processes.setter
    def num_processes(self, num_processes):
        if num_processes < 1:
            raise ValueError('num_processes must be greater than 0.')
        if num_processes > mp.cpu_count():
            raise ValueError('num_processes must be less than or equal to the number of CPUs.')
        self.__num_processes = num_processes

    def _validate_function(self, func):
        """
        Ensures the provided function is callable.

        Args:
            func: The function to validate.

        Raises:
            ValueError: If `func` is not callable.
        """

        if not callable(func):
            raise ValueError("The provided function is not callable.")


    def run_multiprocess(self, func, args, return_results=False):
        """
        Executes the given function in multiple processes.

        Args:
            func: The function to execute.
            args: An iterable of arguments for each process.
            futures (bool, optional): Whether to return futures instead of results.
                Defaults to False.
            return_results (bool, optional): Whether to return the results from each process.
                Defaults to False.
            callback (callable, optional): A function to call with no arguments after each process completes.
                Defaults to None.

        Returns:
            A list of results (if `return_results` is True) or a list of futures (if `futures` is True).
        """

        self._validate_function(func)

        with ProcessPoolExecutor(max_workers=self.num_processes) as executor:
            try:
                results = []
                with tqdm(total=len(args)) as pbar:
                    for result in executor.map(func, args):
                        results.append(result)
                        pbar.update()
                if return_results:
                    return results
            except Exception as e:
                logging.error(e)
                raise e