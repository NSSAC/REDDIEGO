# REDDIEGO

Associated Repositories:
* [Tranportation Module](https://github.com/nssac/quest)
* [Harvey Behavior Module](https://github.com/NSSAC/harvey_behavior_model)


## Overview
This repository contains the framework to organize and run the modules involved under the DARPA REDDIE project. Specifically, this includes the following modules:
- Transportation
- Communication
- Behavior

The model is time-stepped with each of the above modules getting executed 0 or more times per time-step. Each module will consume and generate data that itself or other modules have generated. The data exchange goes through CSV files across modules; a module may use other format internally, but must track this - to the extent possible, this should be avoided. 

Each module will specify the configuration (JSON format) that it needs when invoked. The configuration will have 3 general sections:
- parameters
   - REDDIE-GO parameters: the time-step/tick, the input/output directory;
   - A set of module-specific parameters in a file or as a section;
- an input file section
- an output file section

Later, possibly a separate module to manage statistical designs;

Example: behavior module needs output from comm module from iteration 4 in its own iteration 5 executation.

Storing of files: centrally have something like:

run_id/base/ (would be read-only)
      /tick_0/
      /tick_1/
      /tick_2/
      /tick_3/
      etc

Example:
  Behavior write person behavior data;
  Transportation reads person data from behavior, and generates routes/points;
  Communication reads transportation data;
  
Will use a solution with a common CSV file that is indexed on household with specified columnns from each of the modules; 
Will not be able to rely on a column order in the CSV;
Need a spec format for how modules declare their parameters; 
Option to have static files (e.g. with fixed person or household properties);

Modules must declare their interface: should this use frictionless?
name_input_1; itype_1
name_input_2; itype_2
..
name_output_1; otype_1
name_output_2; otype_2

This "central communication file" would be generated up front by the module owners. It will be provided in the /base directory. If it is named e.g. main_tick_i.csv, modules can access prior times steps;

Files private to modules must also be prepared in their base form; it will be their responsibility to update these files; REDDIE-Go will copy them forward;

As input, each module gets the 'run_id' directory. 

