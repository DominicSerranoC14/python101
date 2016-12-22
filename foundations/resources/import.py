# Syntax for importing modules
import humansizes;

# Print the __name__ prop of the imported module
print(humansizes.__name__)

# Print the doc string of the imported module
print(humansizes.__name__.__doc__)

# Execute methods from the module
print(humansizes.approximate_size(16384, False))
