# REDDIEGO

Associated Repositories:
* [Tranportation Module](https://github.com/nssac/quest)
* [Harvey Behavior Module](https://github.com/NSSAC/harvey_behavior_model)


## Overview
This repository contains the framework to organize and run the modules involved under the DARPA REDDIE project. Specifically, this includes the following modules:
- Transportation
- Communication
- Behavior

The overall model is time-stepped with each of the above modules getting executed 0 or more times per time-step. 


## File formats

Each module will consume and generate data that itself or other modules have generated, updated or modified. The data exchange goes through a collection of common CSV files (modeled after a former database design). A module may additionally use private data which is to be managed as specified below. Common data will all be stored in CSV format; it is recommended that private data also be in CSV format to the extent that it makes sense;

One of the common files will be household.csv. Module owner will in collaboration specify the variable/column names and their data types of each common file, and will then provide boot-strapped version(s) of this/these file(s) to be used in the base/ directory (see below). At a later stage, this step may become automated. This/these files will mimic a database table where fields are queried and updated as the modules are executed. Each common, dynamic file (e.g. household.csv) will minimally have columns run_id and tick, both of which will be updated by the REDDIE-Go framework. Note:

- The base/ directory may additionally contain static files. 
- Module cannot rely on a specific column order in CSV files.

In the preparation of boot-strap files, it will be useful if module owners create a spreadsheet specifying variable names, module interdependencies, read/write access, ticks from which it reads; it can only write to the current tick files. (May consider a frictionless specification)


## Data staging and data exchange between modules

Each instance of REDDIE-Go will have a run_id, and will use a storage directory hierarchy like this:

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

Thus at the start of the simulation, REDDIE-Go will stage all dynamic files into the tick_0 directory with updated run_id and tick number columns. 

## Module configuration files

Each module will specify a module-specific JSON configuration block. This configuration block will be inserted into a JSON file, and the latter will be provided to the module as a commandline argument. Addtionally, this JSON file will contain the keys:
- 'tick': the current tick which can be used to build the paths needed to access data;
- 'cwd': the current working directory; this directory will hold the current version of dynamic files (e.g. household.csv);

## Statistical designs

In a later stage, we will consider a REDDIE-Go module for constructing statistical design. This will require a specification for providing factors and levels using pointers into the per-module JSON configuration fragments.
  
