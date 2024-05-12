#include "search_algos.h"

/**
 * linear_search - a function that searches for a value in an array
 *                 of integers using the Linear search algoritha
 * @array: A pointer to the first element in the array
 * @size: Number of elements in the array
 * @value: The value to search
 *
 * Return: Array[i] if value is found, otherwise -1
*/

int linear_search(int *array, size_t size, int value)
{
	size_t i;

	if (!array || !array[0])
		return (-1);

	for (i = 0; i < size; i++)
	{
		if (value == array[i])
		{
			printf("Value checked array[%li] = [%i]\n", i, array[i]);
			return (array[i]);
		}

		printf("Value checked array[%li] = [%i]\n", i, array[i]);

	}
	return (-1);
}
