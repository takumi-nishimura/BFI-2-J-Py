from math import pi

import matplotlib.pyplot as plt


class RadarChart:
    def __init__(self, labels: list, y_range: list):
        """_summary_

        Args:
            labels (list): Radar chart labels
            y_range (list): Radar chart y range. [min, max]
        """

        self.ax = plt.subplot(111, polar=True)

        self.ax.set_theta_offset(pi / 2)
        self.ax.set_theta_direction(-1)

        self.labels = labels
        self.angles = [
            n / float(len(labels)) * 2 * pi for n in range(len(labels))
        ]
        self.angles += self.angles[:1]

        plt.xticks(self.angles[:-1], self.labels, color="black", size=7)
        self.ax.set_rlabel_position(0)
        plt.yticks(
            range(y_range[0], y_range[1] + 1),
            [str(i) for i in range(y_range[0], y_range[1] + 1)],
            color="gray",
            size=5,
        )
        plt.ylim((y_range[0], y_range[1] + 1))

    def plot(self, values, **kwargs):
        values += values[:1]
        self.ax.plot(self.angles, values, **kwargs)
        self.ax.fill(self.angles, values, alpha=0.05)
