#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * loop - creates an infinite loop
 * Return: always 0
 */

int loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - function create zombie process
 * Return: always 0
 */

int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	loop();
	return (0);
}
