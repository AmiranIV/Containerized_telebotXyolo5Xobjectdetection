from pathlib import Path
from matplotlib.image import imread, imsave


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()


    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

    def rotate(self):
        rotated_data = []
        for j in range(len(self.data[0])):
            rotated_row = []
            for i in range(len(self.data)):
                rotated_row.append(self.data[i][j])
            rotated_data.append(rotated_row)
        self.data = rotated_data

    def salt_n_pepper(self):
        # TODO remove the `raise` below, and write your implementation
        raise NotImplementedError()

    def concat(self, other_img, direction='horizontal'):
        if not isinstance(other_img, Img):
            raise TypeError("The 'other_img' parameter must be an instance of the Img Class.")

        if direction not in ['horizontal', 'vertical']:
            raise ValueError("Invalid 'direction' parameter. It should be either 'horizontal' or 'vertical'.")

        if direction == 'horizontal':
            if len(self.data) != len(other_img.data):
                # Resize images to have the same height
                min_height = min(len(self.data), len(other_img.data))
                self.data = self.data[:min_height]
                other_img.data = other_img.data[:min_height]

            combined_data = []
            for row_self, row_other in zip(self.data, other_img.data):
                if len(row_self) != len(row_other):
                    raise RuntimeError("Both images must have the same width when concatenating horizontally.")
                combined_row = row_self + row_other
                combined_data.append(combined_row)

            # Store the concatenated data in the instance attribute
            self.data = combined_data

        elif direction == 'vertical':
            if len(self.data[0]) != len(other_img.data[0]):
                # Resize images to have the same width
                min_width = min(len(self.data[0]), len(other_img.data[0]))
                for i in range(len(self.data)):
                    self.data[i] = self.data[i][:min_width]
                for i in range(len(other_img.data)):
                    other_img.data[i] = other_img.data[i][:min_width]

            if len(self.data[0]) != len(other_img.data[0]):
                raise RuntimeError("Both images must have the same width when concatenating vertically.")

            # Combine rows of both images
            combined_data = self.data + other_img.data

            # Store the concatenated data in the instance attribute
            self.data = combined_data

    def segment(self):
        # TODO remove the `raise` below, and write your implementation
        raise NotImplementedError()

