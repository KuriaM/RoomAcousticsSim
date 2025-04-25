import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pyroomacoustics as pra

# Room dimensions for a 10 x 15 room with height of 10
dimensions = np.array(
    [
        [0.0, 0.0],
        [0.0, 10.0],
        [15.0, 10.0],
        [15.0, 0.0],
    ]
).T
h = 10.0

# sound source and microphone positions
speaker = np.array([[5.0], [7.0], [9.0]])  # x, y, z
microphone = np.array([[3.0], [8.0], [4.0]])

# Create the room
room = pra.Room.from_corners(dimensions)
room.add_source(speaker[:2])
room.add_microphone(microphone[:2])


#matplot method to display the room with speaker and microphone
fig, ax = room.plot(img_order=2)
ax.set_title("Room Simulation (Top View)")
ax.set_xlim([-1, 16])
ax.set_ylim([-1, 11])
ax.plot(speaker[0], speaker[1], 'ro', label='Speaker')
ax.plot(microphone[0], microphone[1], 'bx', label='Microphone')
ax.legend()
plt.show()
