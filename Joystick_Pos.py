import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from collections import deque
import matplotlib
matplotlib.use('TkAgg')  # Ensures interaction like zoom and pan

# Serial connection
arduino = serial.Serial('COM7', 9600, timeout=1)

# Trail history
trail = deque(maxlen=500)

# Plot configuration
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)  # more space for buttons
ax.set_aspect('equal')
ax.grid(True)
ax.autoscale(enable=True)
circle = plt.Circle((0, 0), 100, color='black', fill=False)
ax.add_patch(circle)

# Dot and trail
dot, = ax.plot([], [], 'ro')  # current point
line, = ax.plot([], [], 'b-', alpha=0.5)  # trail

# Text to display coordinates
text_ax = plt.axes([0.3, 0.2, 0.4, 0.05])
text_ax.axis('off')
coord_text = text_ax.text(0.5, 0.5, 'X: 0, Y: 0', ha='center', va='center', fontsize=12)

# Update function
def update(frame):
    try:
        line_raw = arduino.readline().decode().strip()
        if ',' in line_raw:
            x_str, y_str = line_raw.split(',')
            x, y = int(x_str), int(y_str)

            # Limit to the edge of the circle
            distance = (x**2 + y**2)**0.5
            if distance > 100:
                scale = 100 / distance
                x = int(x * scale)
                y = int(y * scale)

            trail.append((x, y))
            dot.set_data([x], [y])
            xs, ys = zip(*trail)
            line.set_data(xs, ys)

            coord_text.set_text(f'X: {x}, Y: {y}')
        time.sleep(0.05)
    except:
        pass
    return dot, line, coord_text

# Function to clear the trail
def clear(event):
    trail.clear()
    line.set_data([], [])
    fig.canvas.draw_idle()

# Zoom functions
zoom_margin = 20  # initial margin

def zoom(center, margin):
    x, y = center
    ax.set_xlim(x - margin, x + margin)
    ax.set_ylim(y - margin, y + margin)
    fig.canvas.draw_idle()

def zoom_in(event):
    global zoom_margin
    if trail and zoom_margin > 5:
        zoom_margin -= 5
        zoom(trail[-1], zoom_margin)

def zoom_out(event):
    global zoom_margin
    if trail and zoom_margin < 120:
        zoom_margin += 5
        zoom(trail[-1], zoom_margin)

# "Clear" button
ax_button = plt.axes([0.1, 0.05, 0.2, 0.075])
btn_clear = Button(ax_button, 'Clear')
btn_clear.on_clicked(clear)

# "Zoom In" button
ax_zoom_in = plt.axes([0.4, 0.05, 0.2, 0.075])
btn_zoom_in = Button(ax_zoom_in, 'Zoom In')
btn_zoom_in.on_clicked(zoom_in)

# "Zoom Out" button
ax_zoom_out = plt.axes([0.7, 0.05, 0.2, 0.075])
btn_zoom_out = Button(ax_zoom_out, 'Zoom Out')
btn_zoom_out.on_clicked(zoom_out)

# Launch animation
ani = animation.FuncAnimation(fig, update, interval=100)
plt.title("Joystick Position in Real Time")
plt.show()
