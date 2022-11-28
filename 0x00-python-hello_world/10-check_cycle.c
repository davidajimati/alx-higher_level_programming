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
	listint_t *one = list;
	listint_t *two = list;

	while (one != NULL && two != NULL)
	{
		one = list->next;
		two = list->next->next;
		if (one == two)
			return (1);
	}
	return (0);
}
