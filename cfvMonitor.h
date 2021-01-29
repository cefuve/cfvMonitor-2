/*
	cfvMonitor.h - Library for show the state of 
  Arduino's ports on desktop application [cfvMonitor.exe].

	Link - https://github.com/cefuve

	Created by César Fuenzalida Vergara, Sep, 2019.
*/

#ifndef cfvMonitor_h
#define cfvMonitor_h

#include "Arduino.h"

class cfvMonitor
{
  public:
    cfvMonitor();
    void init();
    void print(char* msg);
    void print(int number);
    void println(char* msg);
    void println(int number);
  private:
    
};

#endif