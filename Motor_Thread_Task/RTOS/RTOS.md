### README : RTOS
-------------------------------------------------------------------------------------
- Servo motor 와 bluetooth 통신의 실시간 동기화를 위해서 Multi Thread를 사용했어야 했는데 그로 인해 RTOS를 사용했다.
- RTOS란?
```
RTOS는 실시간 system 을 위해 개발된 운영체제이다. Multi Tasking 환경에서 Task 처리시간을 일관되게 유지하기 위한 용도로 사용한다. 각각의 Task는 시분할 System 하에서 우선순위 기반 스케쥴링을 통해 우선순위가 높은 Task 먼저 작업을 처리 할수있게 함으로써 구현한다.
```

- 추가적인 설명 과 함수는 CMSIS-RTOS-V2 공식 API 문서를 확인해서 사용하면 된다.
- https://www.keil.com/pack/doc/CMSIS/RTOS2/html/group__CMSIS__RTOS.html
### 출처
- https://eteo.tistory.com/165
- https://www.keil.com/pack/doc/CMSIS/RTOS2/html/group__CMSIS__RTOS.html
