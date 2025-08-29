// spam_display.c
// Basic C program to read output from Python ML model

#include <stdio.h>

int main() {
    FILE *file;
    char line[256];

    file = fopen("spam_output.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open output file.\n");
        printf("Run `spam_classifier.py` first to generate spam_output.txt\n");
        return 1;
    }

    printf("=== Spam Email Classification Result ===\n");

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
    return 0;
}
