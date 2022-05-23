#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int count_min(char string[]){
    int char_to_int = 0 , counter = 0;
    for (int i = 0; i < MAX; ++i) {
        char_to_int = (int) string[i];
        if (char_to_int >= 97 && char_to_int <= 122)
            counter++;
        else if (char_to_int == 0)
            break;
    }
    return counter;
}

int main() {
    char input[MAX];
    int min = 0;
    while (1){
        printf("Inserisci il tuo input: ");
        scanf("%[^\n]",&input);
        fflush(stdin);
        min = count_min(input);
        printf("Il numero di caratteri minuscoli e': %d\n", min);
    }

    return 0;
}
