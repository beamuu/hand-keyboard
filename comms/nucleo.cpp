#include <mbed.h>

DigitalOut led(D13);
DigitalIn sw(D3, PullUp);
I2CSlave slave(D4, D5);

int main() {
    char buf[10];
    printf("STM32 started...\n");
    slave.address(0xA0); 
    while (1) {
        int i = slave.receive();
        switch (i) {
            case I2CSlave::WriteAddressed:
                slave.read(buf, 3);
                printf("Read: %s\n", buf);
                break;
            case I2CSlave::ReadAddressed:
                slave.write(buf, 3);
                printf("write complete\n");
                buf[0] = 'E';
                buf[1] = 'M';
                buf[2] = 'P';
                break;
            }
    }
}