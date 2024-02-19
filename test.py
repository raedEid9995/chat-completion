import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(size=100):
    """Generate an array of random numbers.
    
    Parameters:
    - size: int, optional (default=100)
        The number of random numbers to generate.
    
    Returns:
    - data: ndarray
        An array of random numbers.
    """
    data = np.random.rand(size)
    return data

def save_data_to_file(data, filename='dataset.txt'):
    """Save an array of data to a file.
    
    Parameters:
    - data: ndarray
        The array of numbers to save.
    - filename: str, optional (default='dataset.txt')
        The name of the file where data will be saved.
    """
    print("hello")
    np.savetxt(filename, data)

def load_data_from_file(filename='dataset.txt'):
    """Load data from a file into an array.
    
    Parameters:
    - filename: str, optional (default='dataset.txt')
        The name of the file to load data from.
    
    Returns:
    - data: ndarray
        The loaded array of numbers.
    """
    data = np.loadtxt(filename)
    return data

def calculate_statistics(data):
    """Calculate basic statistics of the dataset.
    
    Parameters:
    - data: ndarray
        The array of numbers to analyze.
    
    Returns:
    - stats: dict
        A dictionary containing the mean, median, and standard deviation of the data.
    """
    stats = {
        'mean': np.mean(data),
        'median': np.median(data),
        
    }
    return stats

def visualize_data(data):
    """Visualize the dataset using a histogram.
    
    Parameters:
    - data: ndarray
        The array of numbers to visualize.
    """
    plt.hist(data, bins=10, alpha=0.5)
    plt.title('Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Example usage:
if __name__ == "__main__":
    data = generate_random_data(100)
    save_data_to_file(data)
    loaded_data = load_data_from_file()
    stats = calculate_statistics(loaded_data)
    print(stats)
    visualize_data(loaded_data)
