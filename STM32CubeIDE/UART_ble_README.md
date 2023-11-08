## Author
박재병
<br>
한정재

## What is UART?
UART (Universal asynchronous receiver/transmitter : 범용 비동기화 송수신기)는 병렬 데이터의 형태를 직렬 방식으로 전환하여 데이터를 전송하는 직렬 통신 인터페이스다.
RxD는 수신된 직렬 데이터 신호이고 TxD는 전송된 데이터 신호이다.

UART는 일반적으로 EIA RS-232, RS-422, RS-485와 같은 통신 표준과 함께 사용한다.

비동기 통신이므로 동기 신호가 전달되지 않는다. 따라서 수신 쪽에서 동기신호를 찾아내어 데이터의 시작과 끝을 시간적으로 알아 처리할 수 있도록 약속되어 있다.

## 데이터 송수신 형태
![데이터 송수신 형태]("/assets/images/UART.png")

가장 일반적으로 각 데이터 비트의 시간에 대해 16/64 배 빠른 클럭 신호를 이용하여 시작 비트로부터 세어 각 비트의 경계를 찾아낸다.
보드 설정에 따라 주 클럭으로부터 타이머등을 써서 설정한 속도의 클럭 신호를 만든다.
통신 양쪽에서 설정을 미리 약속하고 클럭 신호 발생부의 레지스터를 같은 속도로 설정해야 통신이 원활하게 이루어진다.
<br>
+ 시작 비트 : 통신의 시작을 의미하며 한 비트 시간 길이 만큼 유지한다. 지금부터 정해진 약속에 따라 통신을 시작한다.
+ 데이터 비트 : 5~8비트의 데이터 전송을 한다. 몇 비트를 사용할 것인지는 해당 레지스터 설정에 따라 결정된다.
+ 패리티 비트 : 오류 검증을 하기 위한 패리티 값을 생성하여 송신하고 수신쪽에 오류 판단한다. 사용안함, 짝수, 홀수 패리티 등의 세가지 옵션으로 해당 레지스터 설정에 따라 선택할 수 있다. '사용안함'을 선택하면 이 비트가 제거된다.
+ 끝 비트 : 통신 종료를 알린다. 세가지의 정해진 비트 만큼 유지해야 한다. 1, 1.5, 2비트로 해당 레지스터 설정에 따라 결정된다.

![Rx-Tx]("/assets/images/UART_tx_rx.png")
<br>
위의 그림에서 보이는것처럼 UART는 주로 디바이스와 디바이스간에 혹은 디바이스와 컴퓨터간에 1:1 통신을 하기위하여 사용되며 송신라인과 수신라인이 따로 있어 동시에 송수신이 가능하다.  

이렇게 동시에 송수신이 되는것을 full-duplex(전이중) 방식이라고 한다. 대표적인 full-duplex 통신은 전화기이다. 말을 하는것과 상대방의 말을 듣는것을 동시에 할 수 있다. 

이와 대비되는 half-duplex 방식의 대표적인 통신으로는 무전기가 있다.  무전기는 평소에는 수신 상태로 있다가 말을 할 때에만 송신 버튼을 누른후에 말을 하여야 한다.  이 순간에는 수신이 불가능하다.

## Using IDE
STM32CubeIDE

## Using Parts    
BLE : HC-06
<br>
MCU : STM32F429 NUucleo-144   


## STM32CubeIDE Setting
1. UART Setting
<br>
![params]("/assets/images/UART_MX_Param_settings.png)
<br>
> 위 사진에서 보듯이 connectivity - USART2 - Parameter settings에서 Baud Rate값을 9600 Bits/s로 변경해 주었다.

또, NVIC settings에서 global interrupt를 활성화 시켜준다

GPIO settings를 확인하여 Rx핀과 Tx핀의 위치를 확인한다.
<br>
![GPIO]("/assets/images/UART_GPIO")
<br>
우리는 Rx핀이 PA3이고 Tx핀이 PD5이다. 

추후에 블루투스 모듈의 Rx와 Tx를 연결하고 블루투스 모듈의 Tx와 Rx를 연결해주면 하드웨어 설정은 끝이난다.

## Code
PC와 stm32보드간의 통신을 위해서 UART통신을 사용하였고, 블루투스 모듈로 연결하기로 하였다.

UART통신을 위한 코드는 첨부 된 링크를 확인하면 된다.
[UART Link][UART-CODE]

[UART-CODE]: https://github.com/Intel-Edge-AI-SW-Developers-2nd-Team-1/HandSignalRecognitionSystem/tree/main/ble

PC에서 stm32으로 명령어를 보내는 코드는 파이썬으로 작성하였다. led를 키는 간단한 예제 코드를 첨부하겠다.
```python
#pip install pybluez
import bluetooth
import time

def bluetoothsetup():
    serverMACAddress = 'your MAC adress' #목표 블루투스 맥주소
    port = 1    #포트는 1번으로 사용하는 것이 일반적
    socekt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socekt.connect((serverMACAddress, port))
    return socekt

#사용 예시
socket = bluetoothsetup()
while(1):
    socket.send("led 1 on\r\n")
    time.sleep(1)
    socket.send("led 1 off\r\n")
    time.sleep(1)
    
socket.close()
```
