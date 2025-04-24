# RoomAcousticsSim
## Overview
This project is a python based simulation tool for modeling room acoustics using the pyroomacoustics library. It allows the user to define custom room geometry, specify where the source of the sound is positioned, and specify the material of the room's surfaces. The simulation is designed to provide insights into acoustic properties such as reverberation time & decay, sound pressure levels, and spatial sound distribution.

## Goals
1. Develop a simulation framework that supports varying room dimensions and material properties.
2. Enable users to visualize acoustics behavior through plots and graphs.
3. Validate simulation results against predictions and published experimental data.
4. Ensure readable and maintainable code with proper documentation and testing.

## Implementation Plan
1. Initial Model Design
    * Define project structure and data flow

    * Create UML diagrams for classes
    

2. Geometry and Materials Setup
    * Allow user input for room dimensions and surface absorption 

    * Support predefined material presets
      

3. Develop Simulation 
    * Integrate Pyroomacoustics to simulate sound propagation

    * Implement variable sound sources and microphones
      

4. Visualization and Analysis
    * Generate impulse responses, reverb decay graphs, and frequency responses

    * Use Matplotlib or other libraries for plotting and graph display
      

5. Testing and Validation
    * Compare results with theoretical models and experimental data

    * Develop tests for functionality

