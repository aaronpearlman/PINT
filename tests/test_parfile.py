#! /usr/bin/env python
import sys,os
import pint.models as tm

testdir=os.path.join(os.getenv('PINT'),'tests');
parfile = os.path.join(testdir,'J1744-1134.basic.par')

TestModel = tm.generate_timing_model("TestModel",(tm.Astrometry,tm.Dispersion,tm.SolarSystemShapiro,tm.Spindown))
m = TestModel()

print "model.param_help():"
m.param_help()
print

print "calling model.read_parfile():"
m.read_parfile(parfile)
print

print "print model:"
print m
print

print "model.as_parfile():"
print m.as_parfile()
print
