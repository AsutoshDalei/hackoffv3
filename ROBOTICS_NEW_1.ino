#include <Servo.h>

Servo servo_test;

int angle = 0;

//int flr_num;
int UDmotorpin1 = 2;
int UDmotorpin2 = 3;
int UDen = 10;

int LRmotorpin1 = 4;
int LRmotorpin2 = 5;
int LRen = 11;
const int t = 200;
void setup()
{
  servo_test.attach(9);
  pinMode(UDmotorpin1, OUTPUT);
  pinMode(UDmotorpin2, OUTPUT);
  pinMode(LRmotorpin1, OUTPUT);
  pinMode(LRmotorpin2, OUTPUT);
  Serial.begin(9600);
}
void up()
{
  Serial.println("moving up");
  digitalWrite(UDen, HIGH);
  digitalWrite(LRen, LOW);
  digitalWrite(UDmotorpin1, HIGH);
  digitalWrite(UDmotorpin2, LOW);
  delay(t);
  digitalWrite(LRmotorpin1, LOW);
  digitalWrite(LRmotorpin2, LOW);

}
void down()
{
  digitalWrite(UDen, HIGH);
  digitalWrite(LRen, LOW);
  Serial.println("going down");
  digitalWrite(UDmotorpin1, LOW);
  digitalWrite(UDmotorpin2, HIGH);
  delay(t);
  digitalWrite(LRmotorpin1, LOW);
  digitalWrite(LRmotorpin2, LOW);

}

void forward()
{
  digitalWrite(UDen, LOW);
  digitalWrite(LRen, HIGH);
  Serial.println("going fwd");
  digitalWrite(UDmotorpin1, LOW);
  digitalWrite(UDmotorpin2, LOW);
  delay(t);
  digitalWrite(LRmotorpin1, HIGH);
  digitalWrite(LRmotorpin2, LOW);

}
void back()
{
  //digitalWrite(UDen, LOW);
  //digitalWrite(LRen, HIGH);
  Serial.println("going back");
  digitalWrite(UDmotorpin1, LOW);
  digitalWrite(UDmotorpin2, LOW);
  delay(t);
  digitalWrite(LRmotorpin1, LOW);
  digitalWrite(LRmotorpin2, HIGH);

}
void stops()
{
  digitalWrite(UDmotorpin1, LOW);
  digitalWrite(UDmotorpin2, LOW);
  digitalWrite(LRmotorpin1, LOW);
  digitalWrite(LRmotorpin2, LOW);
}

void clicks()
{
  for (angle = 0; angle < 180; angle += 1)
  {
    servo_test.write(angle);
    delay(15);
  }

  delay(1000);

  for (angle = 180; angle >= 1; angle -= 5)
  {
    servo_test.write(angle);
    delay(5);
  }

  Serial.println("click button");
}

void loop() {
  // while (Serial.available()==0){}             // wait for user input
  //flr_num = Serial.parseInt();
  int  flr_num = 4;
  if (flr_num < 7 && flr_num > 0)
  {
    if (flr_num % 2 == 0)
    {
      for (int i = 0; i < flr_num / 2; i++)
      {
        Serial.println("y axis - UP");
        up();
        delay(2000);
        stops();
        delay(2000);
      }
      Serial.println("click");
      clicks();
      delay(2000);
      for (int i = 0; i < flr_num / 2; i++)
      {
        Serial.println("y axis - DOWN");
        down();
        delay(2000);
        stops();
        delay(2000);
      }
    }
    else
    {
      Serial.println("x axis - FWD");
      forward();
      delay(2000);
      stops();
      delay(2000);
      for (int i = 0; i < flr_num / 2; i++)
      {
        Serial.println("y axis - UP");
        up();
        delay(2000);
        stops();
        delay(2000);
      }
      Serial.println("click");
      clicks();
      delay(2000);
      for (int i = 0; i < flr_num / 2; i++)
      {
        Serial.println("y axis - DOWN");
        down();
        delay(2000);
        stops();
        delay(2000);
      }
      Serial.println("x axis - BACK");
      back();
      delay(2000);
      stops();
      delay(2000);

    }
  }
  else
  {
    Serial.println("INVALID FLOOR");
  }
  exit(0);
}
