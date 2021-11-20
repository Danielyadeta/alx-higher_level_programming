#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly-linked list
* @head: A pointer the head of the linked list
* @number: The number to insert
*
* Return: pointer to listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
