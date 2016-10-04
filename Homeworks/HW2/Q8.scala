object Q8 {
  def rotate(x:List[Int],l:Int): List[List[Int]]= {
    if (x==Nil)
      return Nil
    else if(l==1)
      return List(x)
    else
      return x :: rotate( (x.last :: x.init),l-1)
  }
  def Permutate(x:List[Int]):List[List[Int]]={
    def helper(x:List[Int],z:Int):List[List[Int]]={
      var y = rotate(x,x.length)
      if (z==0)
        return Nil
      else
        return (rotate(y.head.tail, y.head.tail.length).map(_ :+y.head.head))::: helper(y.last,z-1)
  }
    return helper(x,x.length)
    }
    
 }