#include "lists.h"

/**
* check_cycle - checks if a singly linked list has cycle
* @list: linked list to be checked
*
* Return: 1 if there is cycle, otherwise 0
*/
int check_cycle(listint_t *list)
{
	int found;
	listint_t *head;
	
	found = 0;
	head = list;
	while (list)
	{
		list = list->next;
		if (head == list)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
