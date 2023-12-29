import functools
import inspect
import sys


def log_dependency_by_flush(func):
    """
    Decorator that logs the function call details and flushes the output.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that logs the function call details and flushes the output.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            The result of the decorated function.
        """
        caller_frame = inspect.currentframe().f_back
        file_name = caller_frame.f_code.co_filename
        line_number = caller_frame.f_lineno

        show_with_newline(
            f"Calling function: {func.__name__} in {file_name}, line {line_number}"
        )
        sys.stdout.flush()  # Flush immediately after printing
        result = func(*args, **kwargs)
        show_with_newline(f"Function {func.__name__} completed")
        sys.stdout.flush()  # Flush immediately after printing
        return result

    return wrapper


def log_dependency(func):
    """
    Decorator that logs the function call details.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that logs the function call details.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            The result of the decorated function.
        """
        caller_frame = inspect.currentframe().f_back
        file_name = caller_frame.f_code.co_filename
        line_number = caller_frame.f_lineno

        show_with_newline(
            f"Calling function: {func.__name__} in {file_name}, line {line_number}"
        )
        result = func(*args, **kwargs)
        show_with_newline(f"Function {func.__name__} completed")
        return result

    return wrapper


def string_args(func):
    """
    Decorator that checks if any string parameters are provided.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that checks if any string parameters are provided.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            The result of the decorated function.
        """
        # Check if any string parameters are provided
        string_args = [arg for arg in args if isinstance(arg, str)]
        string_kwargs = {
            key: value for key, value in kwargs.items() if isinstance(value, str)
        }

        if not string_args and not string_kwargs:
            raise ValueError(f"{func.__name__} requires string parameters")

        result = func(*args, **kwargs)
        return result

    return wrapper


def iterable_args(func):
    """
    Decorator that checks if any iterable parameters are provided.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that checks if any iterable parameters are provided.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            The result of the decorated function.
        """
        # Check if any iterable parameters are provided
        iterable_args = [arg for arg in args if hasattr(arg, "__iter__")]
        iterable_kwargs = {
            key: value for key, value in kwargs.items() if hasattr(value, "__iter__")
        }

        if not iterable_args and not iterable_kwargs:
            raise ValueError(f"{func.__name__} requires iterable parameters")

        result = func(*args, **kwargs)
        return result

    return wrapper


def first_arg_iterable_rest_string(func):
    """
    Decorator that requires the first argument to be iterable and the rest to be strings.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that requires the first argument to be iterable and the rest to be strings.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            The result of the decorated function.
        """
        if not args or not hasattr(args[0], "__iter__"):
            raise ValueError(f"The first argument of {func.__name__} must be iterable")

        iterable_arg = args[0]
        string_args = [arg for arg in args[1:] if isinstance(arg, str)]
        string_kwargs = {
            key: value for key, value in kwargs.items() if isinstance(value, str)
        }

        if not (string_args or string_kwargs):
            raise ValueError(
                f"{func.__name__} requires string parameters after the iterable argument"
            )

        result = func(iterable_arg, *string_args, **string_kwargs)
        return result

    return wrapper


class MyIterable:
    """
    Custom iterable class for providing an iterator over a sequence of data.

    Attributes:
        data (list): The underlying data to iterate over.

    Methods:
        __init__(self, data: list): Initializes the MyIterable instance with the provided data.
        __iter__(self): Returns an iterator for the MyIterable instance.
        __next__(self): Retrieves the next item from the data sequence.

    Example:
        >>> data_sequence = [1, 2, 3, 4, 5]
        >>> iterable_instance = MyIterable(data_sequence)
        >>> for item in iterable_instance:
        ...     print(item)
        ...
        1
        2
        3
        4
        5
    """

    def __init__(self, data: list):
        """
        Initializes the MyIterable instance with the provided data.

        Args:
            data (list): The sequence of data to iterate over.
        """
        self.data = data

    def __iter__(self):
        """
        Returns an iterator for the MyIterable instance.

        Returns:
            MyIterable: The iterator itself.
        """
        return self

    def __next__(self):
        """
        Retrieves the next item from the data sequence.

        Returns:
            Any: The next item from the data sequence.

        Raises:
            StopIteration: If there are no more items in the data sequence.
        """
        if not self.data:
            raise StopIteration
        return self.data.pop(0)


@string_args
def show_with_newline(string):
    """
    Function to print a string with a newline and flush the output.

    Args:
        string (str): The string to be printed.

    Returns:
        None
    """
    print(string)
    sys.stdout.flush()


@string_args
def show(string):
    """
    Function to print a string without a newline and flush the output.

    Args:
        string (str): The string to be printed.

    Returns:
        None
    """
    print(string, end="")
    sys.stdout.flush()
