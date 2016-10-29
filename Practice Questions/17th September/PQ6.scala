

object PQ6 {
  def check(x:List[Any], y:List[Any]): Boolean ={
    def helper(x:List[Any], y:List[Any],s:Int): Boolean={
      if(s==0)
        return true
      else if(x==Nil)
        return false
      else if(x.head == y(y.length-s))
        helper(x.tail,y,s-1)
      else
        helper(x.tail,y,y.length)
    }
    return helper(x,y,y.length)
  }
}

/**if(x==Nil)
  return false
else if(x.head==y.head)
  if(x.head==x.last)
    return true
  else if(x.tail.head==y.tail.head)
    return true
else if(x.head!=y.head)
  check(x.tail,y)*/