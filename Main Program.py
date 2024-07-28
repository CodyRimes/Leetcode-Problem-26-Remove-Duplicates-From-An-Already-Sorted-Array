class Solution(object):

    #Test cases go here
    #Declare an empty array, should
    #Declare an array of size 1
    #Declare edge case arrays
    def removeDuplicates(self, OriginalNumberArray):
        """
        :type nums: List[int]
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

        # Lets first cover the condition that in the event we receive an empty array, there is automatically no duplicates so we can return that array
        if len(OriginalNumberArray) == 0 | 1:
            print(
                "The input array is empty or a size of 1 (only one element), returning the same array as there are no duplciates in this array")
            return OriginalNumberArray

        # If the input array is not an empty array,
        # Declaring our first pointer to be set to the beginning of the array
        MyFirstPointerAtIndex = 0

        # Declaring our second pointer to be set to the index right after our first pointer is set to
        MySecondPointerAtIndex = 1

        # Declaring an empty 2nd array that will contain all unique values/non-duplicate values in ascending order
        MyArrayOfNonDuplicates = []

        # Since the input array is not empty, we will always have to put the first element in the array into the non-duplicate array
        # since this is the first numebr we see?
        MyArrayOfNonDuplicates.append(OriginalNumberArray[MyFirstPointerAtIndex])

        # We will need to check if the starting positions of the two pointers are equal to each other, if they're not equal in value
        # then we know we have found a non-duplicate, and must move our pointer positions in order to start off our while loop(???? CHECK THIS LOGIC)
        if OriginalNumberArray[MyFirstPointerAtIndex] != OriginalNumberArray[MySecondPointerAtIndex]:
            print(
                "From the starting positions of our pointers we have found a non-duplicate. Adding this value to our non-duplicate array, and advancing the 2nd pointer to seek out another non-duplicate")
            # Appending the value we found to our non-duplicate array
            MyArrayOfNonDuplicates.append(OriginalNumberArray[MySecondPointerAtIndex])
            # Setting our first pointer equal to the position value of the 2nd pointer
            MyFirstPointerAtIndex = MySecondPointerAtIndex
        # Now lets compare the values of both values at the respective indexes the pointers are initially pointing at (index[0] and index[1]
        # respectively)
        while OriginalNumberArray[MyFirstPointerAtIndex] == OriginalNumberArray[MySecondPointerAtIndex]:
            print(
                "There is a duplicate between where the first pointer is and where the 2nd pointer is, advancing the 2nd pointer to look for a non-duplicate")
            # We must first see if advancing the 2nd pointer will get us to go out of scope of the array, so we need to prevent that
            MySecondPointerAtIndex += MySecondPointerAtIndex
            if OriginalNumberArray[MyFirstPointerAtIndex] != OriginalNumberArray[MySecondPointerAtIndex]:
                print(
                    "The 2nd pointer has advanced and found a non-duplicate. We will set the 1st pointer to the index location the 2nd pointer has landed at, add that value to our non-duplicate array, and continue with our process of advancing the 2nd pointer until a non-duplicate is found")
                MyArrayOfNonDuplicates.append(OriginalNumberArray[MySecondPointerAtIndex])
                MyFirstPointerAtIndex = MySecondPointerAtIndex
                # Do not need this line twice as it's in the outter loop
                # MySecondPointerAtIndex += MySecondPointerAtIndex

        return MyArrayOfNonDuplicates