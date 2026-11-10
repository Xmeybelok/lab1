"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data):
    matrices, vectors = data.matrices, data.vectors
    total = matrices[0] @ vectors[0]

    for i in range(1, len(matrices)): total = total + (matrices[i] @ vectors[i])
    return total


def binarize(data):
    matrix, threshold = data.matrix, data.threshold
    return np.where(matrix > threshold, 1, 0)


def unique_rows(data):
    matrix = data.matrix
    result = []

    for i in range(len(matrix)):
        unique_elements = np.unique(matrix[i])
        result.append(list(unique_elements))

    return result


def unique_columns(data):
    matrix = data.matrix
    result = []
    num_cols = matrix.shape[1]

    for i in range(num_cols):
        unique_elements = np.unique(matrix[:, i])
        result.append(list(unique_elements))

    return result


def matrix_statistics(data):
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    
    np.random.seed(seed)
    matrix = np.random.normal(loc=mean, scale=std, size=(rows, columns))
    
    return MatrixStatistics(
        matrix=matrix,
        row_means=np.mean(matrix, axis=1),
        column_means=np.mean(matrix, axis=0),
        row_variances=np.var(matrix, axis=1),
        column_variances=np.var(matrix, axis=0)
    )


def chess(data):
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    matrix = np.empty((rows, columns))

    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0: matrix[i, j] = first
            else: matrix[i, j] = second

    return matrix


def draw_rectangle(data):
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    for i in range(3):
        image[:, :, i] = background_color[i]
        
    cy = image_height // 2
    cx = image_width // 2
    
    y_start = cy - height // 2
    y_end = cy + height // 2 + height % 2
    x_start = cx - width // 2
    x_end = cx + width // 2 + width % 2
    
    for y in range(max(0, y_start), min(image_height, y_end)):
        for x in range(max(0, x_start), min(image_width, x_end)):
            image[y, x] = shape_color

    return image


def draw_ellipse(data):
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    cy = (image_height - 1) / 2.0
    cx = (image_width - 1) / 2.0
    
    for y in range(image_height):
        for x in range(image_width):
            formula = ((x - cx) ** 2) / (semi_axis_x ** 2) + ((y - cy) ** 2) / (semi_axis_y ** 2)
            if formula <= 1.0:
                image[y, x] = shape_color
            else:
                image[y, x] = background_color
                
    return image


def analyze_time_series(data):
    values, window = data.values, data.window
    series = np.array(values)
    mean = float(np.mean(series))
    variance = float(np.var(series))
    std = float(np.std(series))
    local_maxima_indices = []
    local_minima_indices = []
    moving_average = []

    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            local_maxima_indices.append(i)
        if series[i] < series[i-1] and series[i] < series[i+1]:
            local_minima_indices.append(i)

    for i in range(len(series) - window + 1):
        current_sum = 0.0
        for j in range(window): current_sum = current_sum + series[i + j]
        moving_average.append(current_sum / window)
        
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std,
        local_maxima_indices=local_maxima_indices,
        local_minima_indices=local_minima_indices,
        moving_average=np.array(moving_average)
    )


def one_hot(data):
    labels, class_count = data.labels, data.class_count
    
    if class_count is None:
        max_val = labels[0]
        for val in labels:
            if val > max_val: max_val = val
        class_count = int(max_val) + 1
        
    result = np.zeros((len(labels), class_count), dtype=int)

    for i in range(len(labels)):
        class_index = int(labels[i])
        result[i, class_index] = 1

    return result