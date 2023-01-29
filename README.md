# DataLibrary: A Python library to save data from applications

DataLibrary is a Python library that allows you to save and retrieve Python dictionaries to and from disk as JSON files. Each saved object is accessible via a unique string key. It is a good solution for anyone who needs a tool for saving data from their application with ease.

## Installation
DataLibrary can be installed using pip:

```
pip install DataLibrary
```

## Usage
Once DataLibrary has been installed, you can import it in your Python code and use it:
```
from DataLibrary import DataLibrary

# Initialize DataLibrary with the path to your data directory
data_library = DataLibrary('data/')

# Save a dictionary to disk
data_library.save('key', {'key': 'value'})

# Retrieve a dictionary from disk
data = data_library.retrieve('key')
print(data) # {'key': 'value'}
```

## Contribution
If you would like to contribute to DataLibrary, please fork the repository and create a pull request. 

## License
This project is licensed under the ...
