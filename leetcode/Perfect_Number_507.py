'''
����һ�� ��������������ͳ������������������������֮����ȣ����ǳ���Ϊ������������
����һ�� ������ n�� ������������������� True�����򷵻� False

 
ʾ����
����: 28
���: True
����: 28 = 1 + 2 + 4 + 7 + 14
 
ע��:
��������� n ���ᳬ�� 100,000,000. (1e8)
'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num>0:
            li=[]
            s=int(math.sqrt(num))
            print(s)
            for i in range(1,s+1):
                if num%i==0:
                    a=num//i
                    if i not in li and i!=num:
                        li.append(i)
                    if a not in li and a!=num:
                        li.append(a)
            print(li)
            return num==sum(li)
        else:
            return False
                
'''
ִ����ʱ : 48 ms, ��Perfect Number��Python3�ύ�л�����97.95% ���û�
�ڴ����� : 13.1 MB, ��Perfect Number��Python3�ύ�л�����83.47% ���û�
'''