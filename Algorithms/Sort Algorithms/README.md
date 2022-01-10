## Bubble Sort
Runtime: O(n^2) average and worst case

Memory: O(1)

-  In bubble sort, we start at the beginning of the array and swap the first two elements if the first is greater than the second
  -  Then we go onto the next pair, and so on
  -  In doing so, we the smaller items slowly "bubble" up to the beginning of the list

Advantages:
-  Fast enough when working with small data sets
-  Easy to implement

```
class bubbleSortExample 
{
    // An optimized version of Bubble Sort
    static void bubbleSort(int arr[], int n)
    {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) 
        {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) 
            {
                if (arr[j] > arr[j + 1]) 
                {
                    // swap arr[j] and arr[j+1]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // IF no two elements were 
            // swapped by inner loop, then break
            if (swapped == false)
                break;
        }
    }

    // Function to print an array 
    static void printArray(int arr[], int size)
    {
        int i;
        for (i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[])
    {
        int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
        int n = arr.length;
        bubbleSort(arr, n);
        System.out.println("Sorted array: ");
        printArray(arr, n);
    }
}
```
-----------------
## Selection Sort
Runtime: O(n^2) average and worst case

Memory: O(1)

-  Simple, but inefficient
-  Find the smallest element using a linear scan and move it to the front (swapping it with the first element)
   -  Then, find the second smallest and move it, again doing a linear scan

Advantages:
-  It performs very well on small lists.
-  It is an in-place algorithm. It does not require a lot of space for sorting. Only one extra space is required for holding the temporal variable.
-  It performs well on items that have already been sorted.

When to use:
-  When the array is NOT partially sorted.
-  When we have memory usage constraints.
-  When a simple sorting implementation is desired.
-  When the array to be sorted is relatively small.

```
class SelectionSort
{
    void sort(int arr[])
    {
        int n = arr.length;

        // One by one move boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;

            // Swap the found minimum element with the first
            // element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    // Prints the array
    void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }

    // Driver code to test above
    public static void main(String args[])
    {
        SelectionSort ob = new SelectionSort();
        int arr[] = {64,25,12,22,11};
        ob.sort(arr);
        System.out.println("Sorted array");
        ob.printArray(arr);
    }
}
```
-----------------
## Merge Sort
Runtime: O(n log(n)) Average and worst case

Memory: Depends

-  Merge sort divides the array in half, sorts each of those halves, and then merges them back together.
  -  Each half has the same sorting alogirthm applied to it.
  -  it's the merge part that does the heavy lifting

-----------------
## Quick Sort

## Insertion Sort

## Counting Sort

## Heap Sort

