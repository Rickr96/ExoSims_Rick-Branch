# -*- coding: utf-8 -*-
import numpy as np

class PostProcessing(object):
    """Post Processing class template
    
    This class contains all variables and functions necessary to perform 
    Post Processing Module calculations in exoplanet mission simulation.
    
    Args:
        \*\*specs:
            user specified values
            
    Attributes:
        FAP (float):
            False Alarm Probability
        MDP (float):
            Missed Detection Probability
            
    """
    
    _modtype = 'PostProcessing'

    def __init__(self, **specs):
        # default values
        # false alarm probability
        self.FAP = 0.01/1000. 
        # missed detection probability
        self.MDP = 0.001 
        # replace default values with user specification values if any
        atts = self.__dict__.keys()
        for att in atts:
            if att in specs:
                setattr(self, att, specs[att])
        # initialize values updated by functions
        # set values derived from quantities above
        
    def __str__(self):
        """String representation of Post Processing object
        
        When the command 'print' is used on the Post Processing object, 
        this method will return the values contained in the object"""

        atts = self.__dict__.keys()
        
        for att in atts:
            print '%s: %r' % (att, getattr(self, att))
        
        return 'Post Processing class object attributes'
        
    def det_occur(self, observationPossible):
        """Determines if a detection has occurred and returns booleans 
        
        This method returns three booleans: FA (False Alarm), DET (DETection), 
        and MD (Missed Detection) where True gives the case.
        
        Args:
            observationPossible (ndarray):
                1D numpy ndarray of booleans signifying if each planet is 
                observable
        
        Returns:
            FA, DET, MD, NULL (bool, bool, bool, bool):
                False Alarm boolean, Detection boolean, Missed Detection boolean,
                Null detection boolean
        
        """
        
        FA, DET, MD, NULL = False, False, False, False
        
        if np.any(observationPossible):
            r0 = np.random.rand()
            if r0 <= self.MDP:
                MD = True
            else:
                DET = True
        else:
            r1 = np.random.rand()
            if r1 <= self.FAP:
                FA = True
            else:
                NULL = True
        
        return FA, DET, MD, NULL