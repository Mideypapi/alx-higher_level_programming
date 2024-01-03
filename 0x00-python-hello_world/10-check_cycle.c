#include "lists.h"

/**
 * check_cycle - checks if the linked list contains d cycle
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *eagle = list;
	listint_t *chick = list;

	if (!list)
		return (0);

	while (eagle && chick && chick->next)
	{
		eagle = eagle->next;
		chick = chick->next->next;
		if (eagle == chick)
			return (1);
	}

	return (0);
}
