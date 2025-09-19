#include <stdio.h>

int main(){
    printf("Enter an alphabet: ");
    char ch;
    scanf("%c",&ch);
    if(ch=='a'|| ch=='e'||ch=='i'||ch=='o'||ch=='u'){
        printf("Alphbet is vowel");
    }else{
        printf("Alphabet is a consonant");
    }

    return 0;
}