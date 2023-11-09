### Title : README Motor_Controller_Reference
------------------------------------------------------------------------------------
### 1. Timer
```
TIMER.md
```
- Timer의 개념 및 PWM Servo Motor를 제어하기 위해 필요한 Reference 가 있습니다.

### 2. PWM
```
PWM.md
```
- PWM 의 개념 및 PWM Servo Motor를 제어하기 위해 필요한 Reference가 있습니다.

### 3. RTOS
```
RTOS.md
```
- Servo Motor 두개와 Bluetooth를 동시간 통신 및 동기화를 위해 사용한 Multi Therding 을 사용하기 휘해 필요한 Reference 가 있습니다.

### SG90 Data Sheet(360 Degree)



### Cube MX Setting for Motor_controller
- RTOS 및 Timer setting

![스크린샷 2023-11-08 003054](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/aa466d49-7c99-45e1-9856-d10c309aab71)


![스크린샷 2023-11-09 090931](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/8d0259a8-0e37-4006-ab41-aac210b2caab)

![스크린샷 2023-11-09 085950](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/4b9fbd48-768a-4eeb-878c-ec0ff073a59d)


설명

### Working flowchart

![스크린샷 2023-11-08 012720](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/edfb59f4-9069-4fa0-a151-00079da11235)

### To Do List
1. Calibration
    - Servo Motor의 전격전압의 차이로 인해 발생하는 Calibration을 정확하게 Sensor 로 잡아내는 작업이 추가적으로 필요할것으로 보인다.
    - 정확한 각 제어를 위해 Servo Motor보다 Stepper Dc Motor를 이용해서 두 모터의 동기화에 도움을 주는 작업이 추가적으로 필요할것으로 보인다.
