r=str(input())
if (r=='a' or r=='A' or r=='e' or r=='E' or r=='i' or r=='I' or r=='o' or r=='O' or r=='u' or r=='U'):
    print('Vowel')
elif (r>='a' and r<='z') or (r>='A' and r<='Z'):
    print('Consonant')
else:
    print('invalid')
