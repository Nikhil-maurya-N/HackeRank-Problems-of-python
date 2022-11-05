// Write a function int max_of_four(int a, int b, int c, int d)
//  which reads four arguments and returns the greatest of them.
#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b, int c,int d){
   if(a>b)
       if(a>c)
           if (a>d)
               return a;
    if(b>a)
        if(b>c)
            if (b>d)
                return b;
            
    if(c>a)
        if(b<c)
            if (c>d)
                return c;
            
    if(d>a)
        if(d>c)
            if (b<d)
                return d;
            
            
            
        
    
}
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}