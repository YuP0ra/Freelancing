#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>


const int MAX = 5 , MAXW = 100;

FILE *fp ;
int read_line(char line[] , char *commands[])
{
    int sz = 0;
    line = (char*) malloc(MAX);
    do
    {
        line[sz] = fgetc(fp);
        if (line[sz] == '\n')
            break;
        if (feof(fp))
        {
            exit(0);
        }
        sz++;
        if (sz >= MAX)
        {
            line = (char *)realloc(line, sz + 2);
        }
    } while (1);


    // remove endline
    int i = 0 , sz = strlen(line);
    for( i =0;i<sz;i++)
    {
        if(line[i] == '\n')
        {
            line[i] = '\0';
            return ;
        }
    }

     i =0;
     sz = 1;

     commands[i] = strtok(line , " \t\r\n\a");


     if(commands[i] == NULL)
         return ;
     while(commands[i] != NULL )
     {
         i++;

         commands[i] = strtok(NULL, " \t\r\n\a");

     }

     return 1 ;
}

int excute(char *commands[])
{
    if(commands[0] == NULL)
        return 1;

    if(strcmp( commands[0],  "exit") == 0)
        exit(0);

    pid_t pid = fork();

    if (!pid)
    {
      if (execvp(commands[0], commands) == -1)
      {
        perror("shell");
      }
      exit(0);
    }
    else if (pid < 0)
    {
      perror("shell");
    }
    else
    {
      wait(NULL);
    }

    return 1;
}

void shell_loop(int argc,const char *argv[])
{
    if(argc == 1)
    {
        puts("No file given");
        exit(1);
    }

    char *line ;
    char*commands[MAXW];
    int status = 1, ok;
    fp=fopen(argv[1], "r");
    if (fp == NULL)
    {
        puts("File Not Found");
        exit(1);
    }
    do {
        memset(commands, 0, sizeof(commands));
    ok  =read_line(line , commands);
    if(ok)
        status = excute( commands);


    } while (status);

}
int main(int argc , const char **argv)
{
    shell_loop(argc,argv);
    return 0;
}
