

object Q3 {
  def sortInsert( x:List[Int] ,n:Int): List[Int]={
    if(x.isEmpty || n<=x.head)
      n :: x
    else
     x.head:: sortInsert(x.tail , n)
  }
}