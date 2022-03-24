import Foundation

/*
 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

 Increment the large integer by one and return the resulting array of digits.
 */

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        // if the array is empty, return an empty array
        // Need the last element in the array
        guard let last = digits.last else { return digits }
        
        var mutableDigits = digits
        
        // if it's 9
        if last == 9 {
            // Prepare to call this function again for the rest of
            // the array, except for the last element
            mutableDigits.removeLast()
            
            // If 9 was the only element, return 10
            if mutableDigits.isEmpty {
                return [1, 0]
            }
            
            // Save that new array in property
            var reducedDigits = plusOne(mutableDigits)
            // append 0 at the end of the new array
            reducedDigits.append(0)
            // return new array
            return reducedDigits
        } else {
            // increment the last integer by 1
            let updatedLast = last + 1
            mutableDigits.removeLast()
            mutableDigits.append(updatedLast)
            // return the array
            return mutableDigits
        }
    }
}

let s = Solution()
//let x = s.plusOne([4,3,2,1])
//let x = s.plusOne([9, 9])
let x = s.plusOne([4,3,2,1])
print(x)
