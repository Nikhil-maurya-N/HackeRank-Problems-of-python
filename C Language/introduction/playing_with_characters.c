// # You have to print the character, , in the first line. Then print
// #   in next line. In the last line print the sentence, .
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char ch;
    char s[100];
    char sen[100];
    
    scanf("%c",&ch);
    scanf("%s\n",s);
    scanf("%[^\n]%*c",sen);
    printf("%c\n%s\n%s",ch,s,sen);
    return 0;
}
