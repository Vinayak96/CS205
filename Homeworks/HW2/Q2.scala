

object Q2{
def main(args: Array[String]) :Unit = {

val a = List(1,4,7,6,5,10)
val b = a.length/2
println(split(b,a))  }



def split(n: Int, l: List[Int]):(List[Int], List[Int]) = {
    def _split(c: Int, res: List[Int], rem: List[Int]):(List[Int],List[Int]) = (c, rem) match {
        case (_, Nil) => (res, Nil)
        case (0, rem) => (res, rem)
        case (c, h::tail) => _split(c - 1, res:::(List(h)), tail)
    }
    _split(n, List(), l)
}
}