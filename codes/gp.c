#include <stdio.h>

int main() {
    FILE *file = fopen("sequence_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    int n;
    double x_n = 0.25;

    for (n = 0; n <= 10; n++) {
        fprintf(file, "%d %lf\n", n, x_n);
        x_n *= 2.0; // Equivalent to pow(2, n)
    }

    fclose(file);

    return 0;
}

