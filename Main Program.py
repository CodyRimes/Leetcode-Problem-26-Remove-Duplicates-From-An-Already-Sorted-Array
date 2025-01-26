class Solution(object):
    print("An instance of our 'Solution' class has been called. This is coming from inside the solution class definition")

    def removeDuplicates(self, OriginalNumberArray):
        print(".removeDuplicates has successfully been called. This is coming from within the function declaration.")

        """
        :type nums: List[int]0
        :rtype: int

        Note to self:
        The three '"' quote python syntax allows multi-line block comments, in python referred to as a "doc-string"
        The ':type nums: List[int]' is a "type hint", i.e.  indicates that the parameter nums is expected to be a list of integers. In Python, type hints provide a way to specify the expected data type of variables, function parameters, and return values, which can improve code readability and help with static analysis tools.
        The ':rtype: int' is also a "type hint", i.e. indicates that the return type of the function is expected to be an integer

        Essentially:
        This function takes a list of integers and returns an integer.
        """

        # What I plan on doing here is since the incoming array we take in this function
        # is already sorted in acsending order, we can assume duplicates happen right after
        # we identify the value of the first item we are looking at. Thus if we use a two pointer
        # method we can use one to iterate through the array one by one, and in a nested loop
        # as we use the first pointer to identify the value we are at, we can use a 2nd pointer to
        # look beyond the index that the first pointer is at to identify any duplicates. Once the
        # 2nd pointer is at a value that is not a duplicate to the value of index the first pointer
        # is at, we can set the first pointer to the index the 2nd pointer had moved to. Thus the
        # first pointer will add the value of the index it is at into a new 2nd array, and the 2nd
        # pointer goes ahead to find the next unique/non-duplicate value in the array.
        # You can think of the first pointer as a brute force pointer that would walk through
        # the whole array (if not helped by the 2nd pointer or if the incoming array is full of)
        # unique/non-dublicate ascending values) and the 2nd pointer at each iteration the first pointer
        # is at walks ahead of the 1st pointer to find the next unnique/non-duplicate value. Once
        # the 2nd pointer finds a non-duplicate value, the first pointer is set to the position of
        # the 2nd pointer/skips ahead to where the 2nd pointer is and skips all duplicate values.
        # Thus by this logic no duplicate values should be pushed to the new array of non-duplicate
        # values we are making

        # This would probably be a good example of why we read documentation first. I started out
        # thinking this problem would be solved but us receiving an array and us returning a 2nd, NEW array
        # that meets the problem specifications of removing all duplicates in the original array and returning
        # the NEW array in ascending order with no duplicates. THIS IS NOT THE CASE!!! THIS IS A LEARNING
        # POINT OF WHY WE READ DOCUMENTATION.
        # This problem will be solved by modifying the ARRAY IN PLACE. NO NEW, 2ND ARRAY WILL BE CREATED.
        # However we will still use the same logical process of using two pointers for the meat of solving this problem, however
        # it will be somewhat different since we will not be using a 2nd fresh array but will instead be using the same array
        # we were given/passed to the function and modifying it in place.
        # It is also very important to note that instead of returning back the array we modified in place, we are simply
        # returning the number/count of unique values left in the array after our function modifies it in place

        #Here is some of the problem definition:
        #Consider the number of unique elements of an array to be k, to get accepted, you need to do the following things:

        # Change the array, which we will call nums, such that the first k elements of nums contain the unique elements in the order
        # they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

        # How I plan on solving this problem is using a 2 pointer method.

        # Lets first cover the condition that in the event we receive an empty array, there is automatically no duplicates so we can return that there are zero
        # duplicate elements
        if len(OriginalNumberArray) == 0:
            print("The input array is empty. There can't possibly be any duplicates in this array if there are none")
            return 0;

        # Covering the condition that in the event we receive size one array, there is automatically only 1 unique value, so return 1
        # duplicate elements
        if len(OriginalNumberArray) == 1:
            print("The input array is of only size 1. There can only be one non-duplicate value in this array")
            return 1;

        #We will need a counter for each time the 2nd pointer encounters a unique, non-duplicate value
        CountOfUniqueNonduplicateValues = 0

        # If the input array is not an empty array or size 1 array we can,
        # Declaring our first pointer to be set to the beginning of the array
        MyFirstPointerAtIndex = 0

        # Declaring our second pointer to be set to the index right after our first pointer is set to
        MySecondPointerAtIndex = 1

        # We will need to check if the starting positions of the two pointers are equal to each other, if they're not equal in value
        # then we know we have found a non-duplicate, and must move our pointer positions in order to start off our while loop(???? CHECK THIS LOGIC)
        if OriginalNumberArray[MyFirstPointerAtIndex] != OriginalNumberArray[MySecondPointerAtIndex]:
            print("From the starting positions of our pointers we have found a non-duplicate. We will need to overwrite the position of Pointer1 + 1, then move our Pointer1 to that position, and and then advance the 2nd pointer to seek out another non-duplicate")
            #We will need to update our counter here since we've found a non-duplicate, unique value
            #The below python convention is the same as writing CountOfUniqueNonduplicateValues = CountOfUniqueNonduplicateValues + 1
            CountOfUniqueNonduplicateValues += 1
            # We need to overwrite the position just ahead of the 1st pointer to the value the 2nd pointer found as a non-duplicate
            OriginalNumberArray[MySecondPointerAtIndex + 1] = OriginalNumberArray[MySecondPointerAtIndex]
            # Then we need to advance the 1st pointer to that Pointer1 + 1 position so we can accurately compare against the 2nd pointer's value so we can find another non-duplicate
            MyFirstPointerAtIndex = MyFirstPointerAtIndex + 1

        # Now lets compare the values of both values at the respective indexes the pointers are initially pointing at (index[0] and index[1]
        # respectively)
        while OriginalNumberArray[MyFirstPointerAtIndex] == OriginalNumberArray[MySecondPointerAtIndex]:
            print("There is a duplicate between where the first pointer is and where the 2nd pointer is, advancing the 2nd pointer to look for a non-duplicate")
            # We must first see if advancing the 2nd pointer will get us to go out of scope of the array, so we need to prevent that
            # Lets do some conditional statements to see what advancing the 2nd pointer will do
            if MySecondPointerAtIndex < len(OriginalNumberArray):
                print("Before we have advanced our 2nd pointer, we are inbounds inside the array")
            if MySecondPointerAtIndex + 1 < len(OriginalNumberArray):
                print("Checking to see if advancing our 2nd pointer will be inbounds. Right now it is. ")
            else:
                print("Hypothetically advancing the 2nd pointer will put the 2nd pointer out of bounds and create an error. We have reached that point here")
                return CountOfUniqueNonduplicateValues
            #Advancing the 2nd pointer one step at a time through the array until we find a non-duplicate value with our first pointer
            #Note that when debugging this code on January 25th 2025 I found this line as: MySecondPointerAtIndex += MySecondPointerAtIndex
            #That would be adding the variable value to the variable value itself, thus I was getting a doubling affect that the 2nd pointer was moving at, when it should have been walking through the array 1 step at a time
            #This is the pythonic code I was going for: MySecondPointerAtIndex += 1
            #Instead I will not be doing it the pythonic way, but I will be making this code as verbose and as easy to ready as possible (for me),
            #so I am changing it back to the way I think looks best/most descriptive
            MySecondPointerAtIndex = MySecondPointerAtIndex + 1

            #Check to see if we've reached a non-duplicate number in comparision with the 1st pointer's value after advancing the 2nd pointer
            if OriginalNumberArray[MyFirstPointerAtIndex] != OriginalNumberArray[MySecondPointerAtIndex]:
                print ("Our 2nd pointer has found a non-duplicate! We must now set the position of FirstPointer + 1 equal to what the 2nd pointer has found, and move our 1st Pointer to that new position (FirstPointer + 1)")
                # We will need to update our counter here since we've found a non-duplicate, unique value
                # The below python convention is the same as writing CountOfUniqueNonduplicateValues = CountOfUniqueNonduplicateValues + 1 in C++
                CountOfUniqueNonduplicateValues += 1
                #The position just ahead of our first pointer needs to be overwritten with the value our 2nd pointer found
                OriginalNumberArray[MyFirstPointerAtIndex + 1] = OriginalNumberArray[MySecondPointerAtIndex]
                #We then need to advance our first pointer to the position just ahead of it (the position we just overwrote) so we can compare it with the 2nd pointer
                MyFirstPointerAtIndex = MyFirstPointerAtIndex + 1
                # Do not need this line twice as it's in the outter loop
                # MySecondPointerAtIndex += MySecondPointerAtIndex

        return CountOfUniqueNonduplicateValues

