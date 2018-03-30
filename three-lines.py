import csv


class CsvCoordinates:

    def __init__(self):
        return

    def extract_points(self, filename):
        points = []
        with open(filename) as csvfile:
            fieldnames = ['x', 'y']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                row["x"] = float(row["x"])
                row["y"] = float(row["y"])
                points.append(row)
            return points

    def export_to_csv(self, lines):
        f = open('daniel_coats_lines_output.csv', 'w')
        for line_index, line in enumerate(lines):
            output_text = str(line_index)
            for point in line:
                output_text += "," + str(point)
            f.write(output_text + '\n')
        f.close()


class LineFinder:
    """Finds a line made up of at least 3 points"""
    def __init__(self):
        self.slopes = {}
        self.lines = []

    def find_lines(self, points):
        """Accepts a list of points"""
        # Build a list of all possible slopes.
        self.slopes = self.__build_slopes(points)
        # Every item in lines is a potential 3+ point line.
        for lines_index, point_sets in self.slopes.items():
            for line in point_sets:
                if len(line) >= 3:
                    temp_line = []
                    for point in line:
                        temp_line.append(points[point]["x"])
                        temp_line.append(points[point]["y"])
                    self.lines.append(temp_line)

        return self.lines

    def __build_slopes(self, points):
        slopes = {}
        # Find every possible slope.
        for i in range(0, len(points)):
            for j in range(i, len(points)):
                if i != j:  # We don't need to calculate slope on the same point.
                    slope = self.__calc_slope(points[i], points[j])
                    matching_set = False
                    try:
                        exists = slopes[slope]  # no matching slope exists yet. Exits with KeyError.

                        # It is possible to have n lines with the same slope.
                        # So iterate over each set of points with the same slope.
                        for sep_slope_index, separate_slope in enumerate(slopes[slope]):
                            temp_points = list(separate_slope)
                            collinear = self.__is_collinear(points[temp_points[0]], points[temp_points[1]], points[j])
                            if collinear:  # If we find a match, then we add the point to the current set
                                slopes[slope][sep_slope_index].add(j)
                                matching_set = True
                        if not matching_set:
                            # There is a separate line with the same slope.
                            slopes[slope].append(set([i,j]))
                    except KeyError:  # No matching slope in slopes yet, let's create an entry for this set of points.
                        slopes[slope] = []
                        slopes[slope].append(set([i, j]))
        # Slopes should now be a dictionary of lists.
        # Each dictionary index corresponds to the calculated slope between points.
        # Iterating through each slope's lists will give the corresponding lines as Sets of indices.
        return slopes

    def __calc_slope(self, point_one, point_two):
        numerator = point_two["y"] - point_one["y"]
        denominator = point_two["x"] - point_one["x"]
        if numerator == 0 or denominator == 0:
            return 0.0
        slope = round(numerator/denominator, 3)
        return slope

    def __is_collinear(self, point_one, point_two, point_three):
        # At this point, we know that point_one and point_two are on the same line
        # We can use the following equation to determine if the third point is on the same line.
        a = round(point_one["x"] * (point_two["y"] - point_three["y"]), 3)
        b = round(point_two["x"] * (point_three["y"] - point_one["y"]), 3)
        c = round(point_three["x"] * (point_one["y"] - point_two["y"]), 3)
        total = a + b + c
        return total == 0

coordinates = CsvCoordinates()
lines = LineFinder().find_lines(coordinates.extract_points("lines.csv"))
coordinates.export_to_csv(lines)