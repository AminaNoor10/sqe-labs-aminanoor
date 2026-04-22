import matplotlib.pyplot as plt
import numpy as np

# ============================================
# YOUR RATINGS
# ============================================

# Apple Maps ratings (from your iPhone friend)
APP1_RATINGS = [2, 4, 4, 3, 3, 5, 4, 2]

# Google Maps ratings (your ratings)
APP2_RATINGS = [4, 4, 5, 4, 5, 3, 4, 5]

# ============================================
# CHARACTERISTICS LABELS
# ============================================

characteristics = [
    'Functional\nSuitability',
    'Performance\nEfficiency',
    'Compatibility',
    'Usability',
    'Reliability',
    'Security',
    'Maintainability',
    'Portability'
]

# Weights
weights = [0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10]

# Calculate weighted scores
app1_weighted = sum([APP1_RATINGS[i] * weights[i] for i in range(8)])
app2_weighted = sum([APP2_RATINGS[i] * weights[i] for i in range(8)])

print(f"Apple Maps Weighted Score: {app1_weighted:.2f}/5.00")
print(f"Google Maps Weighted Score: {app2_weighted:.2f}/5.00")

# Create radar chart
angles = np.linspace(0, 2 * np.pi, len(characteristics), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# Apple Maps (Blue)
values1 = APP1_RATINGS + [APP1_RATINGS[0]]
ax.plot(angles, values1, 'o-', linewidth=2, color='blue', label=f'Apple Maps (Wtd: {app1_weighted:.2f})')
ax.fill(angles, values1, alpha=0.25, color='blue')

# Google Maps (Red)
values2 = APP2_RATINGS + [APP2_RATINGS[0]]
ax.plot(angles, values2, 'o-', linewidth=2, color='red', label=f'Google Maps (Wtd: {app2_weighted:.2f})')
ax.fill(angles, values2, alpha=0.25, color='red')

# Set labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(characteristics, fontsize=10)
ax.set_ylim(0, 5.5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
ax.set_title('ISO 25010 Quality Characteristics Comparison\nApple Maps vs Google Maps', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=10)
ax.grid(True)

plt.tight_layout()
plt.savefig('radar_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Radar chart saved as 'radar_chart.png'")