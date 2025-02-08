#include <stdio.h>
#include <stdlib.h>

int* recount(int *arr) {  
    char *ps = s;
    int arr[10] = {0};

    while (*ps != '\0'){
        int n = *ps - 0;
        arr[n]++;
    }    
    
    return arr;
}


char* findValidPair(char* s) {  
    int arr[10] = {0};
    
    char *ps = s;
    char *pss = s;
   
    ps++;
    
    while (*ps != '\0'){
        printf("%c \n",*ps);

        if (*ps != *pss){
            printf("good %c %c \n", *ps, *pss);
        }
        pss++;
        ps++; 
    }
    
    char *str = "hola";
    return str;
}

int main(int argc, char *argv[]) {
	printf("try: %s\n", argv[1]);
    
    char *s = findValidPair(argv[1]);

    printf("result: %s", s);
    return 1;

}
