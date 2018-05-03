#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
	pid_t *PID;
	int i;
	int sleep_time = 5;
	int child_return_status;
	int num_child_proc = 0;

	PID = (pid_t*) malloc(2 * sizeof(pid_t));

	for (i=0; i<2; ++i)
	{
		if ((PID[i] = fork()) < 0) 
		{
			// fail to fork
			exit(0);
		}
		else if (PID[i] == 0) 
		{
			// child process
			if (i == 0)
			{
				printf("This is child %d, my PID is %ld\n", i, (long)PID[i]);
				printf("I am going to sleep for %d secs\n", sleep_time);
				sleep(sleep_time);
				printf("Child %d has woken up, killing myself\n", i);
				exit(0);
			}
			else 
			{
				printf("This is child %d, my PID is %ld\n", i, (long)PID[i]);
				printf("bye\n");
				exit(0);
			}
		}
		else
			num_child_proc++;
	}
	printf("num_child_proc: %d\n", num_child_proc);
	for (i=0; i<num_child_proc; ++i) 
	{
		waitpid(PID[i], &child_return_status, 0);
		if (child_return_status == 0) 
			printf("PID %ld terminated correctly\n", (long) PID[i]);
		if (child_return_status == 1)
			printf("PID %ld terminated with error\n", (long) PID[i]);
	}
	printf("my PID is %ld\n", (long) PID);
	return 0;
}