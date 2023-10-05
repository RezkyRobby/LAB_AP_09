def isPalindrome(string: str) -> str: 
    if (string == string[::-1]) : 
        return "Palindrom" 
    else: 
        return "Bukan Palindrom" 
 
#Enter input string 
string = input("Masukkan String : ").lower()
 
print(isPalindrome(string)) 