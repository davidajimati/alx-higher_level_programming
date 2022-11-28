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
	listint_t *two;
	listint_t *one;

	if (list == NULL || list->next == NULL)
		return (0);

	while (one && two && two->next)
	{
		if (one == two)
			return (1);

		one = list->next;
		two = list->next->next;
	}
	return (0);
}
