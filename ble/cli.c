#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <string.h>

#include "main.h"
#include "uart.h"
#include "cli.h"

typedef struct
{
    char* cmd;
    uint8_t no;
    int (*cbf)(int, char**);
    char* remark;
}CMD_LIST_T;

static int cli_led(int argc, char* argv[]);

const CMD_LIST_T gCmdListObj[] =
{
  {"led", 3, cli_led, "led [2/3] [on/off]"},
  {NULL, 0, NULL, NULL}
};

static int cli_led(int argc, char* argv[])
{
    if (argc != 3) printf("Need more arguments\r\n");

    long led_no = strtol(argv[1], NULL, 10);

    int onoff = strcmp(argv[2], "off");

    if (onoff != 0) onoff = 1;

    printf("led %d %s\r\n", led_no, argv[2]);
    led_onoff(led_no, onoff);

    return 0;
}


#define D_DELIMITER  " ,\r\n"

bool cli_parser(uint8_t* buf)
{
#if 1
    int argc = 0;
    char* argv[10];
    char* ptr;

    ptr = strtok(buf, D_DELIMITER);
    if (ptr == NULL) return false;

    while (ptr != NULL)
    {
        //printf("%s\n", ptr);
        argv[argc] = ptr;
        argc++;
        ptr = strtok(NULL, D_DELIMITER);
    }

    for (int i = 0; gCmdListObj[i].cmd != NULL; i++)
    {
        if (strcmp(gCmdListObj[i].cmd, argv[0]) == 0)
        {
            gCmdListObj[i].cbf(argc, argv);
            return true;
        }
    }

    printf("Unsupported command...\r\n");


#else
    char* ptr = strtok(buf, " ");    //ù��° strtok ���.
    while (ptr != NULL)              //ptr�� NULL�϶����� (= strtok �Լ��� NULL�� ��ȯ�Ҷ�����)
    {
        printf("%s\n", ptr);         //�ڸ� ���� ���
        ptr = strtok(NULL, " ");     //�ڸ� ���� �������� ������ �� ã��
    }

    uart_regcbf(cli_parser2222);
#endif


    return true;
}

void cli_init(void)
{
    uart_regcbf(cli_parser);
}


