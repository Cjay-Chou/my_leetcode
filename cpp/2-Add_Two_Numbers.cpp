/*
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in 
reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any 
leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

//acturally This task is an add function

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	//Build a head , return it's next
	ListNode* pNode = new ListNode(0);
	ListNode* pHead = pNode;

	int flag = 0;//carry flag is 0 at begin
	while (l1 != nullptr&&l2 != nullptr)//if any is empty then END
	{
		int val = l1->val + l2->val + flag;
		ListNode* pCur = new ListNode(val % 10);//Node show add result
		if (val >= 10)
			flag = 1;//Setting carry flag
		else
			flag = 0;
		pNode->next = pCur;//String the nodes together
		pNode = pNode->next;
		l1 = l1->next;
		l2 = l2->next;
	}
	//At this point, there is already an empty list, either L1 or l2.
	ListNode* pTemp = l1;
	if (l1 == nullptr)
		pTemp = l2;
	while (pTemp != nullptr)
	{
		int val = pTemp->val + flag;
		pNode->next = new ListNode(val % 10);
		if (val >= 10)
			flag = 1;
		else
			flag = 0;
		pNode = pNode->next;
		pTemp = pTemp->next;
	}
	//If the last carry is still 1, a new node with value of 1 needs to be placed at the end
	if (flag == 1)
		pNode->next = new ListNode(1);
	return pHead->next;
}
