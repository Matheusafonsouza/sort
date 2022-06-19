from typing import List


def swap(arr: List[int], i: int, j: int) -> None:
    """
    Simple method to swap two arr positions

    :param arr List[int]: list with values to be swaped
    :param i int: first position
    :param j int: second position
    """
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: List[int], left: int, right: int) -> int:
    """
    Algorithm that given a pivot value, separates the array in two slices:
    Values greater than pivot
    Values lower than pivot
    So then, put the pivot value between then.

    :param arr List[int]: list with values
    :param left int: left position pointer of the array
    :param right int: right position pointer of the array
    :returns int: pivot position between slices
    """
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    i += 1
    swap(arr, i, right)
    return i


def quick_sort(arr: List[int], left: int, right: int) -> None:
    """
    Implementation of quick sort algorithm to sort a given array
    :param arr List[int]: list with values to be sorted
    :param left int: left position pointer of the array
    :param right int: right position pointer of the array
    """
    if left >= right:
        return

    pivot_index = partition(arr, left, right)
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)


if __name__ == "__main__":
    arr = [-1, 3, 12, -2, -5, 14, 2]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [-5, -2, -1, 2, 3, 12, 14]
