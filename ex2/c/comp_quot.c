int compute_quotient(int x, int y) 
{
  int quotient;
  quotient = y ? x / y : 2147583647;//in y==0, q = INT_MAX
  return quotient;
}
