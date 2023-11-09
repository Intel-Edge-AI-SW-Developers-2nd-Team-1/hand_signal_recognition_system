### README : PWM
-------------------------------------------------------------------------------------
- STM32 에서의 PWM 제어
- PWM이란?

![Alt text](<스크린샷 2023-11-08 065324.png>)
```
PWM은 Pulse Width Modulation의 약자로 일정한 주기 내에 Duty 비를 변경하여 평균 전압을 제어하는 방법입니다. 이러한 방법을 이용해서 상기 프로젝트에 사용할 Servo Motor의 속도,각을 제어할 수 있습니다.

Duty Cycle : Pluse 파형의 HIGH 상태와 LOW 상태 파형의 비율을 Duty Cycle이라고 한다.

Duty 비를 제어하기 위해서는 Caputure Compare Register(CCR)를 이용해야합니다. Timer를 통해 ARR의 값이 초기화 되는 부분을 확인 후 CCR를 0 ~ ARR 값 범위안에 입력하여서 Duty 비를 제어할 수있습니다. 
```


### Timer Calculation
```
PWM Frequency= ((Internal Clock)/(Prescaler + 1)) / (ARR)

Duty Cycle = (Pulse)/(ARR)*(PWM Period)

```
- STM32 Cube IDE 설정 내에서 Timer의 Setting 에서 PWM Generation 을 설정해줘서 프로젝트에서 필요한 PWM Frequency , Duty Cycle 을 계산한다. 




### 출처
- https://velog.io/@audgus47/Timer-General-Purpose-PWM
- https://m.blog.naver.com/alsrb968/220728192740
- https://m.blog.naver.com/compass1111/221163124212
