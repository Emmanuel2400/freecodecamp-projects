# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main





print(mean_var_std.calculate([2,2,2,3,4,5,2,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)