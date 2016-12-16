#include <stdio.h>

int calculatesum(int max_value) {
    int the_sum = 0;
    for(int i = 3; i < max_value; i++) {
        if(i%3==0 || i%5==0) {
            the_sum += i;
        }
    }

    return the_sum;
}
int main(int argc, char const *argv[]) {
    int max_value = 1000;
    int the_sum = calculatesum(max_value);
    printf("The sum is: %d\n", the_sum); //233168
    return 0;
}
