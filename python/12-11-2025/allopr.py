'''
1.Arithmetic Operations= Used for mathematical calculations.
(+, -, *, /, %, **)

2.Comparison (Relational) Operations= Used to compare values — returns True or False.
==	Equal 
!=	Not equal 
>	Greater than	
<	Less than	
>=	Greater than or equal 
<=	Less than or equal to


3.Used to assign values to variables.

Operator	Example	Meaning
=	x = 5	Assigns 5 to x
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
//=	x //= 3	x = x // 3
%=	x %= 3	x = x % 3
**=	x **= 3	x = x ** 3

 4. Logical Operations

Used for combining conditional statements.

Operator	Example	Meaning	Output
and	(5 > 3) and (2 < 4)	True if both are true	True
or	(5 > 3) or (2 > 4)	True if one is true	True
not	not(5 > 3)	Reverses condition	False

 5. Bitwise Operations

Works on bits (binary level).

Operator	Description	Example	Output
&	AND	5 & 3	1
`	`	OR	`5
^	XOR	5 ^ 3	6
~	NOT	~5	-6
<<	Left Shift	5 << 1	10
>>	Right Shift	5 >> 1	2

 6. Membership Operations

Check if a value exists in a sequence (like string, list, etc.).

Operator	Example	Output
in	'a' in 'apple'	True
not in	'x' not in 'apple'	True

 7. Identity Operations

Check if two variables refer to the same object.

Operator	Example	Output
is	x is y	True if both refer to same object
is not	x is not y	True if not same object

 8. String Operations
Operation	Example	Output
Concatenation	'Hello' + 'World'	'HelloWorld'
Repetition	'Hi' * 3	'HiHiHi'
Indexing	'Python'[0]	'P'
Slicing	'Python'[0:3]	'Pyt'

 9. List Operations
Operation	Example	Output
Append	lst.append(5)	Adds item
Remove	lst.remove(2)	Removes first occurrence
Sort	lst.sort()	Sorts list
Length	len(lst)	Number of elements

 10. File Operations
Operation	Example
Open file	f = open('data.txt', 'r')
Read file	f.read()
Write file	f.write('Hello')
Close file
'''

#1.Arithmetic Operations= Used for mathematical calculations.
# a=10
# b=12
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)


#2.Comparison (Relational) Operations= Used to compare values — returns True or False.
a=10
b=12
print(a==b)                            #
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)