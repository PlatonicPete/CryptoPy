###Base class for all exchange classes, can be customized to work with less common exchanges
import warnings

class Exchange:
    
    def __init__(self):
        self.whitelist = []#The whitelist of 4 letter symbols
    
    def get_ohlc():
        pass
    
    def pair_digest(self,pair):
        """
        A method for handling pair names input by user
        
        It deals with:
            1. Too long pair names, (excepting DASH)***XXX not yet implemented
            2. Non-uppercase pair names
        
        It returns the digested pair, and releases all required warnings.
        
        Returns:
            pair - digested pair
            
        """
        #stores the allowed 4 pairs
        
        #convert the paircode to all uppercase
        pair = pair.upper()
        
        #pair string length check
        if(len(pair)!=6):
            #Except DASH - others may be added later
            if(pair[:4] in self.whitelist or pair[3:7] in self.whitelist):
                if(len(pair)!=7):
                    warnings.warn("The pair length with DASH was not 7 characters! It will be truncated to 7.", RuntimeWarning)
                    pair = pair[0:7]
            else:
                warnings.warn("The pair length was not 6 characters! It will be truncated to 6.", RuntimeWarning)
                pair = pair[0:6]#truncate
        
        return pair
        