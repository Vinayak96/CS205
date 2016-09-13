

object Q4 {
  def insertionSort(x : List[Int]): List[Int]={
    if (x== Nil)
      Nil
    else
      Q3.sortInsert(insertionSort(x.tail), x.head)
      
  }
}