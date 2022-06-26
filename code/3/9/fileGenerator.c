#include <stdio.h>

int main()
{
    FILE * MKTFILE = fopen("./aFileToSort.MKTI","wb");
    for(int i = 0; i < 256; i++)
        fwrite(&i,1,1,MKTFILE);
    fclose(MKTFILE);
    return 0;
}