#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular or not
 * @list: linked list to check
 * Return: 1 (linked list is circular) 0 (no loop detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *node = NULL, *temp = NULL;

	node = temp = list;
	while (list && node && temp && node->next && temp->next)
	{
		node = node->next;
		temp = temp->next->next;
		if (!temp || !node)
			return (0);
		if (temp->next == node)
			return (1); 
	}
	return (0);
}
