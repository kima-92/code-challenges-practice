import Foundation

/*
 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

 Increment the large integer by one and return the resulting array of digits.
 */

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        // if the array is empty, return an empty array
        
        // Need the last element in the array
            // if it's 9
                // call this function again for the rest of the array,
                // except for the last element
                // save that new array in property
                // append 0 at the end of the new array
                // return new array
            // else
                // increment the last integer by 1
                // return the array
        
        // TODO: - Delete
        return []
    }
}
