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
- parameters (including the time-step, the output directory, module-specific parameters that may enter a statistical design)
- an input file section
- and output file section

The input and output sections also serve to specify the staging that REDDIE-GO will conduct when invoking the modules. 
