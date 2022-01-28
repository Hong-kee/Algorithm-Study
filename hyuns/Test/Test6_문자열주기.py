'''

문자열에서 일정한 간격으로 같은 문자열이 반복해서 나타난다면 이를 문자열의 주기라 함.
최소의 문자열 주기길이 출력

ex1) "abababab"

"ab", "abab", "abababab" 가 될 수 있음.
최소의 문자주기는 "ab" -> 2

ex2) "abababac"

"abababac" 가 최소의 문자 주기 -> 8

ex3) "abcabcabc"

"abc" 가 최소의 문자 주기 -> 3

ex4) "aaaaaaaab" -> 9

ex5) "abcabcabd' -> 9

알고리즘 ㄱㄱ

'''

def solution(s):

    answer = s
    half_length = len(s) // 2 + 1

    for i in range(1, half_length+1):
        T = s[:i]
        check = ""
        for _ in range(0, len(s), len(T)):
            check += T
        if check == s:
            answer = T
            break
    
    return len(answer)


print(solution("aaaaaaaab"))