#Creating a main area for the program to run
def main():
    # Test cases go here
    # Declare an empty array, should return 0 unique values, as there are no values in this array
    testEmptyArray = []
    # Declare an array of size 1, should return 1, as there can only be 1 unique value
    testSizeOfSizeOneArray = [1]
    # Declare edge case arrays:

    # Should return 1 as while there is 3 values in the array, they are all the same, thus there is really only 1 unique value
    testAllDuplicatessSameValueTestArray = [1, 1, 1]
    # Should return 10 as while there are a total of 20 values in the array, each value has a copy of itself, thus only leaving 10 real unique values
    testAllDuplicatesMultipleValuesTestArray = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    # Should return 10 as there are 10 completely unique values in the array with no duplicates
    testNoDuplicatesTestArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Here are the test arrays we will be using for this program")
    print("First our empty array (this should return 0): ")
    print(testEmptyArray)
    print("Then our size of 1 array (this should return 1): ")
    print(testSizeOfSizeOneArray)
    print("Next we will be doing an array full of 1's, three to be exact: ")
    print(testAllDuplicatessSameValueTestArray)
    print("Next we will be testing an array with one duplicate of each number in the array, the set of numbers being 1 through 10: ")
    print(testAllDuplicatesMultipleValuesTestArray)
    print("Then an array with no duplicates in it: ")
    print(testNoDuplicatesTestArray)

    #Create an instance of the solution class, should we be passing the arrays here?
    print("Creating a instance of our solution class right now")
    OurInstanceOfTheSolutionClass = Solution()

    #Now we must use the function we built in the Solution class to actually give us the solution to the problem, i.e.
    #the number of unique values our function finds in the array we pass in to the class
    print("Calling our function that is attached to the solution class several times for each test array we made. This will return the number of unique values that it finds for each array passed in")
    print("I will print the capture variables accordingly after")
    captureVariableForOurEmptyArray = OurInstanceOfTheSolutionClass.removeDuplicates(testEmptyArray)
    captureVariableForSizeOfOneArray = OurInstanceOfTheSolutionClass.removeDuplicates(testSizeOfSizeOneArray)
    captureVariableForAllDuplicatesSameValueArray = OurInstanceOfTheSolutionClass.removeDuplicates(testAllDuplicatessSameValueTestArray)
    captureVariableForAllDuplicatesMultipleValuesArray = OurInstanceOfTheSolutionClass.removeDuplicates(testAllDuplicatesMultipleValuesTestArray)
    captureVariableForNoDuplicatesTestArray = OurInstanceOfTheSolutionClass.removeDuplicates(testNoDuplicatesTestArray)

    print("Now that I have captured all the return values that each function call has produced, here are the results for each test array")
    print("In our testEmptyArray, we have: ", captureVariableForOurEmptyArray , "unique values")
    print("In our testSizeOfSizeOneArray, we have: ", captureVariableForSizeOfOneArray , "unique values")
    print("In our testAllDuplicatessSameValueTestArray, we have: ", captureVariableForAllDuplicatesSameValueArray , "unique values")
    print("In our testAllDuplicatesMultipleValuesTestArray, we have: ", captureVariableForAllDuplicatesMultipleValuesArray , "unique values")
    print("In our testNoDuplicatesTestArray, we have: ", captureVariableForNoDuplicatesTestArray , "unique values")


#You may need to refresh yourself on this, but as I understand it in Python any file ran directly on the IDE
#runs as "main", and if you have a function called main() such as I've done above, simulating C++ functionality/coding style,
#you will need to put a function call to your main() function when running the file itself, which will automatically/by standard is named "main"

if __name__ == "__main__":
    main()
