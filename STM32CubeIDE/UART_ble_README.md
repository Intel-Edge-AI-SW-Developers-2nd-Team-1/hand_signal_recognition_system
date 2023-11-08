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
![데이터 송수신 형태](/assets/images/UART.png)

가장 일반적으로 각 데이터 비트의 시간에 대해 16/64 배 빠른 클럭 신호를 이용하여 시작 비트로부터 세어 각 비트의 경계를 찾아낸다.
보드 설정에 따라 주 클럭으로부터 타이머등을 써서 설정한 속도의 클럭 신호를 만든다.
통신 양쪽에서 설정을 미리 약속하고 클럭 신호 발생부의 레지스터를 같은 속도로 설정해야 통신이 원활하게 이루어진다.
<br>
+ 시작 비트 : 통신의 시작을 의미하며 한 비트 시간 길이 만큼 유지한다. 지금부터 정해진 약속에 따라 통신을 시작한다.
+ 데이터 비트 : 5~8비트의 데이터 전송을 한다. 몇 비트를 사용할 것인지는 해당 레지스터 설정에 따라 결정된다.
+ 패리티 비트 : 오류 검증을 하기 위한 패리티 값을 생성하여 송신하고 수신쪽에 오류 판단한다. 사용안함, 짝수, 홀수 패리티 등의 세가지 옵션으로 해당 레지스터 설정에 따라 선택할 수 있다. '사용안함'을 선택하면 이 비트가 제거된다.
+ 끝 비트 : 통신 종료를 알린다. 세가지의 정해진 비트 만큼 유지해야 한다. 1, 1.5, 2비트로 해당 레지스터 설정에 따라 결정된다.

![Rx-Tx](/assets/images/UART_tx_rx.png)
<br>
위의 그림에서 보이는것처럼 UART는 주로 디바이스와 디바이스간에 혹은 디바이스와 컴퓨터간에 1:1 통신을 하기위하여 사용되며 송신라인과 수신라인이 따로 있어 동시에 송수신이 가능하다.  

이렇게 동시에 송수신이 되는것을 full-duplex(전이중) 방식이라고 한다. 대표적인 full-duplex 통신은 전화기이다. 말을 하는것과 상대방의 말을 듣는것을 동시에 할 수 있다. 

이와 대비되는 half-duplex 방식의 대표적인 통신으로는 무전기가 있다.  무전기는 평소에는 수신 상태로 있다가 말을 할 때에만 송신 버튼을 누른후에 말을 하여야 한다.  이 순간에는 수신이 불가능하다.


# Bluetooth

## 정의
    "Wouldn't it be nice if there were a way of bringing electronic gadgets together so they could share whatever signals they need without any wires at all? ... The curious name comes from Harald Bluetooth, a Danish king who united the Scandinavians in the 10th century." 
    from https://www.explainthatstuff.com/howbluetoothworks.html

