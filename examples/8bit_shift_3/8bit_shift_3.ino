#include <cfvMonitor.h>

cfvMonitor cfvmonitor;
int count = 2;
boolean state = true;

void setup() {
  cfvmonitor.init();
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(count, state);
  count++;
  delay(100);

  if (count == 14){
    count = 2;
    state = !state;
  }
}
