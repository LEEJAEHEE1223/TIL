real_numbers = [1, 2, 3, 4, 5, 6]
bonus_number = 8
lucky_numbers = [1, 2, 3, 4, 5, 8]
diff_nums = list(set(lucky_numbers) - set(real_numbers))
result = list(set(lucky_numbers) - set(diff_nums))

if len(diff_nums) == 0:
    print('1등', result )
elif len(diff_nums) == 1:
    if diff_nums[0] == bonus_number:
        print('2등', result, '보너스번호', bonus_number)
    else:
        print('3등', result)
elif len(diff_nums) == 2:
    print('4등', result)
elif len(diff_nums) == 3:
    print('5등', result)
else:
    print('미당첨', result)


match_cnt = len( set(lucky_numbers).intersection(set(real_numbers)) )
if match_cnt == 6:
    print('1등')
elif match_cnt == 5 and bonus_number in lucky_numbers:
    print('2등')
elif match_cnt == 5:
    print('3등')

# real 과 lucky 가
# 1등: 6개가 같다.
# 2등: 5개가 같고, 나머지 하나가 bonus 다.
# 3등: 5개가 같다.
# 4등: 4개가 같다.
# 5등: 3개가 같다.


history = '5등 5등 4등'
grep('5등', history)