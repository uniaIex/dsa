#include <stdio.h>


int main() {
    int numbers[] = {7, 2, 3, 4, 5};
    int min_value = numbers[0];
    for (int i = 0; i < 5; i++) {
        if(numbers[i] < min_value) {
            min_value = numbers[i];
        }
    
    }
    printf("The minimum value is: %d\n", min_value);
    return 0;
}