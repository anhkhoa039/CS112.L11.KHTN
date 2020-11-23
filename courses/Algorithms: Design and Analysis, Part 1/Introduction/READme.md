# Introduction
---  
### Introduce:  
- Discussing algorithm in general  and why they're so important  
- Using the problem of multiplying 2 integers to illustrate how algorithmic ingenuity can often improve over more straightforward or naïve solutions  
- Discuss merge sort - canonical introduction to the "divide and conquer" algorithm design paradism   
 
 
 
### Why study algorithms ?  
- Important for all other branches of computer science  
Example:   
	• Trong lĩnh vực mạng, đinh tuyến sử dụng thuật toán tìm đường đi ngắn nhất  
	• Trong cơ sở dữ liệu, các chỉ số trong cơ sở dữ liệu dựa trên cấu trúc cây cân bằng  
	• Trong sinh học, sử dụng quy hoạch động để so sánh các bộ gen giống nhau   
- Plays a key  role in modern technology innovation   
Example:   
	- search  engines use a tapestry of algorithms to  
	efficiently compute the relevance of  various webpages to it's given search  
	query.  The most famous such algorithm is the  
	page rank algorithm currently in use by  Google  
- Provides novel “lens” on processes outside of computer science and technology   
- Challenging (good for your brain)

### Merge sort
#### why study merge sort ? 
- Good introoduce to dive & conquer
- Motivates guiding principles for algorithm analysis
- Analysis generalizes to "Master Method"


#### Analysis:
- **Running time: O(n*log n)**
#### Why the running time for merge sort is O(n*log n)  
- As we have already learned in Binary Search that whenever we divide a number into half in every step, it can be represented using a logarithmic function, which is log n and the number of steps can be represented by log n + 1(at most)  
- And to merge the subarrays, made by dividing the original array of n elements, a running time of O(n) will be required.  
Hence the total time for mergeSort function will become n(log n + 1), which gives us a time complexity of **O(n*log n).**    
---
- Worst Case Time Complexity [ Big-O ]: **O(n*log n)**      
- Best Case Time Complexity [Big-omega]: **O(n*log n)**     
- Average Time Complexity [Big-theta]: **O(n*log n)**  
--- 
Space Complexity: **O(n)**  
	- Time complexity of Merge Sort is O(n*Log n) in all the 3 cases (worst, average and best) as merge sort always divides the array in two halves and takes linear time to merge two halves.  
	- It requires equal amount of additional space as the unsorted array. Hence its not at all recommended for searching large unsorted arrays.  
	- It is the best Sorting technique used for sorting Linked Lists  
### Guiding Principles for Analysis of Algorithms  
#1. Worst-case analysis  
#2. Don't pay much attention to constants factors(constants depend on architecture/compiler/programer)  
#3. Asymtotic analysis: focus on running time for large input sizes n
#### What is a fast algorithm?
**Fast algorithm** ~~ the worst-case running time  grows slowly  with the input size  
