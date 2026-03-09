import capture_results  # ✅ new
capture_results.start()  # ✅ new (start capture)

import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
program = main(module="test_module", exit=False)  # ✅ new: capture program
capture_results.finish(program)                  # ✅ new: write results