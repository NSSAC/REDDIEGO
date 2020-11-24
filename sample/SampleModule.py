# BEGIN: Copyright 
# Copyright (C) 2020 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

from REDDYGO.ModuleWrapper import ModuleWrapper
# from REDDYGO.REDDYGO import REDDYGO
 

class SampleModule(ModuleWrapper):
    
    def _init(self):
        self.schema = {}
        
        self.data = self.REDDYGO.getConfiguration().loadJsonFile("SampleModule/config.json", self.schema)
        return
        
    def _start(self, startTick, startTime):
        return True
        
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        return True
        
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        return True
        