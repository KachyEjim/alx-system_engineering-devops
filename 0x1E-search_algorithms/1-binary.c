#include "search_algos.h"

/**
 * print_array - prints an array
 *
 * @arr: The array to be printed
 * @left: The left index of the sub-array being printed
 * @right: The right index of the sub-array being printed
 *
 */

void print_array(int arr[], size_t left, size_t right)
{
	size_t i;

	printf("Searching in array: ");
	for (i = left; i <= right; i++)
	{
		printf("%d", arr[i]);
		if (i < right)
			printf(", ");
	}
	printf("\n");
}

/**
 * binary_search - A function that searches for a value in a
 *       sorted array of integers using the Binary search algorithm
 *
 * @array: A pointer to the first element in the array
 * @size: Number of elements in the array
 * @value: The value to search
 *
 * Return: Array[i] if value is found, otherwise -1
 *
 */

int binary_search(int *array, size_t size, int value)
{
	size_t left = 0, right = size - 1, mid;

	if (!array)
		return (-1);


	while (left <= right)
	{
		mid = left + (right - left) / 2;
		print_array(array, left, right);
		if (array[mid] == value)
			return (mid);
		else if (array[mid] < value)
			left = mid + 1;
		else
			right = mid - 1;
	}
	return (-1);
}
