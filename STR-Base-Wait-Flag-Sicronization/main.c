#include <stdio.h>
#include <stdlib.h>
#include <process.h>


char letters[30];
int position = 0;
char flag_A = '1';
char flag_B = '0';
char flag_C = '0';

void thread_A()
{
    while(position < 27)
    {
        while(flag_A == '0');
        letters[position] = 'A';
        position++;
        flag_A = '0';
        flag_B = '1';
    }
}

void thread_B()
{
    while(position < 28)
    {
        while(flag_B == '0');
        letters[position] = 'B';
        position++;
        flag_B = '0';
        flag_C = '1';
    }
}

void thread_C()
{
    while(position < 29)
    {
        while(flag_C == '0');
        letters[position] = 'C';
        position++;
        flag_C = '0';
        flag_A = '1';
    }

    for (position = 0; position < 30; position++)
    {
        printf("%c",letters[position]);
        if(position > 0 && ((position+1) % 3) == 0)
        {
            printf("\n");
        }

    }
}


void start_thread_A()
{
    long int thread_id;
#if defined (__WIN32__)
    if((thread_id = _beginthread(thread_A,4096,NULL) == (unsigned long)-1))
#else
    if((thread_id = _beginthread(thread_A,4096,NULL) == -1))
#endif // defined
    {
        printf("THREAD A NOT SUCCESFULLY CREATED.\n");
        return;
    }
    printf("THREAD A CREATED SUCCESFULLY.\n");

}

void start_thread_B()
{
    long int thread_id;

#if defined(__WIN32__)
    if((thread_id = _beginthread(thread_B,4096,NULL) == (unsigned long)-1))
#else
    if((thread_id = _beginthread(thread_B,4096,NULL) == -1))
#endif // defined
    {
        printf("THREAD B NOT SUCCESFULLY CREATED.\n");
        return;
    }
    printf("THREAD B CREATED SUCCESFULLY.\n");
}

void start_thread_C()
{
    long int thread_id;
#if defined(__WIN32__)
    if((thread_id = _beginthread(thread_C,4096,NULL) == (unsigned long )-1))
#else
    if((thread_id = _beginthread(thread_C,4096,NULL) == -1))
#endif // defined
    {
        printf("THREAD C NOT SUCCESFULLY CREATED.\n");
        return;
    }
    printf("THREAD C CREATED SUCCESFULLY.\n");



}


int main()
{
    start_thread_A();
    start_thread_B();
    start_thread_C();

    system("PAUSE");
    return 0;
}
