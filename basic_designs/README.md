# Running a ghdl design and test bench 

* `$ ghdl -a <file_name>.vhd`           // Compile the <file_name> implementation
* `$ ghdl -a <file_name>_tb.vhd`        // Compile the testbench
* `$ ghdl -e <file_name>_tb`            // Elaborate the testbench
* `$ ghdl -r <file_name>_tb --wave=wave.ghw`  // Run the simulation and generate a waveform file
