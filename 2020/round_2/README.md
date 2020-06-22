***Problem 1***   
Every morning at The Incremental House of Pancakes, the kitchen staff prepares all of its pancakes for the day and arranges them into two stacks. Initially, the stack on the left has L pancakes, and the stack on the right has R pancakes.   
   
This restaurant's customers behave very consistently: the i-th customer to arrive (counting starting from 1) always orders i pancakes. When the i-th customer places their order of i pancakes, you take i pancakes from the stack that has the most pancakes remaining (or from the left stack if both have the same amount). If neither stack has at least i pancakes, the restaurant closes and the i-th customer does not get served any pancakes. You never complete an order using pancakes from both stacks.   
   
Given the initial numbers of pancakes in each stack, you want to know how many customers will be served, and how many pancakes will remain in each stack when the restaurant closes.   
Input   
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing two integers L and R: the initial numbers of pancakes in the left and right stacks, respectively, as described above.   
   
***Output***   
For each test case, output one line containing Case #x: n l r, where x is the test case number (starting from 1), n is the number of customers who will be served, and l and r are the numbers of pancakes that will remain in the left and right stacks, respectively, when the restaurant closes.   
   
***Limits***   
Time limit: 20 seconds per test set.   
Memory limit: 1GB.   
1 ≤ T ≤ 1000.   
   
Test Set 1 (Visible Verdict)   
1 ≤ L ≤ 1000.   
1 ≤ R ≤ 1000.   
   
Test Set 2 (Hidden Verdict)   
1 ≤ L ≤ 1018.   
1 ≤ R ≤ 1018.   
   
***Sample***   
***Input***   
3   
1 2   
2 2   
8 11   
 	   
***Output***   
Case #1: 1 1 1   
Case #2: 2 1 0   
Case #3: 5 0 4   
   
     
In Sample Case #1, the first customer gets 1 pancake from the right stack, leaving 1 pancake in each stack. The second customer wants 2 pancakes, but neither stack has enough for them, even though there are 2 pancakes in total.   
   
In Sample Case #2, the first customer gets 1 pancake from the left stack, because both stacks have the same amount. This leaves 1 pancake in the left stack and 2 in the right stack. The second customer wants 2 pancakes, which you serve to them from the right stack, emptying it. When the third customer arrives, neither stack has 3 pancakes, so no more orders are fulfilled.   
   
In Sample Case #3, the first customer is served from the right stack, leaving 8 pancakes in the left stack and 10 in the right stack. The second customer is also served from the right stack, leaving 8 pancakes in each stack. The third customer is served from the left stack, leaving 5 pancakes there and 8 in the right stack. The fourth customer is then served from the right stack, leaving 4 pancakes there. Serving the fifth customer empties the left stack, and then there are not enough pancakes remaining in either stack to serve a sixth customer.
   
***Problem 2***   
The Apricot Rules company just installed a critical security update on its network. The network has one source computer, and all other computers in the network are connected to the source computer via a sequence of one or more direct bidirectional connections.   
   
This kind of update propagates itself: once a computer receives the update for the first time, that computer immediately begins to transmit the update to all of the computers that are directly connected to it. Each of the direct connections has a latency value: the number of seconds needed for that connection to transmit the update (which is the same in either direction). Therefore, the update does not spread to all computers instantly.   
   
The Apricot Rules engineers do not know any of these latency values, but they know that they are all positive integers. They would like your help in figuring out what these latency values could be, based on how they saw the update spread in a recent experiment.   
   
The Apricot Rules engineers installed the update only on the source computer and then waited for it to propagate throughout the system until every computer was updated. They recorded some information about how the update spread. Specifically, for every computer K other than the source computer, you know exactly one of two things.   
   
The exact time in seconds between the time when the source computer received the update and the time when K first received the update.
The number of other computers (including the source computer) that first got the update strictly before K.   
Notice that multiple computers may have received the update at the exact same time.   
   
You are required to compute a latency in seconds for each of the direct connections between two computers. Each latency value must be a positive integer no greater than 106. The set of latencies that you provide must be consistent with all of the known information. It is guaranteed that there is at least one consistent way to assign latencies.   
   
***Input***   
The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with one line containing two integers C and D: the number of computers and the number of direct connections, respectively. The computers are numbered from 1 to C, with computer 1 being the source computer.   
   
The next line contains C-1 integers X2, X3, ..., XC. A positive Xi value indicates that computer i received the update Xi seconds after computer 1. A negative Xi value indicates that -Xi other computers received the update strictly before computer i; this value includes the source computer.   
   
After that, there are D more lines that represent the D direct connections in the network. The i-th of these lines contains two integers Ui and Vi, indicating that computers Ui and Vi are directly connected to each other.   
   
***Output***   
For each test case, output one line containing Case #x: y1 y2 ... yD, where x is the test case number (starting from 1) and yi is a positive integer not more than 106 representing the latency, in seconds, assigned to the i-th direct connection.   
   
***Limits***   
Time limit: 20 seconds per test set.   
Memory limit: 1GB.   
1 ≤ T ≤ 100.   
2 ≤ C ≤ 100.   
C - 1 ≤ D ≤ 1000.   
1 ≤ Ui < Vi ≤ C, for all i.   
(Ui, Vi) ≠ (Uj, Vj), for all i ≠ j.   
All computers (except the source computer) are connected to the source computer through a sequence of one or more direct connections.   
There exists at least one way of assigning latency values that is consistent with the input.   
   
Test Set 1 (Visible Verdict)   
-C < Xi < 0, for all i. (You get the second type of information for all computers.)   
   
Test Set 2 (Hidden Verdict)   
-C < Xi ≤ 1000, for all i.   
Xi ≠ 0, for all i.   
   
***Sample***   
   
***Input***   
   
***Output***   
   
3   
4 4   
-1 -3 -2   
1 2   
1 3   
2 4   
3 4   
4 4   
-1 -1 -1   
1 4   
1 2   
1 3   
2 3   
3 2   
-2 -1   
2 3   
1 3   
   
   
Case #1: 5 10 1 5   
Case #2: 2020 2020 2020 2020   
Case #3: 1000000 1000000   
   
   
In Sample Case #1, the following picture represents the computer network that is illustrated by the sample output. The i-th computer is represented by the circle with the label i. A line linking two circles represents a direct connection. The number on each line represents the latency of the direct connection.   
   
In Sample Case #2, the first three connections need to have the same latency, while the fourth can have any valid latency. Note that -2, 0, 1000001, and 3.14 are examples of invalid latencies.   
   
In Sample Case #3, remember that the connections are bidirectional, and so the update can travel from computer 3 to computer 2. Any two valid latency values work here.   
   
The following case could not appear in Test Set 1, but could appear in Test Set 2:   
   
1   
6 9   
10 -2 -5 15 20   
1 2   
1 3   
2 3   
2 4   
2 5   
3 5   
3 6   
4 5   
5 6   
One of the correct outputs is 10 12 4 15 8 3 9 7 5, as illustrated by the picture below.   