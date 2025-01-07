2D LiDAR Simulation

This project simulates a 2D LiDAR system in Python using matplotlib for visualization. The simulation generates random obstacles in a defined environment, performs LiDAR scanning, and visualizes the results, including obstacle distances.

Features

Simulates a 2D LiDAR sensor that scans 360 degrees.

Detects and visualizes obstacles within a specified range.

Annotates detected obstacles with their distances from the LiDAR sensor.

Visualizes the data in polar coordinates and a 2D map.

Prerequisites

Python 3.x

Required libraries:

numpy

matplotlib

Install the required libraries using:

pip install numpy matplotlib

How to Run

Clone this repository.

Navigate to the project directory.

Run the simulation script:

python lidar_simulation.py

Output

A polar plot showing the LiDAR scan results.

A 2D map of the environment with:

LiDAR sensor location.

Detected obstacles.

Distances annotated on each obstacle.

Code Overview

Key Parameters

environment_size: Size of the simulated environment.

num_obstacles: Number of random obstacles in the environment.

lidar_range: Maximum range of the LiDAR sensor.

num_rays: Number of rays (angles) scanned by the LiDAR.

Main Functions

LiDAR Scanning:

Calculates the minimum distance to obstacles for each angle.

Visualization:

Plots polar and 2D views of the LiDAR simulation.
