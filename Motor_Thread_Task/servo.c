/*
 * servo.c
 *
 * Created on: Oct 20, 2023
 * Author: SEPC
 */
#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "servo.h"
#include "cmsis_os.h"
#include "string.h" // 문자열 관련 헤더 추가

extern TIM_HandleTypeDef htim3;
extern TIM_HandleTypeDef htim4;

#define ARR_VALUE 1000
uint16_t min = ARR_VALUE * (0.7 / 4.0); // 0도
uint16_t max = ARR_VALUE * (2.3 / 4.0); // 180도
// 추가로 360도 회전과 속도의 값에 따라 바꾸는 코드

osThreadId_t Servo1_thread_handle;
osThreadId_t Servo2_thread_handle;

osMessageQueueId_t servoQueue1=NULL;
osMessageQueueId_t servoQueue2=NULL;

const osThreadAttr_t Servo1_attributes = {
    .name = "SERVO_ONE",
    .stack_size = 256 * 4,
    .priority = osPriorityNormal
};

const osThreadAttr_t Servo2_attributes = {
    .name = "SERVO_TWO",
    .stack_size = 256 * 4,
    .priority = osPriorityNormal
};

static void Servo1_thread_Task(void *arg);
static void Servo2_thread_Task(void *arg);

static void Servo1_go(void);
static void Servo1_stop(void);
static void Servo1_left(void);
static void Servo1_right(void);

static void Servo2_go(void);
static void Servo2_stop(void);
static void Servo2_left(void);
static void Servo2_right(void);

const int currentCommand1 = 0;
const int currentCommand2 = 0;

// servo1 모터 제어코드
/*motor -> 1.DC servo motor 일경우
 * motor -> 2. servo 360 속도 제어
 * motor 안와서 제어코드없이 180도 0도로 thread task작동 확인
 */
static void Servo1_go(void) {
    __HAL_TIM_SetCompare(&htim3, TIM_CHANNEL_1, max);
    HAL_Delay(1000);
    __HAL_TIM_SetCompare(&htim3, TIM_CHANNEL_1, min);
}

static void Servo1_stop(void) {
    __HAL_TIM_SetCompare(&htim3, TIM_CHANNEL_1, min);
}

static void Servo1_left(void) {
    __HAL_TIM_SetCompare(&htim3, TIM_CHANNEL_1, max);
}

static void Servo1_right(void) {
    __HAL_TIM_SetCompare(&htim3, TIM_CHANNEL_1, max);
}

// servo2 모터 제어코드
static void Servo2_go(void) {
    __HAL_TIM_SetCompare(&htim4, TIM_CHANNEL_4, max);
    HAL_Delay(1000);
    __HAL_TIM_SetCompare(&htim4, TIM_CHANNEL_4, min);
}

static void Servo2_stop(void) {
    __HAL_TIM_SetCompare(&htim4, TIM_CHANNEL_4, min);
}

static void Servo2_left(void) {
    __HAL_TIM_SetCompare(&htim4, TIM_CHANNEL_4, min);
}

static void Servo2_right(void) {
    __HAL_TIM_SetCompare(&htim4, TIM_CHANNEL_4, max);
}

void servo_init(void) {
    printf("servo_motor_Initialized...\r\n");
    HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1); // pwm servo channel 3
    printf("Tim3_PWM_Start...\r\n");
    HAL_TIM_PWM_Start(&htim4, TIM_CHANNEL_4); // pwm servo channel 4
    printf("Tim4_PWM_Start...\r\n");

    Servo1_thread_handle = osThreadNew(Servo1_thread_Task, NULL, &Servo1_attributes);
    Servo2_thread_handle = osThreadNew(Servo2_thread_Task, NULL, &Servo2_attributes);

    servoQueue1 = osMessageQueueNew(10, sizeof(int), NULL);
    if (servoQueue1 != NULL) {
        printf("servoQueue1 created successfully\r\n");
    } else {
        printf("Failed to create servoQueue1\r\n");
    }
    servoQueue2 = osMessageQueueNew(10, sizeof(int), NULL);
    if (servoQueue1 != NULL) {
        printf("servoQueue2 created successfully\r\n");
    } else {
        printf("Failed to create servoQueue1\r\n");
    }
}

static void Servo1_thread_Task(void *arg) {
    for (;;) {
        int currentCommand1;
        // 명령 큐에서 명령을 가져와서 현재 명령으로 설정
        osMessageQueueGet(servoQueue1,&currentCommand1, NULL, 200);
       // printf("currentCommand1:%d\r\n",currentCommand1);
        // 현재 몤령에 따라 서보 동작 수행
        if (currentCommand1 != 0) {
            if (currentCommand1 == 1) {
               // printf("servo1_go\r\n");
                Servo1_go();
            } else if (currentCommand1 == 2) {
               // printf("servo1_stop\r\n");
                Servo1_stop();
            } else if (currentCommand1 == 3) {
                //printf("servo1_left\r\n");
                Servo1_left();
            } else if (currentCommand1 == 4) {
                //printf("servo1_right\r\n");
                Servo1_right();
            }
        }

       printf("servo1_thread_start...\r\n");
        //osDelay(200);
    }
}

static void Servo2_thread_Task(void *arg) {
    for (;;) {
        int currentCommand2;

        // 명령 큐에서 명령을 가져와서 현재 명령으로 설정
        osMessageQueueGet(servoQueue2, &currentCommand2, NULL, 250);
        //printf("currentCommand2:%d\r\n",currentCommand2);
        // 현재 몤령에 따라 서보 동작 수행
        if (currentCommand2 != 0) {
            if (currentCommand2 == 1) {
                //printf("servo2_go\r\n");
                Servo2_go();
            } else if (currentCommand2 == 2) {
                //printf("servo2_stop\r\n");
                Servo2_stop();
            } else if (currentCommand2 == 3) {
               // printf("servo2_left\r\n");
                Servo2_left();
            } else if (currentCommand2 == 4) {
                //printf("servo2_right\r\n");
                Servo2_right();
            }
        }

        printf("servo2_thread_start...\r\n");
    }
}

void SendServoCommand(int command) {
    // 서보1 스레드에 명령을 전달
	//printf("command:%d\r\n",command);
    osMessageQueuePut(servoQueue1, &command, 0, 0);
    //printf("succesful\r\n");
    // 서보2 스레드에 명령을 전달
    osMessageQueuePut(servoQueue2, &command, 0, 0);
    //printf("succesful\r\n");

}
