#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("data_ab.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double a = 0.25;
    double b = 0.5;

    for (int n = 0; n < 5; ++n) {
        double x_n = 1;  // Initialize x_n to 1 (since anything to the power of 0 is 1)

        // Calculate a^n + b^n without using pow
        for (int i = 0; i < n; ++i) {
            x_n *= a;
        }
        x_n += 1;  // b^n is 1 for any value of n

        fprintf(fp, "%.4f\n", x_n);
    }

    fclose(fp);

    return 0;
}

