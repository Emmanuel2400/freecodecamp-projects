# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
import demographic_data_analyzer
import medical_data_visualizer
from unittest import main


print(mean_var_std.calculate([2,2,2,3,4,5,2,7,8]))


# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)
