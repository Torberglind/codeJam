# codeJam
Solution for Codejam 2016 Problem A - Counting Sheep
Author: Tor Berglind

For an arbitary number we evaluate which digits it consists of and add them to the array found_digits.
By first initialising an empty array found_digits where we later will add values found evaluating the multiples of the
input number.
Then having a for-loop from 1 - 1000 to loop through up to 1000 multiples of the input number (I asume we found the
desired results by then). For each multiple we make a check for each digit if it already has been found, if so
we add it to the found_digits array. If the length of the array is 10, i.e. if all digits 0-9 has been found we return
current multiple. if the for-loop from 1-1000 finishes all the digits can't be found and we return 'INSOMNIA'.