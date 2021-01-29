#include <cfvMonitor.h>

cfvMonitor cfvmonitor;
int count = 6;
boolean state = true;

void setup() {
  cfvmonitor.init();
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
  delay(500);

  if (count == 14){
    count = 6;
    state = !state;
  }
}
