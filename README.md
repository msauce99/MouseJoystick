# 🖱️ MouseJoystick

This repository contains code — and eventually hardware design files — for a modified joystick system based on the **DigiKey TS-1D1S00A-1294**, interfaced with an **Arduino**.  
The setup is intended for **mouse neural behavioral experiments**, allowing precise tracking of joystick displacements.

## 📁 Repository Structure

### `Joystick_Pos.py`

- Reads positional data from the Arduino.
- Displays a real-time interactive interface for visualizing joystick movement.
- Includes an (currently non-functional) section intended for testing a **force sensor**.

### `Joystick_Pos.ino`

- Arduino firmware that handles communication and data exchange with the Python interface.
- Responsible for reading joystick coordinates and sending them over serial to the computer.

## 🚧 Future Work

- Integration of force sensor functionality.
- Upload of hardware schematics and design files.
- Implementation of the reward and pertubation systems.


