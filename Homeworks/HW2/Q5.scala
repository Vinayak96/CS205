

object Q5 {
  def pivotSort(x:List[Int], n: Int): List[Int]={
    if(x== Nil)
      x:+n
    else if(x.head<=n)
      x.head +: pivotSort(x.tail, n)
    else
        pivotSort(x.tail, n) :+ x.head
  }
  
}