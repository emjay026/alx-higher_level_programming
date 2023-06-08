
#include "lists.h"

/**
 * check_cycle - checks if a cycle exists within a linked list.
 * @list:
 *
 * Return: 1 if cycle exists, 0 otherwise.
*/
int check_cycle(listint_t *list)
{
    listint_t *head = list;
    listint_t *curr = NULL;
    listint_t *prev = NULL;
    int result;

    if (head == NULL)
        return (0);

    if (head->next == NULL)
        return (0);

    if (head->next->next == NULL)
        return (0);

    if (head->next == head)
        return (1);

    if (head->next->next == head || head->next->next == head->next)
        return (1);

    prev = head->next;
    curr = head->next->next;

    while (curr->next != head && curr->next != prev && curr->next != NULL)
    {
        result = check_align(head, prev, curr->next);
        if (result == 1)
            break;
        prev = curr;
        curr = curr->next;
    }

    if (curr->next == NULL)
        return (0);

    if (curr->next == head || curr->next == prev)
        return (1);

    return (result);
}

/**
 * check_align - traverse from head.
 * @head: pointer to head node.
 * @prev: pointer to prev node.
 * @next: pointer to next node.
 *
 * Return: 0 for aligned or 1 for not aligned.
*/
int check_align(listint_t *head, listint_t *prev, listint_t *next)
{
    listint_t *temp = head;

    while (temp != prev && temp != next && temp != NULL)
        temp = temp->next;

    if (temp == NULL)
        return (0);

    if (temp == prev)
        return (0);

    if (temp == next)
        return (1);
}
