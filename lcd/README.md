# I2C Communication
SDA, SCL 2 serial communication
```
Simple hardware
Multi master
Synchronous communication
Dynamic address designation
Low power consumption
```
Uses
```
Sensor(Temperature, acceleration, gyroscope, humidity)
Communication with EEPROM (data read and save)
Display control (OLED, LCD)
Audio device (codec, amplifier, related device communication)
```
How to use
```
SCL(Serial Clock)
    Synchronization of communication
    master->slave transmission for clock signal
SDA(Serial Data)
    SCL clock signal customization
    Master and slave data transmission and reception
EX
    1) When both the SCL and SDA pins are in the high state, the master changes SDA to low to notify the slave of the start of communication.
    2) The master transmits the address of the slave it wishes to communicate with through SDA.
    3) The master communicates with the slave of the address.
    4) With SCL high and SDA low, the master changes SDA to high to notify the slave of the end of communication.

```
Reference
```
Korean
    https://mickael-k.tistory.com/184
    https://blog.naver.com/yuyyulee/220323559541
    https://www.seminet.co.kr/channel_micro.html?menu=content_sub&com_no=702&category=article&no=2109
    https://www.hellmaker.kr/post/303
    https://velog.io/@d3fau1t/I2C-%ED%86%B5%EC%8B%A0-%EC%9D%B4%ED%95%B4-with-MCP23008
    https://ohj-1129.tistory.com/37
    https://cis.cju.ac.kr/wp-content/lecture-materials/computer-networks/I2C%20%ED%86%B5%EC%8B%A0%20%EC%A0%9C%EC%96%B4.pdf
English
    https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/
    https://www.ti.com/lit/an/slva704/slva704.pdf?ts=1699409258760&ref_url=https%253A%252F%252Fwww.google.com%252F
    https://www.analog.com/en/technical-articles/i2c-primer-what-is-i2c-part-1.html
    https://www.geeksforgeeks.org/i2c-communication-protocol/
    https://www.seeedstudio.com/blog/2022/09/02/i2c-communication-protocol-and-how-it-works/
    
```

# LCD 1602(I2C module)
Text output using I2C communication
```
Low voltage, Low power
Easy to use
No graphics or curves
```
Uses
```
Text output 16x2
Check status via text
```
How to use
```
void lcd_init (void); 
void lcd_disp_on(void);
void lcd_disp_off(void);
void lcd_home(void);
void lcd_clear_display(void);
void lcd_locate(uint8_t row, uint8_t column);
void lcd_printchar(unsigned char ascode);
void lcd_print_string (char *str);  // print string to the lcd
void lcd_printf(const char *fmt, ...);
```




