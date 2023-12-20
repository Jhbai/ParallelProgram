#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sched.h>
#include<sys/types.h>

int main(int argc, char** argv){
	printf("Parent Process: PID=%d on CPU=%d\n", getpid(), sched_getcpu());
	int i; // 提供給fork Loop使用的變數
	int flag = 1; // 作為判斷在這個process下是否要繼續fork的變數
	pid_t pid; // 作為fork的依據
	for(i = 0; i < 10; i++){
		if(flag == 0);
		else if(flag == 1){
			pid = fork();
			if(pid == 0){
				flag = 0;
				printf("Child Process: PID=%d on CPU=%d\n", getpid(), sched_getcpu());
			}
		}
		else{
			printf("Fork Failed!!");
			exit(1); // 1表示錯誤退出，0表示正確退出
		}
	}
	return 0;
}

