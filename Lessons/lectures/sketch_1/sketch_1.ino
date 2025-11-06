#include <Servo.h>

Servo servo; 
Servo motor;

void setup() {
  servo.attach(2);  // подключаем серво к пину 2
  motor.attach(3);  // подключаем мотор к пину 3
}

void loop() {
  
  servo.write(0);    // повернуть на 0°
  delay(10000);
  servo.write(90);   // повернуть на 90°
  delay(10000);
  servo.write(180);  // повернуть на 180°
  delay(10000);


  motor.write(0);    // вращение в одну сторону (макс. скорость)
  delay(1000);
  motor.write(90);   // остановка
  delay(10000);
  motor.write(180);  // вращение в другую сторону (макс. скорость)
  delay(1000);
  motor.write(90);   // остановка
  delay(10000);
}
