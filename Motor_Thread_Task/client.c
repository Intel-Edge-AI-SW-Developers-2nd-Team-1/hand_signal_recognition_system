/*
 * client.c
 *
 *  Created on: Oct 17, 2023
 *      Author: IoT025
 */
#include 					<stdio.h>
#include					<stdlib.h>
#include					<stdarg.h>
#include					<stdbool.h>
#include					<string.h>

#include 					"main.h"
#include 					"client.h"
#include 					"servo.h"

typedef struct
{
	char					*cmd;
	uint8_t					  no;
	int						(*cbf)(int, char **);
	char					*remark;
}CMD_LIST_T;

static int cli_go(int argc,char*argv[]);
static int cli_stop(int argc,char*argv[]);
static int cli_left(int argc,char*argv[]);
static int cli_right(int argc,char*argv[]);

const CMD_LIST_T gCmdListObj[]=
{
		{"go",		1,	cli_go,		   "go"},
		{"stop",	1,	cli_stop,	 "stop"},
		{"left",	1,	cli_left,	 "left"},
		{"right",	1,	cli_right,	"right"},
		{NULL,		0,		NULL,	  NULL},
};

static int cli_go(int argc, char *argv[])
{
	if (argc < 1) printf("Need more arguments\r\n");
	printf("go\r\n");
	SendServoCommand(1);
}
static int cli_stop(int argc, char *argv[])
{
	if (argc < 1) printf("Need more arguments\r\n");
	printf("stop\r\n");
	SendServoCommand(2);
}

static int cli_left(int argc, char *argv[])
{
	if (argc < 1) printf("Need more arguments\r\n");
	printf("left\r\n");
	SendServoCommand(3);
}

static int cli_right(int argc, char *argv[])
{
	if (argc < 1) printf("Need more arguments\r\n");
	printf("right\r\n");
	SendServoCommand(4);
}


#define D_DELIMITER	" ,\r\n"

bool cli_parser(uint8_t *buf)
{
#if 1
  int argc = 0;
  char *argv[10];
  char *ptr;

  ptr = strtok((char *)buf, D_DELIMITER);
  if (ptr == NULL) return false;

  while(ptr != NULL) {
    //printf("%s\r\n", ptr);
    argv[argc] = ptr;
    argc++;
    ptr = strtok(NULL, D_DELIMITER);
  }

  for (int i=0; gCmdListObj[i].cmd != NULL; i++) {
    if (strcmp(gCmdListObj[i].cmd, argv[0]) == 0) {
      gCmdListObj[i].cbf(argc, argv);
      return true;
    }
  }

  printf("Unsupported command..\r\n");


#else
  char *ptr = strtok(buf, " ");    //첫번째 strtok 사용.
  while (ptr != NULL)              //ptr이 NULL일때까지 (= strtok 함수가 NULL을 반환할때까지)
  {
      printf("%s\n", ptr);         //자른 문자 출력
      ptr = strtok(NULL, " ");     //자른 문자 다음부터 구분자 또 찾기
  }

  uart_regcbf(cli_parser);
#endif
  return true;
}

void client_init(void)
{
	uart_regcbf(cli_parser);
}
