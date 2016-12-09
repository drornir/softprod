int compute_remainder(int x, int y) 
{
  int remainder;
  remainder = y ? x % y : 0;
  return remainder;
}
