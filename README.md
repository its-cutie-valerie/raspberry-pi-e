# Raspberry Pi(e)

A whimsical, thematic Monte Carlo simulation that "bakes" an estimation of the mathematical constant **π (Pi)** using raspberries, a cake, and a bit of random chance.

![Raspberry Pi Animation](pi_monte_carlo.gif)

## The Concept

This project transforms a classic numerical method into a kitchen experiment. Instead of abstract "points in a square," we are throwing **raspberries** onto a **baking tray**.

*   **The Baking Tray**: A 2x2 square (area = 4).
*   **The Cake**: A circular sponge cake with a radius of 1 (area = π) centered in the tray.
*   **The Ingredients**: 1,500 random points (raspberries) distributed across the tray.

By counting how many raspberries land on the cake versus the total number thrown, we can calculate the ratio of the areas and solve for Pi:

$$ 
\frac{\text{Raspberries on Cake}}{\text{Total Raspberries}} \approx \frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi \times r^2}{(2r)^2} = \frac{\pi}{4} 
$$

Therefore:

$$
\pi \approx 4 \times \left( \frac{\text{Raspberries on Cake}}{\text{Total Raspberries}} \right)
$$

## Features

- **Thematic Aesthetics**: A "Marble & Raspberry" colour palette using custom hex codes for a warm feel.
- **Dynamic Animation**: Real-time visualization of raspberries falling and the Pi estimate updating.
- **Auto-Export**: Automatically saves the simulation as a high-quality GIF (`pi_monte_carlo.gif`).
- **Mathematical Precision**: Uses `numpy` for efficient random sampling and vector calculations.

## Getting Started

### Prerequisites

You will need Python 3.8+ and a few libraries:

```bash
pip install numpy matplotlib pillow
```

*Note: `pillow` is required for saving the animation as a GIF.*

### Running the Recipe

To start baking your own Pi, simply run the main script:

```bash
python pi_monty.py
```

The script will begin "baking" the animation and save it to the current directory.

## Design System

The project uses a certain colour palette to maintain its "baking" theme.

| Element | Colour | Hex |
| :--- | :--- | :--- |
| **Countertop** | Marble White | `#FFF9F0` |
| **Sponge Cake** | Papaya Whip | `#FFEFD5` |
| **Baking Tray** | Tan Wood | `#D2B48C` |
| **Raspberries** | Crimson | `#DC143C` |
| **Accents** | Deep Pink | `#C2185B` |

## Configuration

You can adjust the "baking time" and "accuracy" in the `pi_monty.py` script by modifying the following parameters:

- `TOTAL_POINTS`: Total number of raspberries to throw (default: 1500).
- `BATCH_SIZE`: How many raspberries fall per animation frame (default: 2).
- `INTERVAL`: Delay between frames in milliseconds (default: 20).

---

*Enjoy your Pi(e)!* 
