# RoomAcousticsSim
## Overview
This project is a Python-based simulation tool for modeling room acoustics using the Pyroomacoustics library. It allows users to define custom room geometries, specify surface materials, and simulate how sound propagates within enclosed spaces. The tool is designed to provide insights into key acoustic properties such as reverberation time, sound pressure levels, and spatial sound distribution.

## Goals
1. Develop a flexible simulation framework that supports varying room dimensions and material properties.
2. Enable users to visualize acoustic behavior through intuitive plots and metrics.
3. Provide an accessible tool for educators, audio engineers, and architects to explore and evaluate room acoustics without specialized hardware.
4. Validate simulation results against theoretical predictions and published experimental data.
5. Ensure modular, readable, and maintainable code with proper documentation and test coverage.

## Implementation Plan
1. Initial Model Design
    * Define project structure and data flow

    * Create UML diagrams for core components (to be added in /docs)
    

2. Geometry and Materials Setup

    * Allow user input for room dimensions and surface absorption coefficients

    * Support predefined material presets
      

3. Simulation Core

    * Integrate Pyroomacoustics to simulate sound propagation

    * Implement support for multiple sound sources and microphones
      

4. Visualization and Analysis

    * Generate impulse responses, energy decay curves, and SPL distributions

    * Use Matplotlib for plotting and interactive display
      

5. Testing and Validation

    * Compare results with theoretical models and experimental data

    * Develop unit tests for core functionality

