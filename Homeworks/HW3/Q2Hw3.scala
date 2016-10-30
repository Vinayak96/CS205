

object Q2Hw3 {
  def split(lst:List[Int]):(List[Int],List[Int])={
    var lst1 : List[Int]= List()
    var lst2 : List[Int]= List()
    var ls = lst
    var x = true
    while(x)
    {
      if(ls==Nil)
        x=false
      else if(List(ls.head)== ls)
      {
        lst1= lst1 :+ (ls.head)
        x=false
      }
      else
      {
        lst1=ls.head :: lst1
        lst2=ls.last :: lst2
        ls = ls.tail.init
      }
        
    }
    return (lst1.reverse,lst2)
  }
}