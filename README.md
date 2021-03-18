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

One of the common files will be household.csv. Module owner will in collaboration specify the variable/column names and their data types of each common file, and will then provide boot-strapped version(s) of this/these file(s) to be used in the base/dynamic directory (see below). At a later stage, this step may become automated. This/these files will mimic a database table where fields are queried and updated as the modules are executed. Each common, dynamic file (e.g. household.csv) will minimally have columns run_id and tick, both of which will be updated by the REDDIE-Go framework. Note:

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
- Here run_id will be the working directory. 
- Modules should under no circumstance try to interpret the path and make assumptions on its structure. 
- The base/ directory will hold static files as well as a boot-strapped version of each dynamic file. 
- The REDDIE-Go staging module will at the start of the simulation copy all files base/dynamic to the tick_0 directory. 
- Modules may access the directories tick_i. All files in in tick_i for i < current_tick are read_only. 

Thus at the start of the simulation, REDDIE-Go will stage all dynamic files into the tick_0 directory with updated run_id and tick number columns. 

## Module configuration files

Each module will specify a module-specific JSON configuration format. This configuration will be in a module specific JSON file ([example](https://github.com/NSSAC/REDDIEGO/blob/master/sample/CommandlineModule.json)). 

#### Commandline Module
This description is valid for any modules which are called via the commadline, i.e., the REDDIEGO [CommandlineModule](https://github.com/NSSAC/REDDIEGO/blob/master/REDDIEGO/CommandlineModule.py) will be used to interface with the module. The executable, the environment, and arguments for calling the module must be provided in a JSON file adhering to this [schema](https://github.com/NSSAC/REDDIEGO/blob/master/schema/CommandlineModule.json). Furthermore the following argument are provided when calling the module dependend on the operation mode
__start:__
```
   --mode start
   --startTick tick 
   --startTime time
   --status file
```
__step:__
```
   --mode step
   --lastRunTick tick 
   --lastRunTime time
   --currentTick tick 
   --currentTime time
   --targetTick tick 
   --targetTime time
   --status file
```
__end:__
```
   --mode end
   --lastRunTick tick 
   --lastRunTime time
   --endTick tick 
   --endTime time
   --status file
```    
Here `tick` refers to a possible negative integer and `time` refers to a floating point number. After successful execution REDDIEGO will expect the status file to include `success`. Any other change to the status file will be interpreted as failure. REDDIEGO does not rely on the return code to determine succesful execution since commands like sbatch will return but the scheduled job has not even started.

#### Python Modules
This description is valid for modules wich are implemented in python. These modules will be imported from REDDIEGO and executed within the REDDIEGO Python process. These Python modules must be derived from [AbstractModule](https://github.com/NSSAC/REDDIEGO/blob/master/REDDIEGO/AbstractModule.py). Examples for implementing such a module are [SampleModule](https://github.com/NSSAC/REDDIEGO/blob/master/REDDIEGO/SampleModule.py) and [CommandlineModule](https://github.com/NSSAC/REDDIEGO/blob/master/REDDIEGO/CommandlineModule.py). The content of the module specific JSON configuration file will be provided through the dictionary `self.data`.

#### Configuring REDDIEGO
To execute REDDIEGO one must provide one argument the configuration. In this directory one must minimaly provide a [REDDIEGO.json](https://github.com/NSSAC/REDDIEGO/blob/master/sample/REDDIEGO.json) and a [schedule.json](https://github.com/NSSAC/REDDIEGO/blob/master/sample/schedule.json) file. The files must adhere the [REDDIEGO schema](https://github.com/NSSAC/REDDIEGO/blob/master/schema/REDDIEGO.json) and the [Scheduler schema](https://github.com/NSSAC/REDDIEGO/blob/master/schema/Scheduler.json) respectively. 

## Statistical designs

In a later stage, we will consider a REDDIE-Go module for constructing statistical design. This will require a specification for providing factors and levels using pointers into the per-module JSON configuration fragments.
  
