#include <stdio.h>
#include <string.h>

char main ()
{
    char buf[] ="dbc/qwe/ccd";
    int i = 0;
    char* p = strtok (buf, "/");
    char val[10];
    char* array[3];
    while (p != NULL)
    {
        array[i++] = p;
        p = strtok (NULL, "/");
    }

    for (i = 0; i < 3; ++i) 
        printf("%s\n", array[i]);
    for (i = 0; i < 3; ++i) {
        val[i] = *array[i];
    }
    for (i = 0; i < 3; ++i) 
        printf("%s\n", val[i]);
    return **array;
}