#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char **argv)
{
    pid_t child_pid;
    char inbuffer[200];

    for ( ; ; ) {
        gets(inbuffer);
        if (fork() == 0) {
            // fork success
            char * arg[3];
            arg[0] = "blah";
            arg[1] = "-la";
            arg[2] = NULL;
            // child process
            printf("This is the child process %d\n", getpid());
            execvp(arg[0], arg);
            // printf("done\n");
        }
        wait(NULL);
        printf("-----My process id is %d\n", getpid());
        printf("-----This is the parent process\n");
    }
}
