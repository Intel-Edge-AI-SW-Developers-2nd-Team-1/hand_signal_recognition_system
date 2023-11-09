### README : TIMER
-------------------------------------------------------------------------------------
- STM32 에서의 TIMER

![스크린샷 2023-11-08 023134](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/c32e3543-810b-4b16-bf6b-9fd0b2156c0e)


(출처: STM32/Products Specification)
```
위의 Table 6. Timer features comparison 을 보면 Timer type 는 크게 세가지 로 볼 수 있습니다.

ⓐ basic Timer : 16bit 형식의 타이머로서 input/output 핀 없이 순수 time base generator 동작을 수행하는 Timer 이다.

ⓑ general purpose : 16/32bit 타이머로서 아래에 언급한 모드 (Input Capture mode, Output Compare mode, PWM mode) 등의 기능을 제공하는 Timer이다.

ⓒ advanced timer : 기본적으로 general purpose 타이머의 기능은 모두 제공하며, 모터의 제어나 Digital Power Conversion 에 적합한 Complementary signal, Dead time insertion, Emergency Shut-down input 등의 기능을 제공하는 Timer이다.

Timer는 internal clock나 외부 clock에 의해서 구동될수도있습니다.
Basic Timer는 시간에 따라서 Counter가 증가하는 형식인 time base generator 입니다.
타이머의 모드의 종류는 크게 세가지 로 볼 수 있습니다.

ⓐ Input Capture 모드 : 외부 이벤트의 Frequency 를 측정하는 기능 수행합니다.

ⓑ Output Compare 모드 : 정해진 주기에 따라 Output 제어 수행합니다.

ⓒ PWM 모드 : Edge Aligened 또는 Center Aligned PWM 파형 생성 수행합니다.

```
![스크린샷 2023-11-08 024008](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/1f7dd85a-e6ef-4113-994e-9aa6340f2ffd)

(출처: user/stm32_pj_main함수_screenshot)

```
위의 사진에서 확인 할 수 있듯이 Stm32 에서 제공되는 TIM_Base_InitTypeDef 구조체는 위와 같이 정의되어있다.

1. Prescaler : 타이머로 들어오는 APB1, APB2, 클럭을 나누기 위한 Prescaler 값

2. CounterMode : 카운터가 증가 감소, 증가 후 감소 모드 등을 설정하하는 값

3. Period : 타이머의 주기를 결정하는 값 (0x0 으로 설정 시 타이머 구동 중지)

4. ClockDivision : 내부 타이머 클럭 주기와 ETRx, Tlx 핀에서 사용되는 샘플링 클럭 사이의 Division 비율

5. RepetitionCounter : Update Register 가 Set 되기 전 몇번의 Overflow/Underflow 이벤트가 있어야 하는지 설정, 즉 특정 회수를 반복해야 IRQ 가 발생하도록 설정 가능하다.

6. Auto Reload Register : ARR은 Counter와 동일한 크기를 갖는 Register 이고, Counter에서 언제 Overflow가 발생하는지 결정하는 역할을 수행합니다.


```
- Timer (ARR picture)

![스크린샷 2023-11-08 065324](https://github.com/simpleis6est/HandSignalRecognitionSystem/assets/143490860/81c8d842-ba7f-4629-ade8-2bb7fe1503ba)

- Interrupt Timer

```
먼저 이 언어들을 이해하기 위해서 Timer의 구조에 대해서 알아야합니다.
상기 프로젝트를 진행하는 과정에서 Interrupt를 발생시키는 타이머를 사용하였기 때문에 Interrupt Timer로 설명을 하겠습니다. 먼저 Timer를 제어하기 위해서는 아래의 네가지 개념이 필요합니다.

ⓐ Counter : Register(16bit), 숫자가 증가하는 Counter, 모든 Timer는 자신만의 Counter Register를 가지고 있습니다. 

ⓑ Auto Reload Register(ARR) : ARR은 Counter와 동일한 크기를 갖는 Register 이고, Counter에서 언제 Overflow가 발생하는지 결정하는 역할을 수행합니다. 만약 Counter가 Register의 한계에 도달하면 Overflow가 발생하겠지만, 이는 매번 Register의 크기만큼 즉 같은 주기로만 동작하므로 Overflow 를 조정할수없을것입니다. 즉 ARR은 구체적으로 ARR == Counter 가 된 바로 다음 클럭에 overflow를 발생시켜 0으로 돌아가게끔 하는 것입니다

ex) 0 > 1 > 2 > 3 > 0 > 1 > 2 > 3
                (overflow)

 
ⓒ Prescaler : 분주기(Prescaler) 란, 주기를 쪼개주는 뜻입니다. 분주기는 Counter에 공급되는 클럭을 더 느리게 만들어주는 장치로서 분주를 하게 되면 Timer에 공급되는 여러 클럭이 하나로 합쳐져 타이머가 더 느리게 동작을 하게됩니다. 이 때, 몇개의 분주비로 합쳐지는를 분주비라 합니다. 

즉, 분주기는 Timer와 마찬가지로 내부에 Counter를 가지고있어 이 Counter가 클럭의 Edge에 맞춰어 증가하다가 Counter가 분주비 값에 도달하면 Overflow를 발생하면서 출력을 반전시키는 장치입니다.
다만 주의할 점은 ARR의 경우와 똑같이 분주기에 입력되는 클럭이 x(Hz)라 하고 분주비가 y(1:y)라 하며 분주기의 출력클럭은 x/y가 아니라 f/(x+1) 이 된다는 점입니다. 즉 CubeIDE 에서 prescaler를 설정할 때 설정값+1 로 해야합니다.

ⓓ Preload : Preload는 ARR을 변경할 때 그 변경 시점을 결정하는 설정입니다. 만약 Preload(enable)이면 ARR의 값을 바꾼다 해도 즉시 바뀌지 않고 Preload Register라는 곳에 저장되었다가 Counter Overflow가 발생할 때 동시에 ARR값이 업데이트됩니다. Preload(disable) 이면 ARR값을 바꿀 때 ARR이 즉시 바뀌게 됩니다.

ex)
    - Timer에 공급되는 클럭이 fc (Hz)
    - ARR 값이 a
    - Prescaler 값 p
    이면 Timer Interrupt 발생 주파수 Fi 는 
    Fi = fc/((a+1)(p+1))
    로 계산할수있습니다. 
```
- 즉 일반적으로 Basic Timer는 0 -> Period 값까지 증가하게 된다. 또한 Perscaler 값에 따라서 카운팅 속도는 변할수도 있다. 타이머의 카운터가 Period 값까지 가게 되면 Overflow와 함께 Update Event flag 가 설정되고 인터럽트가 발생하게된다.
그 후에는 다시 0으로 초기화 된 후 다시 증가하게된다. 
- 이러한 Timer의 개념을 이해 후 Timer을 통한 PWM 제어를 설명하겠습니다.


### 출처

- https://blog.naver.com/eziya76/221451890046
- https://velog.io/@audgus47/Timer-General-Purpose-PWM
- https://unknownpgr.com/posts/timer/
- file:///C:/Users/IoT025/STM32Cube/Repository/DS9405.pdf 

