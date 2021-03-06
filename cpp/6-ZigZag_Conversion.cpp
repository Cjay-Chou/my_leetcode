/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
*/


string convert(string s, int numRows) {
	if (numRows == 1)
        return s;
	vector<string> vec(numRows);
	string res;
	int check = numRows * 2 - 2;
	for (int i = 0; i<s.length(); i++)
	{
		if (i%check<numRows)
			vec[i%check]+=s[i];
		else
			vec[check - i%check]+=s[i];
	}
	for (int i = 0; i < numRows; i++)
		res += vec[i];
	return res;
	
}