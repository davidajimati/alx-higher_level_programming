#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - function to check if there is a cycle in linked lists
 *
 * @list: singly linked list
 * Return: 1 if cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
<<<<<<< HEAD
	if (list == NULL || list->next == NULL)
		return (0);

	listint_t *one = malloc(sizeof(list));

	if (one == NULL)
		return (0);

	listint_t *two = malloc(sizeof(list));

	if (two == NULL)
		return (0);

	while (one && two && two->next)
=======
	listint_t *one = list;
	listint_t *two = list;

	while (one != NULL && two != NULL)
>>>>>>> parent of 880d3d4 (solved)
	{
		one = list->next;
		two = list->next->next;
		if (one == two)
			return (1);
	}
	free(one);
	free(two);
	return (0);
}
