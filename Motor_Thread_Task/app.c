/*
 * app.c
 *
 *  Created on: Oct 20, 2023
 *      Author: SEPC
 */
#include <stdio.h>
#include <stdbool.h>
#include "main.h"
#include "cmsis_os.h"
#include "app.h"
#include "servo.h"
#include "uart.h"
#include "client.h"

typedef struct {
	uint32_t counter,period;
	void (*cbf)(void*);
	bool flag;
}PROC_T;

osThreadId_t uartThreadHandle;
const osThreadAttr_t uart_attributes = {
    .name = "UART_THREAD",
    .stack_size = 256 * 4,
    .priority = osPriorityNormal
};
static void Uart_Task(void*arg)
{
	for(;;)
	{
		uart_proc();
		///printf("uart_thread_start...\r\n");
		osDelay(200);
	}
}

// 함수 선언부
void app_init(void);


// 메인 함수 실행부
void app() {
	osKernelInitialize(); // 스케줄러를 초기화하는 함수
    app_init();
    uart_init();  // UART 초기화
    uartThreadHandle = osThreadNew(Uart_Task, NULL, &uart_attributes);
    client_init();
    servo_init(); // 서보 모터 초기화
    osKernelStart();



    while (1)
    {
    }
}

void app_init(void)
{
    printf("app_Initialized...\r\n");
}
