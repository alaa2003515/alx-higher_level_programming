#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *VAR_1 = list, *VAR_2 = list;
    while (VAR_2 != NULL && VAR_2->next != NULL)
    {
        VAR_1 = VAR_1->next;
        VAR_2 = VAR_2->next->next;
if (VAR_1 == VAR_2)
            return (1);
    }

    return (0);
}
