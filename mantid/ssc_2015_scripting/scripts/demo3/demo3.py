"""Demo simple reduction script. - Adapted from HRPD system test

Uses matplotlib plotting
"""
from mantid.simpleapi import *
from matplotlib.pyplot import *

####################################################################
# Script Variables
####################################################################
inst_prefix="HRP"
vanadium_run=39191
vanadium_peaks=[(19970,20140), (39970,40140),(59970,60140),(79970,80140),(99970,100140)]
calib_file="hrpd_new_072_01_corr.cal"

####################################################################
# Reduction
####################################################################

# Load + mask peaks
vanadium = Load(Filename=inst_prefix + str(vanadium_run) + ".RAW")
for xmin, xmax in vanadium_peaks:
    vanadium = MaskBins(Inputworkspace=vanadium, XMin=xmin, XMax=xmax)

# Align & normalise
vanadium = AlignDetectors(InputWorkspace=vanadium,CalibrationFile=calib_file)
vanadium = NormaliseByCurrent(InputWorkspace=vanadium)

# Correct for solid angle
van_solid_angle = SolidAngle(InputWorkspace=vanadium)
vanadium = Divide(LHSWorkspace=vanadium, RHSWorkspace=van_solid_angle)

# Focus
vanadium=ConvertUnits(InputWorkspace=vanadium,Target="dSpacing")
vanadium=DiffractionFocussing(InputWorkspace=vanadium,GroupingFileName=calib_file)

# Plot
x0 = vanadium.readX(0)
x0pts = 0.5*(x0[1:] + x0[:-1])
x1 = vanadium.readX(1)
x1pts = 0.5*(x1[1:] + x1[:-1])
x2 = vanadium.readX(2)
x2pts = 0.5*(x2[1:] + x2[:-1])
plot(x0pts, vanadium.readY(0), 'k-', label="vanadium-sp-1")
plot(x1pts, vanadium.readY(1), 'r-', label="vanadium-sp-2")
plot(x2pts, vanadium.readY(2), 'g-', label="vanadium-sp-3")
title("Focussed HRPD Vanadium (Run %d)" % vanadium_run)
grid('on')
xlim(0,5)
yscale('log')
legend()
show()
