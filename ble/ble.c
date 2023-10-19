#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "string.h"
#include "main.h"
#include "led.h"
#include "cli.h"
#include "uart.h"
#include "ble.h"

extern UART_HandleTypeDef huart2;


void ble_init(void) {
    printf("HELLO!!!\n");
}

void ble(void) {
    uart_init();
    led_init();
    cli_init();
    ble_init();
    while (1)
    {
        uart_proc();

    }
}

