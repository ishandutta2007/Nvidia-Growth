import matplotlib.pyplot as plt
import os

# 10-Year historical data timeline for NVIDIA (2016 - 2026)
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

# Market Cap in Billions of USD (Approximate historical benchmarks)
market_cap_billions = [40.0, 115.0, 120.0, 145.0, 314.0, 618.0, 336.0, 1015.0, 2147.0, 4638.0, 4858.0]

# Total Global Headcount (NVIDIA Fiscal Year Reporting)
employee_count = [9227, 10214, 11528, 13277, 13775, 18975, 22473, 26196, 29600, 35000, 42000]

# Initialize the plot layout
fig, ax1 = plt.subplots(figsize=(13, 8))
plt.title("NVIDIA's Hyper-Growth: Market Cap vs. Employee Count (2016-2026)", fontsize=14, pad=20, fontweight='bold')

# Configure primary Y-axis (Market Capitalization)
color_market = '#76B900'  # Signature NVIDIA Green
ax1.set_xlabel('Year', fontsize=12, labelpad=10)
ax1.set_ylabel('Market Capitalization ($ Billions)', color=color_market, fontsize=12)
line1 = ax1.plot(years, market_cap_billions, color=color_market, marker='o', linewidth=2.5, label='Market Cap ($B)')
ax1.tick_params(axis='y', labelcolor=color_market)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.set_ylim(-100, 5200)

# Instantiate a secondary Y-axis sharing the same X-axis
ax2 = ax1.twinx()
color_employees = '#1434A4'  # Contrast corporate blue
ax2.set_ylabel('Total Full-Time Employees', color=color_employees, fontsize=12)
line2 = ax2.plot(years, employee_count, color=color_employees, marker='s', linewidth=2.5, linestyle='--', label='Employee Count')
ax2.tick_params(axis='y', labelcolor=color_employees)
# Setting ax2 limits to prevent the employee line from looking as steep as the market cap line
# This visually highlights the huge divergence in scaling (121.5x vs 4.6x)
ax2.set_ylim(0, 250000)

# Add a prominent stats contrast card / text box
stats_text = (
    "NVIDIA Efficiency Disparity (2016-2026):\n"
    "• Market Cap: 121.5x growth ($40B → $4,858B)\n"
    "• Headcount: 4.6x growth (9,227 → 42,000)\n"
    "• Market Cap / Employee: 26.7x ($4.3M → $115.7M)"
)
ax1.text(0.02, 0.95, stats_text, transform=ax1.transAxes, fontsize=11, fontweight='bold',
         verticalalignment='top', bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#cbd5e1', alpha=0.95))

# ----------------- CODE ANNOTATIONS START HERE -----------------

# Annotation 1: 2020 Mellanox Acquisition & Work-from-Home Demand
ax1.annotate('Mellanox Buy\n& WFH Spike', 
             xy=(2020, 314.0), 
             xytext=(2018.5, 1200),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
             fontsize=9, bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3))

# Annotation 2: 2024 Generative AI Explosion (H100 GPUs)
ax1.annotate('H100 Launch\nGenerative AI Boom', 
             xy=(2024, 2147.0), 
             xytext=(2021.5, 2400),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
             fontsize=9, bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3))

# Annotation 3: 2026 Peak Scaling (Blackwell Architecture)
ax1.annotate('Blackwell Scaling\n$4.8T+ Cap\n(121.5x Growth)', 
             xy=(2026, 4858.0), 
             xytext=(2022, 4300),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
             fontsize=9, fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', fc='#76B900', alpha=0.2))

# Annotation 4: Corporate Headcount Surge (42k employees)
ax2.annotate('Workforce\nSurges to 42k\n(4.6x Growth)', 
             xy=(2026, 42000), 
             xytext=(2024.5, 65000),
             arrowprops=dict(arrowstyle='->', lw=1, color='#1434A4'),
             fontsize=9, color='#1434A4', bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3))

# Helper function to prevent repetitive annotation block syntax
def add_annotations1(data_list, color_hex, bg_hex, text_y_offset):
    for i, count in enumerate(data_list):
        # Only annotate start, end, and major inflection points to avoid overcrowding
        if i in [0, len(data_list)-1]:
            label = f"${count:,.1f}B\n(Base)" if i == 0 else f"${count:,.1f}B\n(121.5x)"
            ax1.annotate(
                label, 
                (years[i], data_list[i]), 
                textcoords="offset points", 
                xytext=(0, text_y_offset), 
                ha='center', 
                fontsize=9, 
                fontweight='bold',
                color=color_hex,
                bbox=dict(boxstyle="round,pad=0.2", fc=bg_hex, ec=color_hex, lw=1, alpha=0.85)
            )
        elif i in [4, 6, 8]:  # Inflection points: 2020, 2022, 2024
            ax1.annotate(
                f"${count:,.0f}B", 
                (years[i], data_list[i]), 
                textcoords="offset points", 
                xytext=(0, text_y_offset), 
                ha='center', 
                fontsize=8, 
                color=color_hex,
                bbox=dict(boxstyle="round,pad=0.1", fc=bg_hex, ec=color_hex, lw=0.5, alpha=0.7)
            )

# Apply automated annotations with strategic vertical spacing adjustments
add_annotations1(market_cap_billions, '#76B900', '#2c2c2c', -25)

def add_annotations2(data_list, color_hex, bg_hex, text_y_offset):
    for i, count in enumerate(data_list):
        if i in [0, len(data_list)-1]:
            label = f"{count:,}\n(Base)" if i == 0 else f"{count:,}\n(4.6x)"
            ax2.annotate(
                label, 
                (years[i], data_list[i]), 
                textcoords="offset points", 
                xytext=(0, text_y_offset), 
                ha='center', 
                fontsize=9, 
                fontweight='bold',
                color=color_hex,
                bbox=dict(boxstyle="round,pad=0.2", fc=bg_hex, ec=color_hex, lw=1, alpha=0.85)
            )
        elif i in [4, 6, 8]:
            ax2.annotate(
                f"{count:,}", 
                (years[i], data_list[i]), 
                textcoords="offset points", 
                xytext=(0, text_y_offset), 
                ha='center', 
                fontsize=8, 
                color=color_hex,
                bbox=dict(boxstyle="round,pad=0.1", fc=bg_hex, ec=color_hex, lw=0.5, alpha=0.7)
            )

# Apply automated annotations with strategic vertical spacing adjustments
add_annotations2(employee_count, '#0369a1', '#f0f9ff', 15)

# ------------------ CODE ANNOTATIONS END HERE ------------------

# Structure and consolidate the legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right', frameon=True, shadow=True)

# Perfect tick layouts
plt.xticks(years)
fig.tight_layout()

# Display the twin-axis visualization
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
output_path = os.path.join(assets_dir, 'nvidia_growth.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved plot to: {output_path}")
# Use non-blocking plot display if running in environment with GUI
if os.environ.get('DISPLAY') or os.name == 'nt':
    try:
        plt.show(block=False)
        plt.pause(100)
        plt.close()
    except Exception:
        pass