블루투스는 전자 기기 간의 단거리 데이터 교환을 가능케 하는 무선 통신 기술로, 2.4 GHz 대역에서 작동하며 저전력 무선 파장을 사용하여 기기 간 연결을 수립한다. 블루투스는 무선 오디오 스트리밍, 스마트폰 및 컴퓨터 간 데이터 전송, 주변 기기를 호스트 시스템에 연결하는 것을 포함하여 다양한 응용 분야에서 널리 사용됩니다.

 ## 특징

    - 무선 연결: 블루투스는 블루투스 버전 및 클래스에 따라 일반적으로 최대 100m까지의 짧은 거리에서 무선 통신을 지원한다.

    - 저전력 소모: 블루투스는 에너지 효율적으로 설계되어 스마트폰, 헤드폰 및 IoT 기기와 같은 배터리로 작동하는 기기에 적합하다.

    - 점대점 및 점대다중: 블루투스는 일대일(점대점) 및 일대다(점대다중) 연결을 지원하여 여러 주변 기기와 동시에 통신할 수 있다.

    - 보안: 블루투스는 페어링, 암호화 및 인증과 같은 데이터 전송 중 데이터 보호를 위한 보안 기능을 통합한다.

    - 프로파일: 블루투스는 다양한 프로파일을 정의하여 다른 종류의 기기가 어떻게 통신해야 하는지를 지정합니다. 일반적인 프로파일로는 헤드셋 프로파일(HSP), 핸즈프리 프로파일(HFP) 및 A2DP(Advanced Audio Distribution Profile) 이 있다.

    - 상호 운용성: 서로 다른 제조업체의 블루투스 기기는 블루투스 규격을 준수하고 표준화되어 있기 때문에 일반적으로 서로 통신할 수 있다.

    - 블루투스 버전: 블루투스 기술은 끊임없이 발전하며 각 버전은 데이터 전송 속도, 범위 및 에너지 효율성에서 개선 사항을 제공합니다. 일반적인 버전으로는 블루투스 2.0, 3.0, 4.0, 5.0 등이 있다.

 ## STM32IDE에서의 사용

    - 블루투스 모듈: STM32 기반 프로젝트에서 UART와 함께 블루투스를 사용하려면 블루투스 통신을 지원하는 블루투스 모듈이나 마이크로컨트롤러에 통합된 모듈이 필요합니다. 일반적인 모듈로는 HC-05, HC-06 등이 있으며, 사용 중인 특정 STM32 MCU에 따라 다를 수 있다.

    - UART 설정: STM32 마이크로컨트롤러의 UART 인터페이스 중 하나를 직렬 통신용으로 설정해야 합니다. 이 과정은 보레이트, 데이터 비트, 정지 비트 및 패리티 설정을 포함한다.

    - 블루투스 설정: 블루투스 모듈을 구성하여 UART 인터페이스를 사용하여 블루투스 연결을 설정해야 합니다. 이로써 블루투스 모듈을 마스터 또는 슬레이브로 설정하고 연결 매개 변수를 정의하며 STM32의 UART 설정과 일치하도록 구성해야 할 수 있다.

    - 데이터 전송: UART 및 블루투스 모듈이 설정된 후, STM32 마이크로컨트롤러와 다른 블루투스 지원 기기 간에 데이터를 송수신할 수 있습니다. UART를 통해 전송된 데이터는 블루투스를 통해 페어링된 기기로 무선으로 전송되며 그 반대도 가능하다.

    - STM32IDE 개발: STM32IDE를 사용하여 STM32 마이크로컨트롤러 패밀리를 지원하는 펌웨어를 개발할 수 있습니다. 코드에서 UART 통신을 관리하고 데이터 전송을 처리하기 위해 블루투스 관련 기능을 통합해야 한다.

    - 블루투스 스택: STM32 프로젝트에 블루투스 통신을 용이하게 하기 위해 블루투스 스택 또는 라이브러리를 포함해야 할 수 있습니다. 이러한 스택은 블루투스 프로토콜과 프로파일을 처리하기 위한 API를 제공한다.

[![N|Solid](https://dl.cdn-anritsu.com/images/tm/solutions/bluetooth5-02/iot-applications-for-bluetooth-5.jpg)](https://nodesource.com/products/nsolid)


## Using IDE
STM32CubeIDE

## Using Parts    
BLE : HC-06
<br>
MCU : STM32F429 NUucleo-144   


## STM32CubeIDE Setting
![params](/assets/images/UART_MX_Param_settings.png)
<br>
위 사진에서 보듯이 connectivity - USART2 - Parameter settings에서 Baud Rate값을 9600 Bits/s로 변경해 주었다.

또, NVIC settings에서 global interrupt를 활성화 시켜준다

GPIO settings를 확인하여 Rx핀과 Tx핀의 위치를 확인한다.

![GPIO](/assets/images/UART_GPIO.png)
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
