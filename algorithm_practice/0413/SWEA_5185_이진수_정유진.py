T=int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()  # 자리수, N자리 16진수
    ref = '0123456789ABCDEF'  # 16진수 참고
    answer = ''

    for num in hex_num:
        dec_num = ref.index(num)  # 16진수 숫자 => 10진수 
        bin_num = [0, 0, 0, 0]  # 16진수 1자리 = 2진수 4자리

        for i in range(3, -1, -1):  # 2진수로 바꾸기: 2로 나눈 나머지를 뒤에서 부터 채운다.
            bin_num[i] = dec_num % 2
            dec_num //= 2

        answer += ''.join(map(str, bin_num))  # 하나의 string 으로 연결

    print('#{} {}'.format(tc, answer))
