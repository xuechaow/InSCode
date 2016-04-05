# Data Computation Script
# run as: python3 average_degree.py <input_file_path> <output_file_path>
import time
import sys
import insight

start_time = time.time()

data_list = insight.i_load_data(sys.argv[1])
output_fp = open(sys.argv[2],'w')

window_heap = insight.Data_window()
for item in data_list:
	window_heap.update_heap(item)
	window_heap.update_graph()
	# uncomment to output 2-digit decimal with rounding up (5/3=1.67)
	# output_fp.write("%.2f\n" % window_heap.calculate_average_degree())
	# output 2-digit decimal without rounding up (5/3=1.66)
	avd = insight.i_2_digits(window_heap.calculate_average_degree())
	output_fp.write("%.2f\n" % avd)

output_fp.close()

print("Running time: %s seconds" % (time.time()-start_time))

	








