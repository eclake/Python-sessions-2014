
import numpy as np

def ConvertMicroJyToAbMag(flux):

    if hasattr(flux, '__len__'):
        if (type(flux) != np.ndarray):
            flux = np.array(flux)
            
        flux = flux * 1.E-23 * 1.E-6 # to erg/s/cm2/Hz
        positiveIdx = np.where(flux > 0)
        mag = np.array(flux) * 0. - 1
        mag[positiveIdx] = (-2.5) * np.log10(flux[positiveIdx]) - 48.56
    else:
        if flux > 0:
            mag = (-2.5) * np.log10(flux) - 48.56
        else:
            mag = -1
        
    return mag

def ConvertErrMicroJyToAbMag(fluxerr,flux):
    
    if hasattr(flux, '__len__'):
        if (type(flux) != np.ndarray):
            flux = np.array(flux)
            
        if hasattr(fluxerr, '__len__'):
            if (type(fluxerr) != np.ndarray):
                fluxerr = np.array(fluxerr)
                
        if (len(flux) != len(fluxerr)):
            return -1
        
        okIdx = np.where(flux != 0)
        magerr = np.array(flux) * 0. -1.
        magerr[okIdx] = 1.087 * fluxerr[okIdx] / flux[okIdx]
    else:     
        if (flux != 0):
            magerr = 1.087 * fluxerr / flux
        else:
            magerr = -1
            
    return magerr