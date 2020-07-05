package Go

import "strconv"

func add(param1 int, param2 int) int {
	sum := param1 + param2
	return sum

}

func centuryFromYear(year int) int {
	if year % 100 == 0{
		return year/100
	}
	return (year/100) + 1
}

func checkPalindrome(inputString string) bool {

	reversed:= ""
	for i:= len(inputString)-1; i >= 0; i-- {
		reversed=  reversed + string(inputString[i])
	}
	return reversed == inputString

}

func adjacentElementsProduct(inputArray []int) int {
	largestProduct:= -999

	for i:=0; i< len(inputArray)-1; i++{
		pair_product:= inputArray[i] * inputArray[i+1]
		if pair_product> largestProduct{
			largestProduct = pair_product
		}

	}

	return largestProduct


}


func shapeArea(n int) int {
	result:= 1
	for i:=0; i<n; i++{
		result += i*4
	}
	return result



}


func makeArrayConsecutive2(statues []int) int {
	max:= statues[0]
	min:= statues[0]

	for i, element:= range statues{
		if max < element{
			max = element
		}

		if min > element{
			min = element
		}
	}

	return max-min + 1 - len(statues)

}

func almostIncreasingSequence(sequence []int) bool {
	if checkSequence(sequence){
		return true
	}
	var miss int = 0

	for i:= range sequence{
		if i == len(sequence)-1{
			break
		}
		if sequence[i] > sequence[i+1]{
			miss = i
		}

	}

	length:= len(sequence)
	if checkSequence(sequence) == false{
		for i:=miss; i< len(sequence); i++ {
			var temp = make([]int,length)
			copy(temp[:], sequence)

			temp = append(temp[:i], temp[i+1:]...)
			if checkSequence(temp) == true {
				return true
			}
			temp = sequence

		}
		return false
	}

	return true

}
func checkSequence(sequence []int ) bool {
	for i:=0; i < len(sequence)-1; i++ {
		if sequence[i] >= sequence[i+1] {
			return false
		}
	}
	return true
}

func matrixElementsSum(matrix [][]int) int {

	sum := 0
	for x := 0; x < len(matrix[0]); x++ {
		for y := 0; y < len(matrix) && matrix[y][x] != 0; y++ {
			sum += matrix[y][x]
		}
	}

	return sum
}

func allLongestStrings(inputArray []string) []string {
	var result = make([]string, 0)

	var max int
	for i:=0; i< len(inputArray); i++{
		if max < len(inputArray[i]){
			max = len(inputArray[i])
		}
	}
	for i:=0; i< len(inputArray); i++{
		if len(inputArray[i]) == max{
			result = append(result, inputArray[i])
		}
	}


	return result

}

func commonCharacterCount(s1 string, s2 string) int {
	count := 0
	seen := make(map[rune]int)
	for _, e := range s1 {
		seen[e]++
	}

	for _, e := range s2 {
		if seen[e] > 0 {
			seen[e]--
			count++
		}
	}
	return count

}


func isLucky(n int) bool {
	var nString string = strconv.Itoa(n)
	var firstHalf string = nString[:len(nString)/2]
	var secondHalf string = nString[len(nString)/2:]

	sum1:=0
	sum2:=0
	for i:=0; i< len(nString)/2; i++{
		sum1+= toInt(string(firstHalf[i]))
		sum2+= toInt(string(secondHalf[i]))
	}

	return sum1 == sum2

}

func toInt(numS string) int{
	num, _:= strconv.Atoi(numS)
	return num
}




func main() {

}
