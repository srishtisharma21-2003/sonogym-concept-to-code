import numpy as np
import matplotlib.pyplot as plt

# 1. Create a 3D "Bone" (A dense sphere inside a grid)
def create_phantom(size=64):
    phantom = np.zeros((size, size, size))
    center = size // 2
    radius = size // 4
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if (x - center)**2 + (y - center)**2 + (z - center)**2 < radius**2:
                    phantom[x, y, z] = 1.0 # High density (Bone)
    return phantom

# 2. Simulate the Sound Waves (Rays) hitting the bone
def simulate_ultrasound(phantom, probe_pos, probe_dir, resolution=64):
    image = np.zeros((resolution, resolution))
    size = phantom.shape[0]
    
    for i in range(resolution):
        for j in range(resolution):
            # Spread the rays out like a flashlight
            offset_x = (i - resolution/2) * 0.5
            offset_y = (j - resolution/2) * 0.5
            ray_dir = probe_dir
            ray_pos = probe_pos + np.array([offset_x, offset_y, 0])
            
            depth = 0.0
            while depth < 40.0:
                current_pos = ray_pos + ray_dir * depth
                x, y, z = int(current_pos[0]), int(current_pos[1]), int(current_pos[2])
                
                # If the ray hits the bone, record the depth
                if 0 <= x < size and 0 <= y < size and 0 <= z < size:
                    if phantom[x, y, z] > 0.5:
                        image[i, j] = 1.0 - (depth / 40.0) 
                        break
                depth += 0.5
                
    # Add static (speckle noise) to make it look like a real US machine
    noise = np.random.normal(0, 0.1, image.shape)
    return np.clip(image + noise, 0, 1)

# 3. Run the simulation from 3 different angles
phantom = create_phantom()
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Probe Centered
img1 = simulate_ultrasound(phantom, np.array([32, 32, 0]), np.array([0, 0, 1]))
axes[0].imshow(img1, cmap='gray')
axes[0].set_title("Probe Pose 1 (Centered)")
axes[0].axis('off')

# Probe Shifted Right
img2 = simulate_ultrasound(phantom, np.array([42, 32, 0]), np.array([0, 0, 1]))
axes[1].imshow(img2, cmap='gray')
axes[1].set_title("Probe Pose 2 (Shifted)")
axes[1].axis('off')

# Probe Angled (Simulating a bad scan angle)
img3 = simulate_ultrasound(phantom, np.array([32, 32, 0]), np.array([0.5, 0, 1]))
axes[2].imshow(img3, cmap='gray')
axes[2].set_title("Probe Pose 3 (Angled)")
axes[2].axis('off')

plt.tight_layout()
plt.savefig("raycaster_proof.png") # THIS SAVES THE IMAGE
plt.show()
