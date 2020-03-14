a_str="abcdefghi"
b=""
for i in range(len(a_str)):
    if i%2 !=0:
        b=b+a_str[i]
print(a_str)

#q3
n=int(input())-1
a_str=a_str[:n]+a_str[n+1:len(a_str)]
print(a_str)

#q4
def list_word(word_list):
    a=""
    for i in range(len(word_list)):
        if len(word_list[i])>len(a):
            a=word_list[i]

    print(a)
list_word(['word','mukesh','ronak','allan','himanshu','urvashi'])

#q2
list1=[1,2,3,3,4,4]
a=dict()
for i in range(len(list1)):
    if str(list1[i]) in a:
        a[str(list1[i])]=a[str(list1[i])]+1
    else:
        a[str(list1[i])]=1
print(a)
