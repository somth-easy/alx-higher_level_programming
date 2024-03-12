#include "lists.h"

/**
 * check_cycle - entry point
 * @list: agurment one
 *
 * Description - longer description
 * Return: on success
 */

int check_cycle(listint_t *list)
{
	listin_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fastt->next->next;
	}
	return (0);
}
