package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func sum(data []int) int {
	sum := 0
	for _, a := range data {
		sum += a
	}
	return sum;
}

func find_max(values []int) int {
	max := values[0]
	for _, v := range values {
		if (v > max) {
			max = v
		}
	}
	return max
}

func read_file(){
	path := "/home/looten/workspace/advent_of_code/2022/input_data.txt"
	// path := "/home/looten/workspace/advent_of_code/2022/test_data.txt"
	file, err := os.Open(path)
	check(err)

	defer file.Close()
	scanner := bufio.NewScanner(file)
    
	var values []int
	var tmp []int
	//idx := 0
    for scanner.Scan() {
		str := scanner.Text()
		if len(str) > 0 {
			// found value on row
			value, err := strconv.Atoi(str)
			check(err)
			tmp = append(tmp, value)
		} else {
			// empty row
			tot_sum := 0
			tot_sum = sum(tmp)
			values = append(values, tot_sum)
			values = append(values, -1)
			tmp = nil
		}
    }
	fmt.Println(find_max(values))
}

func main(){
	read_file()
}