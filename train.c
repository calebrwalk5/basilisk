#include <stdio.h>
#include <stdlib.h>

int main() {
	char training_data[69];
	printf("Training data file: ");
	fscanf("%s", training_data);
	system("python3 src/encode.py training/*.txt training/output.npz");
	system("python3 src/train.py --dataset training/output.npz");
	return 0;
}
