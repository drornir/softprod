int reverse(int x) 
{
	
	int reversedNumber = 0, remainder;
	int upper_bound = (1 << 30);
	int lower_bound = (1 << 31);

	while(x != 0)
	{
		remainder = x%10;
		if(reversedNumber < lower_bound/10 || reversedNumber > upper_bound/10) return 0;
		reversedNumber = reversedNumber*10 + remainder;
		x /= 10;
	}

	return reversedNumber;

}


