int gcd(int x, int y) 
{ 
  x = x > 0 ? x : -x;
  y = y > 0 ? y : -y;
  if(x < 0 || y < 0){
	return 0;
  }
  if(!x){
    return y;
  }
  if(!y){
    return x;
  }
  while(x!=y)
  {
    if(x > y)
      x -= y;
    else
      y -= x;
  }
  return x;
}
