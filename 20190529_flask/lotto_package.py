import random


def get_lotto_numbers(lotto_numbers, bonus_number):

    my_numbers = random.sample(range(1, 46), 6)
    diff_nums = list(set(my_numbers) - set(lotto_numbers))
    result = list(set(my_numbers) - set(diff_nums))

    if len(diff_nums) == 0:
        output = f'1등{result}'
    elif len(diff_nums) == 1:
        if diff_nums[0] == bonus_number:
            output = f'2등{result} 보너스번호{bonus_number}'
            # print('2등', result, '보너스번호', bonus_number)
        else:
            output = f'3등{result}'
            # print('3등', result)
    elif len(diff_nums) == 2:
        output = f'4등{result}'
    elif len(diff_nums) == 3:
        output = f'5등{result}'
    else:
        output = f'미당첨{result}'
        # print('미당첨', result)

    return {'lotto_numbers':lotto_numbers,
            'my_numbers': my_numbers,
            'diff_nums': diff_nums,
            'result': result,
            'output': output
            }