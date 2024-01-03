#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert the node in the linked list sorted
 * @head: pointer to the head 
 * @number: number into the linked list
 * Return: address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *copy_head;

	copy_head = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	
	new_node->n = number;

	if (copy_head == NULL || number < copy_head->n)
	{
		new_node->next = copy_head;
		*head = new_node;
		return (new_node);
	}

	while (copy_head ->next)
	{
		if (copy_head->n <= number && number <= copy_head->next->n)
			{
				new_node->next = copy_head->next;
				copy_head->next = new_node;
				return (new_node);
			}
		copy_head = copy_head->next;
	}
	new_node->next = copy_head->next;
	copy_head->next = new_node;
	return(new_node);
}
