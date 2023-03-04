## Logic of Counting sort:

Counting sort in essence is an efficient sorting method compared to traditional comparison sorting. 
Assume we are to sort the following array using counting sort: 
arr = [1,3,1,4,5].
Initialize a count_arr that will have elements from 1 to 5; i.e. 

          | 1 | 2 | 3 | 4 | 5 | --> elements in the array, in step of 1
count_arr | 0 | 0 | 0 | 0 | 0 | --> will fill in the frequency which the value occur

          | 1 | 2 | 3 | 4 | 5 |  
count_arr | 2 | 0 | 1 | 1 | 1 | 

          | 1 | 2 | 3 | 4 | 5 |
count_arr | 2 | 2 | 3 | 4 | 5 | --> this sums the count, giving off the position(s) of the element

from here, we can see that there is a duplicate of sum in 1 and 2. This means that element '2' does not exist in the array. 
arr = [NULL, 1, 3, 4, 5] 
After inputting the elements in their respective position, we decrease the sum by one, shown below:

          | 1 | 2 | 3 | 4 | 5 |
count_arr | 1 | 2 | 2 | 3 | 4 |

from count_arr, we deduce that there are still values under each of the element. However, as the position of it are already occupied, it will not
replace the current element in that position of the arr. Since, position '1' is currently NULL, element '1' will be inputted into the arr.

Final arr: 
[1, 1, 3, 4, 5]

Time complexity of CountingSort is O(n+k). 

Pseudocode: 

CountSort(A,B,k){
   n = arr.last() // getting the count of the last element in the array
      for (i=1 to k){ // initialize the count_arr to 0
         count[i] = 0
      }
      
      for(j=1 to n){ // count[i] now contains the no. of elements = i
          count[A[j]] += 1
      }
      
      for(i=1 to k){ // count[i] now contains the no. of elements <= i
          count[i] += count[i-1]
      }
      
      for (j=n downto 1){
          B[count[A[j]]] = A[j] 
          count[A[j]] -= 1 //decrease counter by 1
      }
}
       
