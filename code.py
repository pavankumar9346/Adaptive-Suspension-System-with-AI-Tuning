import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------
# Adaptive Suspension System (Rule-based version)
# ----------------------------------------------

def adaptive_damping(road_roughness, speed):
    """
    Simple adaptive damping control logic.
    - Soft damping for smooth roads or low speed.
    - Stiff damping for rough roads or high speed.
    """
    damping = 0.3 + 0.5 * road_roughness + 0.002 * speed
    return np.clip(damping, 0, 1)

def simulate_suspension(steps=60):
    time = []
    damping_values = []
    comfort_score = []
    road_data = []
    speed_data = []
    
    for t in range(steps):
        road = np.random.uniform(0, 1)   # road roughness
        speed = np.random.uniform(20, 120)  # vehicle speed (km/h)
        
        damping = adaptive_damping(road, speed)
        
        # Estimate comfort (lower acceleration = better comfort)
        acceleration = abs(road * (1 - damping) * np.random.uniform(0.8, 1.2))
        comfort = 1 - np.clip(acceleration, 0, 1)
        
        time.append(t)
        damping_values.append(damping)
        comfort_score.append(comfort)
        road_data.append(road)
        speed_data.append(speed)
        
        print(f"t={t:02d} | Road={road:.2f} | Speed={speed:.1f} | "
              f"Damping={damping:.2f} | Comfort={comfort:.2f}")
    
    return np.array(time), damping_values, comfort_score, road_data, speed_data

# Run the simulation
time, damping, comfort, road, speed = simulate_suspension(steps=60)

# Plot results
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(time, road, label="Road Roughness", color='brown')
plt.ylabel("Roughness")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, damping, label="Adaptive Damping", color='blue')
plt.ylabel("Damping")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, comfort, label="Ride Comfort", color='green')
plt.xlabel("Time (s)")
plt.ylabel("Comfort")
plt.legend()

plt.tight_layout()
plt.show()
