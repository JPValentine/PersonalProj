#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main(){


	while(fork()>0);
	printf("yut\n");
	return 0;
}
