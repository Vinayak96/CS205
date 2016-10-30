import scala.io._
object Q1Hw3{
  class Queue(var q:List[Any]) {
    def Enque(x:Any)={
      val y=List(x)
      q = q:::y
    }
    def Deque() = {
      if(q==Nil)
        println("empty Queue")
      else
        q = q.tail
    }
  
    def equals(that: Queue): Boolean={
      (this.q, that.q) match{
        case (Nil, Nil) => true
        case (hd1::rest1, hd2::rest2) => (hd1.equals(hd2)) && (rest1.equals(rest2))
        case _ => false
        }
      }
    override def hashCode(): Int={
      var mult: Int=1
      this.q.foreach{
      mult*=_.hashCode()
      }
      mult
      }
  }
  
  def main(args: Array[String]){
    println("Enter element to be added:")
    val add= scala.io.StdIn.readLine()
    val obj=new Queue(Nil)
    obj.Enque(add)
    println(obj.q)
    }
 }