import capture_results
capture_results.start()

import demographic_data_analyzer
from unittest import main
import traceback

program = None
runtime_error = None

try:
    demographic_data_analyzer.calculate_demographic_data()

    program = main(module="test_module", exit=False)

except Exception as e:
    runtime_error = e
    traceback.print_exc()

finally:
    capture_results.finish(program, runtime_error)