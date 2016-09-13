object Q8 {
  def interChange(x:Int, l:List[Int]):List[List[Int]] = l match { 
    case Nil => List(List(x))
    case (head::tail) => (x :: head :: tail) :: interChange(x, tail).map(head :: _)
}
  

  def permutationsGen(l:List[Int]):List[List[Int]] = l match {
    case Nil => List(List())
    case (head::tail) => for(p0 <- permutationsGen(tail); p1 <- interChange(head, p0)) yield p1
}
  def main(args: Array[String]): Unit = {
    var lst = List(1,2,3)
    println(permutationsGen(lst).distinct)
   
    }
    
    
   
  }