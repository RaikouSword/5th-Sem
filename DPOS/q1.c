#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
	pid_t c1=fork();
	if(c1==0){
		fprintf(stderr, "Child, id=%d", getpid());
		while(1);
	}else{
		fprintf(stderr, "Parent, id=%d", getpid());
		wait(NULL);
		while(1);
	}
	return 0;
}
