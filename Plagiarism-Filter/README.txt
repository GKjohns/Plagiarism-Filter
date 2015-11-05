README.txt

/*** 
 * Document Similarity Filter
 * author: G. Kyle Johnson
 * Introduction to Python
 * Professor Lawrence S. Stead
 * Final Project
 */

   I wrote this program as a quantifiable way for instructors to determine if
two essays are similar enough to be considered plagiarized. This product took
on many forms before the present one; it evolved after each iteration exposed
 a weakness in an approach. Originally I wanted to return the longest
few common substrings. This approach, apart from having an unfavorable time
 complexity, was easy for a student to get around. If the simply changed the
 structure of the sentences, the program could not detect the similarity.
 	
	In order to deal with this, I chose to determine how many common groups
of 2 and 3 words appear between the documents. I then weighted the results
(after testing them on real plagiarized document and speeches written by
the same author). I also included the percentage of common words, but gave
it little weight because documents on the same subject should be very
similar.

    After testing the results on many documents and getting the weights just 
right, I'm happy that the program is robust and effective enough to be an
effective filter to two documents that might strike an instructor as 
"eerily similar". Though I originally intended to have this program detect 
plagiarism on its own, I learned that there is a fine line between making it
 robust and raising too many false alarms. I discovered that it would be best
 used as either a preliminary filter or one that that can be used as a
 quantifiable way to demonstrate that students might have cheated. In other
 words, it would help allow professors to present proof that students are 
copying others work—-bolstering their claims.

   In terms of implementation, I found that python made it very easy to implement
my ideas very quickly. In a language like C or even Java, I would be spending 
a good deal of time "reinventing the wheel". With convenient features like 
python's robust list indexing (being able to use list[-1] to get the last
 element or list[5:11] to get a slice) and list comprehensions, I found myself 
working at a higher level of abstraction, playing working with ideas and 
potential features as opposed to nuts and bolts.

   Though I normally prefer working with python version 2.7, I opted to use 
version 3.3 as an opportunity to explore python 3. I included two Barack Obama 
speeches that on the same topic to demonstrate the way in which the program 
works. Try using it on some of your own essays and drafts of the same paper 
for fun!

   ***To use the program, simply run the following command from the command line 

   'python DocSimilarity.py'

   From there, enter the names of the documents in question for an analysis.