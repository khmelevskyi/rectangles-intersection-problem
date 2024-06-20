import math
import random
from pprint import pprint

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2

def lines_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    return False

def is_overlap(rect1, rect2):
    # Ensure the rectangles are numpy arrays
    rect1 = np.array(rect1)
    rect2 = np.array(rect2)
    # Add the first point at the end to close the rectangle
    rect1 = np.append(rect1, [rect1[0]], axis=0)
    rect2 = np.append(rect2, [rect2[0]], axis=0)
    # Check every edge of rect1 against every edge of rect2
    for i in range(len(rect1) - 1):
        for j in range(len(rect2) - 1):
            if lines_intersect(rect1[i], rect1[i + 1], rect2[j], rect2[j + 1]):
                return True
    return False


class StripesConstructor:
    def __init__(self, n_stripes: int, max_x: int, max_y: int, rectangles = None):
        self.number_of_stripes = n_stripes
        self.max_x = max_x
        self.max_y = max_y
        self.rectangles = {} if rectangles==None else rectangles
        self.P_matrix = [[0]*n_stripes for _ in range(n_stripes)]

    def generate_random_rectangles(self):
        for i in range(self.number_of_stripes):
            # Generate random center point (cx, cy) as integers
            cx = random.randint(0, self.max_x)
            cy = random.randint(0, self.max_y)
            # Generate random width and height as integers
            width = random.randint(self.max_x // 6, self.max_x // 3)
            height = random.randint(self.max_x // 10, self.max_y // 7)
            # Generate random rotation angle in degrees and convert to radians
            angle = math.radians(random.randint(0, 360))
            # Calculate the coordinates of the corners
            half_width = width / 2
            half_height = height / 2
            # Corner relative coordinates before rotation
            corners = [(-half_width, -half_height),
                       (half_width, -half_height),
                       (half_width, half_height),
                       (-half_width, half_height)]
            # Rotate and translate corners
            rotated_corners = []
            for (dx, dy) in corners:
                rotated_x = cx + dx * math.cos(angle) - dy * math.sin(angle)
                rotated_y = cy + dx * math.sin(angle) + dy * math.cos(angle)
                rotated_corners.append((round(rotated_x), round(rotated_y)))
            self.rectangles[i] = rotated_corners
        return self.rectangles

    def visualize_rectangles(self):
        def random_color():
            return (random.random(), random.random(), random.random())
        
        fig, ax = plt.subplots()
        ax.set_xlim(0-20, self.max_x+20)
        ax.set_ylim(0-20, self.max_y+20)

        for i, rect in self.rectangles.items():
            polygon = patches.Polygon(rect, closed=True, fill=False, edgecolor=random_color())
            ax.add_patch(polygon)
            # Calculate the centroid of the rectangle to place the text
            cx = sum([point[0] for point in rect]) / 4
            cy = sum([point[1] for point in rect]) / 4
            # Add the rectangle number at the centroid
            plt.text(cx, cy, str(i), fontsize=12, ha='center', va='center', color='black')

        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    def construct_P_matrix(self):
        for i, rect1 in self.rectangles.items():
            for j, rect2 in self.rectangles.items():
                if rect1 != rect2:
                    self.P_matrix[i][j] = int(is_overlap(rect1, rect2))
                else:
                    self.P_matrix[i][j] = -1
        return self.P_matrix
    
    @classmethod
    def generate_P_matrix_with_known_F(cls, n_stripes, bottom_fill=0.6, upper_fill=0.9):
        min_ones = int(bottom_fill * n_stripes) 
        max_ones = int(upper_fill * n_stripes) 
        num_ones = np.random.randint(min_ones, max_ones + 1) 
    
        X_opt = np.array([1] * num_ones + [0] * (n_stripes - num_ones)) 
        np.random.shuffle(X_opt) 
    
        P = np.zeros((n_stripes, n_stripes), dtype=int) 
    
        for i in range(n_stripes): 
            for j in range(i+1, n_stripes): 
                if X_opt[i] == 1 and X_opt[j] == 1: 
                    P[i][j] = 0 
                else: 
                    P[i][j] = np.random.choice([0, 1], p=[0.3, 0.7]) 
    
                P[j][i] = P[i][j] 
    
        X_opt = X_opt.tolist() 
        return P, np.sum(X_opt)

    @classmethod
    def generate_random_P_matrix(cls, n_stripes):
        P_matrix = [[0]*n_stripes for _ in range(n_stripes)]
        for i in range(n_stripes):
            for j in range(i+1, n_stripes):
                P_matrix[i][j] = np.random.choice([0, 1])
                P_matrix[j][i] = P_matrix[i][j]
        return P_matrix

    @classmethod
    def generate_random_P_with_percentage(cls, n_stripes, percentage): 
        P_matrix = [[0] * n_stripes for _ in range(n_stripes)] 
        num_upper_triangle_elements = n_stripes * (n_stripes - 1) // 2 
        num_ones = int(percentage * num_upper_triangle_elements) 
    
        # Create a list of indices for the upper triangle elements 
        upper_triangle_indices = [(i, j) for i in range(n_stripes) for j in range(i + 1, n_stripes)] 
        
        # Randomly select indices to be set to 1 
        ones_indices = random.sample(upper_triangle_indices, num_ones) 
        
        for i, j in ones_indices: 
            P_matrix[i][j] = 1 
            P_matrix[j][i] = 1  # Ensure symmetry 
        
        return P_matrix




if __name__ == "__main__":
    # Example usage:
    n = 9  # number of rectangles
    max_x = 100
    max_y = 100

    stripes_constructor = StripesConstructor(n, max_x, max_y)
    rectangles = stripes_constructor.generate_random_rectangles()
    P_matrix = stripes_constructor.construct_P_matrix()

    print("number of rectangles:", n)
    for rect_ii in rectangles:
        print(f"Rectangle{rect_ii} points: {rectangles[rect_ii]}")
    print()

    stripes_constructor.visualize_rectangles()
    print()

    pprint(P_matrix, width=100)