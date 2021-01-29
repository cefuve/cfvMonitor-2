/*
	cfvMonitor.h - Library for show the state of 
    Arduino's ports on desktop application [cfvMonitor.exe].

	Repository Link - https://github.com/cefuve
    Web Link - https://www.cefuve.com

	Created by César Fuenzalida Vergara, Ene, 2021.
*/

#include "cfvMonitor.h"
#include "HardwareSerial.h"

int timer1_counter;
int pin_status;
int pin_direction;

cfvMonitor::cfvMonitor()
{
}

void cfvMonitor::init()
{
    Serial.begin(115200);

    noInterrupts();
    TCCR1A = 0;
    TCCR1B = 0;

       //timer1_counter = 64911;   // preload timer 65536-16MHz/256/100Hz
    timer1_counter = 64286;   // preload timer 65536-16MHz/256/50Hz
       //timer1_counter = 34286;   // preload timer 65536-16MHz/256/2Hz
    
    TCNT1 = timer1_counter;   // preload timer
    TCCR1B |= (1 << CS12);    // 256 prescaler 
    TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
    interrupts();             // enable all interrupts
}

void cfvMonitor::print(char* msg)
{
    Serial.print("~");
    Serial.println(msg);
}

void cfvMonitor::print(int number)
{
    Serial.print("~");
    Serial.println(number, DEC);
}

void cfvMonitor::println(char* msg)
{
    Serial.print("~ln");
    Serial.println(msg);
}

void cfvMonitor::println(int number)
{
    Serial.print("~ln");
    Serial.println(number, DEC);
}

ISR(TIMER1_OVF_vect)
{
    //B (digital pin 8 to 13)
    //C (analog input pins)
    //D (digital pins 0 to 7)

    TCNT1 = timer1_counter;

    pin_status = PORTD;
    pin_status += PORTB << 8;

    pin_direction = DDRD;
    pin_direction += DDRB << 8;
    
    /*
    pin_status += pow(2,0) * bitRead(PORTD, 0);
    pin_status += pow(2,1) * bitRead(PORTD, 1);
    pin_status += pow(2,2) * bitRead(PORTD, 2);
    pin_status += pow(2,3) * bitRead(PORTD, 3);
    pin_status += pow(2,4) * bitRead(PORTD, 4);
    pin_status += pow(2,5) * bitRead(PORTD, 5);
    pin_status += pow(2,6) * bitRead(PORTD, 6);
    pin_status += pow(2,7) * bitRead(PORTD, 7);

    pin_status += pow(2,8) * bitRead(PORTB, 0);
    pin_status += pow(2,9) * bitRead(PORTB, 1);
    pin_status += pow(2,10) * bitRead(PORTB, 2);
    pin_status += pow(2,11) * bitRead(PORTB, 3);
    pin_status += pow(2,12) * bitRead(PORTB, 4);
    pin_status += pow(2,13) * bitRead(PORTB, 5);
    */

    int i = 0;
    Serial.print("P");
    while (i <= 13)
    {
        Serial.print( bitRead(pin_status, i) );
        ++i;
    }
    Serial.println();

    int x = 0;
    Serial.print("D");
    while (x <= 13)
    {
        Serial.print( bitRead(pin_direction, x) );
        ++x;
    }
    Serial.println();
}
