// Definir los pines analógicos a los que está conectado el joystick
const int joystickX = A0; // Pin analógico para el eje X
const int joystickY = A1; // Pin analógico para el eje Y

void setup() {
  // Iniciar comunicación serial para mostrar los valores en el monitor serie
  Serial.begin(9600);
}

void loop() {
  // Leer los valores de los ejes X y Y
  int xValue = analogRead(joystickX);
  int yValue = analogRead(joystickY);

  // Escalar los valores para que el centro del joystick sea 0,0
  int scaledX = xValue - 512; // Restar 512 para que el centro sea 0
  int scaledY = yValue - 512; // Restar 512 para que el centro sea 0

  // Imprimir los valores escalados de los ejes en el monitor serie
  Serial.print(scaledX);
  Serial.print(",");
  Serial.println(scaledY);

  // Hacer una pequeña pausa para evitar que la lectura sea demasiado rápida
  delay(100);
}
