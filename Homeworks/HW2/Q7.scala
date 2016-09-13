

object Q7 {
  var result=1
  def fastPower( x:Int , n:Int): Int={
    if(n==0)
      return result
    else if(n%2==0)
    	{
    	result = fastPower(x,n/2)
    	return (result*result)
    	}
    else
      return ( x* fastPower(x,n-1))
}
}