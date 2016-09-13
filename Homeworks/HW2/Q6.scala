

object Q6 {
def quickSort(l: List[Int]): List[Int] = l match {
    case Nil => Nil
    case head :: tail => {
        val (low, high) = tail.partition(_ < head)
        quickSort(low) ::: head :: quickSort(high)
    }
}}