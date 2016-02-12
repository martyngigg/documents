
class Point2D {
public:
  Point2D(double x, double y) : m_x(x), m_y(y) {}
  inline double x() const { return m_x; }
  inline double y() const { return m_y; }
  inline double norm2() const { return m_x*m_x + m_y*m_y; }
  private:
  double m_x, m_y;
};
