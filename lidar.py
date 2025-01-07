import numpy as np
import matplotlib.pyplot as plt

# Environment dimensions
environment_size = 20
num_obstacles = 10

# Generate random obstacles
obstacles = np.random.uniform(0, environment_size, size=(num_obstacles, 2))

# LiDAR sensor parameters
lidar_position = np.array([environment_size / 2, environment_size / 2])  # Sensor center
lidar_range = 10  # Maximum detection range
num_rays = 360  # Scanning angle (in degrees)

# Perform scanning
angles = np.linspace(0, 2 * np.pi, num_rays)
distances = []

for angle in angles:
    min_distance = lidar_range
    for obs in obstacles:
        # Calculate the distance between the obstacle and the LiDAR
        vector = obs - lidar_position
        distance = np.linalg.norm(vector)
        angle_to_obs = np.arctan2(vector[1], vector[0])
        # Normalize the angle (-pi to pi)
        angle_diff = np.arctan2(np.sin(angle - angle_to_obs), np.cos(angle - angle_to_obs))
        if distance <= lidar_range and abs(angle_diff) < (np.pi / num_rays):
            min_distance = min(min_distance, distance)
    distances.append(min_distance)

# Visualize the data in polar coordinates
ax = plt.subplot(111, polar=True)
ax.plot(angles, distances, label="LiDAR Scan")
ax.set_ylim(0, lidar_range)
plt.legend()
plt.show()

# Visualize the environment and obstacles
plt.figure(figsize=(8, 8))
plt.xlim(0, environment_size)
plt.ylim(0, environment_size)

# Plot LiDAR sensor position
plt.scatter(*lidar_position, color="blue", label="LiDAR Sensor")

# Plot obstacles
plt.scatter(obstacles[:, 0], obstacles[:, 1], color="red", label="Obstacles")

# Plot LiDAR scan results and annotate distances
for angle, distance in zip(angles, distances):
    end_point = lidar_position + distance * np.array([np.cos(angle), np.sin(angle)])
    plt.plot([lidar_position[0], end_point[0]], [lidar_position[1], end_point[1]], color="green", alpha=0.5)

# Annotate each obstacle with its distance
for obs in obstacles:
    distance_to_sensor = np.linalg.norm(obs - lidar_position)
    plt.annotate(f"{distance_to_sensor:.2f}",
                 (obs[0], obs[1]),
                 textcoords="offset points",
                 xytext=(5, 5),
                 ha='center',
                 fontsize=9,
                 color="black")

plt.legend()
plt.title("2D LiDAR Simulation with Distances on Obstacles")
plt.show()
