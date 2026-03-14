import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# --- Configuration & Styling (Raspberry Cake Theme) ---
BG_COLOR = "#FFF9F0"       # Marble countertop
CAKE_COLOR = "#FFEFD5"     # Sponge cake (PapayaWhip)
TRAY_COLOR = "#D2B48C"     # Wooden tray (Tan)
RASPBERRY_COLOR = "#DC143C" # Bright crimson raspberries
SUGAR_COLOR = "#E8E8E8"    # Powdered sugar
TEXT_COLOR = "#4E342E"     # Dark cocoa
ACCENT_COLOR = "#C2185B"   # Raspberry pink

plt.rcParams['text.color'] = TEXT_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['font.family'] = 'serif'

# Simulation Parameters
TOTAL_POINTS = 1500
BATCH_SIZE = 2
INTERVAL = 20

def run_pi_simulation():
    # Pre-generate points
    x = np.random.uniform(-1, 1, TOTAL_POINTS)
    y = np.random.uniform(-1, 1, TOTAL_POINTS)
    dist = x**2 + y**2
    inside_circle = dist <= 1

    # Setup Figure
    fig, ax = plt.subplots(figsize=(8, 9), facecolor=BG_COLOR)
    fig.subplots_adjust(top=0.85, bottom=0.1)
    
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axis('off')

    # Draw Baking Tray (Square) and Cake (Circle)
    tray = patches.Rectangle((-1, -1), 2, 2, fill=True, color=TRAY_COLOR, alpha=0.3, zorder=1)
    tray_border = patches.Rectangle((-1, -1), 2, 2, fill=False, color=TRAY_COLOR, linewidth=5, zorder=2)
    cake = patches.Circle((0, 0), 1, fill=True, color=CAKE_COLOR, alpha=0.9, zorder=3)
    cake_border = patches.Circle((0, 0), 1, fill=False, color="#E6BE8A", linewidth=2, zorder=4)
    
    ax.add_patch(tray)
    ax.add_patch(tray_border)
    ax.add_patch(cake)
    ax.add_patch(cake_border)

    # Scatters: Raspberries (In) and Missed Raspberries (Out)
    scat_in = ax.scatter([], [], color=RASPBERRY_COLOR, s=40, alpha=0.9, 
                        edgecolors='#880E4F', linewidths=0.5, zorder=5, label='On Cake')
    scat_out = ax.scatter([], [], color=RASPBERRY_COLOR, s=25, alpha=0.15, 
                         edgecolors='none', zorder=4, label='Missed')

    # Themed Text Display
    title_text = ax.text(0, 1.3, "Baking a Raspberry Pi(e)", ha='center', va='center', 
                        fontsize=22, fontweight='bold', fontname='serif', color=TEXT_COLOR)
    
    subtitle_text = ax.text(0, 1.18, "Estimating π via Monte Carlo Ingredients", ha='center', va='center', 
                           fontsize=12, style='italic', color=TEXT_COLOR)

    pi_display = ax.text(0, -1.3, "", ha='center', va='center', 
                        fontsize=26, fontweight='bold', color=ACCENT_COLOR,
                        bbox={'facecolor': 'white', 'alpha': 0.8, 'edgecolor': ACCENT_COLOR, 'pad': 8, 'boxstyle': 'round,pad=0.5'})
    
    counts_text = ax.text(0, -1.1, "", ha='center', va='center', fontsize=11, color=TEXT_COLOR, alpha=0.7)

    # Data tracking
    points_in_x, points_in_y = [], []
    points_out_x, points_out_y = [], []

    def init():
        scat_in.set_offsets(np.empty((0, 2)))
        scat_out.set_offsets(np.empty((0, 2)))
        pi_display.set_text("π ≈ 0.0000")
        counts_text.set_text("Ingredients: 0 | Raspberries on Cake: 0")
        return scat_in, scat_out, pi_display, counts_text

    def animate(frame):
        end = (frame + 1) * BATCH_SIZE
        if end > TOTAL_POINTS: return scat_in, scat_out, pi_display, counts_text

        # Get latest point(s)
        current_range = slice(frame * BATCH_SIZE, end)
        new_x = x[current_range]
        new_y = y[current_range]
        new_inside = inside_circle[current_range]

        # Update collections
        points_in_x.extend(new_x[new_inside])
        points_in_y.extend(new_y[new_inside])
        points_out_x.extend(new_x[~new_inside])
        points_out_y.extend(new_y[~new_inside])

        # Calc π
        inside_count = len(points_in_x)
        total_count = end
        current_pi = 4 * (inside_count / total_count)
        
        # Plot
        scat_in.set_offsets(np.column_stack((points_in_x, points_in_y)))
        scat_out.set_offsets(np.column_stack((points_out_x, points_out_y)))

        # Update Text
        pi_display.set_text(f"π ≈ {current_pi:.4f}")
        counts_text.set_text(f"Raspberries in Total: {total_count} | Raspberries on Cake: {inside_count}")

        return scat_in, scat_out, pi_display, counts_text

    # Create Animation
    ani = FuncAnimation(fig, animate, frames=TOTAL_POINTS // BATCH_SIZE, 
                        init_func=init, blit=True, interval=INTERVAL, repeat=False)

    print("Baking your Raspberry Pi animation...")
    ani.save('pi_monte_carlo.gif', writer='pillow', fps=60)
    print("Recipe complete! Saved to pi_monte_carlo.gif")

if __name__ == "__main__":
    run_pi_simulation()
