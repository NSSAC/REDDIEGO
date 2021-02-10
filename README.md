# REDDIEGO

Associated Repositories:
* [Tranportation Module](https://github.com/nssac/quest)
* [Harvey Behavior Module](https://github.com/NSSAC/harvey_behavior_model)


## Overview
This repository contains the framework to organize and run the modules involved under the DARPA REDDIE project. Specifically, this includes the following modules:
- Transportation
- Communication
- Behavior

The overall model is time-stepped with each of the above modules getting executed 0 or more times per time-step. Each module will consume and generate data that itself or other modules have generated, updated or modified. The data exchange goes through a collection of common CSV files (modeled after a former database design). A module may additionally use private data which is to be managed as specified below. Common data will all be stored in CSV format; it is recommended that private data also be in CSV format to the extent that it makes sense;

## Data staging and data exchange between modules

Each instance of REDDIE-Go will have a run_id, and will use a storage diretory hierarchy like this:

```
run_id/base/ (would be read-only)
      /tick_0/
      /tick_1/
      /tick_2/
      /tick_3/
      etc
```
- Here run_id will be a fully qualifed path. 
- Modules should under no circumstance try to interpret the path and make assumptions on its structure. 
- The base/ directory will hold static files as well as a boot-strapped version of each dynamic file. 
- The REDDIE-Go staging module will at the start of the simulation copy all base files to the tick_0 directory. 
- Modules may access the directories tick_i. All files in in tick_i for i < current_tick are read_only. 



Each module will specify the configuration (JSON format) that it needs when invoked. The configuration will have 3 general sections:
- parameters
   - REDDIE-GO parameters: the time-step/tick, the input/output directory;
   - A set of module-specific parameters in a file or as a section;
- an input file section
- an output file section

Later, possibly a separate module to manage statistical designs;

Example: behavior module needs output from comm module from iteration 4 in its own iteration 5 executation.


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

This "central communication file" would be generated up front by the module owners. It will be provided in the /base directory. If it is named e.g. main.csv, modules can access prior times steps; may allow multiple common files;

Files private to modules must also be prepared in their base form; it will be their responsibility to update these files; REDDIE-Go will copy them forward;

As input, each module gets the 'run_id' directory. 

