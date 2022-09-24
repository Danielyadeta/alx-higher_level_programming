#include "lists.h"
/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int s = 0, i = 0;
	int arr[2048];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (*head != NULL)
	{
		arr[s] = (*head)->n;
		*head = (*head)->next;
		s++;
	}

	while (s >= i)
	{
		if (arr[i] != arr[s - 1])
			return (0);
		s--;
		i++;
	}
	return (1);
}
