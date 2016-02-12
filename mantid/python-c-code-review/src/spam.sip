// filename: spam.sip
%Module spam
class Point2D {
%TypeHeaderCode
#include "Point2D.h"
%End
public:
  Point2D(double x, double y);
  double norm2() const;
  double x
  {
    %GetCode
    sipPy = PyFloat_FromDouble(sipCpp->x());
    %End
    %SetCode
    sipErr = 1;
    %End
  };
};
