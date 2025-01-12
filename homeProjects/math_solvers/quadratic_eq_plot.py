import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

# constants
CRV_OFFSET = 5


class SolveQuadratic:

    def __init__(self, coeffs):
        self.coeffs = coeffs  # Coefficients for 3x^2-5x-2 = 0 are [3, -5, -2]

    def f(self, x):
        y = 0
        for index, value in enumerate(self.coeffs):
            y += value * x ** (len(self.coeffs) - (index + 1))
        return y

    def solve(self):

        # Find roots
        roots = np.roots(self.coeffs)

        # Plotting the roots
        for root in roots:
            plt.plot(root, 0, 'ro')  # 'ro' for red circle marker
            plt.annotate(f'({root:.4f}, 0)', (root, 0), textcoords="offset points", xytext=(0, 10), ha='center')

        x = np.linspace(roots.min() - CRV_OFFSET, roots.max() + CRV_OFFSET, 100)  # Creates 100 points between -5 and 5
        y = self.f(x)  # Apply the function to each x

        plt.plot(x, y)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f"Plot of y = {self.coeffs[0]}x^2+{self.coeffs[1]}x+{self.coeffs[2]}")
        plt.grid(True)
        plt.axhline(y=0, color='k')  # x-axis line for clarity

        plt.show()


class SolveSystem:
    def f1(self, x):
        return 5 - x

    def f2(self, x):
        return np.sqrt(25 - 2 * x ** 2)

    def find_intersections(self, x):
        f_diff = self.f1(x) - self.f2(x)
        intersections = []

        # Look for sign changes
        for i in range(len(f_diff) - 1):
            if f_diff[i] * f_diff[i+1] < 0:  # Sign change indicates a root between these points
                # Use brentq to find the root between x[i] and x[i+1]
                root = brentq(lambda x: self.f1(x) - self.f2(x), x[i], x[i+1])
                intersections.append((root, self.f1(root)))

        return intersections

    def draw(self, x, y1, y2, title):
        plt.figure()
        plt.plot(x, y1, label='y = 5 - x')
        plt.plot(x, y2, label='y = sqrt(25 - 2x^2)')

        # Find all intersections
        intersections = self.find_intersections(x)

        # Plot intersections
        for x_cross, y_cross in intersections:
            plt.plot(x_cross, y_cross, 'ro')  # Mark the intersection point
            plt.annotate(f'({x_cross:.2f}, {y_cross:.2f})', (x_cross, y_cross),
                         textcoords="offset points", xytext=(0,10), ha='center')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.grid(True)
        plt.axhline(y=0, color='k')  # x-axis line for clarity
        plt.legend()
        plt.show()

    def solve(self):
        x1 = np.linspace(-10 - CRV_OFFSET, 10 + CRV_OFFSET, 10000)  # Increased precision for more accurate intersections
        y1 = self.f1(x1)
        y2 = self.f2(x1)

        self.draw(x1, y1, y2, "Plot for functions with intersections")

        plt.show()
