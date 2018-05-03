#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int word_count  (char const *string, char const *delim, char const *sdelim);
int word_count_r(char const *string, char const *delim, char const *sdelim);

int main(int argc, char ** argv) {
    char *original_string;
    char *delim = strdup(".");
    char *sdelim = strdup(" ");
    FILE *fp;
    size_t file_size;

    fp = fopen("input.txt", "r");
    if (fp) {
        fseek(fp, 0, SEEK_END);
        file_size = ftell(fp);
        fseek(fp, 0, SEEK_SET);

        original_string = (char *)malloc(file_size + 1);
        fread(original_string, file_size, 1, fp);
        printf("%d words from strtok_r\n\n", word_count_r(original_string, delim, sdelim));
        printf("%d words from strtok\n", word_count(original_string, delim, sdelim));

    }

    fclose(fp);
}

int word_count_r(const char *string, char const * delim, char const *sdelim) {
    char *original_sentence, *sentence, *words, *brko, *brks;
    int sentence_count = 0, sentence_word_count = 0, total_word_count = 0;
    original_sentence = strdup(string);
    for (sentence = strtok_r(original_sentence, delim, &brko); sentence; sentence = strtok_r(NULL, delim, &brko)) {
        // printf("%s\n", sentence);
        sentence_word_count = 0;
        for (words = strtok_r(sentence, sdelim, &brks); words; words = strtok_r(NULL, sdelim, &brks)) {
            ++sentence_word_count;
            ++total_word_count;
            // printf("\t%d %s\n", sentence_word_count, words);
        }
        printf("sentence %d has %2d words\n", sentence_count, sentence_word_count);
        ++sentence_count;
    }
    printf("\n");
    printf("There are %d sentences, with %d word(s) in total\n", sentence_count, total_word_count);

    return total_word_count;
}

int word_count  (char const *string, char const *delim, char const *sdelim) {
    char *sentence, *words;
    int sentence_count = 0, sentence_word_count = 0, total_word_count = 0;
    char *original_string = strdup(string);

    sentence = strchr(original_string, *delim);

    while (sentence != NULL) {
        *sentence++ = '\0';
        sentence_word_count = 0;
        // printf("sentence: %s\n", original_string);
        for (words = strtok(original_string, sdelim); words; words = strtok(NULL, sdelim)) {
            ++total_word_count;
            ++sentence_word_count;
            // printf("\t%s\n", words);
        }
        original_string = sentence;
        sentence = strchr(original_string, *delim);
        printf("sentence %d has %2d words\n", sentence_count, sentence_word_count);
        ++sentence_count;
    }

    printf("\n");
    printf("There are %d sentences, with %d word(s) in total\n", sentence_count, total_word_count);

    return total_word_count;
}
