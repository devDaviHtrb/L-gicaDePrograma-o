#include <stdio.h>

void main()
{
    int n;
    n = 0;
    while (n <= 38)
    {
        printf("%d", n);
        n += 2;
    };
    n = 0;
    do
    {
        printf("%d", n);
        n += 2;
    } while (n <= 38);
    
}
